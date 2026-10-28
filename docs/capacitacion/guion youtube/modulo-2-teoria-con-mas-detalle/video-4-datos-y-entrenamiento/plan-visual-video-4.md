# Plan visual del módulo 2, video 4: Datos, entrenamiento y validación

Lo que lleva cada diapositiva. El guion habla de estas imágenes y de estos números tal como están aquí, así que el mazo debe respetarlos. Si algo cambia en el mazo, hay que cambiar el guion (las dos versiones) y viceversa.

Estilo: el de los videos 1 a 3 del módulo 2 (fondo oscuro y claro alternados, azul marino, azul petróleo, celeste y naranja como único acento, letra grande, pocas ideas por diapositiva). Los dibujos son propios, en SVG. Lo marcado como calculado sale de la salida guardada del cuaderno de entrenamiento (`entrenamiento/entrenar_mask_rcnn.ipynb`, corrida de ejemplo, perfil de fluorescencia) o del modelo del sitio.

Origen de las imágenes:
- Calculado: se genera con Python y se guarda como PNG o como gráfica.
- SVG: dibujo propio dentro del mazo.
- Reutilizado: imagen de un mazo anterior del módulo 2 (curvas del video 3).
- Las fotos del cliente no se publican. Donde haga falta una foto se usa la imagen de muestra del sitio (`app/static/muestras/prueba.png`, dibujada por computadora) y la diapositiva lo dice.

| N.º | Diapositiva | Qué se ve | Origen |
|---|---|---|---|
| 1 | Datos, entrenamiento y validación | Etiqueta "Módulo 2 · Video 4". Tres tarjetas en fila con una flecha entre ellas: "Datos" (foto y contorno), "Entrenamiento" (la red ajusta sus pesos) y "Validación" (prueba con lo que no vio). Debajo, una línea: "Un modelo vale lo que valen sus datos y su prueba". | SVG |
| 2 | Qué es un dato | Una foto con su contorno dibujado (recorte de la imagen de muestra, con su contorno). A la derecha, una gráfica de barras con las etiquetas por foto: 6, 10, 120 y 122, con las dos barras altas resaltadas ("242 de 258"). Tarjeta: "Lado mayor: 10 a 116 px, mediana 63". | Calculado |
| 3 | ¿Cuántas fotos hacen falta? | Tres tarjetas con los tres factores (variedad de las fotos, dificultad de la tarea, red preentrenada) y un esquema de la comparación: entrenar con la mitad de las fotos, con todas, y comparar la validación de las dos. Sin cifras en el esquema. | SVG |
| 4 | Anotar en CVAT | Flujo en cuatro pasos con iconos: crear la tarea con las fotos, definir la etiqueta, dibujar un polígono por espermatozoide, exportar en formato COCO. A un lado, un recorte con el borrador del pre-anotador (contorno punteado) y el contorno corregido. Nota: "Las fotos del cliente solo en Drive, no en el repositorio". | SVG, calculado |
| 5 | El criterio de anotación | Cuatro casos dibujados, cada uno con una pregunta: mancha difusa, cabeza tapada por una cola, dos cabezas pegadas, espermatozoide cortado por el borde. Tres tarjetas debajo: "Criterio escrito", "Una persona con conocimiento biológico valida", "Dos personas, las mismas 10 fotos, IoU entre ellas". Pie: lo que revisa el cuaderno antes de entrenar. | SVG |
| 6 | Separar entrenamiento y validación | Las cuatro fotos dibujadas como rectángulos con su zona de entrenamiento, el margen de 100 px y la franja de validación, con los contornos de cada zona: foto 1: 5 y 0; foto 2: 3 y 5; foto 3: 77 y 28; foto 4 (vertical): 78 y 31. Totales: 163 para entrenar, 64 para validar, 31 en el margen. Las dos reglas (10 o más fotos: fotos completas; menos: franja). | SVG |
| 7 | Aumento de datos | Un mismo recorte de la imagen de muestra en seis variantes: original, volteo, giro de 90°, acercado, más oscuro y con ruido. Lista de los rangos: volteos (1/2 cada uno), giros de 90°, escala de 0.8 a 1.25, brillo de 0.7 a 1.3 (±20), ruido. Pie: 80 % de los recortes centrados en un espermatozoide. | Calculado |
| 8 | Entrenar en Colab | Tarjetas con la configuración: 60 épocas, 400 recortes de 512 × 512 por época, lotes de 4 (100 pasos), momento 0.9, tasa 0.005, GPU T4. Una línea de tiempo de las 60 épocas con marcas de validación (cada 5) y de guardado (cada 10). "0.6 min por época, unos 36 min". | SVG |
| 9 | Qué se mide | Tres barras alineadas: 66 etiquetados, 75 marcas, 60 aciertos, con las 15 marcas falsas y los 6 que se escaparon. Las fórmulas: precisión 60 ÷ 75 = 0.80; exhaustividad 60 ÷ 66 = 0.91; F1 = 0.85. Una tarjeta: "AP50 del mejor modelo: 0.888". | SVG |
| 10 | Elegir el umbral | Tabla del barrido de umbrales de 0.3 a 0.9 con marcas, precisión, exhaustividad y F1, con la fila de 0.8 resaltada, y una gráfica del F1. Nota naranja: "El modelo del sitio guarda 0.9 y AP50 0.9148 (época 25): viene de otra corrida". | Calculado |
| 11 | Sobreajuste | Un esquema (no a escala) con dos curvas que se separan: la pérdida de entrenamiento sigue bajando y la validación se aplana. Una tarjeta con la analogía del examen pasado. Cuatro defensas: más datos, aumento, transferencia, guardar el mejor modelo. | SVG |
| 12 | La gráfica de curvas | Las dos curvas del video 3 (pérdida épocas 1 a 46; AP50 cada 5 épocas), con una línea vertical en la época 20. Tres reglas de lectura. Pie: "Con 66 espermatozoides, la validación tiene ruido". | Reutilizado |
| 13 | Qué tan confiables son los números | Tres tarjetas con las debilidades (mismas fotos, elegido con la misma validación, solo 66). Una tabla de conteos de fotos completas (etiquetados y detectados: 6 y 11; 10 y 16; 120 y 119; 122 y 119). Una tarjeta naranja: "Campo claro: 2 espermatozoides, 1.00, no prueba nada". | SVG |
| 14 | Cómo mejorar el modelo | Un ciclo de cuatro pasos con flechas: más fotos variadas, fotos sin espermatozoides, validar con fotos nuevas, corrida nueva (vuelve a partir de COCO) y comparar. Una tarjeta: "El sitio no aprende de lo que suben los usuarios". | SVG |
| 15 | Lo que vimos y lo que sigue | Los cuatro videos del módulo 2 en cuatro tarjetas (cómo ve una imagen una red, Mask R-CNN, transferencia, datos y validación) y una tarjeta "Siguiente: Módulo 3, el sitio funcionando". | SVG |

## Cómo se obtienen las imágenes calculadas

- **Diapositiva 2:** las etiquetas por foto salen de la lista del cuaderno (6, 10, 120 y 122). El recorte con contorno sale de la imagen de muestra pasada por el modelo del sitio.
- **Diapositiva 7:** se aplican a un recorte de la imagen de muestra las mismas operaciones que el cuaderno (volteo, giro, escala, brillo y contraste, ruido) con rangos de la configuración.
- **Diapositiva 10:** la tabla y el F1 salen de la salida del cuaderno (barrido de umbrales).
- **Diapositiva 12:** se reutilizan `curva_perdida.png` y `curva_ap50.png` del mazo del video 3.

## Cifras que dice el guion y que hay que mantener

- Datos del cuaderno de ejemplo (perfil de fluorescencia): 4 fotos (tres de 1792 × 1374 y una de 1374 × 1792) y 258 etiquetas: 6, 10, 120 y 122. Las dos últimas suman 242, más del 90 %. Lado mayor de 10 a 116 px, mediana 63.
- Separación: con 10 fotos o más, fotos completas (una de cada cinco, mínimo una); con menos, una franja de 25 % del lado más largo y un margen de 100 px. Con 4 fotos: 163 para entrenar, 64 para validar y 31 en el margen. Zonas: foto 1, 5 y 0; foto 2, 3 y 5; foto 3, 77 y 28; foto 4, 78 y 31.
- Aumento de datos: volteos con probabilidad de 0.5 cada uno, giros de 90°, escala de 0.8 a 1.25, brillo ×0.7 a ×1.3 y desplazamiento de hasta 20, ruido; 80 % de los recortes centrados en un espermatozoide; un espermatozoide cortado cuenta si se ve al menos el 30 %.
- Entrenamiento: 60 épocas; 400 recortes de 512 × 512 por época; lotes de 4 (100 pasos por época); momento 0.9; tasa 0.005; validación cada 5 épocas; archivo de continuación cada 10 épocas (unos 350 MB); 0.6 min por época, unos 36 min; GPU Tesla T4 de Colab.
- Validación con umbral 0.5: 66 etiquetados, 75 marcas, 60 aciertos (precisión 0.80, exhaustividad 0.91, F1 0.85). Mejor modelo: época 20, AP50 0.888.
- Barrido de umbrales (marcas, precisión, exhaustividad, F1): 0.3 (79; 0.759; 0.909; 0.828), 0.4 (76; 0.789; 0.909; 0.845), 0.5 (75; 0.800; 0.909; 0.851), 0.6 (74; 0.811; 0.909; 0.857), 0.7 (73; 0.822; 0.909; 0.863), 0.8 (70; 0.843; 0.894; 0.868), 0.9 (65; 0.862; 0.849; 0.855). Elegido: 0.8. De 0.5 a 0.9 los aciertos pasan de 60 a 56.
- Curvas: pérdida de 1.39 (época 1) a 0.46 (20) y 0.36 (46); AP50 con máximo en la época 20 (0.888) y entre 0.81 y 0.87 de la 25 a la 45.
- Fotos completas (etiquetados y detectados): 6 y 11, 10 y 16, 120 y 119, 122 y 119. Campo claro: 2 espermatozoides en la validación.
- Modelo del sitio (`model/fluorescencia.pt`): versión 0.3.1, época 25, AP50 0.9148, umbral 0.9. No es la corrida del ejemplo.

## Decidido al armar el mazo

- La diapositiva 2 usa el recorte de la imagen de muestra con tres contornos (el mismo del video 2); las barras de contornos por foto son cuadros dibujados con anchura proporcional.
- La diapositiva 4 muestra el contorno que calculó el modelo sobre un espermatozoide de la imagen de muestra, simplificado a siete vértices, como ejemplo de un polígono de anotación. No es un dibujo hecho en CVAT.
- La diapositiva 5 lleva cuatro dibujos propios de los casos de anotación, hechos como ilustración.
- La diapositiva 6 dibuja las zonas a la escala de cada foto (entrenar, margen de 100 px, validar); no son fotos del cliente.
- La diapositiva 7 aplica a un recorte de la imagen de muestra las operaciones del cuaderno; el ruido es el máximo del cuaderno y casi no se nota.
- La diapositiva 10 usa una tabla en lugar de una gráfica del F1.
- La diapositiva 11 es un esquema que no sale de los datos del proyecto. Las curvas reales están en la 12.
- La diapositiva 12 redibuja las curvas del video 3 en fondo oscuro y marca la época 20.
- Las notas del orador de cada diapositiva resumen lo que dice el guion.

## Pendiente de confirmar

- **Documentos que se contradicen.** `docs/base-conocimiento/04-resultados.md` y `06-preguntas.md` describen el modelo de fluorescencia del sitio con AP50 0.888, umbral 0.8 y 66 espermatozoides en la validación, que son los de la corrida del cuaderno de ejemplo. El archivo `model/fluorescencia.pt` guarda AP50 0.9148 y umbral 0.9, y `docs/contexto-qa.md` dice AP50 0.91. Hay que decidir cuál corrida está en el servidor y corregir los documentos. El guion no afirma cuál es la del sitio.
- **Qué cubre el contorno.** Los documentos dicen que el contorno incluye la cabeza y el primer tramo de la cola, pero la clase se llama "cabeza" y el curso habla de cabezas. El guion dice "espermatozoide, con la cabeza y el primer tramo de la cola".
- **Un criterio escrito y quién valida.** El guion los recomienda; no hay constancia de que ya existan. En `docs/preguntas-cliente.md` quedaron como preguntas abiertas.
- **Experimento de la mitad de las fotos.** La diapositiva 3 lo propone como método; no se hizo con los datos del proyecto.
- **Pre-anotador.** Lo descrito sale de la documentación del script (`scripts/preanotar.py`). Conviene confirmar si se usó con las fotos del ejemplo.
