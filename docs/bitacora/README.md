# Bitácora de aprendizaje

Notas personales para aprender el proyecto a la par que se construye. Cada módulo sigue el orden de construcción y coincide con una sesión de la [capacitación](../capacitacion/README.md), así que estas notas también sirven como material para enseñar.

## Módulos

| # | Días (2026) | Lo que se construye | Lo que se aprende | Sesión de capacitación |
|---|---|---|---|---|
| 1 | 8 oct | Entorno de trabajo | Terminal, Python, entornos virtuales (`venv`), `pip`, Git | — |
| 2 | 11 y 12 oct | Paso del boceto a Flask: sitio informativo bilingüe | Rutas, plantillas Jinja, archivos estáticos, traducciones ES/EN | 5 |
| 3 | 13 oct | Cuentas y base de datos | SQLite, SQLAlchemy, Flask-Login, contraseñas cifradas | 5 |
| 4 | 14 y 15 oct | Carga de imagen y resultados con análisis provisional; CSV y PDF | Formularios, subida de archivos, generación de archivos | 1 y 5 |
| 5 | 16 oct | Despliegue en el VPS | Linux, SSH, Nginx, Gunicorn, HTTPS | 5 |
| 6 | Cuando haya datos del cliente | Abrir y explorar la imagen de ejemplo | Imagen digital: píxeles, canales RGB, arreglos de numpy, OpenCV | 2 |
| 7 | Cuando haya datos del cliente | Medición de cabezas: contornos, área, longitud y color | Umbrales, contornos, escala en µm, proporción de rojo y verde | 2 |
| 8 | Cuando haya datos del cliente | Anotación de imágenes y entrenamiento del modelo esqueleto | Redes neuronales, CNN, transfer learning, Mask R-CNN, CVAT | 3 y 4 |
| 9 | Cuando haya datos del cliente | Evaluación del modelo y conexión con el sitio | Entrenamiento, validación y prueba; épocas; métricas; sobreajuste | 4 |

Los módulos 6 a 9 (la red neuronal) esperan a tener las respuestas del cliente sobre tinciones, escala y significado del color. Mientras tanto, el módulo 4 usa un análisis provisional (resultados de ejemplo) para que el flujo completo del sitio ya funcione.

## Cómo se trabaja cada módulo

1. **Antes:** explicación de qué se va a construir y por qué, en unos 5 minutos y sin código.
2. **Durante:** el código se escribe en pasos pequeños. Cada paso se ejecuta y se lee antes de seguir.
3. **Tu turno:** en cada módulo hay una pieza pequeña marcada `# TU TURNO` que escribo yo, con pistas pero sin la respuesta.
4. **Al cerrar:** escribo la nota del día con la plantilla de abajo y se revisa para corregir lo que haya quedado mal entendido.

Además, durante todo el proyecto:

- Cada término nuevo va a [`glosario.md`](glosario.md), definido con mis palabras.
- Cada error que aparezca va a [`errores.md`](errores.md), con su causa y cómo se resolvió.

## Plantilla de la nota del día

Nombre del archivo: `AAAA-MM-DD-tema.md`, por ejemplo `2026-10-08-entorno.md`.

```markdown
# Módulo N — Tema

## Qué construimos

## Conceptos nuevos (en mis palabras)

## Comandos y código que usé

## Lo que no entendí / dudas

## Cómo lo explicaría en la capacitación
```

## Notas

| Fecha | Módulo | Nota |
|---|---|---|
| 7 oct 2026 | 1 — Entorno de trabajo | [Python 3.12 y entorno virtual](2026-10-07-entorno.md) |
| 7 oct 2026 | Transversal | [Ingeniería de software: qué hacer después del boceto](2026-10-07-ingenieria-de-software.md) |
