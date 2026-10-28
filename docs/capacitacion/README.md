# Capacitación

Curso BIOIMAGE 2026 (UAM Unidad Iztapalapa), con enfoque en investigación y uso de la inteligencia artificial. Se hace solo en video: cuatro módulos, con 15 videos de unos 20 minutos en total. No hay sesiones en vivo.

Este documento es la planeación vigente. Si otra sesión de trabajo la retoma, aquí está el estado y lo que falta.

## Formato

- Todo se graba y se publica en video. Ya no hay sesiones en vivo ni Zoom (problemas de la escuela), así que tampoco hay público presente ni preguntas en el momento.
- Un módulo agrupa varios videos. Cada video dura unos 20 minutos (unas 3,500 palabras a 175 palabras por minuto) y, después del primero de cada módulo, abre con una frase que lo une con el anterior.
- Perfil del público: mixto, con algo de programación y algo de biología.
- Lenguaje profesional pero platicado: sin comentarios que sugieran que el público no sabe, con un término técnico explicado en una frase la primera vez que aparece, y con las ideas intuitivas antes de la definición formal.
- Apoyos visuales sencillos donde ayuden (la tabla de píxeles, una pendiente, una guitarra y un ukulele para la transferencia) y ejemplos numéricos cortos.
- No hay un taller de práctica. El código y los cuadernos de Colab se muestran en demostración.
- Cada video tiene dos versiones del guion: la humanizada y la natural (escrita para decirse en voz alta), las dos con su documento de Word.

## Plan de videos (borrador)

El objetivo es reducir los 24 videos que saldrían de 4 módulos de 2 horas a unos 15. Presupuesto: unos 300 minutos de habla en total.

| Módulo | Carácter | Videos | Contenido | Estado |
|---|---|---|---|---|
| 1 | Teoría fundamental | 3 | Problema e imagen digital; IA, entrenamiento y neurona; capas, aprendizaje y cierre | Guion terminado en [`guion youtube/modulo-1-el-problema-y-las-bases`](guion%20youtube/modulo-1-el-problema-y-las-bases) |
| 2 | Teoría con más detalle | 4 | Redes convolucionales; Mask R-CNN; aprendizaje por transferencia; datos, anotación, entrenamiento y validación | Guiones de los 4 videos terminados en [`guion youtube/modulo-2-teoria-con-mas-detalle`](guion%20youtube/modulo-2-teoria-con-mas-detalle) |
| 3 | Presentación del sistema y, sobre todo, código | 4 | Frontend (con el sitio funcionando); backend; inferencia con recortes; medición, escala y retos | Guion pendiente |
| 4 | Código y despliegue | 4 | Cuaderno de Colab en dos videos; despliegue (VPS, SSH, Docker); Nginx, dominio, HTTPS y cierre | Guion pendiente |
| Total | | 15 | | |

El módulo 1 salió de seis videos (unos 110 minutos de habla), guardados en [`guion youtube/anteriores-6-videos`](guion%20youtube/anteriores-6-videos), a tres de unos 21 minutos. Se quitó material del problema y se dejó casi todo lo teórico (imagen digital, redes neuronales y cómo aprenden).

## Temario por módulo

### Módulo 1. El problema y las bases

Guion terminado: [`guion youtube/modulo-1-el-problema-y-las-bases`](guion%20youtube/modulo-1-el-problema-y-las-bases).

- Video 1, el problema y la imagen digital: el caso de estudio (contar y medir espermatozoides en fotos de microscopio), qué se quiere medir, el camino de una imagen a un número, y qué es una imagen digital (píxeles, color, resolución, histograma, formatos, aumentos y escala).
- Video 2, inteligencia artificial, entrenamiento y neurona: definiciones, palabras clave, entrenamiento contra inferencia, el umbral como primer intento, la neurona, el sesgo y la activación.
- Video 3, capas, aprendizaje y cierre: capas y red, una red pequeña a mano, profundidad, cómo aprende una red, anotación, aprendizaje supervisado, pérdida, descenso del gradiente, retropropagación, lotes y épocas, semillas, límites de un modelo.

Material que se quitó del módulo 1 y debe reaparecer en otro lugar o en un documento escrito (por confirmar):

- Colab, Python, Flask y servidor: módulo 3.
- Cómo se ve un cuaderno de Colab: módulo 4.
- Media y desviación estándar, y los dos tipos de imagen con su modelo: módulo 3.
- Glosario y preguntas frecuentes: documento escrito.

### Módulo 2. Teoría con más detalle

Guiones de los 4 videos terminados en `guion youtube/modulo-2-teoria-con-mas-detalle/`. Sigue siendo teórico, pero con más detalle que el módulo 1. Ya no incluye umbral, neurona, capa, pérdida ni descenso del gradiente, que están en el módulo 1.

- Video 1, cómo ve una imagen una red convolucional: el filtro que recorre la imagen, con el ejemplo numérico de 3 por 3. Terminado, con plan visual y mazo.
- Video 2, Mask R-CNN, en lenguaje sencillo: cinco etapas, anclas, umbrales, IoU, repetidos, las cinco pérdidas y límites. Terminado, con plan visual y mazo.
- Video 3, aprendizaje por transferencia (guitarra y ukulele): qué se reutiliza de la red preentrenada con COCO, qué se cambia, congelar o afinar, un entrenamiento de ejemplo y sus límites. Terminado, con plan visual y mazo.
- Video 4, datos y entrenamiento en teoría (pasan aquí desde el antiguo módulo 4): cuántas imágenes hacen falta, anotación en CVAT, criterio de anotación y quién valida; entrenamiento y validación, sobreajuste y la gráfica de curvas. Terminado, con plan visual y mazo.

### Módulo 3. Presentación del sistema y código

Guion pendiente. Aquí el sitio se presenta funcionando y, a partir de ahí, casi todo es código en pantalla.

- Video 1, frontend: se abre con el sitio funcionando (visitante, cuenta, análisis, resultados, descargas y "Mis análisis"; abrir una imagen marcada y revisar un contorno a mano) y se explica cómo está hecho, en código: plantillas Jinja2 (`app/templates`), Bootstrap, `estilos.css` y `sitio.js`, y la pantalla de resultados con el zoom y la gráfica. No hay framework de frontend.
- Video 2, backend: Flask, las rutas y qué pasa cuando se sube una imagen (`app/__init__.py`, `app/analisis/rutas.py`, cuentas y base de datos).
- Video 3, inferencia, en código: la misma preparación que en el entrenamiento, recortes (teselas), juntar resultados y quitar repetidos. El modelo se carga una vez.
- Video 4, medición y retos, en código: contorno, área, largo y escala (60 px = 1 µm en todas las imágenes, para estandarizar el tamaño; el largo en el código es el lado mayor del rectángulo mínimo que encierra el contorno). Retos y cómo se resolvieron: espermatozoides empalmados, falsos positivos y la escala.
- Material que se quitó del módulo 1 y reaparece aquí: Python, Flask, servidor, media y desviación estándar, y los dos tipos de imagen con su modelo.

### Módulo 4. Código y despliegue

Guion pendiente. Cierra el código y lleva el sitio a internet.

- Videos 1 y 2, el cuaderno de Colab, en código (`entrenamiento/entrenar_mask_rcnn.ipynb`; el cuaderno se quitó del módulo 1 y se retoma aquí). Se muestra con `MODO_PRUEBA = True`, sin correr el entrenamiento completo. Reparto propuesto, por confirmar contra el cuaderno real: el video 1 va del entorno y la configuración hasta preparar las imágenes y los recortes (leer las etiquetas, separar entrenamiento y validación); el video 2 va de construir la red a partir de una ya entrenada hasta entrenar, ver los resultados y exportar el modelo.
- Videos 3 y 4, **despliegue en la nube y cierre** (el video 3 llega hasta Docker Compose; el 4 va de Nginx al cierre). Es contenido vivido en el proyecto, con ejemplos reales:
  - El VPS y la clave SSH: la clave pública va al servidor y la privada no sale de la computadora. Mejor una clave por uso.
  - Docker en tres ideas: imagen (la receta), contenedor (el programa corriendo) y volumen (donde viven los datos, para que reconstruir no los borre).
  - Docker Compose: un archivo que levanta los dos servicios del sitio, `web` y `nginx`, con un comando.
  - Nginx, el dominio y HTTPS: Nginx recibe las visitas; el dominio apunta a la IP con un registro A; Let's Encrypt da el certificado.
  - Actualizar el sitio: `git push` en la computadora y `git pull` más `docker compose up -d --build` en el servidor. Los modelos y el archivo `.env` no están en Git.
  - Errores reales que sirven de ejemplo: un registro CNAME de `www` que chocaba con el registro A, y una configuración de Nginx que no arranca sin certificado (por eso hay `nginx.conf` y `nginx-http.conf`).
  - La guía paso a paso está en [`../despliegue.md`](../despliegue.md).
- Cierre: las tres ideas principales (la red localiza, el código mide, las personas verifican), dónde están los materiales y cómo enviar preguntas por escrito.

## Estado del despliegue

El sitio ya está en un VPS de Hostinger con Ubuntu, Docker y Nginx, con el dominio `imagebiopro.cloud` y HTTPS con Let's Encrypt (el certificado vence en enero de 2027 y se renueva con una tarea programada). Falta que el contenido real de Nosotros, Aliados e infografías esté cargado y que los modelos estén copiados en el servidor.

## Pendientes

- Confirmar el plan de videos (cuántos por módulo y qué se recorta) y la duración máxima de cada video.
- Escribir los guiones de los módulos 3 y 4, con el mismo formato que los del módulo 1.
- Armar los tres mazos del módulo 1 (hoy hay seis mazos, uno por cada video anterior) y los de los otros módulos: numerados, con letra grande, pocas ideas por diapositiva y dibujos sencillos.
- Definir las fechas de publicación de los videos y dónde se publican. El calendario del flyer (23 al 27 de octubre) era para sesiones en vivo.
- Corregir el README principal y los guiones para que todo diga lo mismo sobre cómo se mide el largo (hoy el código mide el lado mayor del rectángulo mínimo, no la longitud a lo largo de la curva).
- El color se calcula pero ya no se muestra (indicación del cliente del 16 de octubre): los guiones y los mazos no deben decir que el sistema lo entrega.

## Materiales

Se preparan a partir del trabajo de desarrollo.

- [x] Guion del módulo 1 en tres videos: [`guion youtube/modulo-1-el-problema-y-las-bases`](guion%20youtube/modulo-1-el-problema-y-las-bases).
- [x] Guiones del módulo 2 en cuatro videos: [`guion youtube/modulo-2-teoria-con-mas-detalle`](guion%20youtube/modulo-2-teoria-con-mas-detalle).
- [ ] Guiones de los módulos 3 y 4 (cada video tiene ya su carpeta vacía en `guion youtube`).
- [ ] Mazos por video.
- [ ] Capturas del sitio (en `capturas/`, ya hay las del módulo 1).
- [ ] Cuaderno de Colab para mostrar en el módulo 4: `entrenamiento/entrenar_mask_rcnn.ipynb`.

Notas de la reunión de ensayo del 20 de octubre: [`ensayo-presentacion.md`](ensayo-presentacion.md) y [`transcripcion-ensayo-combinada.md`](transcripcion-ensayo-combinada.md).
