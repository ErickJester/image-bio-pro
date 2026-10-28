# Plan visual del módulo 2, video 3: Aprendizaje por transferencia

Lo que lleva cada diapositiva. El guion habla de estas imágenes y de estos números tal como están aquí, así que el mazo debe respetarlos. Si algo cambia en el mazo, hay que cambiar el guion (las dos versiones) y viceversa.

Estilo: el de los videos 1 y 2 del módulo 2 (fondo oscuro y claro alternados, azul marino, azul petróleo, celeste y naranja como único acento, letra grande, pocas ideas por diapositiva). Los dibujos son propios, en SVG. Lo marcado como calculado sale del modelo real del sitio (`model/fluorescencia.pt`) o de la salida guardada del cuaderno de entrenamiento (`entrenamiento/entrenar_mask_rcnn.ipynb`).

Origen de las imágenes:
- Calculado: se genera con Python y se guarda como PNG o como gráfica.
- SVG: dibujo propio dentro del mazo.
- Reutilizado: imagen del mazo del video 1 (filtros y mapas de características).

| N.º | Diapositiva | Qué se ve | Origen |
|---|---|---|---|
| 1 | Mucha red y pocas fotos | Etiqueta "Módulo 2 · Video 3". A la izquierda, una pila grande con "43.9 millones de pesos"; a la derecha, una pila chica con "4 fotos · 258 espermatozoides etiquetados · 163 para entrenar". Entre las dos, un signo de pregunta. | SVG |
| 2 | Empezar de cero | Un filtro de la primera capa con valores al azar (ruido) junto a un filtro ya aprendido, con el rótulo "no sabe qué es un borde". La cuenta: 43,922,395 pesos ÷ 163 espermatozoides ≈ 270,000 pesos por ejemplo. Una línea: "recortes nuevos en cada época, las mismas 163 cabezas". | Calculado, SVG |
| 3 | La guitarra y el ukulele | Una guitarra (6 cuerdas) y un ukulele (4 cuerdas) dibujados con líneas sencillas. Debajo, dos columnas: "Ya trae: oído, ritmo, dedos" (lo general) y "Le falta: 4 cuerdas, afinación, acordes" (lo propio). Al lado, la correspondencia con la red: bordes y formas / espermatozoides. | SVG |
| 4 | Qué aprende cada parte de la red | Los filtros de la primera capa (64 de 7 × 7) y los mapas de características de capas cada vez más profundas, con una flecha de "general" a "específico". Rótulo: "64 × 3 × 7 × 7 = 9,408 pesos". Al final de la flecha, "cabeza de clasificación: depende de las clases". | Reutilizado del video 1 |
| 5 | La idea: partir de lo ya aprendido | Esquema de tres cajas con flechas: "Tarea de origen · muchas fotos" → "Pesos copiados" → "Tarea de destino · pocas fotos · se afinan". Debajo, tres tarjetas con los términos: preentrenada, tarea de origen / de destino, afinar (fine-tuning). Nota: "Descargar los pesos: unos segundos. Entrenamiento de ejemplo: unos 36 minutos." | SVG |
| 6 | COCO, la tarea de origen | Un dibujo propio de una escena sencilla con tres objetos (taza, bicicleta, perro) con su contorno, rotulado "ejemplo dibujado, no es una foto de COCO". A la derecha, las cifras: "más de 100 mil fotos · 80 tipos de objetos · contornos hechos por personas · pesos de unos 170 MB". Una tarjeta naranja: "Ahí no hay microscopía". | SVG |
| 7 | Qué se reutiliza y qué se cambia | Una barra dividida: 99.4 % (43,649,231 pesos, "viene de COCO") y 0.6 % (273,164, "nuevo"). Debajo, las piezas reutilizadas con sus pesos (base 23,454,912; pirámide 3,344,384; propuestas 593,935; cabeza de caja 13,895,680; capas de filtros de la máscara 2,360,320) y las nuevas (última capa de clasificación 10,250; final de la máscara 262,914). A un lado, una nota: "Anclas: COCO 32 a 512 px, sitio 16 a 256 px". | SVG |
| 8 | Congelar o afinar | Dos columnas: "Congelar" (casi todo fijo, solo lo nuevo se entrena; rápido; poco riesgo; se adapta menos) y "Afinar" (casi todo se entrena; se adapta mejor; más riesgo con pocos datos). Abajo, la barra de la base del sitio: congelado 222,400 (9,408 de la primera capa y 212,992 del primer bloque, 0.5 %) y afinado 43,699,995 (43.7 millones). Nota: "Normalización fija · calentamiento de 100 pasos". | SVG |
| 9 | Un entrenamiento de ejemplo | Dos gráficas lado a lado. Izquierda: pérdida por época (épocas 1 a 46, de 1.39 a 0.36). Derecha: AP50 de validación cada 5 épocas (0.857, 0.840, 0.819, 0.888, 0.857, 0.856, 0.808, 0.872, 0.865) con la época 5 y la 20 marcadas. Cifras: 4 fotos, 258 etiquetas, 163 entrenamiento, 64 validación, 400 recortes por época, 0.6 min por época. Pie: "validación pequeña, de las mismas fotos: cifras orientativas". | Calculado |
| 10 | Lo que la transferencia no resuelve | Cuatro tarjetas: "No arregla etiquetas descuidadas", "No hace confiable una validación pequeña", "Hereda lo que COCO enseñó (fibras y manchas)", "Contesta aunque no conozca la foto (0.96 sobre un núcleo)". | SVG |
| 11 | Cuándo conviene y cuándo no | Tabla de dos por dos: filas "Tareas parecidas" y "Tareas distintas", columnas "Pocos datos" y "Muchos datos", con la acción en cada celda (congelar casi todo; afinar con confianza; difícil, hace falta más datos; afinar casi todo). Una marca en la celda del proyecto. Pie: "Cada corrida nueva vuelve a partir de COCO". | SVG |
| 12 | Cómo se ve en el código | Tres líneas de código del cuaderno en letra monoespaciada (cargar con `COCO_V1`, cambiar `box_predictor`, cambiar `mask_predictor`) y, al lado, un esquema de los dos modos: "entrenar: con pesos de COCO" y "servir: sin pesos, se carga el archivo del modelo". | SVG |
| 13 | Lo que vimos y lo que sigue | Cinco o seis puntos del resumen y una tarjeta "Siguiente: datos, entrenamiento y validación". | SVG |

## Cómo se obtienen las imágenes calculadas

- **Diapositiva 2:** un filtro de 7 × 7 con valores al azar (semilla fija) y, al lado, un filtro de la primera capa del modelo del sitio, graficados con el mismo mapa de color. Los dos son calculados.
- **Diapositiva 4:** se reutilizan los filtros de la primera capa y los mapas de características del mazo del video 1.
- **Diapositiva 9:** la pérdida y el AP50 se copian de la salida guardada del cuaderno (`corrida_06`, versión 0.5.1 del cuaderno), que está en el volcado de trabajo `nb_dump.txt`. La salida se corta en la época 46, así que la gráfica llega hasta ahí; el mejor modelo (época 20, AP50 0.888) lo confirma el propio cuaderno.

## Cifras que dice el guion y que hay que mantener

- Modelo: 43,922,395 pesos. Reutilizados desde COCO: 43,649,231 (99.4 %). Nuevos: 273,164 (0.6 %), que son 10,250 de la última capa de clasificación y 262,914 del final de la cabeza de máscara.
- Red original de torchvision (COCO): 44,401,393 pesos, 80 tipos de objetos (91 salidas), archivo de unos 170 MB, anclas de 32 a 512 píxeles. En el sitio: anclas de 16 a 256.
- Congelado: primera capa 9,408 + primer bloque 212,992 = 222,400 (0.5 %). Se afinan 43,699,995 (43.7 millones). Normalización fija.
- Primera capa: 64 filtros de 7 × 7 con 3 canales de entrada = 9,408 pesos.
- Datos de la corrida de ejemplo: 4 fotos de fluorescencia, 258 espermatozoides etiquetados, 163 en entrenamiento, 64 en validación (31 en la franja de separación de 100 px). El cuaderno cuenta 66 etiquetados al medir la validación; el guion dice "alrededor de 65".
- Entrenamiento: 400 recortes de 512 × 512 por época, lotes de 4 (100 pasos por época), calentamiento de 100 pasos, 0.6 min por época en GPU T4, 60 épocas (unos 36 min).
- Pérdida: 1.39 (época 1), 0.87 (2), 0.70 (5), 0.46 (20). Validación: AP50 0.857 en la época 5 (precisión 0.77, exhaustividad 0.86); mejor modelo en la época 20, AP50 0.888; entre las épocas 25 y 45 oscila entre 0.81 y 0.87.
- Cuenta de la diapositiva 2: 43,922,395 ÷ 163 ≈ 270,000.

## Decidido al armar el mazo

- La diapositiva 4 usa los 64 filtros de la primera capa (imagen del video 1) y una tira con los pesos de cada bloque de la base (9,408; 212,992; 1,212,416; 7,077,888 y 14,942,208, que suman 23,454,912) en lugar de los mapas de características, que no están ordenados por profundidad.
- La diapositiva 2 compara 16 filtros al azar con 16 filtros de la primera capa del modelo del sitio (los de más contraste).
- La diapositiva 6 lleva un dibujo propio de una taza, una bicicleta y una silla con contornos punteados, rotulado como dibujo, para no usar fotos de COCO.
- La diapositiva 9 grafica la pérdida (épocas 1 a 46) y el AP50 (épocas 5 a 45) de la salida del cuaderno.
- El mazo calcula lo congelado como 222,400 pesos (9,408 de la primera capa y 212,992 del primer bloque). Con las capas de normalización fijas, estas no cuentan como pesos.
- Las notas del orador de cada diapositiva resumen lo que dice el guion.

## Pendiente de confirmar

- La corrida del cuaderno (versión 0.5.1, AP50 0.888, umbral elegido 0.8) no es la del modelo que está en el servidor (`model/fluorescencia.pt`: versión 0.3.1, época 25, AP50 0.9148, umbral 0.9). El guion dice "una corrida de ejemplo del cuaderno" y no afirma que sea la del sitio. En el video 4 hay que reconciliar las dos.
- Ninguna comparación contra una red entrenada desde cero: el guion lo dice. Si se hace, se puede agregar una diapositiva.
