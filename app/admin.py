"""Administración: cuentas con rol y artículos del blog. Solo para personas con rol "admin"."""
import os
import re
import secrets
import unicodedata
from functools import wraps

import bleach
import click
import markdown
import csv
import io

from flask import (Blueprint, Response, abort, current_app, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask.cli import with_appcontext
from flask_login import current_user, login_required
from markupsafe import Markup

from app.extensiones import db
from app.modelos import Articulo, ImagenBanco, SolicitudCalendario, Usuario

bp = Blueprint("admin", __name__, url_prefix="/admin")

ROLES = ("usuario", "admin")
ESTADOS_BANCO = ("pendiente", "aprobada", "rechazada")
EXTENSIONES_IMAGEN = {"png", "jpg", "jpeg", "gif", "webp"}
LIMITE_IMAGEN = 5 * 1024 * 1024

# Lo único que puede traer un artículo al mostrarse; lo demás se quita.
ETIQUETAS = ["p", "br", "h2", "h3", "h4", "ul", "ol", "li", "strong", "em", "blockquote",
             "code", "pre", "a", "img", "hr", "table", "thead", "tbody", "tr", "th", "td"]
ATRIBUTOS = {"a": ["href", "title"], "img": ["src", "alt", "title"]}

# Cuentas con las que arranca el sitio. Las contraseñas no están en el código: se generan al crearlas.
ADMINS_INICIALES = [
    ("Administrador 1", "id634296@gmail.com"),
    ("José Luis Sánchez", "sanchezmxjoseluis@gmail.com"),
]


def solo_admin(vista):
    @wraps(vista)
    @login_required
    def envoltura(*args, **kwargs):
        if not current_user.es_admin:
            abort(403)
        return vista(*args, **kwargs)
    return envoltura


def hacer_slug(titulo):
    base = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:80] or "articulo"
    slug, n = base, 2
    while Articulo.query.filter_by(slug=slug).first():
        slug, n = f"{base}-{n}", n + 1
    return slug


def html_seguro(texto):
    """Markdown a HTML, sin etiquetas ni enlaces peligrosos."""
    crudo = markdown.markdown(texto or "", extensions=["extra", "sane_lists"])
    limpio = bleach.clean(crudo, tags=ETIQUETAS, attributes=ATRIBUTOS,
                          protocols=["http", "https", "mailto"], strip=True)
    limpio = bleach.linkify(limpio, callbacks=[bleach.callbacks.nofollow], skip_tags=["pre", "code"])
    return Markup(limpio)


# --- Panel y cuentas -------------------------------------------------------------

@bp.route("/")
@solo_admin
def panel():
    return render_template("admin/panel.html", total_usuarios=Usuario.query.count(),
                           total_articulos=Articulo.query.count(),
                           total_calendario=SolicitudCalendario.query.count(),
                           total_banco=ImagenBanco.query.count())


@bp.route("/usuarios")
@solo_admin
def usuarios():
    lista = Usuario.query.order_by(Usuario.creado.desc()).all()
    return render_template("admin/usuarios.html", usuarios=lista)


@bp.route("/usuarios/<int:usuario_id>/rol", methods=["POST"])
@solo_admin
def cambiar_rol(usuario_id):
    usuario = db.get_or_404(Usuario, usuario_id)
    rol = request.form.get("rol")
    if rol not in ROLES:
        abort(400)
    if usuario.id == current_user.id and rol != "admin":
        flash("No puedes quitarte tu propio rol de administrador.", "warning")
    else:
        usuario.rol = rol
        db.session.commit()
        flash(f"{usuario.nombre} ahora es {'administrador' if rol == 'admin' else 'usuario'}.", "success")
    return redirect(url_for("admin.usuarios"))


@bp.route("/calendario")
@solo_admin
def solicitudes_calendario():
    lista = SolicitudCalendario.query.order_by(SolicitudCalendario.fecha.desc()).all()
    return render_template("admin/calendario.html", solicitudes=lista)


@bp.route("/banco")
@solo_admin
def banco():
    from app.banco import GB, usado_en_banco
    filtro = request.args.get("estado")
    consulta = ImagenBanco.query
    if filtro in ESTADOS_BANCO:
        consulta = consulta.filter_by(estado=filtro)
    lista = consulta.order_by(ImagenBanco.fecha.desc()).all()
    conteo = {e: ImagenBanco.query.filter_by(estado=e).count() for e in ESTADOS_BANCO}
    return render_template("admin/banco.html", imagenes=lista, filtro=filtro, conteo=conteo, usado_gb=usado_en_banco() / GB,
                           limite_gb=current_app.config["BANCO_LIMITE_GB"])


@bp.route("/banco/<int:imagen_id>/estado", methods=["POST"])
@solo_admin
def banco_estado(imagen_id):
    imagen = db.get_or_404(ImagenBanco, imagen_id)
    estado = request.form.get("estado")
    if estado not in ESTADOS_BANCO:
        abort(400)
    imagen.estado = estado
    db.session.commit()
    flash(f"La imagen {imagen.id} quedó como {estado}.", "success")
    return redirect(url_for("admin.banco", estado=request.form.get("filtro") or None))


@bp.route("/banco/<int:imagen_id>/archivo")
@solo_admin
def banco_archivo(imagen_id):
    imagen = db.get_or_404(ImagenBanco, imagen_id)
    return send_from_directory(current_app.config["CARPETA_BANCO"], imagen.archivo, as_attachment=True,
                               download_name=f"{imagen.id}_{imagen.nombre_original}")


@bp.route("/banco/exportar.csv")
@solo_admin
def banco_csv():
    """Una fila por imagen con todos sus datos, para armar el conjunto de entrenamiento."""
    salida = io.StringIO()
    escritor = csv.writer(salida)
    escritor.writerow(["id", "fecha", "archivo", "nombre_original", "mb", "cuenta", "nombre", "institucion",
                       "especie", "organo", "tincion", "experimento", "comite", "autoriza_entrenamiento", "estado"])
    for i in ImagenBanco.query.order_by(ImagenBanco.id).all():
        escritor.writerow([i.id, i.fecha.strftime("%Y-%m-%d %H:%M"), i.archivo, i.nombre_original,
                           round(i.tamanio / 1048576, 2), i.usuario.correo, i.nombre, i.institucion, i.especie,
                           i.organo, i.tincion, "si" if i.experimento else "no", i.comite,
                           "si" if i.autoriza_entrenamiento else "no", i.estado])
    return Response("﻿" + salida.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=banco_de_imagenes.csv"})


# --- Artículos ---------------------------------------------------------------------

@bp.route("/articulos")
@solo_admin
def articulos():
    return render_template("admin/articulos.html",
                           articulos=Articulo.query.order_by(Articulo.actualizado.desc()).all())


def _guardar(articulo):
    titulo = request.form.get("titulo", "").strip()
    if not titulo:
        flash("El artículo necesita un título.", "warning")
        return False
    articulo.titulo = titulo[:200]
    articulo.resumen = request.form.get("resumen", "").strip()[:400]
    articulo.cuerpo = request.form.get("cuerpo", "")
    articulo.publicado = bool(request.form.get("publicado"))
    if articulo.id is None:
        articulo.slug = hacer_slug(titulo)
        articulo.autor_id = current_user.id
        db.session.add(articulo)
    db.session.commit()
    return True


@bp.route("/articulos/nuevo", methods=["GET", "POST"])
@solo_admin
def articulo_nuevo():
    articulo = Articulo()
    if request.method == "POST" and _guardar(articulo):
        flash("Artículo guardado.", "success")
        return redirect(url_for("admin.articulo_editar", articulo_id=articulo.id))
    return render_template("admin/articulo_form.html", articulo=articulo, form=request.form)


@bp.route("/articulos/<int:articulo_id>/editar", methods=["GET", "POST"])
@solo_admin
def articulo_editar(articulo_id):
    articulo = db.get_or_404(Articulo, articulo_id)
    if request.method == "POST" and _guardar(articulo):
        flash("Cambios guardados.", "success")
        return redirect(url_for("admin.articulo_editar", articulo_id=articulo.id))
    return render_template("admin/articulo_form.html", articulo=articulo, form=request.form)


@bp.route("/articulos/<int:articulo_id>/borrar", methods=["POST"])
@solo_admin
def articulo_borrar(articulo_id):
    articulo = db.get_or_404(Articulo, articulo_id)
    db.session.delete(articulo)
    db.session.commit()
    flash("Artículo borrado.", "info")
    return redirect(url_for("admin.articulos"))


@bp.route("/imagenes", methods=["POST"])
@solo_admin
def subir_imagen():
    """Guarda una imagen para un artículo y devuelve la línea de Markdown que la inserta."""
    archivo = request.files.get("imagen")
    if archivo is None or not archivo.filename:
        return {"error": "Elige una imagen."}, 400
    extension = archivo.filename.rsplit(".", 1)[-1].lower() if "." in archivo.filename else ""
    if extension not in EXTENSIONES_IMAGEN:
        return {"error": "Solo PNG, JPG, GIF o WebP."}, 400
    datos = archivo.read(LIMITE_IMAGEN + 1)
    if len(datos) > LIMITE_IMAGEN:
        return {"error": "La imagen pesa más de 5 MB."}, 400
    nombre = f"{secrets.token_hex(8)}.{extension}"
    with open(os.path.join(current_app.config["CARPETA_ARTICULOS"], nombre), "wb") as f:
        f.write(datos)
    url = url_for("sitio.imagen_articulo", nombre=nombre)
    return {"url": url, "markdown": f"![descripción]({url})"}


# --- Comando para crear a los primeros administradores ------------------------------

@click.command("crear-admins")
@with_appcontext
@click.option("--reiniciar", is_flag=True, help="Genera contraseña nueva aunque la cuenta ya exista.")
def crear_admins(reiniciar):
    """Crea (o promueve) a los administradores iniciales con contraseñas de prueba.

    Las contraseñas no se muestran: se guardan en instance/admins_iniciales.txt, que no se sube a Git.
    Cada persona debe cambiarla desde Mi perfil.
    """
    lineas = []
    for nombre, correo in ADMINS_INICIALES:
        usuario = Usuario.query.filter_by(correo=correo).first()
        clave = None
        if usuario is None:
            usuario = Usuario(nombre=nombre, correo=correo)
            db.session.add(usuario)
            clave = secrets.token_urlsafe(9)
        elif reiniciar:
            clave = secrets.token_urlsafe(9)
        if clave:
            usuario.poner_clave(clave)
            lineas.append(f"{correo}  {clave}")
        usuario.rol = "admin"
    db.session.commit()
    if lineas:
        ruta = current_app.config.get("ARCHIVO_ADMINS") or os.path.join(current_app.instance_path, "admins_iniciales.txt")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("Contraseñas de prueba. Cámbialas desde Mi perfil y borra este archivo.\n"
                    + "\n".join(lineas) + "\n")
        click.echo(f"Listo. Las contraseñas están en {ruta}")
    else:
        click.echo("Las cuentas ya existían y ahora son administradoras (se conservaron sus contraseñas).")
