# Guía de pantalla del módulo 3, video 2: Inferencia con recortes

Este video no lleva mazo. Se graba la pantalla: el editor con el código, la terminal y dos imágenes, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se hace clic o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, los cuatro comandos de la terminal y las cifras que el guion y la pantalla deben respetar. Si algo cambia en el código o en los modelos, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | De la caja negra al código | Editor | Comentario inicial de `modelo.py` y la función `detectar` |
| 2 | Dos modelos y cómo se elige | Editor, terminal | `ARCHIVOS`, `tipo_de_foto`, comando A y la prueba |
| 3 | El archivo del modelo | Terminal, editor | Comando C, `model/README.md` y `carpeta_modelos` |
| 4 | Armar y cargar la red | Editor | `_construir_red`, `_hilos` y `_cargar` |
| 5 | Preparar la foto | Editor | `preparar_imagen` y su prueba |
| 6 | Las teselas | Editor, terminal, imagen | `_posiciones`, comando B y `figuras/teselas.png` |
| 7 | Cada tesela por la red | Editor | Lote, relleno, tensor y llamada a la red |
| 8 | Lo que sale de la red | Editor | Máscaras, puntajes, puntaje mínimo y caja |
| 9 | Lo que toca el borde interno | Editor | Descarte por borde interno y coordenadas de la foto |
| 10 | Juntar y quitar repetidos | Editor | Deduplicación, `_iou`, `_quitar_repetidos` y su prueba |
| 11 | De la máscara al contorno | Editor, terminal, imagen | `_a_contorno`, `detectar`, comando D y `figuras/puntajes.png` |
| 12 | Un análisis a la vez | Editor | Candados, `with _BLOQUEO_INFERENCIA` y variables del compose |
| 13 | Si no hay modelo y cómo se comprueba | Editor | `disponible`, `detectar_espermatozoides` y las pruebas |
| 14 | Lo que vimos y lo que sigue | Editor | `modelo.py`, línea 248, mientras se resume |

## Antes de grabar

- Entorno de Python creado y activado en la terminal, como en la guía del video 1 (sección Entorno de Python). Las órdenes se corren en la carpeta del proyecto.
- Los dos archivos `fluorescencia.pt` y `campo_claro.pt` en `model/`. No están en Git (se copian a mano; ver `model/README.md`). Sin ellos, los comandos A y B funcionan, pero C y D fallan.
- El editor con estas pestañas, en el orden en que se usan: `app/analisis/modelo.py`, `tests/test_modelo.py`, `model/README.md`, `docker-compose.yml` y `app/analisis/medicion.py`. Letra grande y números de línea visibles.
- Las dos imágenes del tramo 6 y del 11 abiertas en un visor: `figuras/teselas.png` y `figuras/puntajes.png`, en esta misma carpeta.
- El comando D tarda unos segundos (carga el modelo y analiza la imagen de ejemplo). Probarlo antes y dejar la terminal lista.
- No mostrar el archivo `.env` ni rutas con datos personales.

## Los cuatro comandos de la terminal

Se pegan en la terminal, en la carpeta del proyecto y con el entorno activado. Los cuatro se probaron el 30/10/2026.

**A. Tipo de foto de la imagen de ejemplo** (tramo 2). Debe imprimir `fluorescencia`.

```
python -c "import cv2; from app.analisis import modelo; rgb = cv2.cvtColor(cv2.imread('app/static/muestras/prueba.png'), cv2.COLOR_BGR2RGB); print(modelo.tipo_de_foto(rgb))"
```

**B. Posiciones de las teselas de la imagen de ejemplo** (tramo 6). Debe imprimir `[0, 384, 688]` y `[0, 384, 388]`.

```
python -c "from app.analisis import modelo; print(modelo._posiciones(1200, 512, 384)); print(modelo._posiciones(900, 512, 384))"
```

**C. Contenido del archivo del modelo** (tramo 3). Debe imprimir las cinco claves (`version`, `state_dict`, `config`, `epoca`, `ap50_validacion`) y la configuración de fluorescencia.

```
python -c "import torch; from torch.torch_version import TorchVersion; torch.serialization.add_safe_globals([TorchVersion]); c = torch.load('model/fluorescencia.pt', map_location='cpu', weights_only=True); print(list(c)); print(c['config'])"
```

**D. Conteo de detecciones por puntaje** (tramo 11). Debe imprimir `75 57 41`: las detecciones que devuelve la red ya sin repetidos, las de 0.5 o más y las de 0.9 o más.

```
python -c "import cv2; from app.analisis import modelo as m; rgb = cv2.cvtColor(cv2.imread('app/static/muestras/prueba.png'), cv2.COLOR_BGR2RGB); red, cfg = m._cargar('fluorescencia'); det = m._inferir(red, m.preparar_imagen(rgb, cfg), cfg); p = [d['puntaje'] for d in det]; print(len(p), sum(x >= 0.5 for x in p), sum(x >= 0.9 for x in p))"
```

Las dos imágenes de `figuras/` salen de esos mismos cálculos con la imagen de ejemplo del sitio: `teselas.png` dibuja las 9 teselas con su posición, y `puntajes.png` dibuja las 75 detecciones, en verde las de 0.9 o más (41), en naranja las de 0.5 a 0.9 (16) y en rojo las de menos de 0.5 (18).

## Comprobar antes de grabar

- **Los cuatro comandos.** Si el resultado cambia (por ejemplo, otro modelo en `model/`), cambiar el guion: 75, 57 y 41 se dicen en el tramo 11.
- **Los modelos de `model/`.** El guion dice los valores de la configuración de estos archivos: fluorescencia con teselas de 512, traslape de 128, anclas de 16 a 256, 300 detecciones máximas, umbral de cajas 0.6 y umbral de detección 0.9; campo claro con teselas de 640, traslape de 384, reducción de 0.5, inversión y umbral 0.5. Si se cambia un modelo, el comando C da los valores nuevos.
- **Líneas que nombra el guion.** Se comprobaron con el código de la versión 1.11.0 (tabla de abajo). Si `modelo.py` cambia, hay que volver a comprobarlas.
- **Las imágenes de `figuras/`.** Se regeneran si cambia el modelo o la imagen de ejemplo.

## Cifras que dice el guion y que hay que mantener

- Imagen de ejemplo: 1200 × 900, tipo `fluorescencia`; mediana del brillo máximo de la foto reducida a un octavo: 0. Preparada: 900 × 1200 en grises.
- Teselas de la imagen de ejemplo en fluorescencia: 9 (3 × 3), con posiciones x = 0, 384, 688 y y = 0, 384, 388. Para una foto de 1792 × 1374: 20 teselas en fluorescencia y 4 en campo claro. Para una de 3584 × 2748: 63 y 24. En campo claro la foto de 1200 × 900 se reduce a 600 × 450 y cabe en una tesela.
- Detecciones de la imagen de ejemplo: 75 (con puntaje de 0.05 o más, ya sin repetidos), 57 con 0.5 o más y 41 con 0.9 o más; el resultado en el sitio es 41.
- Umbrales: 127 para elegir el modelo; 0.05 de puntaje mínimo; 0.5 para la máscara; IoU de 0.5 entre teselas; contenido de 0.5; umbral de detección 0.9 (fluorescencia) y 0.5 (campo claro).
- Lotes de 2 teselas; hasta 4 hilos de PyTorch (variable `TORCH_HILOS`); cada archivo de modelo pesa unos 176 MB.
- Conteos de la comprobación contra el cuaderno: 114, 9, 2, 1 y 43 contornos en cinco fotos (`docs/integracion-modelos.md`).

## Líneas que nombra el guion

| Archivo | Líneas |
|---|---|
| `app/analisis/modelo.py` | comentario inicial 1 a 15; `ARCHIVOS` y umbrales 26 a 29; candados 31 a 33; `carpeta_modelos` 36 a 39; `disponible` y `motivo_no_disponible` 46 a 61; `tipo_de_foto` 64 a 68; normalización congelada 73 a 79 (uso en 102); `_construir_red` 82 a 103; `_hilos` 106 a 108; `_cargar` 111 a 137 (carga segura 119 a 126; pesos y comprobación 127 a 137); `preparar_imagen` 142 a 152 (reducir 144 a 148; brillo máximo 149; invertir 150 a 152); `_posiciones` 155 a 158; `_interseccion` y `_iou` 161 a 173; `_quitar_repetidos` 176 a 183; `_inferir` 188 a 234 (teselas 192 a 195; lotes 196 a 199; recorte y relleno 200 a 205; tensor 206 y 207; red 208; máscaras y puntajes 209 y 210; puntaje mínimo 211 a 213; caja 214 a 217; borde interno 218 a 221; coordenadas 222 a 226; deduplicación 227 a 231); `_a_contorno` 237 a 245; `detectar` 248 a 267 (candado 256) |
| `app/analisis/medicion.py` | `detectar_espermatozoides` 101 a 114 |
| `docker-compose.yml` | `MODELOS_DIR` y `TORCH_HILOS` 8 a 11 |
| `tests/test_modelo.py` | `tipo_de_foto` 18 a 24; sin modelos 27 a 29; `preparar_imagen` 32 a 40; teselas 43 a 46; repetidos 49 a 56; modelos reales 59 a 71 |
| `model/README.md` | tabla de los dos archivos |

## Cosas que el guion dice con cuidado

- No se da ningún tiempo de análisis: no hay medición del servidor real. El comando D tarda unos segundos en una computadora de escritorio; ese tiempo no se dice en el video.
- No se citan las medidas de acierto (AP50). El archivo del modelo guarda `ap50_validacion`, pero el video no las usa; ver el módulo 2.
- La razón de reducir la foto a la mitad en campo claro se dice como "así se entrenó el modelo", sin dar otra explicación.
- El tamaño del lote (2) se presenta como un número pequeño para cuidar la memoria; el código no dice por qué es 2.
- Que el umbral de 0.9 se eligió probando varios con la validación viene del módulo 2, video 4.
- Los conteos 114, 9, 2, 1 y 43 vienen de la documentación; las fotos son del cliente y no se muestran.
- Que el sitio use bien el modelo no prueba que el modelo cuente bien; el guion lo dice así.
- Que la última tesela casi repita a la anterior (384 y 388) es un efecto real de `_posiciones`; el guion lo presenta como efecto pequeño que no daña el resultado, porque la deduplicación lo corrige.
