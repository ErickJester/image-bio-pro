# Módulo 2 — Aplicación Flask mínima

Fecha: 13 de octubre de 2026. Estado: en curso (primer paso: una ruta de inicio).

## Qué construimos

La app Flask más pequeña que funciona: un paquete `app` con una función que crea la aplicación y una sola ruta, `/`, que responde "Hola, Image Bio Pro". Es el primer paso del [esqueleto que camina](2026-10-07-ingenieria-de-software.md): todavía no hay plantillas, traducciones ni base de datos.

## Conceptos nuevos (en mis palabras)

- **Flask:** librería de Python para hacer sitios web. Recibe una petición del navegador y devuelve una respuesta.
- **Ruta (`@app.route`):** une una dirección del sitio (`/`) con la función que responde cuando alguien la visita.
- **Función fábrica (`crear_app`):** en lugar de crear la aplicación suelta, se crea dentro de una función. Así después se puede crear con otra configuración (pruebas, servidor) y todo queda ordenado.
- **Paquete (`app/__init__.py`):** una carpeta con un archivo `__init__.py` es un paquete de Python y se puede importar como `app`.
- **`__pycache__`:** carpeta que Python genera sola con código ya compilado (`.pyc`). No se escribe a mano ni se sube a Git.

## Comandos y código que usé

`app/__init__.py`:

```python
from flask import Flask


def crear_app():
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        return "Hola, Image Bio Pro"

    return app
```

Para verla en el navegador (con el entorno virtual activo):

```powershell
flask --app app run
```

Y se abre la dirección que muestre la terminal, normalmente `http://127.0.0.1:5000`.

`.gitignore` creado hoy, para que Git deje de mostrar `.venv/` y `__pycache__/` como pendientes de subir.

## Lo que no entendí / dudas

-

## Cómo lo explicaría en la capacitación

> Un sitio Flask empieza con muy poco: una función que crea la aplicación y una ruta que dice qué responder cuando alguien visita una dirección. Todo lo demás (páginas, idiomas, base de datos, el clasificador) se va agregando encima de este esqueleto, un paso a la vez.
