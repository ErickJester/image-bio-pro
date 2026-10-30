# Plan del módulo 3: presentación del sistema y código

Plan para escribir los guiones de los cuatro videos del módulo 3 (videos 8 a 11 del curso). Está hecho leyendo el código del repositorio en la versión 1.11.0, la documentación en `docs/` y el README de capacitación. Los guiones de los videos 1 y 2 ya están hechos, en formato de pantalla; los videos 3 y 4 faltan.

> **Cambio de orden (30 de octubre de 2026).** El backend abre el módulo y el sitio funcionando va al final. Orden actual: 1 Backend, 2 Inferencia con recortes, 3 Medición, escala y retos, 4 Frontend: el sitio funcionando. Los números 8 a 11 de abajo son los del curso. Los títulos y el orden del sitio (`_VIDEOS` en `app/sitio.py`) todavía siguen el orden anterior.

## Qué es el módulo

- Es el primer módulo donde el sitio se ve funcionando y casi todo es código en pantalla. No hay taller de práctica: el código se muestra en demostración.
- Cuatro videos de unos 20 minutos (unas 3,300 a 3,500 palabras cada uno). Cada uno abre con una frase que lo une con el anterior. El video 1 (backend) abre el módulo, uniendo con el módulo 2, y el video 4 (el sitio funcionando) lo cierra.
- Mismo formato que los módulos anteriores: guion humanizado y guion natural, cada uno con su Word; una guía de pantalla en lugar del plan visual y del mazo (el módulo se graba mostrando el sitio y el código mientras se habla; los bloques `> En pantalla:` del guion dicen qué se abre en cada tramo); y los datos del video para YouTube (título, descripción, capítulos).
- Los títulos y las descripciones cortas ya están en el sitio (`app/sitio.py`, diccionario `_VIDEOS`, números 8 a 11): Frontend: el sitio funcionando; Backend; Inferencia con recortes; Medición, escala y retos. Los guiones deben usar esos títulos.

## Material que se quitó del módulo 1 y vuelve aquí

El README de capacitación lo deja pendiente. Se puede reutilizar, ya escrito, de `guion youtube/anteriores-6-videos`:

| Material | Dónde está | Dónde vuelve |
|---|---|---|
| Python, Flask y servidor | Video 3 anterior, diapositivas 7, 8 y 10 | Video 1 (backend) |
| Media y desviación estándar, con un ejemplo | Video 1 anterior, diapositiva 9 | Video 3 (medición) |
| Dos tipos de imagen, dos modelos | Video 2 anterior, diapositiva 10 | Video 2 (inferencia) |
| Entrenamiento aparte, inferencia en el servidor | Video 4 anterior, diapositiva 1 | Video 2 (inferencia) |
| Colab y cómo se ve un cuaderno | Video 3 anterior, diapositivas 6 y 11 | Módulo 4, no aquí |

## Vista general

| Video | Título | Qué es | Archivos que se muestran |
|---|---|---|---|
| 8 (módulo 3, video 1) | Backend | Qué pasa desde que se sube una imagen hasta que se descargan los resultados | `app/__init__.py`, `app/analisis/rutas.py`, `app/cuentas.py`, `app/modelos.py`, `app/analisis/reportes.py`, `tests/` |
| 9 (video 2) | Inferencia con recortes | Cómo el servidor usa el modelo | `app/analisis/modelo.py` |
| 10 (video 3) | Medición, escala y retos | Del contorno a las medidas, la escala y lo que costó resolver | `app/analisis/medicion.py` |
| 11 (video 4) | Frontend: el sitio funcionando | Sitio en demostración y después cómo está hecho | `app/templates/` (base, resultados, ia), `app/static/estilos.css`, `app/static/sitio.js` |

## Video 8: Backend

**Objetivo:** seguir una imagen desde que se sube hasta que se guardan sus resultados, y explicar por qué cada pieza está donde está.

**Frase de unión:** el módulo 2 terminó con una red y unos datos, y un modelo por sí solo es un archivo que no hace nada; hace falta un sitio. Este video abre el módulo: presenta los cuatro videos y muestra el sitio por detrás, usándolo solo lo necesario. La demostración completa queda para el último video.

**Diapositivas propuestas (14):**

| N.º | Diapositiva | Qué se muestra |
|---|---|---|
| 1 | Qué pasa al subir una imagen | El recorrido: navegador, Nginx, Gunicorn, Flask, modelo, medición, resultados |
| 2 | Python y Flask | Reutilizar las diapositivas del video 3 anterior |
| 3 | Crear la aplicación | `crear_app` en `app/__init__.py`: configuración, carpetas, extensiones, blueprints |
| 4 | Las rutas | Tabla de rutas por blueprint: sitio, cuentas y análisis |
| 5 | Cuentas | Registro e inicio con Flask-Login; contraseña cifrada con `generate_password_hash`; `destino_seguro` contra redirecciones a otros sitios |
| 6 | Protección CSRF | Flask-WTF y el token en cada formulario |
| 7 | Recuperar la contraseña | Token firmado con `itsdangerous` (dura una hora), la misma respuesta exista o no la cuenta, correo por SMTP desde variables de entorno |
| 8 | La base de datos | SQLite con SQLAlchemy: `Usuario`, `Analisis` (resultados en JSON) y `Mensaje` |
| 9 | La ruta `/analizar` | Validaciones, nombre generado con `uuid`, guardar, analizar y borrar la imagen |
| 10 | Guardar y mostrar | `_guardar_y_mostrar`: el diccionario de resultados, el JSON, el PDF y la redirección |
| 11 | Cada quien ve lo suyo | `_analisis_propio` responde 404 si no es tuyo; las imágenes marcadas solo se sirven si están en tus resultados |
| 12 | CSV y PDF | `reportes.py`: CSV, gráfica con matplotlib y PDF con fpdf2 |
| 13 | Un proceso, cuatro hilos y las pruebas | Por qué un solo proceso; qué comprueba `pytest` y qué no |
| 14 | Lo que vimos y lo que sigue | Puente a la inferencia |

**Cifras comprobadas:** `MAX_IMAGENES` = 10; `MAX_CONTENT_LENGTH` = 300 MB; contraseña de al menos 8 caracteres; enlace de recuperación de 3,600 segundos; un proceso de Gunicorn con 4 hilos y 1,800 s por petición (`docs/base-conocimiento/02-arquitectura.md`).

**Preparar antes de grabar:** correr `python -m pytest` en pantalla y anotar el resultado de ese día. La documentación dice 33 pruebas con 32 pasadas y 1 omitida, pero desde entonces se agregaron pruebas (recuperar contraseña); no repetir esa cifra sin comprobarla.

## Video 9: Inferencia con recortes

**Objetivo:** que se entienda cómo `modelo.py` repite en el servidor lo que hizo el cuaderno, y por qué hay que mantenerlos iguales. Une con el módulo 2 (video 2 sobre Mask R-CNN y video 4 sobre validación).

**Frase de unión:** hasta ahora la red era una caja; ahora se ve cómo se le da una foto y cómo se recogen sus respuestas.

**Diapositivas propuestas (14):**

| N.º | Diapositiva | Qué se muestra |
|---|---|---|
| 1 | De la foto al contorno | Los cuatro pasos del encabezado de `modelo.py` |
| 2 | Dos modelos y cómo se elige | `tipo_de_foto`: mediana del brillo máximo de la foto reducida a un octavo; arriba de 127, campo claro |
| 3 | El archivo del modelo | Pesos y configuración dentro del `.pt`: `lado`, `solape`, `anclas`, `bn_eps`, `umbral_deteccion` |
| 4 | Cargar el modelo una sola vez | `_cargar`: candado, carga segura (`weights_only=True`), comprobación de las claves y `set_num_threads` |
| 5 | Preparar la foto | `preparar_imagen`: reducción, brillo máximo de los canales e inversión en campo claro, igual que en el entrenamiento |
| 6 | Las teselas | `_posiciones` con un ejemplo: la imagen de muestra, de 1200 × 900, da 9 teselas; una foto de 1792 × 1374, 20 |
| 7 | Cada tesela por la red | Lotes de 2, relleno en las orillas, `inference_mode`, máscara con 0.5 y puntaje mínimo de 0.05 |
| 8 | Lo que toca el borde interno | Se descarta porque la tesela vecina lo ve entero (se une con la diapositiva 12 del video 2) |
| 9 | Juntar los resultados | Coordenadas de la foto, duplicados con IoU de 0.5 o más, filtro de contenido de 0.5 |
| 10 | De la máscara al contorno | `_a_contorno` y el umbral guardado en el modelo (0.9 en fluorescencia) |
| 11 | Un análisis a la vez | `_BLOQUEO_INFERENCIA`; por qué (un núcleo, 176 MB por modelo); variables `MODELOS_DIR` y `TORCH_HILOS` |
| 12 | Si no hay modelo | La detección provisional (`detectar_cabezas`: Otsu, el rojo domina al verde, apertura) y el aviso en rojo |
| 13 | Comprobar que es igual al cuaderno | Los conteos 114, 9, 2, 1 y 43 en cinco fotos |
| 14 | Lo que vimos y lo que sigue | Puente a la medición |

**Cifras comprobadas con el código:** teselas de 512 con traslape de 128 en fluorescencia (paso de 384); en campo claro, foto reducida a la mitad y teselas de 640 con traslape de 384. Una foto de 1792 × 1374 en fluorescencia usa 20 teselas, y una de 3584 × 2748, 63. En campo claro, 4 y 24 respectivamente.

**Cuidado con los tiempos:** hay cifras de escritorio (unos 40 s por foto de 1792 en fluorescencia) y de Colab en CPU (unos 2.6 s por tesela). Del servidor real no hay medición. No dar un tiempo del VPS en el video hasta medirlo.

## Video 10: Medición, escala y retos

**Objetivo:** mostrar cómo el código convierte un contorno en números, de qué depende la escala y qué dificultades tuvo el proyecto. Cierra el módulo.

**Frase de unión:** la red ya entregó los contornos; ahora el código los mide.

**Diapositivas propuestas (14):**

| N.º | Diapositiva | Qué se muestra |
|---|---|---|
| 1 | La red localiza, el código mide | `analizar_imagen`: el orden de lo que se hace con cada contorno |
| 2 | Área y largo | `medir_cabeza`: píxeles de la máscara y lado mayor del rectángulo mínimo (`cv2.minAreaRect`) |
| 3 | La escala | `PX_POR_MICRA` = 60: el área entre 60² y el largo entre 60; la regla de 300 px (5 µm) en la imagen marcada |
| 4 | Una escala provisional | No sale de las fotos: no traen barra ni regla. Es la indicación del cliente. Plan de la tabla de escalas por resolución |
| 5 | Media y desviación estándar | `resumen` con un ejemplo numérico; reutilizar la diapositiva del video 1 anterior |
| 6 | El histograma | `histograma`: 10 intervalos entre el mínimo y el máximo; en el promedio entre imágenes, un rango común |
| 7 | El resultado de una imagen | Los estados (`ok`, `aviso`, `no_analizada`) y qué hace el sitio con pocos espermatozoides |
| 8 | La imagen marcada | `dibujar_marcas`: borde oscuro y trazo blanco, número, regla, copia reducida y copia ampliada |
| 9 | Reto 1: espermatozoides empalmados | Contornos repetidos o partidos y los tres filtros |
| 10 | Reto 2: falsos positivos | Fibras y manchas; el 0.96 sobre un núcleo de célula; no hay ejemplos negativos |
| 11 | Reto 3: el largo | Es el lado mayor del rectángulo mínimo, no la longitud de la curva, y el contorno incluye el primer tramo de la cola |
| 12 | Reto 4: las fotos | Dos tipos de foto, JPG con compresión, imágenes muy grandes y la espera |
| 13 | Lo que no se mide y lo que falta | Medir de cabeza a cola, calibrar la escala, aviso de imagen ajena, medir en el VPS, control contra tratamiento |
| 14 | Lo que vimos en el módulo 3 y lo que sigue | Puente al módulo 4 |

**Cifras comprobadas:** `PX_POR_MICRA` = 60; regla de 300 px = 5 µm; histograma de 10 intervalos; aviso con menos de 3 espermatozoides; área mínima de 20 píxeles solo en la detección provisional.

## Video 11: Frontend, el sitio funcionando

**Objetivo:** que quien ve el video sepa usar el sitio completo y entienda con qué está hecha cada pantalla. Es el último video del módulo 3. Va en dos partes: unos 8 minutos de recorrido y 12 de código.

**Frase de unión:** el backend, el modelo y la medición ocurren por detrás; ahora se ve todo junto en el sitio que cualquiera usa. Cierra el módulo y apunta al módulo 4 (el cuaderno de Colab y el despliegue).

**Diapositivas propuestas (16):**

| N.º | Diapositiva | Qué se muestra | Pantallas existentes |
|---|---|---|---|
| 1 | De la teoría al sitio | Mapa del módulo 3 | |
| 2 | Lo que ve el visitante | Inicio, Nosotros, Aliados, Infografías, Contacto | 01 a 06 |
| 3 | Español e inglés | El selector y la traducción automática | 07 |
| 4 | Crear la cuenta y entrar | Registro, inicio de sesión y recuperar la contraseña | 08 a 11 |
| 5 | Analizar una imagen | Formatos, hasta 10 imágenes, errores, la espera | 12 a 14 |
| 6 | Los resultados | Conteo, área media, desviación estándar y la imagen marcada | 15 a 17 |
| 7 | Revisar a mano | Zoom, detalle al pasar el cursor y tabla por espermatozoide | 18 a 24 |
| 8 | Varias imágenes, descargas e historial | Promedio, CSV, PDF y "Mis análisis" | 25 a 31 |
| 9 | Cómo está hecho el frontend | Plantillas Jinja2, Bootstrap, una hoja de estilos y un archivo de JavaScript. Sin framework | |
| 10 | La plantilla base | `base.html`: bloques, menú, mensajes (`get_flashed_messages`), pie | |
| 11 | Una plantilla con datos | `resultados.html`: `for`, `if`, filtros como `sort`, `url_for` y el token CSRF de los formularios | |
| 12 | La imagen con una zona por espermatozoide | El SVG con un polígono por contorno y el detalle de `sitio.js` (`iniciarDetalleEsperma`) | |
| 13 | El visor con zoom | Ventana de Bootstrap con eventos del puntero (`iniciarVisorZoom`) | |
| 14 | La gráfica | Chart.js con datos que el servidor mete con `tojson` | |
| 15 | Detalles que importan | `aria-label`, la tabla como alternativa a la gráfica, `no-imprimir` y `notranslate` | |
| 16 | Lo que vimos y lo que sigue | Resumen y puente al backend | |

**Cifras comprobadas:** 15 plantillas en `app/templates`; `estilos.css` de 1,210 líneas; `sitio.js` de 273 líneas y `videos.js` de 86; Bootstrap 5.3.3 y Chart.js 4.4.1 desde CDN; hasta 10 imágenes por análisis y 300 MB por envío.

**Preparar antes de grabar:**
- Las 31 capturas de `docs/capacitacion/capturas` son del 19 de octubre. Desde entonces cambiaron el pie de página (v1.10), Videos e Infografías (v1.8) y apareció "¿Olvidaste tu contraseña?" (v1.11). Hay que repetir al menos las de inicio, el pie, la entrada y el menú, y agregar la de recuperar contraseña.
- Decidir dónde se graba la demostración (ver "Decisiones").

## Cosas del código que el guion debe decir con cuidado

1. **El color se calcula pero no se muestra.** `medir_cabeza` calcula `indice_color` y `asignar_grados` los reparte en 10 grados, y se guardan, pero ni la pantalla ni el CSV ni el PDF los muestran (indicación del cliente del 16 de octubre). El guion no debe decir que el sistema entrega el color. Conviene mencionarlo en una frase, con el código a la vista, para que no sorprenda.
2. **Los nombres heredados.** En los datos guardados la lista de espermatozoides se llama `cabezas`, y la clase del modelo, "cabeza", aunque el contorno cubre la cabeza y el primer tramo de la cola. El código lo explica en un comentario; el video debe decirlo.
3. **El largo.** Es el lado mayor del rectángulo mínimo del contorno, no la longitud a lo largo de la curva. El README principal aún dice otra cosa en algunos lugares (pendiente anotado en el README de capacitación).
4. **La escala.** Es una constante provisional. La tabla de escalas y el mensaje a Saúl para pedir la calibración siguen pendientes (`docs/integracion-modelos.md`).
5. **Los números del modelo.** Los documentos dicen AP50 0.888 y umbral 0.8 para el modelo del sitio, pero el archivo `model/fluorescencia.pt` guarda 0.9148 y 0.9. Si el video 9 dice un umbral, debe ser el del archivo (0.9).
6. **La calidad.** Las pruebas automáticas y la prueba de integración comprueban que el sitio usa bien el modelo, no la calidad científica. El guion lo dice así.

## Decisiones que hacen falta

1. **Dónde se graba la demostración.** El sitio en producción está en la versión 1.0.0 y el repositorio va en la 1.11.0. Opciones: (a) actualizar el VPS antes de grabar (`git pull` y `docker compose up -d --build`) y grabar en `imagebiopro.cloud`; (b) grabar en la computadora con `python run.py`. La opción (a) muestra el sitio real, pero recuperar la contraseña exige configurar el correo en el servidor; con (b) se puede mostrar el aviso de "correo sin configurar".
2. **Cuánto código se muestra en pantalla.** Propuesta: fragmentos de 8 a 15 líneas por diapositiva, con el nombre del archivo, y una captura del editor con el código completo solo cuando ayuda. No más de 8 fragmentos por video.
3. **Si el video 11 se divide.** Con 8 minutos de recorrido más 12 de código, queda justo. Alternativa: dejar la demostración del sitio al principio del video 11 y pasar la parte de Chart.js y el visor de zoom a un recuadro opcional.
4. **Los títulos de YouTube.** Siguen la numeración del curso (8 a 11). Hay que confirmar que los títulos del sitio (`_VIDEOS`) son los que se van a usar.

## Orden de trabajo propuesto

Un video a la vez, en este orden, con el mismo recorrido que en el módulo 2:

1. Guion humanizado, con las cifras comprobadas en el código.
2. Guion natural.
3. Word de los dos.
4. Guía de pantalla (preparación, cifras y líneas de código que nombra el guion).
5. Comprobar que las dos versiones traen las mismas cifras.
6. Archivo `.txt` de YouTube, cuando exista el video grabado, para que los capítulos salgan de los tiempos reales.

Los videos 9 y 10 (inferencia y medición) usan las mismas cifras de `modelo.py` y `medicion.py`, y el video 11 (el sitio) se apoya en los tres anteriores, así que conviene escribirlos en orden.
