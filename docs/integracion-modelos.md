# Integración de los modelos al sitio

Plan del 17 de octubre de 2026. Estado: **por aprobar**, no se ha escrito código del sitio.

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
- **Escala en micras.** Sigue provisional: 60 píxeles por micra, sin calibrar. En campo claro no hay ninguna calibración conocida.
- **Datos de entrenamiento.** Fluorescencia: 4 fotos y 258 etiquetas. Campo claro: 4 fotos y 45 etiquetas. Las pruebas en campo claro se hicieron con otras tomas de las mismas escenas del entrenamiento; no se sabe cómo responderá con otras muestras, otras tinciones o fotos con compresión.
- **Conteos aproximados.** En zonas con muchos espermatozoides juntos el modelo repite o parte contornos y no encuentra algunos (en fluorescencia, de 85 de cada 100 amontonados). Los conteos son aproximados.

## Decisiones pendientes

1. Aprobar el plan o cambiarlo.
2. Análisis largos: limitar fotos y tamaño por subida (más simple) o procesar en segundo plano (más trabajo). Recomendación: empezar limitando y dejar el segundo plano como mejora.
3. Cambiar "cabeza" por "espermatozoide" en pantalla, CSV y PDF.

## Tiempo estimado

De 2 a 3 días de trabajo, dejando el último tramo antes del 28 de octubre para probar en el servidor.
