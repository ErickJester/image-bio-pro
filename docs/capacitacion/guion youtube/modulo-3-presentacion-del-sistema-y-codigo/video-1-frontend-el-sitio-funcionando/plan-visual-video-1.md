# Plan visual del módulo 3, video 1: Frontend, el sitio funcionando

Lo que lleva cada diapositiva. El guion habla de estas imágenes y de estos números tal como están aquí, así que el mazo debe respetarlos. Si algo cambia en el mazo, hay que cambiar el guion (las dos versiones) y viceversa.

Estilo: el de los videos del módulo 2 (fondo oscuro y claro alternados, azul marino, azul petróleo, celeste y naranja como único acento, letra grande, pocas ideas por diapositiva). Los dibujos son propios, en SVG. Este video muestra el sitio y su código, así que lleva dos tipos de imagen que el módulo 2 casi no usó: capturas del sitio y fragmentos de código.

Origen de las imágenes:
- Captura: pantalla del sitio funcionando, tomada con la versión actual del repositorio (no con la de producción, que va atrás). Hay que volver a tomarlas si el sitio cambia. Las capturas del 19 de octubre están desactualizadas.
- Código: fragmento real de un archivo del repositorio, copiado tal cual (sin adornos) y con el nombre del archivo y las líneas.
- Calculado: sale de analizar la imagen de ejemplo del sitio (`app/static/muestras/prueba.png`) con `medicion.analizar_imagen`.
- SVG: dibujo propio dentro del mazo.
- Las fotos del cliente no se publican. Todas las capturas de resultados usan la imagen de ejemplo.

Regla para el código en pantalla: 6 a 12 líneas por diapositiva, letra de 24 px o más, el resto del archivo se omite con una línea de puntos. Lo que el guion nombra (extends, url_for, flash, tojson) debe verse resaltado en el fragmento.

| N.º | Diapositiva | Qué se ve | Origen |
|---|---|---|---|
| 1 | De la teoría al sitio | Etiqueta "Módulo 3 · Video 1". A la izquierda, el archivo del modelo (`fluorescencia.pt`) con la leyenda "sin página no hace nada"; a la derecha, la captura del sitio con resultados; una flecha entre ambos. Debajo, los cuatro videos del módulo en una fila, con el primero resaltado. | SVG, captura |
| 2 | Lo que ve el visitante | Captura del inicio. A un lado, el menú abierto con sus siete secciones. Debajo, tres tarjetas con los tres capítulos del inicio (el problema, el recorrido de una imagen, resultados que se pueden revisar). Una nota: "Sin cuenta se ve todo menos el análisis". | Captura, SVG |
| 3 | Español e inglés | Dos capturas del inicio, una en ES y otra en EN, con el selector resaltado. Debajo, un esquema de cuatro pasos: clic en EN, cookie con el par de idiomas, recarga, el traductor la lee. Una tarjeta naranja: "notranslate: el nombre del proyecto y los nombres de archivo no se traducen". | Captura, SVG |
| 4 | Crear la cuenta y entrar | Captura de la pantalla Mi cuenta con sus dos columnas. Debajo, un esquema de la recuperación de contraseña: correo, enlace por correo, una hora, contraseña nueva. Tarjeta: "La respuesta es la misma exista o no la cuenta". | Captura, SVG |
| 5 | Analizar una imagen | Captura de la pantalla de análisis. Tres tarjetas: "Hasta 10 imágenes", "BMP, PNG o TIFF (JPG con aviso)", "Se borran al terminar". Al lado, la cubierta de espera con su barra de progreso y el aviso "Tu análisis sigue en curso" que sale al minuto. | Captura |
| 6 | Los resultados | Captura de la pantalla de resultados con la imagen de ejemplo. Tarjetas con los tres números grandes: conteo 41; área media 0.08 µm²; desviación estándar 0.02 µm². Debajo, los mismos datos en píxeles: área media 301.8 px² (desviación estándar 55.9) y largo medio 28.6 px (0.48 µm). Datos del archivo: PNG, 1200 × 900, unos 134 KB. Aviso azul: "60 píxeles por micra (provisional)". | Captura, calculado |
| 7 | Revisar a mano | Captura de la imagen marcada con la regla de 300 px (5 µm) abajo a la izquierda. Una ampliación del visor con el recuadro de detalle sobre un espermatozoide: número, área y largo, en píxeles y en micras. Cuatro iconos: rueda, arrastre, doble clic, dos dedos. | Captura, calculado |
| 8 | Varias imágenes, descargas e historial | Captura de la gráfica del promedio y de los cuatro botones del final (imprimir, PDF, CSV, analizar otras). Captura de la tabla Mis análisis del perfil. Nota: "Cada persona ve solo los suyos". | Captura |
| 9 | Cómo está hecho el frontend | Cinco tarjetas en fila: plantillas Jinja2 (15), Bootstrap 5.3.3, estilos.css (unas 1,200 líneas), JavaScript (sitio.js unas 270 y videos.js unas 90), Chart.js 4.4.1. Debajo, un árbol de carpetas: `templates/` con base (1), sitio (8), cuentas (4) y análisis (2). Tarjeta: "Sin framework de frontend". | SVG |
| 10 | La plantilla base | Código de `app/templates/base.html` en dos fragmentos: la lista de rutas con su ciclo y `url_for`; y el bloque que dibuja los avisos de `flash`. Al lado, un esquema: la base con tres huecos (título, contenido, scripts) y otra plantilla con `extends` que los llena. | Código, SVG |
| 11 | Una plantilla con datos | Código de `app/templates/analisis/resultados.html`: el ciclo por imagen, la condición y el ciclo de filas. Al lado, un esquema "datos del servidor → plantilla → HTML". Tarjeta: "Jinja2 escapa los datos: un nombre con signos no se vuelve código". | Código, SVG |
| 12 | La imagen con una zona por espermatozoide | Esquema en capas: la imagen marcada, el SVG con polígonos transparentes, el recuadro de detalle. Código del polígono con sus atributos (`data-area-um`, `data-largo-um`) y la línea del ciclo que los ordena de mayor a menor área. Pie: "Al pasar el cursor no se pide nada al servidor". | Código, SVG |
| 13 | El visor con zoom | Esquema del zoom hacia el cursor: antes y después, con el punto bajo el cursor fijo. Código de la transformación (traslación y escala). Tarjetas: "Escala de 1 a 12", "Copia reducida (1,400 px) y ampliada (2,800 px)", "Ratón o dos dedos". | Código, SVG |
| 14 | La gráfica | Código de la llamada a `graficaBarras(...)` con `\| tojson`. Al lado, la gráfica de barras de la imagen de ejemplo (10 intervalos, frecuencias 3, 1, 7, 7, 7, 8, 4, 2, 1, 1; bordes de 179 a 455 px²). Tarjeta: "La misma información está en la tabla". | Código, calculado |
| 15 | Detalles que importan | Cinco tarjetas con icono: teclado (saltar al contenido), lectores de pantalla, impresión, movimiento reducido, celular. A un lado, dos capturas: la página en pantalla y la vista de impresión. | SVG, captura |
| 16 | Lo que vimos y lo que sigue | Dos columnas: "El sitio" (cuenta, análisis, resultados, revisión, descargas, historial) y "El frontend" (plantillas, Bootstrap, JavaScript puntual, Chart.js). Una tarjeta: "Siguiente: el backend". | SVG |

## Cómo se obtienen las imágenes

- **Capturas:** con la versión actual del repositorio corriendo en local (`docker compose up`), sesión iniciada con una cuenta de prueba y la imagen de ejemplo. Una captura por pantalla, en ventana de 1440 px de ancho, sin datos de personas reales. No se capturan correos ni cuentas del cliente.
- **Código:** se copia del archivo, con su nombre y rango de líneas al pie. Si el archivo cambia antes de grabar, se vuelve a copiar.
- **Diapositivas 6, 7 y 14:** los números salen de analizar la imagen de ejemplo con `medicion.analizar_imagen`. Si el modelo o la escala cambian, estos números cambian y hay que corregir el guion.

## Cifras que dice el guion y que hay que mantener

- Imagen de ejemplo: 1200 × 900, PNG, unos 134 KB. Conteo 41. Área media 301.8 px² (desviación estándar 55.9). Largo medio 28.6 px (desviación estándar 16.7). En micras: área media 0.08 µm² y largo medio 0.48 µm.
- Escala del sitio: 60 píxeles por micra, provisional. La regla del marcado mide 300 píxeles y equivale a 5 micras.
- Histograma de ejemplo: 10 intervalos, de 179 a 455 px²; frecuencias 3, 1, 7, 7, 7, 8, 4, 2, 1, 1.
- Límites del sitio: 10 imágenes por análisis; formatos BMP, PNG y TIFF (JPG con aviso); aviso de espera al minuto; enlace de recuperación de una hora.
- Frontend: 15 plantillas (base 1, sitio 8, cuentas 4, análisis 2); Bootstrap 5.3.3; Chart.js 4.4.1; `estilos.css` 1,210 líneas; `sitio.js` 273; `videos.js` 86; `resultados.html` 178.
- Visor: escala de 1 a 12; copia marcada de hasta 1,400 px de lado y copia ampliada de hasta 2,800 px.
- Contornos guardados: simplificados (tolerancia de 1.5 px) y ordenados de mayor a menor área.

## Cosas que el guion dice con cuidado

- El color de cada cabeza se calcula pero no se muestra en los resultados. El guion no habla de clasificar por color en pantalla.
- La traducción al inglés es automática (traductor de Google); no es una traducción revisada.
- La escala de 60 píxeles por micra es provisional. El guion remite al video 4 del módulo.
- El modelo que mide es el que está desplegado; si el sitio de producción va atrás del repositorio (1.0.0 contra 1.11.0), las capturas deben tomarse en local y la diferencia no se menciona en el video.

## Imágenes del mazo (cómo quedó)

- Las capturas se tomaron con la versión actual del repositorio corriendo en local (puerto 5055), con una base de datos aparte y una cuenta de prueba, y con la imagen de ejemplo. Resultados: 41 espermatozoides, área media 0.08 µm² (301.8 px²), largo medio 28.6 px (0.48 µm).
- La imagen principal del inicio todavía es un marcador de posición ("[imagen principal]"). Las capturas del inicio la dejan fuera (se recorta la barra y el texto). Cuando haya imagen, conviene volver a tomarlas.
- Diapositiva 5: la cubierta de espera se capturó con el aviso del minuto ya visible (se forzó en la página); el análisis con la imagen de ejemplo termina en menos de un segundo.
- Diapositiva 6: los tres números grandes de la pantalla de resultados están en micras cuadradas (conteo, área media y desviación estándar); los valores en píxeles salen en el texto de abajo. El guion y el mazo dicen lo mismo.
- Diapositiva 8: con un solo análisis no se ve la gráfica del promedio; el mazo lo dice y el guion explica cuándo aparece.
- Diapositivas 10 a 14: el código es real, copiado de `base.html`, `resultados.html` y `sitio.js`. Algunas líneas se parten o se omiten con puntos suspensivos para que quepan, y el pie de cada diapositiva lo dice.
- Diapositiva 13: el dibujo de antes y después del zoom es un esquema, no una captura.
- Diapositiva 14: el histograma es una captura de la gráfica real de la imagen de ejemplo, con la misma lista de frecuencias que muestra el código.

