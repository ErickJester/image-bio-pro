"""Páginas informativas: inicio, nosotros, aliados, infografías, videos, contacto."""
from flask import (Blueprint, abort, current_app, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import current_user

from app.extensiones import db
from app.modelos import Articulo, Mensaje, SolicitudCalendario

bp = Blueprint("sitio", __name__)

# Contenido de relleno hasta que el grupo pase los textos, fotos e infografías.
LOREM = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor "
         "incididunt ut labore et dolore magna aliqua.")

# Personas del proyecto, en el orden y con los datos del documento de correcciones del cliente.
# foto: ruta dentro de app/static (aliados/); sin-foto.svg = silueta. scholar: perfil de Google Scholar; None = sin enlace.
ALIADOS = [
    {"nombre": 'Dra. Sheila Irais Peña Corona', "foto": 'aliados/sheila-irais-pena-corona.jpg', "scholar": None, "lineas": [
        'Responsable y líder del proyecto BioImage-Repro UAM',
        'Profesora-Investigadora',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
        'Investigadora Nacional Nivel I del SNI',
    ]},
    {"nombre": 'Dr. Saúl Jiménez Jiménez', "foto": 'aliados/sin-foto.svg', "scholar": None, "lineas": [
        'Responsable del desarrollo del sitio web y del modelo de inteligencia artificial de BioImage-Repro UAM',
        'Investigador posdoctoral SECIHTI en la Universidad Autónoma Metropolitana, Unidad Iztapalapa',
        'Departamento de Química',
        'División de Ciencias Básicas e Ingeniería',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
        'Candidato a Investigador Nacional del SNI',
    ]},
    {"nombre": 'Dra. Edith Arenas Ríos', "foto": 'aliados/edith-arenas-rios.jpg', "scholar": None, "lineas": [
        'Colaboradora',
        'Directora de la División de Ciencias Biológicas y de la Salud',
        'Profesora-Investigadora',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
        'Investigadora Nacional Nivel II del SNI',
    ]},
    {"nombre": 'Dra. María del Rosario Tarragó Castellanos', "foto": 'aliados/rosario-tarrago-castellanos.jpg', "scholar": None, "lineas": [
        'Colaboradora',
        'Jefa del Departamento de Biología de la Reproducción',
        'Profesora-Investigadora',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
    ]},
    {"nombre": 'Luis Enrique Pérez Caltzontzin', "foto": 'aliados/luis-enrique-perez-caltzontzin.jpg', "scholar": None, "lineas": [
        'Logística y coordinador de actividades de difusión',
        'Estudiante de posgrado',
        'Departamento de Producción Agrícola y Animal UAM-X',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Xochimilco',
    ]},
    {"nombre": 'Dr. Roberto Carlos Lazzarini Lechuga', "foto": 'aliados/roberto-carlos-lazzarini-lechuga.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Profesor-Investigador',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
        'Investigador Nacional Nivel I del SNI',
    ]},
    {"nombre": 'Dr. Jorge Eduardo Vieyra Durán', "foto": 'aliados/jorge-eduardo-vieyra-duran.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Profesor-Investigador',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
    ]},
    {"nombre": 'Dra. María del Socorro Imelda Retana Márquez', "foto": 'aliados/maria-del-socorro-imelda-retana-marquez.jpg', "scholar": None, "lineas": [
        'Colaboradora',
        'Profesora-Investigadora',
        'Departamento de Biología de la Reproducción',
        'División de Ciencias Biológicas y de la Salud',
        'Universidad Autónoma Metropolitana Unidad Iztapalapa',
        'Investigadora Nacional Nivel II del SNI',
    ]},
    {"nombre": 'M. en C. Adrián Emmanuel Iglesias Reyes', "foto": 'aliados/adrian-emmanuel-iglesias-reyes.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Profesor-Investigador',
        'Departamento de Producción Agrícola y Animal UAM-X',
        'División de Ciencias Biológicas y de la Salud',
    ]},
    {"nombre": 'Dra. Marcela Vergara Onofre', "foto": 'aliados/marcela-vergara-onofre.png', "scholar": None, "lineas": [
        'Colaboradora',
        'Coordinadora de la Maestría en Ciencias Agropecuarias',
        'Profesora-Investigadora',
        'Departamento de Producción Agrícola y Animal UAM-X',
        'División de Ciencias Biológicas y de la Salud',
        'Investigadora Nacional Nivel I del SNI',
    ]},
    {"nombre": 'Dr. Juan José Pérez Rivero Cruz y Celis', "foto": 'aliados/juan-jose-perez-rivero-cruz-y-celis.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Presidente de la Asociación Mexicana de Epidemiología Veterinaria A.C. (AMEV)',
        'Profesor-Investigador',
        'Departamento de Producción Agrícola y Animal UAM-X',
        'División de Ciencias Biológicas y de la Salud',
        'Investigador Nacional Nivel II del SNI',
    ]},
    {"nombre": 'M. en C. Juan Isaac Chávez Corona', "foto": 'aliados/juan-isaac-chavez-corona.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Estudiante de posgrado',
        'Facultad de Medicina Veterinaria y Zootecnia, UNAM',
    ]},
    {"nombre": 'Dra. Dinorah Vargas Estrada', "foto": 'aliados/dinorah-vargas-estrada.png', "scholar": None, "lineas": [
        'Colaboradora',
        'Departamento de Fisiología y Farmacología',
        'Facultad de Medicina Veterinaria y Zootecnia',
        'Universidad Nacional Autónoma de México',
        'Investigadora Nacional Nivel II del SNI',
    ]},
    {"nombre": 'Dr. Gerardo Leyva Gómez', "foto": 'aliados/gerardo-leyva-gomez.jpg', "scholar": None, "lineas": [
        'Colaborador',
        'Departamento de Farmacia',
        'Facultad de Química',
        'Universidad Nacional Autónoma de México',
        'Investigador Nacional Nivel II del SNI',
    ]},
    {"nombre": 'Dra. Laura Olivia Arvizu Tovar', "foto": 'aliados/laura-olivia-arvizu-tovar.jpg', "pos": "0% 50%", "scholar": None, "lineas": [
        'Colaboradora',
        'Departamento de Medicina Preventiva y Salud Pública',
        'Facultad de Medicina Veterinaria y Zootecnia',
        'Universidad Nacional Autónoma de México',
        'Candidata a Investigadora Nacional del SNI',
    ]},
    {"nombre": 'Dra. Patricia Mora Medina', "foto": 'aliados/patricia-mora-medina.jpg', "ajuste": "contain", "scholar": None, "lineas": [
        'Colaboradora',
        'Departamento de Ciencias Pecuarias',
        'Facultad de Estudios Superiores Cuautitlán',
        'Universidad Nacional Autónoma de México',
        'Investigadora Nacional Nivel I del SNI',
    ]},
    {"nombre": 'Dra. María Josefa Bernad Bernad', "foto": 'aliados/maria-josefa-bernad-bernad.png', "scholar": None, "lineas": [
        'Colaboradora',
        'Departamento de Farmacia',
        'Facultad de Química',
        'Universidad Nacional Autónoma de México',
        'Investigadora Nacional Nivel I del SNI',
    ]},
    {"nombre": 'Dra. Xelhua Elihut Marcos Benítez', "foto": 'aliados/xelhua-elihut-marcos-benitez.jpg', "pos": "50% 100%", "scholar": None, "lineas": [
        'Colaboradora',
        'Unidad de Innovación y Desarrollo Farmacéutico. Centro Interdisciplinario de Medicina Predictiva, ITEMS',
        'Instituto Tecnológico y de Estudios Superiores de Monterrey',
    ]},
]

INFOGRAFIAS = [
    {"numero": i, "titulo": f"Título de la infografía {i}", "imagen": None, "texto": LOREM}
    for i in range(1, 9)
]

# Videos del curso en dos secciones. Cada video lleva su número en el curso (1 a 15) y el módulo al que
# pertenece. youtube_id es lo que va después de "watch?v="; None = marcador de posición hasta subir el video
# (los ids están en _YOUTUBE).
_VIDEOS = {
    1: ("El problema y la imagen digital", "Contar y medir espermatozoides a mano, y qué es una imagen para una computadora."),
    2: ("Inteligencia artificial, entrenamiento y la neurona", "Definiciones, entrenamiento contra inferencia y la neurona artificial."),
    3: ("Capas, cómo aprende una red y cierre", "De la neurona a la red, y cómo una red aprende de ejemplos."),
    4: ("Cómo ve una imagen una red convolucional", "El filtro que recorre la imagen, con un ejemplo numérico de 3 por 3."),
    5: ("Mask R-CNN", "La red que usa el sistema, explicada en lenguaje sencillo."),
    6: ("Aprendizaje por transferencia", "Cómo aprovechar una red entrenada para otra cosa."),
    7: ("Datos y entrenamiento", "Anotación, entrenamiento y validación, sobreajuste y curvas."),
    8: ("Frontend: el sitio funcionando", "Cómo se ve y cómo está hecho el sitio: plantillas, Bootstrap y la pantalla de resultados."),
    9: ("Backend", "Flask, las rutas y qué pasa cuando se sube una imagen."),
    10: ("Inferencia con recortes", "Cómo se usa el modelo: recortes, juntar resultados y quitar repetidos."),
    11: ("Medición, escala y retos", "Contorno, área, largo y escala, y cómo se resolvieron los retos."),
    12: ("Cuaderno de Colab, primera parte", "Del entorno a la preparación de las imágenes y los recortes."),
    13: ("Cuaderno de Colab, segunda parte", "Construir la red, entrenar, ver los resultados y exportar el modelo."),
    14: ("Despliegue en la nube", "El servidor, la clave SSH, Docker y Docker Compose."),
    15: ("Nginx, dominio y HTTPS", "Cómo recibe visitas el sitio, el dominio, el certificado y el cierre."),
}
# Videos ya subidos a YouTube: número del curso -> id. Los que no están salen como marcador de posición.
_YOUTUBE = {
    # 1: "ucNXMX2AXAg",
    # 2: "5LMw9Kyl1j4",
    # 3: "pqSKnbEho38",
}
# (nombre de la sección, nombre corto para la pestaña, [(número, módulo del curso), ...])
_SECCIONES = [
    ("Desarrollo de la red neuronal convolucional", "Red neuronal",
     [(1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2), (7, 2), (12, 4), (13, 4)]),
    ("Desarrollo del sitio web", "Sitio web",
     [(8, 3), (9, 3), (10, 3), (11, 3), (14, 4), (15, 4)]),
]
VIDEOS = [
    {"nombre": nombre, "corto": corto,
     "videos": [{"numero": n, "modulo": m, "titulo": _VIDEOS[n][0], "texto": _VIDEOS[n][1], "youtube_id": _YOUTUBE.get(n)}
                for n, m in lista]}
    for nombre, corto, lista in _SECCIONES
]


@bp.route("/")
def inicio():
    return render_template("sitio/inicio.html")


@bp.route("/nosotros")
def nosotros():
    return render_template("sitio/nosotros.html")


@bp.route("/aliados")
def aliados():
    return render_template("sitio/aliados.html", aliados=ALIADOS)


@bp.route("/infografias")
def infografias():
    return render_template("sitio/infografias.html", infografias=INFOGRAFIAS)


@bp.route("/videos")
def videos():
    total_videos = sum(len(g["videos"]) for g in VIDEOS)
    return render_template("sitio/videos.html", videos=VIDEOS, total_videos=total_videos)


@bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        texto = request.form.get("mensaje", "").strip()
        if not (nombre and correo and texto):
            flash("Llena tu nombre, tu correo y el mensaje.", "warning")
            return render_template("sitio/contacto.html", form=request.form)
        db.session.add(Mensaje(nombre=nombre[:120], correo=correo[:254], texto=texto))
        db.session.commit()
        flash("Gracias, recibimos tu mensaje.", "success")
        return redirect(url_for("sitio.contacto"))
    return render_template("sitio/contacto.html", form={})


@bp.route("/calendario", methods=["GET", "POST"])
def calendario():
    if request.method == "POST":
        direccion = request.form.get("correo", "").strip().lower()
        if "@" not in direccion or len(direccion) > 254:
            flash("Escribe un correo electrónico válido.", "warning")
            return render_template("sitio/calendario.html", form=request.form)
        db.session.add(SolicitudCalendario(correo=direccion))
        db.session.commit()
        flash("Gracias. Te enviaremos la invitación al calendario.", "success")
        return redirect(url_for("sitio.calendario"))
    return render_template("sitio/calendario.html", form={})


@bp.route("/articulos")
def articulos():
    lista = Articulo.query.filter_by(publicado=True).order_by(Articulo.creado.desc()).all()
    return render_template("sitio/articulos.html", articulos=lista)


@bp.route("/articulos/<slug>")
def articulo(slug):
    art = Articulo.query.filter_by(slug=slug).first_or_404()
    # Los borradores solo los ve quien administra
    if not art.publicado and not (current_user.is_authenticated and current_user.es_admin):
        abort(404)
    return render_template("sitio/articulo.html", articulo=art)


@bp.route("/articulos/imagen/<nombre>")
def imagen_articulo(nombre):
    return send_from_directory(current_app.config["CARPETA_ARTICULOS"], nombre)


@bp.route("/aviso-de-privacidad")
def privacidad():
    return render_template("sitio/privacidad.html")
