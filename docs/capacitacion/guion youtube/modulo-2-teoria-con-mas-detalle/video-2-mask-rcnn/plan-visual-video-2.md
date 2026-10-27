# Plan visual del módulo 2, video 2: Mask R-CNN, la red completa

Lo que lleva cada diapositiva. El guion habla de estas imágenes y de estos números tal como están aquí, así que el mazo debe respetarlos. Si algo cambia en el mazo, hay que cambiar el guion (las dos versiones) y viceversa.

Estilo: el del video 1 del módulo 2 (fondo oscuro y claro alternados, azul marino, azul petróleo, celeste y naranja como único acento, letra grande, pocas ideas por diapositiva). Los dibujos son propios, en SVG. Lo marcado como calculado sale del modelo real del sitio (`model/fluorescencia.pt`, cargado con `app/analisis/modelo.py`).

Origen de las imágenes:
- Calculado: se genera con Python y el modelo real, y se guarda como PNG.
- SVG: dibujo propio dentro del mazo.
- Foto: foto de Erin Rod (CC BY 4.0, Wikimedia Commons), con su crédito en el pie. Solo en la diapositiva 15.
- Muestra: la imagen de muestra del sitio (`app/static/muestras/prueba.png`), dibujada por computadora. No es una foto real y la diapositiva lo dice.

| N.º | Diapositiva | Qué se ve | Origen |
|---|---|---|---|
| 1 | Mask R-CNN, la red completa | Etiqueta "Módulo 2 · Video 2". Un recorte de la imagen de muestra con tres espermatozoides, cada uno con su caja y su contorno de un color distinto, y al lado tres etiquetas: "encontrar", "encuadrar" y "delinear". | Calculado |
| 2 | De dónde viene | Línea de tiempo con cuatro puntos: R-CNN 2014, Fast R-CNN 2015, Faster R-CNN 2015 y Mask R-CNN 2017, con una frase cada uno: "unas 2,000 regiones, cada una por separado"; "mapas una sola vez para toda la foto"; "una red que aprende a proponer regiones"; "agrega la máscara y el recorte alineado". | SVG |
| 3 | Vista general: cinco etapas | Cinco cajas en fila con flechas: base convolucional, pirámide, propuestas, recorte alineado, cabezas (clasificación y máscara). Debajo, los pesos: 23.5, 3.3 y 0.6 millones, ninguno en el recorte, 13.9 y 2.6 millones. Total: 43.9 millones. | SVG |
| 4 | La base y la pirámide | Los cuatro mapas de la base (256 × 128 × 128, 512 × 64 × 64, 1,024 × 32 × 32, 2,048 × 16 × 16) a la izquierda, los cinco mapas de la pirámide a la derecha (todos de 256 canales: 128, 64, 32, 16 y 8 por lado) y flechas de ampliar y sumar entre ellos. Etiqueta: "filtro de 1 × 1" y "filtro de 3 × 3". | SVG |
| 5 | Las anclas | Una tesela con cajas cuadradas de 16, 32, 64, 128 y 256 px sobre un punto, y las tres proporciones (más ancha que alta, cuadrada, más alta que ancha). La cuenta en grande: 128² + 64² + 32² + 16² + 8² = 21,824 puntos; × 3 = 65,472 anclas. | SVG |
| 6 | La red de propuestas | Un espermatozoide con un ancla que no encaja y la caja corregida que sí. Dos salidas rotuladas: "¿hay algo? (1 puntaje)" y "ajuste de la caja (4 números)". Embudo: 65,472 anclas → hasta 1,000 propuestas. | SVG |
| 7 | El recorte alineado | Una propuesta sobre un mapa y las dos cuadrículas a las que se lleva: 7 × 7 (para la caja) y 14 × 14 (para la máscara), ambas de 256 canales. Rotulado "sin redondear". | SVG |
| 8 | La cabeza de clasificación | Esquema: recorte de 7 × 7 × 256 → 12,544 números → 1,024 neuronas → 1,024 neuronas → dos salidas: puntaje por clase (fondo, espermatozoide) y 4 números de caja. Pesos: 12.8 millones en la primera capa, 13.9 millones en total, 10,250 en la última. | SVG |
| 9 | La cabeza de máscara | El recorte de 14 × 14, cuatro filtros de 3 × 3, la ampliación y la máscara de 28 × 28 como mapa de calor de un espermatozoide real, con el contorno que resulta al aplicar el umbral de 0.5. Pesos: 2.6 millones. | Calculado, SVG |
| 10 | El puntaje de seguridad | Tres contornos reales de la imagen de muestra con su puntaje encima (uno cercano a 0.99, uno a 0.93 y uno bajo, de unos 0.3), una barra del umbral en 0.9 y la aclaración de los dos umbrales (0.5 por punto, 0.9 por detección). | Calculado, SVG |
| 11 | IoU: qué tanto coinciden dos contornos | Dos contornos de 100 píxeles que se traslapan en 60 (diagrama de conjuntos), con la cuenta 60 / (100 + 100 − 60) = 0.43 y, al lado, el caso de 80 en común: 80 / 120 = 0.67. Rótulos "no cuenta" y "cuenta" (criterio: 0.5). | SVG |
| 12 | Los repetidos | Tres filtros en fila: (1) dos cajas con IoU > 0.6, se queda la de mayor puntaje; (2) teselas de 512 con traslape de 128, un espermatozoide visto dos veces y borde interno descartado; (3) un contorno de 40 px dentro de uno de 100: IoU 0.4, pero contenido 100 %, se descarta. | SVG |
| 13 | Las cinco pérdidas | Las cinco etapas con su pérdida: propuestas (¿hay algo?, ajuste de caja), cabeza de clasificación (¿qué es?, ajuste de caja final), cabeza de máscara (forma). Una suma "+" hacia un solo número. | SVG |
| 14 | Un ejemplo con la imagen de muestra | La imagen de muestra (1200 × 900) con los 41 contornos que dibuja la red. Cifras al lado: 46 cabezas por color, 37 contornos sobre cabezas, 4 sobre filamentos largos y unas 9 cabezas sin contorno. Rótulo: "imagen dibujada por computadora, no es una foto real". | Calculado |
| 15 | Límites | A la izquierda, un acercamiento de la imagen de muestra con un filamento marcado. A la derecha, el recorte de la foto de células de Erin Rod con las detecciones del modelo (núcleo 0.96, fibra 1.00). Crédito en el pie. | Calculado, foto |
| 16 | Lo que vimos y lo que sigue | Cinco o seis puntos del resumen y una tarjeta "Siguiente: aprendizaje por transferencia". | SVG |

## Cómo se obtienen las imágenes calculadas

- **Diapositivas 1, 10 y 14** salen de pasar la imagen de muestra por la misma función que usa el sitio (`modelo.detectar`) y dibujar los contornos con OpenCV. Ya hay una versión de prueba en la carpeta de trabajo (`ejemplo_prueba.png`).
- **Diapositiva 9:** la máscara de 28 × 28 sale de la cabeza de máscara de la red (`roi_heads.mask_predictor`) sobre una propuesta de un espermatozoide de la imagen de muestra, con la función sigmoide para pasar a probabilidad.
- **Diapositiva 15:** el recorte de la foto de células (512 por 512) pasa por la red completa; se dibujan las detecciones con puntaje de 0.9 o más. Salieron cinco: un núcleo con 0.96 y un trozo de fibra con 1.00.

## Cifras que dice el guion y que hay que mantener

- Espermatozoides de fluorescencia: lado mayor de 10 a 116 px, mediana de 63 (del cuaderno de entrenamiento).
- Pirámide: cinco mapas de 256 canales (128, 64, 32, 16 y 8 por lado). Los cuatro primeros los usa el recorte alineado.
- Anclas: tamaños 16, 32, 64, 128 y 256, tres proporciones. 21,824 puntos y 65,472 anclas por tesela de 512.
- Propuestas: hasta 1,000 por tesela, con supresión de 0.7 dentro de la red de propuestas.
- Recorte alineado: 7 × 7 para la caja y 14 × 14 para la máscara. Máscara resultante: 28 × 28.
- Pesos: base 23,454,912; pirámide 3,344,384; propuestas 593,935; cabeza de caja 13,895,680 (la última capa, 10,250); cabeza de máscara 2,623,234 (2,360,320 y 262,914). Total 43,922,395.
- Umbrales: 0.5 por punto de la máscara; 0.05 mínimo que devuelve la red; 0.9 guardado en el modelo de fluorescencia.
- Repetidos: supresión de cajas 0.6; duplicados entre teselas con IoU de 0.5; filtro de contenido de 0.5. Teselas de 512 con traslape de 128.
- IoU de ejemplo: 100 y 100 px con 60 en común da 60 / 140 = 0.43; con 80 en común, 80 / 120 = 0.67.
- Imagen de muestra: 1200 × 900; 46 cabezas por color; 41 contornos; 37 sobre cabezas; 4 sobre filamentos; unas 9 cabezas sin contorno.

## Decidido al armar el mazo

- Los puntajes de la diapositiva 10 son los de tres contornos reales de la imagen de muestra: 0.99 y 0.93, sobre dos cabezas, y 0.30, sobre un filamento largo.
- El conteo de 46 cabezas es propio, por color (componentes de color de al menos 60 píxeles), y no una etiqueta hecha a mano. El mazo lo dice en el pie de la diapositiva 14.
- La diapositiva 1 muestra una zona de la imagen de muestra con exactamente tres espermatozoides detectados. Los puntajes de la diapositiva 8 (0.97 y 0.03) son un ejemplo y el pie lo dice.
