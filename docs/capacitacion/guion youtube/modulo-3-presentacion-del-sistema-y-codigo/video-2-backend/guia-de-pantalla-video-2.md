# Guía de pantalla del módulo 3, video 2: Backend

Este video no lleva mazo. Se graba la pantalla: el editor con el código, una terminal y el navegador con el sitio, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se hace clic o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar y las cifras que el guion y la pantalla deben respetar. Si algo cambia en el código, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | Qué pasa al subir una imagen | Navegador | F12, pestaña de red, Probar con la imagen de ejemplo; señalar el POST 302 y el GET 200 |
| 2 | Python y Flask | Editor | `requirements.txt`, `requirements-modelo.txt` y `run.py` |
| 3 | Crear la aplicación | Editor | `crear_app` en `app/__init__.py` y `app/extensiones.py` |
| 4 | Las rutas | Terminal, editor | `flask --app run routes` y los decoradores de los tres archivos |
| 5 | Cuentas | Editor | `entrar`, `destino_seguro`, y en `modelos.py` la huella y el cargador de usuario |
| 6 | Protección CSRF | Editor, navegador | Dos líneas de código, el campo oculto en Elementos y la prueba desde la consola |
| 7 | Recuperar la contraseña | Editor | Token firmado, `olvide`, `restablecer`, `correo.py` y las variables del compose |
| 8 | La base de datos | Editor, explorador | Las tres clases de `modelos.py` y la carpeta `instance` |
| 9 | La ruta analizar | Editor | Validaciones, nombre con `uuid`, `try/finally` y `analizar_prueba` |
| 10 | Guardar y mostrar | Editor, navegador | `_guardar_y_mostrar` y recargar con F5 |
| 11 | Cada quien ve lo suyo | Editor, navegador | `_analisis_propio`, `imagen_marcada` y el 404 en la dirección |
| 12 | CSV y PDF | Editor | `reportes.py` y las rutas de descarga |
| 13 | Un proceso, cuatro hilos y las pruebas | Editor, terminal | `Dockerfile`, `nginx.conf`, `python -m pytest` y los archivos de pruebas |
| 14 | Lo que vimos y lo que sigue | Navegador | Página de resultados mientras se resume |

## Antes de grabar

- Sitio con la versión actual del repositorio corriendo en local (`python run.py` o `docker compose up`), con una cuenta de prueba nueva y sin datos de personas reales. El sitio de producción va atrás del repositorio (1.0.0 contra 1.11.0), así que no se usa para este video.
- Dependencias del proyecto instaladas en el entorno de la terminal, incluido `pytest`. Las órdenes `flask --app run routes` y `python -m pytest` se corren en la carpeta del proyecto. Comprobar las dos antes de grabar.
- Navegador con la cuenta de prueba ya iniciada para el tramo 1, a 1440 px de ancho y zoom al 100 %. Abrir F12 en la pestaña de red con la opción de conservar el registro (el 302 y el 200 se ven en la misma lista).
- Editor con las pestañas abiertas en el orden en que se usan: `requirements.txt`, `requirements-modelo.txt`, `run.py`, `app/__init__.py`, `app/extensiones.py`, `app/sitio.py`, `app/cuentas.py`, `app/modelos.py`, `app/correo.py`, `app/analisis/rutas.py`, `app/analisis/reportes.py`, `docker-compose.yml`, `Dockerfile`, `deploy/nginx.conf`, `tests/test_sistema.py` y `tests/test_modelo.py`. Letra grande y números de línea visibles. No mostrar el archivo `.env`.
- Para el tramo 11, una segunda cuenta de prueba con un análisis, para usar su número en la dirección; si no, un número que no exista.
- Para el tramo 8, la carpeta `instance` del entorno de grabación, ya con la base de datos, `pdfs`, `marcadas` y `subidas` creadas por haber corrido un análisis.
- Datos personales: nada de rutas del equipo, cuentas ni correos reales a la vista (barra de título del editor, historial, marcadores).

## Comprobar antes de grabar

- **Resultado de pytest.** El guion no dice cuántas pruebas hay ni cuántas pasan: se lee en pantalla el resultado del día. La documentación (`docs/base-conocimiento`) cita 33 pruebas con una omitida, pero desde entonces se agregaron pruebas (recuperar contraseña) y esa cifra no se debe repetir sin comprobarla. La prueba con los modelos reales se omite si no está `PROBAR_MODELOS=1`; es lo esperado. El 29/10/2026, en este equipo, el resultado fue 39 pruebas recogidas: 38 pasaron y 1 se omitió.
- **La petición sin token (tramo 6).** El guion dice que `fetch('/salir', {method: 'POST'})` sin token da 400 con la sesión abierta. Probarlo antes: debe responder 400 y la sesión debe seguir abierta.
- **`flask --app run routes` (tramo 4).** Debe mostrar las 19 rutas propias más la de archivos estáticos. Si el número cambia, cambiar el guion.
- **Líneas que nombra el guion.** Se comprobaron con el código de la versión 1.11.0 (tabla de abajo). Si cualquiera de esos archivos cambia, hay que volver a comprobarlas.
- **Enlace del correo de recuperación.** El código no usa `ProxyFix`, así que Flask no ve que la visita llegó por HTTPS y el enlace del correo puede salir con `http://` en lugar de `https://` (Nginx lo redirige). El guion no lo menciona. Si se corrige antes de grabar, no cambia nada en el guion.

## Cifras que dice el guion y que hay que mantener

- Rutas: 19 propias (sitio 7, cuentas 5, análisis 7) más la de archivos estáticos; 8 con `login_required` (salir, perfil, analizar, analizar/prueba, resultados, imagen marcada, CSV y PDF).
- Configuración: `MAX_CONTENT_LENGTH` de 300 MB; `MAX_IMAGENES` de 10; contraseña de al menos 8 caracteres; enlace de recuperación de 3,600 segundos.
- Servidor: Gunicorn con 1 proceso, 4 hilos y 1,800 s de tiempo máximo; Nginx con `client_max_body_size 300m` y 1,800 s de espera; cada modelo ocupa unos 176 MB (`docs/base-conocimiento/02-arquitectura.md`).
- Tablas: `Usuario`, `Analisis` (resultados en una columna JSON) y `Mensaje`. Base `instance/imagebio.db`. Carpetas de `instance`: `pdfs`, `marcadas` y `subidas`.
- Extensiones permitidas: BMP, PNG, TIF, TIFF, JPG y JPEG (el guion dice BMP, PNG, TIFF o JPG).
- Respuestas: el POST a `/analizar/prueba` responde 302 y el GET a `/resultados/N`, 200; sin token, un POST responde 400; un análisis ajeno o inexistente responde 404 (no 403).
- CSV con columnas imagen, espermatozoide, `area_px`, `longitud_px`, `area_um2` y `longitud_um`, y una marca de orden de bytes al inicio.

## Líneas que nombra el guion

| Archivo | Líneas |
|---|---|
| `app/__init__.py` | `crear_app` 9; configuración 12 a 26; carpetas 30 a 32; extensiones 34 a 39 (CSRF 35); blueprints 41 a 48; `create_all` 54 y 55 |
| `app/extensiones.py` | completo (7 líneas) |
| `app/cuentas.py` | `destino_seguro` 19; `entrar` 26; registro 36 a 53; inicio de sesión 55 a 59; token 78 a 95; `olvide` 98 a 117; `restablecer` 120 a 137 |
| `app/modelos.py` | `Usuario` 10; huella 20 a 24; `Analisis` 27; `Mensaje` 45; cargador de usuario 54 |
| `app/correo.py` | completo (36 líneas) |
| `app/analisis/rutas.py` | `analizar` 33 a 63 (validaciones 39 a 49; nombre 51 a 56; `try/finally` 58 a 61); `analizar_prueba` 66 a 73; `_guardar_y_mostrar` 81 a 103; `_analisis_propio` 106 a 111; `imagen_marcada` 122 a 129; CSV y PDF 132 a 150 |
| `app/analisis/reportes.py` | `generar_csv` 18 a 28; Agg 8; `_texto` 31 a 33; `_grafica_barras` 36 a 50; `generar_pdf` 87 a 131 |
| `docker-compose.yml` | variables de correo 16 a 20 |
| `Dockerfile` | `CMD` 23 |
| `deploy/nginx.conf` | `client_max_body_size` 41; esperas 49 a 51 |
| `tests/test_sistema.py` | fixture `app` 18 a 30 |
| `tests/test_modelo.py` | prueba con los modelos reales 59 |

## Cosas que el guion dice con cuidado

- La huella de la contraseña no es un cifrado. El campo se llama `clave_cifrada`, y el guion lo dice así.
- La validación de formato mira el nombre del archivo, no su contenido; el guion lo dice y explica quién descubre un archivo que no es imagen.
- No hay herramienta de migraciones: `create_all` crea tablas que faltan, no cambia las que existen.
- Analizar corre dentro de la petición, sin cola de tareas; el guion lo presenta como una decisión de simplicidad con sus límites.
- Las pruebas comprueban que el sitio use bien lo que entrega el modelo, no la calidad científica del conteo ni de la medición.
- La consola (F12) se usa para comprobar la protección CSRF; hay que decir que es una forma de comprobarlo y que no es algo que haga el visitante.
- No se da ningún tiempo de análisis del servidor: no hay medición del VPS.
