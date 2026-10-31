# Guía de pantalla del módulo 3, video 3: Medición, escala y retos

Este video no lleva mazo. Se graba la pantalla: el editor con el código, la terminal y una imagen, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se hace clic o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, los siete comandos de la terminal y las cifras que el guion y la pantalla deben respetar. Si algo cambia en el código, en los modelos o en la imagen de ejemplo, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | La red localiza, el código mide | Editor | Comentario inicial de `medicion.py` y la función `analizar_imagen` |
| 2 | Área y largo | Editor, terminal | `medir_cabeza`, máscara, `minAreaRect` y comando A |
| 3 | La escala | Editor, terminal | `PX_POR_MICRA`, las dos divisiones y la salida del comando A |
| 4 | Una escala provisional | Terminal | Comando B; el resto se cuenta hablando (la escala se acordó con el laboratorio) |
| 5 | Media y desviación estándar | Editor, terminal | `resumen` y comando C |
| 6 | El histograma | Editor, terminal | `histograma`, salida del comando B y `promedios_entre_imagenes` |
| 7 | El resultado de una imagen y sus estados | Editor, terminal | `analizar_imagen`, comando D y las pruebas de JPG e imagen negra |
| 8 | La imagen marcada | Editor, imagen | `dibujar_marcas`, `figuras/marcada.png`, `dibujar_regla`, copias y `contorno_simple` |
| 9 | Reto 1: espermatozoides juntos | Editor, terminal | `detectar_cabezas` y comando E |
| 10 | Reto 2: falsos positivos | Editor | El freno de `analizar_imagen` |
| 11 | Reto 3: el largo | Terminal | Comando F y la salida del comando B |
| 12 | Reto 4: las fotos | Editor, terminal | Formatos y comando G; los tiempos de espera se cuentan hablando |
| 13 | Lo que no se mide y lo que falta | Editor | Color; el trabajo futuro se cuenta hablando |
| 14 | Lo que vimos y lo que sigue | Editor | `medicion.py`, línea 237, mientras se resume |

## Antes de grabar

- Entorno de Python creado y activado en la terminal, como en la guía del video 1 (sección Entorno de Python). Las órdenes se corren en la carpeta del proyecto.
- Los dos archivos `fluorescencia.pt` y `campo_claro.pt` en `model/`. No están en Git (se copian a mano; ver `model/README.md`). Sin ellos, los comandos B, F y G dan otro resultado, porque el sitio usa la detección provisional.
- El editor con estas pestañas, en el orden en que se usan: `app/analisis/medicion.py` y `tests/test_sistema.py`. No se abre ningún documento de `docs/`. Letra grande y números de línea visibles.
- La imagen del tramo 8 abierta en un visor: `figuras/marcada.png`, en esta misma carpeta.
- Los comandos B y G tardan unos segundos (cargan el modelo). Probarlos antes y dejar la terminal lista.
- No mostrar el archivo `.env` ni rutas con datos personales.

## Los siete comandos de la terminal

Se pegan en la terminal, en la carpeta del proyecto y con el entorno activado. Los siete se probaron el 30/10/2026. Los comandos B y D guardan archivos en la carpeta temporal del sistema.

**A. Un rectángulo de 60 por 20 píxeles** (tramos 2 y 3). Debe imprimir `{'area_px': 1281, 'longitud_px': 60.0, 'area_um2': 0.356, 'longitud_um': 1.0, 'indice_color': 0.5}`.

```
python -c "import numpy as np; from app.analisis import medicion as m; t = np.full((60,100,3),200,np.uint8); c = np.array([[[10,10]],[[70,10]],[[70,30]],[[10,30]]],np.int32); print(m.medir_cabeza(t,c))"
```

**B. Análisis de la imagen de ejemplo** (tramos 4, 6 y 11). Con los modelos en `model/`, debe imprimir `ok fluorescencia 41`, el resumen del área y del largo en píxeles, el largo en micras y el histograma (la última línea).

```
python -c "import os, tempfile; from app.analisis import medicion as m; r = m.analizar_imagen('app/static/muestras/prueba.png','prueba.png', os.path.join(tempfile.gettempdir(),'marcada.jpg')); print(r['estado'], r['detector'], r['conteo']); print(r['area']); print(r['longitud']); print(r['longitud_um']); print(r['histograma'])"
```

**C. Resumen de tres números** (tramo 5). Debe imprimir `{'media': 20.0, 'desviacion': 10.0, 'minimo': 10.0, 'maximo': 30.0}`.

```
python -c "from app.analisis import medicion as m; print(m.resumen([10,20,30]))"
```

**D. Una imagen toda negra** (tramo 7). Debe imprimir `no_analizada` y la lista con el mensaje en rojo (`danger`) de que no se encontraron espermatozoides.

```
python -c "import numpy as np, cv2, os, tempfile; from app.analisis import medicion as m; d = tempfile.gettempdir(); cv2.imwrite(os.path.join(d,'negra.png'), np.zeros((200,200,3),np.uint8)); r = m.analizar_imagen(os.path.join(d,'negra.png'),'negra.png',os.path.join(d,'m.jpg')); print(r['estado']); print(r['mensajes'])"
```

**E. Conteo de la detección provisional** (tramo 9). Debe imprimir `45`.

```
python -c "import cv2; from app.analisis import medicion as m; rgb = cv2.cvtColor(cv2.imread('app/static/muestras/prueba.png'), cv2.COLOR_BGR2RGB); print(len(m.detectar_cabezas(rgb)))"
```

**F. Los contornos más alargados** (tramo 11). Para cada contorno del modelo calcula lado mayor entre lado menor del rectángulo mínimo. Debe imprimir `[(39, 14.6, 87.5), (18, 13.3, 79.0), (5, 11.9, 72.5), (9, 11.6, 68.3), (14, 3.2, 38.9), (28, 2.2, 27.3)]`: número del contorno, relación y largo en píxeles.

```
python -c "import cv2; from app.analisis import medicion as m; rgb = cv2.cvtColor(cv2.imread('app/static/muestras/prueba.png'), cv2.COLOR_BGR2RGB); cs, _, _ = m.detectar_espermatozoides(rgb); r = [(i, round(max(l) / min(l), 1), round(max(l), 1)) for i, c in enumerate(cs, 1) for l in [cv2.minAreaRect(c)[1]]]; r.sort(key=lambda x: -x[1]); print(r[:6])"
```

**G. La misma foto en PNG y en JPG** (tramo 12). Debe imprimir cuatro líneas: `png 41`, `95 45`, `75 49` y `50 45`.

```
python -c "import os, tempfile, cv2; from app.analisis import medicion as m; d = tempfile.gettempdir(); img = cv2.imread('app/static/muestras/prueba.png'); [print(q, m.analizar_imagen(p, 'f', os.path.join(d,'f.jpg'))['conteo']) for q, p in [('png', 'app/static/muestras/prueba.png')] + [(q, (cv2.imwrite(os.path.join(d,f'q{q}.jpg'), img, [cv2.IMWRITE_JPEG_QUALITY, q]), os.path.join(d,f'q{q}.jpg'))[1]) for q in (95, 75, 50)]]"
```

La imagen `figuras/marcada.png` es la copia ampliada que guarda `analizar_imagen` para la imagen de ejemplo (1200 × 900, con 41 contornos numerados y la regla abajo a la izquierda). En ella los contornos 5, 9, 18 y 39 son los delgados que siguen una cola, y se ven cabezas de color sin contorno.

## Comprobar antes de grabar

- **Los siete comandos.** Si el resultado cambia (por ejemplo, otro modelo en `model/`), cambiar el guion: 41, 45, 49, la media de 28.62 y las demás cifras de abajo se dicen en varios tramos.
- **Los modelos de `model/`.** Con otros archivos cambian el conteo de 41, el histograma, los contornos alargados y los conteos del JPG.
- **Líneas que nombra el guion.** Se comprobaron con el código de la versión 1.11.0 (tabla de abajo). Si `medicion.py` o las pruebas cambian, hay que volver a comprobarlas.
- **La imagen de `figuras/`.** Se regenera si cambia el modelo o la imagen de ejemplo.

## Cifras que dice el guion y que hay que mantener

- Imagen de ejemplo: 1200 × 900, PNG, 134 KB, tipo `fluorescencia`; estado `ok` con 41 espermatozoides.
- Área en píxeles: media 301.8, desviación 55.88, mínimo 179, máximo 455. Largo en píxeles: media 28.62, desviación 16.72, mínimo 15.0, máximo 87.5. Largo en micras: media 0.48, desviación 0.28, mínimo 0.25, máximo 1.46.
- Histograma del área: bordes de 179.0 a 455.0 (10 intervalos de 27.6), frecuencias 3, 1, 7, 7, 7, 8, 4, 2, 1 y 1 (suman 41); 29 de los 41 caen entre 234.2 y 344.6 píxeles.
- Rectángulo de prueba: 60 × 20 de lado; la máscara cuenta 61 × 21 = 1281 píxeles; largo 60.0 px = 1.0 µm; área 1281 / 3600 = 0.356 µm².
- Resumen de 10, 20 y 30: media 20, desviación 10 (se divide entre n − 1 = 2), mínimo 10, máximo 30.
- Escala: `PX_POR_MICRA` = 60; regla de 300 px = 5 µm; 60² = 3600 px² por µm². Una cabeza (largo medio 28.62 px) mide alrededor de una décima parte de la regla.
- Detección provisional de la imagen de ejemplo: 45 contornos (162 contornos en total, 45 con 20 píxeles o más; ninguno quitado por tamaño ni por alargamiento; umbral de Otsu 81). El modelo da 41.
- Contornos alargados: los números 39, 18, 5 y 9 tienen relaciones de 14.6, 13.3, 11.9 y 11.6; el quinto, 3.2; el resto, 2.2 o menos. Sin esos cuatro quedan 37 contornos con largo medio 23.41 px y desviación 4.33 (con ellos, 28.62 y 16.72).
- JPG de la misma foto: PNG 41; JPG de calidad 95, 45; de 75, 49; de 50, 45.
- Umbrales y constantes: 10 intervalos del histograma; aviso con menos de 3 espermatozoides; área mínima de 20 píxeles, 6 veces la mediana y relación de 5 a 1 (solo en la detección provisional); copias de 1400 y 2800 píxeles de lado mayor, calidad 90 y 88; regla de 300 px con margen de 40; tolerancia de 1.5 px en `contorno_simple`.
- Fotos del laboratorio: 1792 × 1374 y 3584 × 2748 (20 y 63 teselas en fluorescencia); objetivo de 40 aumentos.
- Hasta 10 imágenes por subida; tiempos de espera de 1800 s en Gunicorn y Nginx; análisis de una en una.
- Modelos entrenados con cuatro fotos por tipo.
- Del módulo 2, video 2: sobre un recorte de una foto de células sin espermatozoides, el modelo dio 0.96 en un núcleo y 1.00 en un trozo de fibra.

## Líneas que nombra el guion

| Archivo | Líneas |
|---|---|
| `app/analisis/medicion.py` | comentario inicial 1 a 9 (nota de `cabezas` en 8 y 9); grados de color 31 a 35; escala 38 a 40 (la línea 37 no se enseña: nombra a quien dio la indicación); regla 43; histograma 46; formatos 47; `detectar_cabezas` 67 a 98; `detectar_espermatozoides` 101 a 114; `medir_cabeza` 117 a 137 (máscara 119 a 121; índice de color 125 y 126; rectángulo 128; área 129; largo 130; micras 134 y 135); `contorno_simple` 140 a 144; `resumen` 171 a 178 (desviación 175); `histograma` 181 a 185; `dibujar_regla` 188 a 205 (omisión 192 y 193); `dibujar_marcas` 217 a 234; `analizar_imagen` 237 a 297 (abrir y formato 239 a 252; sin contornos 259 a 265; marcas 284; estados 288 a 296); `promedios_entre_imagenes` 300 a 313 |
| `tests/test_sistema.py` | JPG 111 a 116; imagen negra 119 a 124; regla 164 a 176; dos copias 214 a 220 |

## Cosas que el guion dice con cuidado

- **La escala no es calibración.** El guion dice que la escala es provisional, que se habló con el laboratorio y de ahí salió el valor de partida, y que el sitio la presenta como escala común. El código dice «300 px = 5 micras» en la regla y la página de resultados dice «para estandarizar el tamaño». Del laboratorio solo se dice que la escala es un valor de trabajo, sin medición hecha con una regla en su microscopio, y que falta aclarar con ellos si las fotos de 1,792 y de 3,584 píxeles son del mismo campo. El guion sigue al código.
- **Las micras de la imagen de ejemplo no son creíbles.** Con 60 px por micra, la cabeza media sale de 0.48 µm. El guion dice que una cabeza mide varias micras y que no se sabe con qué ajuste se tomó la imagen de ejemplo; no afirma cuál es la escala correcta ni que la imagen sea de otra resolución.
- **Las colas marcadas son una observación hecha al preparar el video.** Que los contornos 5, 9, 18 y 39 son colas sale de su relación de aspecto (de 11.6 a 14.6 contra 3.2 o menos) y de la imagen marcada; no viene de ningún documento. Que el filtro de alargamiento no esté en el camino del modelo se comprobó leyendo `modelo.py`. El guion lo presenta como mejora posible, no como error del sitio.
- **El experimento del JPG usa una sola imagen.** El guion dice que no es un estudio y que no hay una tendencia limpia.
- **No se da ningún tiempo de análisis.** Solo «decenas de segundos» por foto y que del servidor real no hay medición, igual que en el video 2.
- **Los conteos 41 y 45 no dicen cuál es el correcto.** El guion lo dice así.
- **Los documentos del proyecto no se enseñan.** Ni `docs/integracion-modelos.md` ni `docs/base-conocimiento/`. Lo que ahí se explica (escala, falsos positivos, largo, trabajo futuro) se dice hablando, sin abrirlos y sin decir «la documentación».
- **El 0.96 y el 1.00 vienen del módulo 2, video 2.** Aquí solo se recuerdan.
