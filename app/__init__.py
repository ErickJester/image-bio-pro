import os
from datetime import datetime

from flask import Flask, request, session

from app.extensiones import csrf, db, login_manager


def crear_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.update(
        # En el servidor, SECRET_KEY debe venir de una variable de entorno
        SECRET_KEY=os.environ.get("SECRET_KEY", "solo-para-desarrollo"),
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, "imagebio.db"),
        # Hasta 10 imágenes BMP sin compresión (RF-35)
        MAX_CONTENT_LENGTH=300 * 1024 * 1024,
        MAX_IMAGENES=10,
        # Solo para desarrollo: muestra un temporizador en la pantalla de espera del análisis.
        # Se activa con la variable de entorno MOSTRAR_TEMPORIZADOR=1; en el servidor del cliente va apagado.
        MOSTRAR_TEMPORIZADOR=os.environ.get("MOSTRAR_TEMPORIZADOR") == "1",
        CARPETA_PDF=os.path.join(app.instance_path, "pdfs"),
        CARPETA_SUBIDAS=os.path.join(app.instance_path, "subidas"),
        # Copias reducidas con las cabezas marcadas, para volver a ver un análisis (RF-48)
        CARPETA_MARCADAS=os.path.join(app.instance_path, "marcadas"),
        # Imágenes que los administradores suben a los artículos
        CARPETA_ARTICULOS=os.path.join(app.instance_path, "articulos"),
        # Banco de imágenes: se guarda en el disco del servidor (50 GB). Topes en GB; ver docs/despliegue.md
        CARPETA_BANCO=os.path.join(app.instance_path, "banco"),
        BANCO_LIMITE_GB=float(os.environ.get("BANCO_LIMITE_GB", "30")),
        BANCO_MARGEN_GB=float(os.environ.get("BANCO_MARGEN_GB", "5")),
        BANCO_MAX_POR_ENVIO=20,
    )
    if config:
        app.config.update(config)

    for carpeta in (app.instance_path, app.config["CARPETA_PDF"], app.config["CARPETA_SUBIDAS"],
                    app.config["CARPETA_MARCADAS"], app.config["CARPETA_ARTICULOS"], app.config["CARPETA_BANCO"]):
        os.makedirs(carpeta, exist_ok=True)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "cuentas.entrar"
    login_manager.login_message = "Inicia sesión para continuar."
    login_manager.login_message_category = "info"

    from app import modelos  # noqa: F401  (registra las tablas)
    from app.admin import bp as bp_admin, crear_admins, html_seguro
    from app.analisis.rutas import bp as bp_analisis
    from app.banco import bp as bp_banco
    from app.cuentas import bp as bp_cuentas
    from app.sitio import bp as bp_sitio

    app.register_blueprint(bp_sitio)
    app.register_blueprint(bp_cuentas)
    app.register_blueprint(bp_analisis)
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_banco)
    app.cli.add_command(crear_admins)
    app.jinja_env.filters["markdown_seguro"] = html_seguro

    @app.before_request
    def contar_visitante():
        """Suma un visitante la primera vez que una sesión abre una página (sin guardar datos de la persona)."""
        if request.method != "GET" or not request.endpoint or request.endpoint == "static" or session.get("contado"):
            return
        from app.modelos import Contador
        fila = db.session.get(Contador, "visitantes")
        if fila is None:
            fila = Contador(clave="visitantes", valor=0)
            db.session.add(fila)
        fila.valor += 1
        db.session.commit()
        session["contado"] = True

    @app.context_processor
    def datos_globales():
        from app.modelos import Contador
        fila = db.session.get(Contador, "visitantes")
        return {"anio": datetime.now().year, "visitantes": fila.valor if fila else 0}

    with app.app_context():
        db.create_all()
        # Bases creadas antes de los roles no tienen la columna: se agrega sin perder datos
        columnas = [c["name"] for c in db.inspect(db.engine).get_columns("usuario")]
        if "rol" not in columnas:
            db.session.execute(db.text("ALTER TABLE usuario ADD COLUMN rol VARCHAR(20) NOT NULL DEFAULT 'usuario'"))
            db.session.commit()
        if "imagen_banco" in db.inspect(db.engine).get_table_names():
            columnas_banco = [c["name"] for c in db.inspect(db.engine).get_columns("imagen_banco")]
            if "estado" not in columnas_banco:
                db.session.execute(db.text(
                    "ALTER TABLE imagen_banco ADD COLUMN estado VARCHAR(20) NOT NULL DEFAULT 'pendiente'"))
                db.session.commit()

    return app
