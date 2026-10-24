# Capacitación

Curso BIOIMAGE 2026 (UAM Unidad Iztapalapa), con enfoque en investigación y uso de la inteligencia artificial. Se hace solo en video: cuatro módulos, con unos 10 videos de unos 20 minutos en total. No hay sesiones en vivo.

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

El objetivo es reducir los 24 videos que saldrían de 4 módulos de 2 horas a unos 10. Presupuesto: unos 200 minutos de habla en total.

| Módulo | Videos | Contenido | Estado |
|---|---|---|---|
| 1 | 3 | Problema e imagen digital; IA, entrenamiento y neurona; capas, aprendizaje y cierre | Guion terminado en [`guion youtube/modulo-1`](guion%20youtube/modulo-1) |
| 2 | 2 | Redes convolucionales, Mask R-CNN y transferencia | Guion pendiente |
| 3 | 2 o 3 | El sistema por dentro | Guion pendiente |
| 4 | 3 | Datos, reentrenamiento y despliegue | Guion pendiente |
| Total | 10 a 11 | | |

El módulo 1 salió de seis videos (unos 110 minutos de habla), guardados en [`guion youtube`](guion%20youtube), a tres de unos 21 minutos. Se quitó material del problema y se dejó casi todo lo teórico (imagen digital, redes neuronales y cómo aprenden).

## Temario por módulo

### Módulo 1. El problema y las bases

Guion terminado: [`guion youtube/modulo-1`](guion%20youtube/modulo-1).

- Video 1, el problema y la imagen digital: el caso de estudio (contar y medir espermatozoides en fotos de microscopio), qué se quiere medir, el camino de una imagen a un número, y qué es una imagen digital (píxeles, color, resolución, histograma, formatos, aumentos y escala).
- Video 2, inteligencia artificial, entrenamiento y neurona: definiciones, palabras clave, entrenamiento contra inferencia, el umbral como primer intento, la neurona, el sesgo y la activación.
- Video 3, capas, aprendizaje y cierre: capas y red, una red pequeña a mano, profundidad, cómo aprende una red, anotación, aprendizaje supervisado, pérdida, descenso del gradiente, retropropagación, lotes y épocas, semillas, límites de un modelo.

Material que se quitó del módulo 1 y debe reaparecer en otro lugar o en un documento escrito (por confirmar):

- Colab, Python, Flask y servidor: módulo 3.
- Cómo se ve un cuaderno de Colab: módulo 4.
- Media y desviación estándar, y los dos tipos de imagen con su modelo: módulo 3.
- Glosario y preguntas frecuentes: documento escrito.

### Módulo 2. Redes convolucionales y transferencia

Guion pendiente. Ya no incluye umbral, neurona, capa, pérdida ni descenso del gradiente, que están en el módulo 1.

- Cómo ve una imagen una red convolucional: el filtro que recorre la imagen, con el ejemplo numérico de 3 por 3.
- Mask R-CNN y aprendizaje por transferencia (guitarra y ukulele), en lenguaje sencillo.
- Los retos del modelo pasan al módulo 3.

### Módulo 3. Cómo funciona el sistema por dentro

Guion pendiente.

- Backend: Flask, las rutas y qué pasa cuando se sube una imagen.
- Cómo se usa el modelo (inferencia): la misma preparación que en el entrenamiento, recortes (teselas), juntar resultados y quitar repetidos. El modelo se carga una vez.
- La medición: contorno, área, largo y escala (60 px = 1 µm en todas las imágenes, para estandarizar el tamaño). El largo en el código es el lado mayor del rectángulo mínimo que encierra el contorno.
- Retos y cómo se resolvieron: espermatozoides empalmados, falsos positivos y la escala.
- Demostración: abrir una imagen marcada y revisar un contorno a mano.

### Módulo 4. Datos, reentrenamiento y despliegue

Guion pendiente. Si no cabe, el reentrenamiento se muestra más corto y los detalles quedan en material aparte.

- Datos: cuántas imágenes hacen falta, anotación en CVAT, criterio de anotación y quién valida.
- Entrenamiento y validación: sobreajuste y la gráfica de curvas.
- Reentrenar en Colab: qué se cambia y qué esperar. Se muestra el cuaderno con `MODO_PRUEBA = True`, sin correr el entrenamiento completo.
- **Despliegue en la nube (bloque propio, unos 20 minutos, un video).** Es contenido vivido en el proyecto, con ejemplos reales:
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
- Escribir los guiones de los módulos 2, 3 y 4, con el mismo formato que los del módulo 1.
- Armar los tres mazos del módulo 1 (hoy hay seis mazos, uno por cada video anterior) y los de los otros módulos: numerados, con letra grande, pocas ideas por diapositiva y dibujos sencillos.
- Definir las fechas de publicación de los videos y dónde se publican. El calendario del flyer (23 al 27 de octubre) era para sesiones en vivo.
- Corregir el README principal y los guiones para que todo diga lo mismo sobre cómo se mide el largo (hoy el código mide el lado mayor del rectángulo mínimo, no la longitud a lo largo de la curva).
- El color se calcula pero ya no se muestra (indicación del cliente del 16 de octubre): los guiones y los mazos no deben decir que el sistema lo entrega.

## Materiales

Se preparan a partir del trabajo de desarrollo.

- [x] Guion del módulo 1 en tres videos: [`guion youtube/modulo-1`](guion%20youtube/modulo-1).
- [ ] Guiones de los módulos 2, 3 y 4.
- [ ] Mazos por video.
- [ ] Capturas del sitio (en `capturas/`, ya hay las del módulo 1).
- [ ] Cuaderno de Colab para mostrar en el módulo 4: `entrenamiento/entrenar_mask_rcnn.ipynb`.

Notas de la reunión de ensayo del 20 de octubre: [`ensayo-presentacion.md`](ensayo-presentacion.md) y [`transcripcion-ensayo-combinada.md`](transcripcion-ensayo-combinada.md).
