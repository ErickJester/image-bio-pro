import json
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensiones import db, login_manager


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(254), unique=True, nullable=False, index=True)
    clave_cifrada = db.Column(db.String(256), nullable=False)
    creado = db.Column(db.DateTime, default=datetime.now, nullable=False)
    # "usuario" (puede analizar) o "admin" (además administra cuentas y artículos)
    rol = db.Column(db.String(20), default="usuario", nullable=False)

    analisis = db.relationship("Analisis", backref="usuario", lazy="dynamic",
                               order_by="Analisis.fecha.desc()")

    @property
    def es_admin(self):
        return self.rol == "admin"

    def poner_clave(self, clave):
        self.clave_cifrada = generate_password_hash(clave)

    def revisar_clave(self, clave):
        return check_password_hash(self.clave_cifrada, clave)


class Analisis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False, index=True)
    fecha = db.Column(db.DateTime, default=datetime.now, nullable=False)
    # Resultados completos en JSON, para volver a mostrarlos igual que al hacerlos (RF-48)
    resultados_json = db.Column(db.Text, nullable=False)
    # Nombre del PDF guardado en instance/pdfs (RF-46)
    pdf = db.Column(db.String(255))

    @property
    def resultados(self):
        return json.loads(self.resultados_json)

    @property
    def nombres_imagenes(self):
        return [img["nombre"] for img in self.resultados["imagenes"]]


class Mensaje(db.Model):
    """Mensajes del formulario de contacto. Se guardan mientras no haya correo definido."""
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(254), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now, nullable=False)


class SolicitudCalendario(db.Model):
    """Correos de quienes piden la invitación al calendario de uso del microscopio de fluorescencia."""
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(254), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now, nullable=False)


class Contador(db.Model):
    """Contadores del sitio. Hoy solo cuenta visitantes: una persona cuenta una vez por sesión del navegador."""
    clave = db.Column(db.String(40), primary_key=True)
    valor = db.Column(db.Integer, default=0, nullable=False)


class Articulo(db.Model):
    """Artículo del blog. El cuerpo se escribe en Markdown y se limpia al mostrarlo."""
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    resumen = db.Column(db.String(400), default="", nullable=False)
    cuerpo = db.Column(db.Text, default="", nullable=False)
    publicado = db.Column(db.Boolean, default=False, nullable=False)
    creado = db.Column(db.DateTime, default=datetime.now, nullable=False)
    actualizado = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    autor = db.relationship("Usuario")


@login_manager.user_loader
def cargar_usuario(usuario_id):
    return db.session.get(Usuario, int(usuario_id))
