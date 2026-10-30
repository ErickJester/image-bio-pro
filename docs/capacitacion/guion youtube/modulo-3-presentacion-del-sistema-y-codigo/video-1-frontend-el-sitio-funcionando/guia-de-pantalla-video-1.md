# Guía de pantalla del módulo 3, video 1: Frontend, el sitio funcionando

Este video no lleva mazo. Se graba la pantalla: el navegador con el sitio y el editor con el código, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se hace clic o se baja (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar y las cifras que el guion y la pantalla deben respetar. Si algo cambia en el sitio o en el código, hay que cambiar el guion (las dos versiones) y esta guía.

## Dos escenarios

| Escenario | Qué se abre | Tramos |
|---|---|---|
| Navegador | El sitio, con una cuenta de prueba y la imagen de ejemplo | 1 a 8, y partes de 12, 14, 15 y 16 |
| Editor | `base.html`, `resultados.html`, `sitio.js` y `estilos.css` | 9 a 15 |

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | De la teoría al sitio | Explorador, navegador | Mostrar `model/fluorescencia.pt` y pasar al inicio del sitio |
| 2 | Lo que ve el visitante | Navegador | Bajar el inicio, abrir el menú y entrar a cada sección |
| 3 | Español e inglés | Navegador | Cambiar a EN y volver a ES; señalar el nombre del proyecto |
| 4 | Crear la cuenta y entrar | Navegador | Mi cuenta, recuperar contraseña y crear la cuenta de prueba |
| 5 | Analizar una imagen | Navegador, consola | Formatos, aviso de error, cubierta de espera y análisis del ejemplo |
| 6 | Los resultados | Navegador | Recorrer la pantalla de arriba abajo |
| 7 | Revisar a mano | Navegador | Recuadro de detalle y visor con zoom |
| 8 | Varias imágenes, descargas e historial | Navegador | Promedio, CSV, PDF, imprimir, Mis análisis y el 404 |
| 9 | Cómo está hecho el frontend | Editor | Árbol de `app/` y líneas de Bootstrap y Chart.js |
| 10 | La plantilla base | Editor | `base.html`: bloques, menú, avisos, sesión y CSRF |
| 11 | Una plantilla con datos | Editor | `resultados.html`: ciclos, condición y valores |
| 12 | La imagen con una zona por espermatozoide | Editor, navegador | Polígonos en `resultados.html`, Elementos (F12) y `sitio.js` |
| 13 | El visor con zoom | Editor, navegador | `iniciarVisorZoom` y el visor funcionando |
| 14 | La gráfica | Editor, navegador | `graficaBarras`, `tojson` y el código fuente de la página |
| 15 | Detalles que importan | Navegador, editor | Tab, imprimir, ancho de celular, variables y `notranslate` |
| 16 | Lo que vimos y lo que sigue | Navegador | Inicio del sitio mientras se resume |

## Antes de grabar

- Sitio con la versión actual del repositorio corriendo en local (`python run.py` o `docker compose up`), con una base de datos aparte y una cuenta de prueba nueva. El sitio de producción va atrás del repositorio (1.0.0 contra 1.11.0), así que no se usa para este video hasta actualizarlo. Mientras no se decida dónde se graba (ver `../../plan-modulo-3.md`), se graba en local.
- Sin sesión iniciada al empezar: el tramo 4 crea la cuenta frente a la cámara. No usar correos ni nombres de personas reales.
- Navegador a 1440 px de ancho, zoom al 100 %, sin otras pestañas ni extensiones visibles.
- Editor con las cuatro pestañas ya abiertas en el orden en que se usan (`base.html`, `resultados.html`, `sitio.js`, `estilos.css`), letra grande y números de línea visibles.
- Antes del tramo 8, subir tres copias de `app/static/muestras/prueba.png` con otros nombres para tener un análisis con varias imágenes. Con una sola imagen no sale la gráfica del promedio.
- Para el tramo 5, un archivo `.txt` para el aviso de formato y la línea de la consola que muestra la cubierta de espera (está en el guion). Con la imagen de ejemplo el análisis termina en menos de un segundo.
- Para la última frase del tramo 8, una segunda cuenta de prueba con un análisis, o un número que no exista.
- Las capturas del 19 de octubre ya no sirven; si se quiere una imagen fija de apoyo, hay que tomarla de nuevo.
- La imagen principal del inicio sigue siendo un marcador ("[imagen principal]"). Se ve en el tramo 2; hay que decidir si se graba así o cuando ya haya imagen.
- Datos personales: el menú del navegador, la barra de marcadores y el editor no deben mostrar rutas ni cuentas del equipo.

## Cifras que dice el guion y que hay que mantener

- Imagen de ejemplo: 1200 × 900, PNG, unos 134 KB. Conteo 41. Área media 301.8 px² (desviación estándar 55.9). Largo medio 28.6 px (desviación estándar 16.7). En micras: área media 0.08 µm² (desviación estándar 0.02) y largo medio 0.48 µm.
- Escala del sitio: 60 píxeles por micra, provisional. La regla del marcado mide 300 píxeles y equivale a 5 micras.
- Histograma de ejemplo: 10 intervalos, de 179 a 455 px²; frecuencias 3, 1, 7, 7, 7, 8, 4, 2, 1, 1.
- Límites del sitio: 10 imágenes por análisis; formatos BMP, PNG y TIFF (JPG con aviso); aviso de espera al minuto; enlace de recuperación de una hora.
- Frontend: 15 plantillas (base 1, sitio 8, cuentas 4, análisis 2); Bootstrap 5.3.3; Chart.js 4.4.1; `estilos.css` 1,210 líneas; `sitio.js` 273; `videos.js` 86; `resultados.html` 178.
- Visor: escala de 1 a 12; copia marcada de hasta 1,400 px de lado y copia ampliada de hasta 2,800 px.
- Contornos guardados: simplificados (tolerancia de 1.5 px) y ordenados de mayor a menor área.

## Líneas que nombra el guion

El guion dice números de línea en pantalla. Se comprobaron con el código de la versión 1.11.0; si cualquiera de estos archivos cambia, hay que volver a comprobarlas.

| Archivo | Líneas |
|---|---|
| `app/templates/base.html` | Bootstrap 10; bloques 6, 80 y 115; sesión 47; CSRF 50; ciclo del menú 60 a 64; avisos 71 a 76; `notranslate` 33 |
| `app/templates/analisis/resultados.html` | `notranslate` 27; ciclo por imagen 25; condición 40; SVG y polígonos 48 a 58; canvas 82; filas de la tabla 94; PDF 114; Chart.js 145; `graficaBarras` 152 y 171 |
| `app/static/sitio.js` | `iniciarVisorZoom` 121; `aplicar` 141; transformación 143; `zoomEn` 154; `iniciarDetalleEsperma` 230 |
| `app/static/estilos.css` | `:root` 4; impresión 943; movimiento reducido 962 |

## Cosas que el guion dice con cuidado

- El color de cada cabeza se calcula pero no se muestra en los resultados. El guion no habla de clasificar por color en pantalla.
- La traducción al inglés es automática (traductor de Google); no es una traducción revisada.
- La escala de 60 píxeles por micra es provisional. El guion remite al video 4 del módulo.
- Si el sitio de producción va atrás del repositorio, la diferencia no se menciona en el video.
- La consola (F12) solo se usa en el tramo 5, para dejar a la vista la cubierta de espera; hay que decir que es una forma de enseñarla y que no es algo que el visitante haga.
- La cuenta de prueba se crea frente a la cámara: usar una contraseña de prueba, sin reutilizar ninguna real.
