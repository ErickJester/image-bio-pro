# Integración de los modelos al sitio

Plan del 17 de octubre de 2026. Estado: **pasos 1 a 6 hechos el 17 de octubre**, probados en una computadora de escritorio con fotos reales. **Falta medir en el VPS real** (tiempos y memoria) y la tabla de escalas.

## Punto de partida

- Modelos entrenados en Colab con `entrenamiento/entrenar_mask_rcnn.ipynb`:
  - `corrida_02`: fluorescencia (fondo oscuro), teselas de 512 px.
  - `corrida_04`: campo claro (fondo claro), fotos reducidas a la mitad, teselas de 640 px.
- Hoy el sitio detecta con un umbral de color de OpenCV (`app/analisis/medicion.py`) y marca los resultados como provisionales.
- El análisis corre dentro de la petición, imagen por imagen (`app/analisis/rutas.py`). Gunicorn y Nginx tienen un tope de 300 segundos.
- Los resultados incluyen el grado y el índice de color, que el cliente pidió omitir (chat del 16 de octubre, de segunda mano).

## Pasos

1. **Módulo nuevo `app/analisis/modelo.py`.**
   - Carga los dos modelos una sola vez, la primera vez que se usan.
   - Mide el brillo de la foto (mediana del valor máximo de rojo, verde y azul; más de 127 es fondo claro) y elige el modelo.
   - Aplica la misma preparación del entrenamiento (reducción, valor máximo de los canales, inversión en campo claro), corta en teselas con traslape, junta los resultados, quita los contornos repetidos y devuelve los contornos en las coordenadas de la foto original (dividiendo entre la reducción).
   - Lee de cada archivo `.pt` su configuración: `lado`, `solape`, `anclas`, `roi_mascara` (si falta, 14), `reduccion_foto`, `bn_eps`, `umbral_deteccion` y `umbral_contenido`.
2. **Conectarlo a `medicion.analizar_imagen`** en lugar de la detección provisional. Conteo, área, largo, histograma, CSV y PDF salen de los contornos del modelo.
3. **Color: declarado sin usar.** El campo se sigue guardando, pero deja de mostrarse en resultados, CSV y PDF.
4. **Avisos.** El mensaje de detección provisional se cambia por uno de modelo preliminar entrenado con pocas imágenes. Si faltan los archivos de los modelos, el sitio usa la detección anterior y lo avisa.
5. **Servidor.** PyTorch y torchvision para CPU en `requirements.txt` y en el contenedor. Los `.pt` (unos 176 MB cada uno) no van a Git: se montan como volumen de solo lectura. Limitar los hilos con `torch.set_num_threads`.
6. **Pruebas y documentación.** Las pruebas actuales deben seguir pasando. Pruebas nuevas que se saltan solas si no están los modelos. Actualizar el README y `docs/despliegue.md`.

## Riesgos y cosas a tener en cuenta

- **Tiempo en el VPS.** En una computadora de escritorio, sin otros procesos, se midieron unos 40 s por foto de 1792 px en fluorescencia y unos 10 a 20 s en campo claro. El plan más barato del VPS probablemente tiene una sola CPU y puede tardar varias veces más. Hay que medirlo en el servidor real.
- **Tope de 300 segundos.** Con varias fotos grandes se puede rebasar. El cliente dijo que 2 o 3 minutos le parece bien (RNF-06). Opciones: limitar fotos y tamaño por subida, o analizar en segundo plano con página de espera.
- **Qué se mide.** Los contornos cubren el espermatozoide visible completo, con parte de la cola, no solo la cabeza. Los textos "Área de la cabeza" y "Largo de la cabeza" deberían decir "espermatozoide" en pantalla, CSV y PDF.
- **Escala en micras.** Sigue provisional: 60 píxeles por micra, sin calibrar. En campo claro no hay ninguna calibración conocida. Ver la sección "Escala en micras" más abajo.
- **Datos de entrenamiento.** Fluorescencia: 4 fotos y 258 etiquetas. Campo claro: 4 fotos y 45 etiquetas. Las pruebas en campo claro se hicieron con otras tomas de las mismas escenas del entrenamiento; no se sabe cómo responderá con otras muestras, otras tinciones o fotos con compresión.
- **Conteos aproximados.** En zonas con muchos espermatozoides juntos el modelo repite o parte contornos y no encuentra algunos (en fluorescencia, de 85 de cada 100 amontonados). Los conteos son aproximados.

## Escala en micras

**Por qué no se puede sacar de las fotos.** Las fotos del cliente no traen barra de escala ni regla impresa, y la cabecera de los BMP no trae medida. Ni el cliente ni los usuarios conocen la escala. De la imagen sola no se puede deducir cuánto mide un píxel sin suponer el tamaño de algo, y no se debe suponer nada del espermatozoide.

**De qué depende realmente.** Del aumento del objetivo (40x, ya conocido), del tamaño del sensor de la cámara y de cualquier adaptador, y de la resolución a la que se guarda la foto (1792 o 3584 px de ancho). Se calibra una sola vez por equipo; los usuarios no tienen que conocerla.

**Ya implementado (provisional).** Constante `PX_POR_MICRA = 60` en `app/analisis/medicion.py`, a partir de la indicación de Saúl del 16 de octubre (una raya de 300 px equivale a 5 micras). La imagen marcada lleva abajo a la izquierda una regla de 300 px con el texto "300 px = 5 micras (escala provisional)", y los resultados, el CSV y el PDF avisan que la escala no está calibrada.

**Solución propuesta.**
1. Una tabla de escalas en un archivo de configuración, con píxeles por micra para cada resolución (1792 y 3584). Se edita sin tocar el código; el sitio la usa en cada análisis. Si una resolución no está en la tabla, usa la constante provisional y lo dice.
2. Cómo se obtiene cada valor, de más a menos confiable: una foto de una regla de calibración (micrómetro de platina) tomada con ese microscopio y esa cámara a 40x; la calibración del programa de la cámara; o el cálculo a partir de la ficha de la cámara y el adaptador.
3. Una herramienta pequeña para el desarrollador, no para los usuarios: dada la foto de la regla y la distancia conocida entre dos marcas, calcula el valor y lo guarda en la tabla.
4. Mientras no haya un valor medido, la medida en píxeles es el dato principal y las micras se presentan como aproximadas.
5. Si algún día las fotos traen una barra de escala impresa, se puede leer con procesamiento de imagen (una línea recta y larga en una esquina), sin necesidad de una red neuronal. Hace falta ver ejemplos reales primero.

**Pregunta abierta.** Si las fotos de 1792 y de 3584 px son del mismo campo con distinta resolución, cada una necesita su propio valor (el de 3584 sería el doble). Si no lo son, la constante actual estaría mal para una de las dos.

## Mensaje para Saúl (borrador)

> Hola Saúl. Para dar las medidas en micras necesito la escala real de las fotos, y las fotos no la traen: no tienen barra de escala ni regla impresa. Mientras tanto estamos usando la que me indicaste (300 px = 5 micras, o sea 60 px por micra) y el sitio avisa en cada resultado que es provisional.
>
> ¿Me ayudas a preguntarle al cliente tres cosas?
>
> 1. ¿Con qué cámara y con qué programa toman las fotos del microscopio (marca y modelo)? Si el programa tiene una opción para calibrar o medir distancias, ahí suele estar la escala.
> 2. ¿Tienen una regla de calibración, es decir, una laminilla con una regla grabada (micrómetro de platina)? Si la tienen, ¿pueden tomarle una foto con el objetivo de 40x, a las dos resoluciones en que guardan las fotos? Con eso se calcula la escala exacta una sola vez.
> 3. Las fotos vienen en dos tamaños (1792 × 1374 y 3584 × 2748 píxeles). ¿Son del mismo campo del microscopio con distinta resolución, o se tomaron con otro ajuste?
>
> Con eso queda resuelto, y los usuarios no tendrán que conocer ni escribir la escala. Gracias.

## Decisiones

1. Plan aprobado el 17 de octubre.
2. **Análisis largos: no se limitó el número de imágenes.** El cliente pidió poder subir 10 imágenes a la vez (RF-35) y una barra de progreso (RF-36), así que se mantienen los dos y se resolvió con tiempos de espera altos (1800 s en Gunicorn y Nginx), un solo proceso con 4 hilos que carga los modelos una vez, y análisis de uno en uno (los demás esperan turno). Si en el VPS 10 imágenes tardan demasiado, se limita por subida o se pasa a segundo plano.
3. "Cabeza" cambió a "espermatozoide" en pantalla, CSV y PDF. Dentro de los datos guardados la lista sigue llamándose `cabezas`, para que los análisis ya guardados se abran.
4. Color: se sigue calculando y guardando, pero ya no se muestra (resultados, CSV y PDF). Sale de la indicación de Saúl del 16 de octubre.
5. **Pendiente:** enviar el mensaje a Saúl y, con la respuesta, armar la tabla de escalas y la herramienta de calibración.

## Qué quedó hecho

- `app/analisis/modelo.py`: elige el modelo por el brillo de la foto, la prepara igual que en el entrenamiento, analiza por teselas, junta y limpia. Se comprobó que da los mismos conteos que el cuaderno (114, 9, 2, 1 y 43 contornos en cinco fotos).
- `app/analisis/medicion.py`: usa el modelo si está disponible y, si no, la detección provisional; cada imagen guarda con qué detector se analizó.
- Resultados, CSV y PDF: textos nuevos, sin el color, con aviso de modelo preliminar o de detección provisional.
- Servidor: `requirements-modelo.txt`, `Dockerfile`, `docker-compose.yml` (volumen `model/`), Nginx y la guía `docs/despliegue.md`.
- Pruebas: 27 pasan sin PyTorch; con PyTorch y los modelos, 28.

## Tiempo estimado

La integración se hizo en un día. El tiempo que queda hasta el 28 de octubre es para probar en el servidor real, afinar los tiempos de espera y calibrar la escala.
