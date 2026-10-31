# Guía de pantalla del módulo 4, video 2: El cuaderno de Colab, segunda parte

Este video no lleva mazo. Se graba la pantalla: el cuaderno de Colab, celda por celda, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de celda, se ejecuta o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, lo que se espera ver al ejecutar cada celda y las cifras que el guion debe respetar. Si cambia el cuaderno, las fotos o el perfil, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Celdas | Qué se hace |
|---|---|---|---|
| 1 | Paso 7: la red | 17 y 18 | Se explican el texto y `construir_modelo`; se ejecuta y cuenta los parámetros |
| 2 | Paso 8: cómo se mide si funciona | 19 y 20 | Se recorren `detectar`, el IoU, `quitar_repetidos`, `aciertos_de_zona`, `metricas` y `validar`; se ejecuta (no imprime) |
| 3 | Paso 9: preparar el entrenamiento | 21 y 22 | Se explican el guardado atómico, las configuraciones, el optimizador y la reanudación; se ejecuta (no imprime) |
| 4 | Paso 9: entrenar | 23 | Se recorre el ciclo y se ejecutan las dos épocas del modo de prueba |
| 5 | Paso 10: los resultados | 24 a 28 | Gráficas, mejor modelo, barrido de umbrales, tipos de foto y fotos de revisión |
| 6 | Paso 11: exportar el modelo | 29 y 30 | Se guarda `modelo_cabezas.pt`, se explica cómo lo carga el servidor y se comprueba |
| 7 | Mejorar el modelo y de aquí al servidor | 31 | La última celda de texto y la carpeta `model/` del proyecto |

Los números de celda cuentan todas las celdas del archivo `.ipynb` (de texto y de código) desde cero; Colab no los muestra. En pantalla se buscan por su título.

## Antes de grabar

- El mismo cuaderno del video 1 en Colab, con el entorno de ejecución en GPU y las celdas hasta la revisión visual de los recortes ya ejecutadas (celdas 0 a 16). Si la sesión se cerró, se corren de nuevo desde la primera.
- `MODO_PRUEBA = True` y `PERFIL = "fluorescencia"`. El entrenamiento que se ejecuta son solo dos épocas cortas.
- Números de línea activados en Colab (Herramientas, Configuración, Editor).
- **Cambio previo en el cuaderno.** La última línea que imprime la celda de exportación (línea 70 de la celda del Paso 11) dice de quién es el servidor y nombra a quien pidió el sitio. Antes de grabar hay que reescribirla («la del servidor»); si no, saldrá en pantalla al ejecutar la celda. Se suma a las dos líneas del video 1 (introducción, línea 35, y configuración, línea 32). Cambiar el cuaderno es un cambio del proyecto y lleva versión; está sin hacer.
- La primera ejecución de la celda del Paso 7 descarga los pesos de COCO (hace falta internet en la sesión de Colab).
- La carpeta `model/` del proyecto abierta en un explorador de archivos, para el último tramo.

## Qué se espera al ejecutar cada celda

Marcado como **real** lo que se ejecutó el 30/10/2026 en CPU en esta computadora, en modo de prueba, con la foto de ejemplo del sitio como única foto, los contornos del modelo como etiquetas y la red sin los pesos de COCO (para no descargarlos). Sirve para ver el formato; los números no significan nada. Marcado como **por confirmar** lo que solo se puede ver en Colab.

| Celda | Qué imprime | Estado |
|---|---|---|
| 18 (la red) | `Parámetros: 43.9 M (43.7 M se ajustan al entrenar)` | Calculado con la misma construcción de la red; por confirmar en Colab, donde además descarga los pesos de COCO |
| 20 (métricas) | Nada: solo define funciones | Real |
| 22 (preparación) | Nada en la primera corrida. Si reanuda: `Reanudando desde la época N de M` | Real |
| 23 (entrenamiento) | Una línea por época: `Época   1/2  pérdida 35.9461  (0.8 min)  \| validación: AP50 0.000 …  <- mejor` | Real para el formato; en Colab, con tarjeta gráfica, cada época tarda mucho menos y las cifras son otras |
| 25 (gráficas) | Dos gráficas: pérdida y métricas de validación | Real para el formato (ver `figuras/curvas-de-prueba.png`) |
| 26 (mejor modelo) | `Mejor modelo: época …`, validación final, tabla de siete umbrales, umbral elegido, avisos y una línea por tipo de foto | Real para el formato |
| 28 (fotos) | `prueba.png: 41 etiquetados, 9 detectados` y la foto dibujada | Real para el formato (ver `figuras/revision-de-prueba.png`). En Colab habrá una línea por foto |
| 30 (exportar) | `Guardado: … (176 MB)`, versiones, `Diferencia máxima … (debe ser menor que 1e-3)`, conteos, segundos por tesela y minutos por foto | Real para el formato. Los segundos por tesela dependen de la CPU (2.5 s en esta computadora) |

Salidas del ejemplo del guion, comprobadas con las funciones del cuaderno: IoU de dos cuadrados de 10 por 10 corridos 5 píxeles, 0.333; con 10 etiquetados, 8 marcas y 6 aciertos, precisión 0.75, recall 0.6 y F1 0.667.

## Cifras que el guion usa

- Parámetros: 43.9 millones, de los que se ajustan 43.7 (los bloques `conv1` y `layer1` de la parte que ve la imagen quedan congelados; se ajustan `layer2`, `layer3` y `layer4`).
- Clases de la red de COCO: 91. Clases del cuaderno: 2 (fondo y espermatozoide).
- Anclas por defecto: de 20 a 576; fluorescencia, de 16 a 256; campo claro, de 32 a 512. Tres formas de caja (0.5, 1 y 2). Umbral de cajas traslapadas, 0.6. Hasta 300 detecciones por tesela. Épsilon de la normalización, 0.0 en los modelos guardados y 0.00001 en las capas normales.
- Teselas: foto de 1,792 por 1,374 con teselas de 512 y paso de 384, 5 columnas por 4 filas, 20 teselas; foto de 3,584 por 2,748, 9 por 7, 63 teselas.
- Descartes en `detectar`: puntaje menor a 0.05; objeto que toca un borde interno de la tesela; IoU de 0.5 entre teselas; filtro de contenido de 0.5.
- Aciertos: IoU de al menos 0.5. Métricas: precisión, exhaustividad (recall), F1 y AP50.
- Optimizador: SGD, momento 0.9, decaimiento de pesos 0.0001. Tasa de aprendizaje: 0.005 en el perfil de fluorescencia, con calentamiento de 100 iteraciones y descenso en coseno hasta el 1 % del valor inicial. Norma máxima del gradiente: 10.
- Entrenamiento real de fluorescencia: 60 épocas, 400 recortes por época, lote de 4, o sea 100 iteraciones por época; se valida cada 5 épocas y se guarda `ultimo.pt` cada 10. Modo de prueba: 2 épocas, 16 recortes, 4 iteraciones por época (8 en total), por lo que el calentamiento no termina.
- Pesos: `ultimo.pt` unos 350 MB (351 MB en la prueba), `mejor.pt` y `modelo_cabezas.pt`, unos 176 MB.
- Barrido de umbrales: 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 y 0.9. Con menos de 10 espermatozoides en la validación no se elige umbral (queda el de la configuración); con menos de 50, aviso de estimación poco firme; por tipo de foto, con menos de 20, aviso de cifra inestable.
- Comprobación de la exportación: diferencia máxima menor que 1e-3; las detecciones pueden diferir hasta en 2 o el 5 %.
- En `model/` de esta computadora: `fluorescencia.pt` viene de la corrida 02 con el cuaderno 0.3.1 y `campo_claro.pt` de la corrida 04 con el 0.5.0 (así lo dice `model/README.md` y lo confirman las versiones guardadas dentro de los archivos). Cada uno pesa unos 176 MB. El campo claro se exportó con umbral 0.5.

## Líneas que nombra el guion

Las líneas se cuentan dentro de cada celda.

| Celda | Líneas |
|---|---|
| Paso 7, texto (17) | 1 a 10 |
| Paso 7, la red (18) | normalización congelada 9 a 15; `construir_modelo` 18 a 44 (opciones 21 a 27, pesos 28 a 32, dos clases 33 a 37, épsilon 38 a 43); creación y conteo 47 a 50 |
| Paso 8, texto (19) | 1 a 10 |
| Paso 8, métricas (20) | `interseccion_mascaras`, `iou_mascaras` y `quitar_repetidos` 1 a 28; `_posiciones` 31 a 34; `detectar` 37 a 85; `etiquetas_de_zona` 88 a 100; `aciertos_de_zona` 103 a 118; `metricas` 121 a 139; `pares_de_validacion` y `validar` 142 a 157 |
| Paso 9, texto (21) | 1 a 7 |
| Paso 9, preparación (22) | `escribir_atomico` 1 a 5; `configuracion_del_modelo` 8 a 17; `configuracion_de_entrenamiento` 20 a 28; optimizador 31 a 34; `factor_lr` 37 a 41; planificador y precisión mixta 44 a 46; reanudar 48 a 68 |
| Paso 9, entrenamiento (23) | ciclo de la época 1 a 25; registro, validación y guardado 27 a 44; línea impresa 45 a 51 |
| Paso 10, texto (24) | 1 a 5 |
| Paso 10, gráficas (25) | 1 a 13 |
| Paso 10, mejor modelo (26) | carga y medida 1 a 7; barrido y elección 9 a 23; por tipo de foto 24 a 38 |
| Paso 10, fotos (28) | 1 a 29 |
| Paso 11, texto (29) | 1 a 6 |
| Paso 11, exportar (30) | guardar 1 a 8; `cargar_modelo_para_inferencia` 11 a 29; comprobación 32 a 62; tiempos 64 a 69 (la 70 se cambia antes de grabar) |
| Mejorar el modelo (31) | 1 a 7 |

## Cosas que el guion dice con cuidado

- **El entrenamiento que se ejecuta es de mentira.** Son dos épocas cortas del modo de prueba. El guion lo dice y no le da ningún valor a la pérdida ni a la validación que salgan. Con tan pocas iteraciones, el calentamiento de la tasa de aprendizaje ni termina.
- **Los números de la prueba local no son los de Colab.** La pérdida de 35.9 y 24.2, el AP50 de 0 y los 2.5 segundos por tesela salen de una CPU y de una red sin los pesos de COCO. No se citan en el guion.
- **Los 43.9 y 43.7 millones de parámetros** están calculados con la misma construcción, no leídos de una sesión de Colab. Confirmarlos al grabar.
- **Los archivos de `model/` y la documentación no coinciden del todo.** `docs/base-conocimiento/04-resultados.md` dice que el mejor modelo de fluorescencia es de la época 20, con AP50 de 0.888 y umbral de 0.8. El archivo `model/fluorescencia.pt` guarda la época 25, un AP50 de validación de 0.915 y un umbral de 0.9. El guion no cita ninguna de esas cifras. Hay que decidir cuál es la vigente antes de citarlas en otro lado.
- **Con cuatro fotos, la validación sale de las mismas fotos.** El guion lo recuerda al hablar de la elección del umbral y de la validación de campo claro (dos espermatozoides).
- **Los pesos de COCO se descargan la primera vez** que se ejecuta la celda del Paso 7, y eso exige internet en la sesión de Colab. El guion lo menciona solo de pasada.
- **La carpeta `model/` no está en Git.** El guion lo dice y deja el cómo copiarla para el video siguiente.
- **No se muestran los documentos del proyecto.** Lo que explican se dice hablando.
- **El guion pasa de los 20 minutos previstos** (23.1 minutos en las dos versiones de habla, sin contar los tiempos de ejecución de las celdas). Si hay que recortar, lo más fácil es el detalle de `detectar` y `quitar_repetidos` en el tramo 2, que repite lo del módulo 3.
