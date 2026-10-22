# Capacitación

8 horas de capacitación en línea para la comunidad universitaria y el grupo del proyecto, en 4 sesiones de 2 horas por Zoom. Se anuncia como el curso BIOIMAGE 2026 (UAM Unidad Iztapalapa), con enfoque en investigación y uso de la inteligencia artificial.

Este documento es la planeación vigente. Si otra sesión de trabajo la retoma, aquí está el estado y lo que falta.

## Participantes y formato

- Unas 6 o 7 personas en el grupo base, aunque el curso es público y podrían conectarse más. Perfil mixto: algo de programación y algo de biología. Dos personas con mucha experiencia.
- Es una charla informativa y educativa, estilo ponencia. Quien presenta habla; el público puede preguntar en cualquier momento y quien presenta no hace preguntas al público. Las respuestas son breves, y lo muy técnico se deja para el final.
- Las sesiones se graban y se suben a redes. Hay que decirlo al inicio de cada una.
- Lenguaje profesional pero platicado: sin comentarios que sugieran que el grupo no sabe, con un término técnico explicado en una frase la primera vez que aparece, y con las ideas intuitivas antes de la definición formal.
- Apoyos visuales sencillos donde ayuden (la tabla de píxeles, una pendiente, una guitarra y un ukulele para la transferencia) y ejemplos numéricos cortos.
- No hay un taller de práctica con los participantes. El código y los cuadernos de Colab se muestran en demostración.

## Calendario (según el flyer)

| Sesión | Fecha (2026) | Horario | Tema |
|---|---|---|---|
| 1 | Viernes 23 de octubre | 6:00 a 8:00 pm | El problema y el sitio |
| 2 | Sábado 24 de octubre | 9:00 a 11:00 am | Cómo aprende la computadora |
| 3 | Lunes 26 de octubre | 6:00 a 8:00 pm | Cómo funciona el sistema por dentro |
| 4 | Martes 27 de octubre | 6:00 a 8:00 pm | Datos, reentrenamiento y despliegue |

El flyer anuncia cuatro áreas de enfoque: frontend para el desarrollo web, backend en el desarrollo web, redes neuronales convolucionales y cloud computing. El temario las cubre así: frontend en la sesión 1, redes convolucionales en la 2, backend en la 3 y cloud en la 4. El 28 de octubre queda libre para la entrega.

## Temario por sesión

Referencia de tiempo: 170 palabras por minuto. En cada sesión caben unos 50 minutos de habla (unas 8,500 palabras); el resto es demostración, pausa y margen.

### Sesión 1. El problema y el sitio

Guion terminado: [`guion-sesion-1.md`](guion-sesion-1.md).

- El caso de estudio: contar y medir espermatozoides en fotos de microscopio. La red localiza y el código mide.
- Por qué una plataforma web, y entrenamiento contra inferencia.
- Qué es una imagen digital: píxeles, brillo, formatos y escala.
- El sitio en vivo: visitante, cuenta, análisis, resultados, descargas y "Mis análisis".
- Lo que no es un espermatozoide: falsos positivos (en programación, alucinaciones).

### Sesión 2. Cómo aprende la computadora

Guion pendiente. Es la sesión más pesada: lo que cabe en 2 horas obliga a recortar.

- Umbralización como primer intento, y por qué no basta. Se presenta como la solución sencilla y se conecta con la red: la red retoma esa idea y suma otros factores.
- La neurona, la capa y la red, con una figura sencilla.
- Cómo se ve una imagen una red convolucional: el filtro que recorre la imagen, con el ejemplo numérico de 3 por 3.
- Cómo aprende: predecir, medir el error, ajustar y repetir. Pérdida, descenso del gradiente (la pendiente en la niebla), tasa de aprendizaje y retropropagación explicada primero con el juego de Batalla naval.
- Mask R-CNN y aprendizaje por transferencia (guitarra y ukulele), en lenguaje sencillo.
- Orden pedido en el ensayo: primero qué es una imagen (sesión 1), después qué es una red, después cómo aprende, y al final los resultados. Los términos (hiperparámetro, retropropagación) se dicen primero con palabras sencillas y después con su definición formal.
- Los retos del modelo pasan a la sesión 3 para que esta no se desborde.

### Sesión 3. Cómo funciona el sistema por dentro

Guion pendiente.

- Backend: Flask, las rutas y qué pasa cuando se sube una imagen.
- Cómo se usa el modelo (inferencia): la misma preparación que en el entrenamiento, recortes (teselas), juntar resultados y quitar repetidos. El modelo se carga una vez.
- La medición: contorno, área, largo y escala (60 px = 1 µm en todas las imágenes, para estandarizar el tamaño). El largo en el código es el lado mayor del rectángulo mínimo que encierra el contorno.
- Retos y cómo se resolvieron: espermatozoides empalmados, falsos positivos y la escala.
- Demostración: abrir una imagen marcada y revisar un contorno a mano.

### Sesión 4. Datos, reentrenamiento y despliegue

Guion pendiente. Es una sesión con mucho contenido; si no cabe, el reentrenamiento se muestra más corto y los detalles quedan en material aparte.

- Datos: cuántas imágenes hacen falta, anotación en CVAT, criterio de anotación y quién valida.
- Entrenamiento y validación: sobreajuste y la gráfica de curvas.
- Reentrenar en Colab: qué se cambia y qué esperar. Se muestra el cuaderno con `MODO_PRUEBA = True`, sin correr el entrenamiento completo en vivo.
- **Despliegue en la nube (bloque propio, unos 20 minutos).** Es contenido vivido en el proyecto, con ejemplos reales:
  - El VPS y la clave SSH: la clave pública va al servidor y la privada no sale de la computadora. Mejor una clave por uso.
  - Docker en tres ideas: imagen (la receta), contenedor (el programa corriendo) y volumen (donde viven los datos, para que reconstruir no los borre).
  - Docker Compose: un archivo que levanta los dos servicios del sitio, `web` y `nginx`, con un comando.
  - Nginx, el dominio y HTTPS: Nginx recibe las visitas; el dominio apunta a la IP con un registro A; Let's Encrypt da el certificado.
  - Actualizar el sitio: `git push` en la computadora y `git pull` más `docker compose up -d --build` en el servidor. Los modelos y el archivo `.env` no están en Git.
  - Errores reales que sirven de ejemplo: un registro CNAME de `www` que chocaba con el registro A, y una configuración de Nginx que no arranca sin certificado (por eso hay `nginx.conf` y `nginx-http.conf`).
  - La guía paso a paso está en [`../despliegue.md`](../despliegue.md).
- Cierre: las tres ideas principales (la red localiza, el código mide, las personas verifican), dónde están los materiales y cómo enviar preguntas por escrito.

## Estado del despliegue

El sitio ya está en un VPS de Hostinger con Ubuntu, Docker y Nginx, con el dominio `imagebiopro.cloud` y HTTPS con Let's Encrypt (el certificado vence en enero de 2027 y se renueva con una tarea programada). Para el viernes falta: que el contenido real de Nosotros, Aliados e infografías esté cargado y que los modelos estén copiados en el servidor.

## Pendientes

- Confirmar con el cliente las fechas y horarios del flyer, el número de participantes y quién envía el enlace de Zoom.
- Escribir los guiones de las sesiones 2, 3 y 4 con el mismo formato que el de la sesión 1 (idea que debe quedar, ideas en orden, frases ancla y tiempos).
- Armar las diapositivas de cada sesión: numeradas, con letra grande, pocas ideas por diapositiva y dibujos sencillos. La presentación actual tiene 129 diapositivas y sigue el orden anterior.
- Decidir cuándo se responden las preguntas que lleguen por escrito.
- Confirmar qué se dice sobre dónde se publica la grabación.
- Corregir el README principal y el guion para que todo diga lo mismo sobre cómo se mide el largo (hoy el código mide el lado mayor del rectángulo mínimo, no la longitud a lo largo de la curva).

## Materiales

Se preparan a partir del trabajo de desarrollo. El material de cada sesión se termina a más tardar el día anterior.

- [x] Guion de la sesión 1.
- [ ] Guiones de las sesiones 2, 3 y 4.
- [ ] Diapositivas por sesión.
- [ ] Capturas del sitio (en `capturas/`, ya hay las de la sesión 1).
- [ ] Cuaderno de Colab para mostrar en la sesión 4: `entrenamiento/entrenar_mask_rcnn.ipynb`.
- [ ] Grabaciones de las sesiones.

Notas de la reunión de ensayo del 20 de octubre: [`ensayo-presentacion.md`](ensayo-presentacion.md) y [`transcripcion-ensayo-combinada.md`](transcripcion-ensayo-combinada.md).
