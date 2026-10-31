# Guía de pantalla del módulo 4, video 1: El cuaderno de Colab, primera parte

Este video no lleva mazo. Se graba la pantalla: el cuaderno de Colab, celda por celda, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de celda, se ejecuta o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, lo que se espera ver al ejecutar cada celda y las cifras que el guion debe respetar. Si cambia el cuaderno, las fotos o el perfil, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Celdas | Qué se hace |
|---|---|---|---|
| 1 | Un cuaderno de Colab y de dónde sale el modelo | Introducción | Se enseñan la introducción, los diez pasos y los requisitos; no se ejecuta nada |
| 2 | Paso 1: el entorno | 2 y 3 | Se ejecutan la comprobación de la GPU y la conexión a Drive |
| 3 | Paso 2: la configuración | 5 y 6 | Se recorre la celda de configuración y se ejecutan ella y la de imports |
| 4 | Paso 3: leer las etiquetas | 8 | Se explica `leer_anotaciones` y se ejecuta |
| 5 | Paso 4: entrenamiento y validación | 10 | Se explica `crear_zonas` y se ejecuta |
| 6 | Paso 5: preparar las fotos | 12 | Se explican `preparar_imagen` y `preparar_cache` y se ejecuta |
| 7 | Paso 6: recortes y aumento de datos | 14 y 16 | Se recorre `RecortesEntrenamiento` y se ejecuta la revisión visual |
| 8 | Lo que ya está listo y lo que sigue | Introducción | Se vuelve a la lista de pasos |

Los números de celda cuentan todas las celdas del archivo `.ipynb` (de texto y de código) desde cero; Colab no los muestra. En pantalla se buscan por su título.

## Antes de grabar

- El cuaderno `entrenamiento/entrenar_mask_rcnn.ipynb` abierto en Colab, con el entorno de ejecución en GPU (Entorno de ejecución, Cambiar tipo de entorno).
- En Drive, la estructura que pide el cuaderno: `MyDrive/image-bio-pro/datos/imagenes/` con las fotos BMP etiquetadas y `MyDrive/image-bio-pro/datos/instances_default.json` con el archivo COCO exportado de CVAT.
- En la celda de configuración, `MODO_PRUEBA = True` y `PERFIL = "fluorescencia"`. No se toca nada más.
- Números de línea activados en Colab (Herramientas, Configuración, Editor). El guion cita líneas dentro de cada celda.
- **Cambio previo en el cuaderno.** Dos comentarios nombran a quien pidió la opción: la línea 35 de la celda de introducción («Las fotos son del …») y la línea 32 de la celda de configuración («petición del …»). Antes de grabar hay que cambiarlos por «laboratorio» o evitar enseñar esas líneas. Cambiar el cuaderno es un cambio del proyecto y lleva versión; está sin hacer.
- Al conectar Drive, Google pide permiso desde la cuenta de la persona. No se muestra el correo ni la pantalla de la cuenta al grabar.
- Las fotos son del laboratorio. Si se muestran en pantalla (por ejemplo en la revisión visual), confirmar antes que se pueden mostrar.
- La figura `figuras/revision-de-recortes.png` abierta en un visor, como referencia de lo que debe verse en la revisión visual. No es de las fotos del laboratorio.

## Qué se espera al ejecutar cada celda

Marcado como **real** lo que se ejecutó el 30/10/2026 en esta computadora con la foto de ejemplo del sitio (una sola foto, con los contornos del modelo en lugar de etiquetas de CVAT). Marcado como **por confirmar** lo que solo se puede ver en Colab con las fotos del laboratorio.

| Celda | Qué imprime | Estado |
|---|---|---|
| 2 (GPU) | Versiones de PyTorch y torchvision, `GPU disponible: True` y el nombre de la tarjeta | Por confirmar. Los metadatos del cuaderno piden una T4 |
| 3 (Drive) | Ventana de permiso de Google; no imprime nada si conecta | Por confirmar |
| 5 (configuración) | `MODO_PRUEBA activo: 2 épocas muy cortas, solo para comprobar que todo corre.` y `Cuaderno versión 0.5.1 \| perfil: fluorescencia \| corrida: corrida_05_prueba` | Real |
| 6 (imports) | `Dispositivo: cuda \| salida: /content/drive/MyDrive/image-bio-pro/entrenamiento/corrida_05_prueba` | Por confirmar (sin tarjeta gráfica el cuaderno se detiene) |
| 8 (etiquetas) | Fotos y espermatozoides etiquetados, tabla por foto, lado mayor mínimo, mediana y máximo | Por confirmar. Según el proyecto: fluorescencia, 4 fotos y 258; campo claro, 4 fotos y 45 |
| 10 (zonas) | Tabla de zonas, totales, avisos y `Recortes por época: 16` | Real con la foto de ejemplo: 28 y 10 espermatozoides, y el aviso de pocos para validar. Con las fotos del laboratorio, otras cifras |
| 12 (fotos) | `N fotos preparadas en X s: a de fluorescencia y b de campo claro` | Por confirmar. Los archivos se llaman `<id>_g_r100.npy` en fluorescencia y `<id>_gi_r50.npy` en campo claro |
| 14 (recortes) | `N espermatozoides disponibles para centrar recortes` | Real con la foto de ejemplo: 28. Por confirmar con las fotos del laboratorio |
| 16 (revisión) | Seis recortes con el contorno verde y el número de espermatozoides en cada título | Real con la foto de ejemplo: ver `figuras/revision-de-recortes.png` |

## Cifras que el guion usa

- Perfiles: mixto, teselas de 1024 y traslape de 768 (los valores de arriba, sin cambios). Fluorescencia: teselas de 512, traslape de 128, sin invertir. Campo claro: fotos reducidas a la mitad, teselas de 640, traslape de 384, brillo invertido.
- El espermatozoide más grande mide 677 píxeles en campo claro y 116 en fluorescencia (comentario de la línea 41 de la configuración).
- Semilla 42. Modo de prueba: 2 épocas, 16 recortes por época, se valida y se guarda cada época, y el nombre de la corrida termina en `_prueba`.
- Validación: 10 fotos o más, una quinta parte y por lo menos una; menos de 10, una franja de un cuarto de cada foto con 100 píxeles de separación. Una foto de 1,792 píxeles de ancho: entrenamiento de 0 a 1,244 y validación de 1,344 a 1,792 (comprobado con `crear_zonas`).
- Avisos: menos de 20 espermatozoides en la validación, métricas poco confiables; menos de 10, no se elige el mejor modelo ni el umbral con ella (el umbral queda en 0.5).
- Recortes por época fuera del modo de prueba, con el perfil de fluorescencia: el mayor entre 400 y 16 por foto de entrenamiento, es decir 400 con 4 fotos.
- Validación de las corridas documentadas: fluorescencia, 66 espermatozoides; campo claro, 2.
- Caché: `g_r100` (fluorescencia) y `gi_r50` (campo claro). Una foto BMP pesa unos 30 megabytes; en grises, un arreglo ocupa un tercio del tamaño con tres canales (comprobado: 1,080,000 contra 3,240,000 bytes en la foto de ejemplo del sitio).
- Recortes: 80 % centrados en un espermatozoide; factor de escala de 0.8 a 1.25; desplazamiento hasta ±35 % del lado; un espermatozoide cortado cuenta si queda visible al menos el 30 % de su área y 20 píxeles; volteo horizontal y vertical con 50 % cada uno; giros de 0 a 3 veces 90°; brillo de 0.7 a 1.3 más un desplazamiento de ±20; ruido hasta 6.
- Versiones guardadas en los archivos de modelo de esta computadora: fluorescencia 0.3.1 y campo claro 0.5.0; el cuaderno es el 0.5.1.

## Líneas que nombra el guion

Las líneas se cuentan dentro de cada celda.

| Celda | Líneas |
|---|---|
| Introducción (0) | pasos 14 a 25; requisitos 27 a 42 (la 35 nombra a quien pidió la opción) |
| Configuración (5) | rutas y modo 1 a 25; clase y preparación de la imagen 26 a 37 (la 32 nombra a quien pidió la opción); recortes y tamaño 38 a 53; separación 55 a 68 y entrenamiento 69 a 82 (solo se señalan); perfiles 95 a 111; modo de prueba y mensaje 113 a 119 |
| Imports (6) | 1 a 22 (dispositivo 14 a 17, semillas 19 y 20) |
| Etiquetas (8) | `leer_anotaciones` 17 a 84 (categoría 20 a 23, fotos 25 a 47, anotaciones 49 a 71, avisos 72 a 84); resumen 87 a 105 |
| Zonas (10) | `crear_zonas` 1 a 22; tabla y avisos 30 a 42; recortes por época 44 a 47 |
| Fotos (12) | `preparar_imagen` 1 a 12; `preparar_cache` 15 a 24; ejecución 27 a 30 |
| Recortes (14) | `mascara_local` 1 a 16; clase 23 a 52; cortar 54 a 71; máscaras 73 a 85; aumento 87 a 101; objetivo 103 a 116 |
| Revisión (16) | 1 a 16 |

## Cosas que el guion dice con cuidado

- **No se corre el entrenamiento.** Este video llega hasta la revisión visual. El modo de prueba se enciende aquí porque la configuración se ejecuta ahora, pero las dos épocas se corren en el video siguiente.
- **Con cuatro fotos, la validación sale de las mismas fotos.** El guion lo dice así y no presenta la validación como una prueba con fotos nuevas. Con dos espermatozoides en la validación de campo claro, un resultado perfecto no prueba nada.
- **Las cifras de 258, 45, 66 y 2 vienen del proyecto, no de una corrida de hoy.** Hay que confirmarlas con la salida real de las celdas 8 y 10 en Colab antes de grabar, y ajustar el guion si no coinciden.
- **Los modelos que hay en `model/` salieron de versiones anteriores del cuaderno.** El guion lo dice como curiosidad y sin dar a entender que el cuaderno actual produce exactamente esos archivos.
- **La T4 «del plan gratuito».** Los metadatos del cuaderno piden una T4; que Colab la dé en su plan gratuito no se comprobó hoy.
- **Que invertir el brillo ayude no está comprobado.** El comentario del cuaderno lo dice y el guion lo repite.
- **La figura de la revisión visual usa contornos del modelo, no etiquetas de CVAT.** Las colas marcadas como espermatozoide que se ven en ella son del modelo (ver el reto 3 del módulo 3).
- **No se muestran los documentos del proyecto.** Lo que explican se dice hablando.
- **El guion pasa de los 20 minutos previstos** (22.5 y 22.9 minutos de habla, sin contar las pausas de ejecutar celdas). Si hay que recortar, lo más fácil es la explicación de la configuración (tramo 3) y el detalle del aumento de datos (tramo 7).
