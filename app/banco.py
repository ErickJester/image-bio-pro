"""Banco de imágenes: las personas con cuenta aportan fotografías con sus datos y quedan guardadas en el servidor."""
import os
import shutil
import uuid

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from PIL import Image, UnidentifiedImageError
from sqlalchemy import func

from app.extensiones import db
from app.modelos import ImagenBanco

bp = Blueprint("banco", __name__, url_prefix="/banco")

# Formato real de la imagen (lo que dice Pillow, no la extensión del nombre) -> extensión con la que se guarda
FORMATOS = {"BMP": "bmp", "PNG": "png", "TIFF": "tif", "JPEG": "jpg"}
LIMITE_ARCHIVO = 60 * 1024 * 1024        # una fotografía BMP grande pesa unos 10 a 20 MB
GB = 1024 ** 3
CAMPOS = [  # (campo del formulario, etiqueta, largo máximo)
    ("nombre", "Nombre", 120),
    ("institucion", "Institución", 200),
    ("especie", "Especie", 120),
    ("organo", "Órgano reproductivo", 120),
    ("tincion", "Tipo de tinción", 120),
]


def usado_en_banco():
    return db.session.query(func.coalesce(func.sum(ImagenBanco.tamanio), 0)).scalar()


def hay_espacio(necesario):
    """Respeta el tope del banco y deja libre un margen en el disco para el sistema y los modelos."""
    tope = current_app.config["BANCO_LIMITE_GB"] * GB
    libre = shutil.disk_usage(current_app.config["CARPETA_BANCO"]).free
    return usado_en_banco() + necesario <= tope and libre - necesario >= current_app.config["BANCO_MARGEN_GB"] * GB


def validar_datos(form):
    """Devuelve (datos, errores). Si la imagen vino de un experimento, el número del comité es obligatorio."""
    datos, errores = {}, []
    for campo, etiqueta, largo in CAMPOS:
        valor = form.get(campo, "").strip()
        if not valor:
            errores.append(f"Falta el campo «{etiqueta}».")
        datos[campo] = valor[:largo]
    experimento = form.get("experimento")
    if experimento not in ("si", "no"):
        errores.append("Indica si la imagen se tomó durante un experimento.")
    datos["experimento"] = experimento == "si"
    comite = form.get("comite", "").strip()[:80]
    if datos["experimento"] and not comite:
        errores.append("Escribe el número de aceptación del comité interno de cuidado y uso de animales.")
    datos["comite"] = comite if datos["experimento"] else ""
    if not form.get("autorizo"):
        errores.append("Debes autorizar el uso de las imágenes para entrenar el modelo.")
    return datos, errores


def guardar_archivo(archivo):
    """Guarda una imagen en el banco. Devuelve (nombre_en_disco, tamaño) o lanza ValueError con el motivo."""
    carpeta = current_app.config["CARPETA_BANCO"]
    temporal = os.path.join(carpeta, f"tmp_{uuid.uuid4().hex}")
    archivo.save(temporal)
    try:
        tamanio = os.path.getsize(temporal)
        if tamanio > LIMITE_ARCHIVO:
            raise ValueError("pesa más de 60 MB")
        try:
            with Image.open(temporal) as img:
                formato = img.format
                img.verify()
        except (UnidentifiedImageError, OSError, SyntaxError):
            raise ValueError("no es una imagen válida")
        if formato not in FORMATOS:
            raise ValueError("el formato no es BMP, PNG, TIFF ni JPG")
        if not hay_espacio(tamanio):
            raise ValueError("el banco no tiene espacio disponible")
        nombre = f"{uuid.uuid4().hex}.{FORMATOS[formato]}"
        os.replace(temporal, os.path.join(carpeta, nombre))
        return nombre, tamanio
    finally:
        if os.path.exists(temporal):
            os.remove(temporal)


@bp.route("/", methods=["GET", "POST"])
@login_required
def subir():
    if request.method == "POST":
        archivos = [a for a in request.files.getlist("imagenes") if a and a.filename]
        datos, errores = validar_datos(request.form)
        if not archivos:
            errores.insert(0, "Elige al menos una imagen.")
        maximo = current_app.config["BANCO_MAX_POR_ENVIO"]
        if len(archivos) > maximo:
            errores.append(f"Puedes subir como máximo {maximo} imágenes a la vez.")
        if errores:
            for e in errores:
                flash(e, "warning")
        else:
            guardadas, rechazadas = 0, []
            for archivo in archivos:
                original = os.path.basename(archivo.filename)[:200]
                try:
                    nombre, tamanio = guardar_archivo(archivo)
                except ValueError as motivo:
                    rechazadas.append(f"{original} ({motivo})")
                    continue
                db.session.add(ImagenBanco(usuario_id=current_user.id, archivo=nombre, nombre_original=original,
                                           tamanio=tamanio, autoriza_entrenamiento=True, estado="pendiente", **datos))
                guardadas += 1
            db.session.commit()
            if guardadas:
                flash(f"Se recibieron {guardadas} imagen{'' if guardadas == 1 else 'es'}. Quedan pendientes de aprobación "
                      "por parte del equipo del proyecto. Gracias por aportarlas.", "success")
            if rechazadas:
                flash("No se guardaron: " + "; ".join(rechazadas) + ".", "danger")
            if guardadas and not rechazadas:
                return redirect(url_for("banco.subir"))
    mias = current_user.imagenes_banco.all()
    return render_template("banco/subir.html", form=request.form, campos=CAMPOS, mias=mias,
                           maximo=current_app.config["BANCO_MAX_POR_ENVIO"])
