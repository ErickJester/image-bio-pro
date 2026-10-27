# Plan visual del módulo 2, video 1: Cómo ve una imagen una red convolucional

Lo que lleva cada diapositiva. El guion habla de estas imágenes y de estos números tal como están aquí, así que el mazo debe respetarlos. Si algo cambia en el mazo, hay que cambiar el guion (las dos versiones) y viceversa.

Estilo: el del módulo 1 (fondo oscuro y claro alternados, azul marino, azul petróleo, celeste y naranja como único acento, letra grande, pocas ideas por diapositiva). Los números de los ejemplos van en casillas grandes. Los dibujos son propios, en SVG, salvo los marcados como IA, que se piden a Gemini con prompt completo.

Origen de las imágenes:
- Calculado: se genera con Python (OpenCV y el modelo real del sitio) y se guarda como PNG.
- SVG: dibujo propio dentro del mazo.
- IA: ilustración creada con Gemini.
- Foto: tesela de fluorescencia de 512 por 512 px. Se usa una de las fotos del cliente (si él lo permite) o la foto de Erin Rod (CC BY 4.0, Wikimedia Commons) con su crédito en el pie. El guion dice solo "una foto de fluorescencia", sirve cualquiera de las dos.

| N.º | Diapositiva | Qué se ve | Origen |
|---|---|---|---|
| 1 | Cómo ve una imagen una red convolucional | Etiqueta "Módulo 2 · Video 1". La tesela de 512 por 512 con un cuadro de 3 por 3 marcado en naranja, y a un lado ese cuadro ampliado (nueve casillas). Los cuatro videos del módulo en una columna, con el 1 resaltado. | Foto, SVG |
| 2 | Conectar todo con todo no funciona | Tres cifras, una debajo de otra: "512 × 512 = 262,144 píxeles"; "Una neurona: 262,144 pesos"; "Una capa del mismo tamaño: 68,719,476,736 pesos". Dibujo: una rejilla de píxeles con líneas hacia un solo punto de salida. | SVG |
| 3 | La idea: un detector pequeño que recorre la imagen | Una imagen con una ventana pequeña en tres posiciones sucesivas, unidas por flechas (izquierda a derecha y luego bajar una fila). Etiquetas: "filtro" y "convolución". | SVG |
| 4 | El filtro de tres por tres | Tabla de 3 × 3 con −1, 0, 1 en cada fila. Los negativos en azul, el cero en gris y los positivos en naranja. Etiqueta "9 pesos". Frase: "resta la izquierda, suma la derecha". | SVG |
| 5 | La cuenta a mano | Parche 3 × 3 con tres filas "0 0 9" junto al filtro. Cada producto escrito en su casilla (−1·0, 0·0, 1·9 por fila). Total en grande: 27. Abajo, un parche parejo de nueves que da 0. | SVG |
| 6 | Deslizar el filtro: el mapa de características | Imagen de 5 × 5 con las columnas 0 0 9 9 9 (las cinco filas iguales). El filtro en tres posiciones de la primera fila y el mapa de 3 × 3 que resulta: cada fila 27, 27, 0. | SVG |
| 7 | Paso y relleno | Tres miniaturas de la imagen de 5 × 5 con su mapa: paso 1, mapa de 3 × 3; paso 2, mapa de 2 × 2; relleno de 1, mapa de 5 × 5 (con el borde de ceros dibujado). | SVG |
| 8 | Qué detecta un filtro en una foto real | La tesela de fluorescencia y dos resultados a su lado: el del filtro (−1, 0, 1) y el de ese filtro girado (bordes horizontales). Se calculan con la misma cuenta, con valor absoluto y ajustados para verse. | Calculado |
| 9 | Otros filtros: suavizar y resaltar manchas | Dos filtros con su cuenta. Promedio: nueve pesos de 1/9, parche con un 9 en el centro y ceros alrededor, resultado 1. Mancha: un 8 en el centro y −1 en los ocho vecinos; parche parejo de nueves da 0 y el parche del punto aislado da 72. | SVG |
| 10 | Muchos filtros, muchos mapas | La tesela a la izquierda, cuatro filtros distintos en el centro (borde vertical, horizontal, diagonal, mancha) y los cuatro mapas apilados a la derecha, como hojas. Etiqueta "canal". | Calculado, SVG |
| 11 | La activación después del filtro | Mapa de 3 × 3 con 27, 27, 0 / 27, 0, −27 / 0, −27, −27 a la izquierda y, a la derecha, el mismo mapa con la activación: 27, 27, 0 / 27, 0, 0 / 0, 0, 0. | SVG |
| 12 | Reducir para ver más grande | Mapa de 4 × 4 (1 3 2 0 / 4 8 1 1 / 0 2 5 6 / 1 1 7 3) dividido en cuatro bloques de 2 × 2 con colores. Resultado de 2 × 2: 8, 2 / 2, 7. | SVG |
| 13 | Capas apiladas: de bordes a objetos | Tres cuadros de 3 × 3, 5 × 5 y 7 × 7 marcados sobre la misma foto. Debajo, el esquema de un bloque (filtros, activación, reducción) repetido, y la escalera "bordes, curvas y esquinas, partes, objeto". | Foto, SVG |
| 14 | Los filtros se aprenden | Cuadrícula de 8 × 8 con los 64 filtros reales de la primera capa de nuestro modelo (cada uno de 7 × 7). Tres tarjetas: "9 pesos por filtro", "36,864 pesos: 64 filtros de 3 × 3 sobre 64 mapas", "68,719,476,736 pesos: capa conectada a todo". | Calculado, SVG |
| 15 | ResNet50: la base de nuestra red | Tabla de lo que sale de cada etapa para una tesela de 512 por 512: primera capa 64 mapas de 256 × 256; tras la reducción 128 × 128; bloque 1, 256 mapas de 128 × 128; bloque 2, 512 de 64 × 64; bloque 3, 1,024 de 32 × 32; bloque 4, 2,048 de 16 × 16. Tarjetas: "50 capas", "9,408 pesos en la primera capa", "23.5 de 43.9 millones de pesos". Nota: "el brillo se repite en los tres canales". | SVG |
| 16 | Lo que sale y lo que falta | La tesela de entrada a la izquierda y seis mapas de características reales del primer bloque de la red a la derecha. Rótulo: "mapas, no contornos". | Calculado |
| 17 | Lo que vimos y lo que sigue | Cinco puntos del resumen y una tarjeta "Siguiente: Mask R-CNN". | SVG |

## Cómo se obtienen las imágenes calculadas

- **Diapositivas 8, 10 y 16** salen de la misma tesela de 512 por 512. Las diapositivas 8 y 10 aplican los filtros con OpenCV (`cv2.filter2D`) con los pesos exactos del guion. La 16 pasa la tesela por la base ResNet50 del modelo real (`model/fluorescencia.pt`, cargado con `app/analisis/modelo.py`) y toma seis canales del primer bloque.
- **Diapositiva 14** dibuja los 64 filtros de `backbone.body.conv1.weight` del mismo modelo, cada uno normalizado para verse. Ya hay una versión de prueba en la carpeta de trabajo y los colores se ven como detectores de bordes y manchas.
- **Diapositiva 15.** Los tamaños de la tabla se comprobaron pasando una entrada de 512 por 512 por la base: 256 × 128 × 128, 512 × 64 × 64, 1,024 × 32 × 32 y 2,048 × 16 × 16. La primera capa da 64 mapas de 256 × 256 y la reducción los deja en 128 × 128.

## Cifras que dice el guion y que hay que mantener

- 512 × 512 = 262,144 píxeles. Una capa del mismo tamaño: 262,144² = 68,719,476,736 pesos.
- Imagen de 5 × 5 con filtro de 3 × 3: paso 1 da 3 × 3, paso 2 da 2 × 2, relleno de 1 da 5 × 5.
- Primera capa de ResNet50: 64 filtros de 7 × 7 con 3 canales, 64 × 7 × 7 × 3 = 9,408 pesos.
- Base ResNet50: unos 23.5 millones de pesos; el modelo completo, 43.9 millones.
- Ejemplo de una capa de 64 filtros de 3 × 3 sobre 64 mapas: 64 × 3 × 3 × 64 = 36,864 pesos.
- El modelo exportado pesa 176 MB.

## Decidido al armar el mazo

- La tesela de las diapositivas 1, 8, 10, 13 y 16 es un recorte de 512 por 512 de la foto de Erin Rod (CC BY 4.0, Wikimedia Commons), con el crédito en el pie de cada una. En la 1 y la 13 va en color; en la 8, la 10 y la 16 va en tonos de gris, que es el brillo máximo de rojo, verde y azul, lo que de verdad recibe la red.
- Los números de la diapositiva 1 son el brillo real de los nueve píxeles marcados, y las imágenes calculadas (8, 10, 14 y 16) salen del modelo `fluorescencia.pt` y de OpenCV.
