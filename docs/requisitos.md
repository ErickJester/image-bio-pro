# Requisitos

Requisitos de Image Bio Pro tomados **solo de la transcripción de la reunión con el cliente**. Cada uno cita la frase de donde sale. Lo que no se dijo en la reunión no está aquí: las decisiones técnicas van en el [README](../README.md) y lo que quedó sin resolver está al final, en "Pendientes".

Versión del 7 de octubre de 2026, pendiente de validar con el cliente junto con el boceto.

- **Funcional:** algo que el sistema **hace**.
- **No funcional:** **cómo** debe ser o qué condiciones debe cumplir.

## Requisitos funcionales

### Sitio informativo

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-01 | El sitio tiene un menú tipo hamburguesa con sus secciones, entre ellas una de infografías. | "el menú de hamburguesa, por lo general las pestañas… una sección de infografía" |
| RF-02 | La página principal lleva como título *Image Bio Pro*. | "aquí como título iría *Image Bio Pro*" |
| RF-03 | El sitio está en inglés y español, con un selector EN/ES y traducción automática con la API de Google Traductor. | "me pidieron es que estuviera en inglés y español"; "se puede traer la API de Google Traductor, y ya se lo traduce automáticamente" |
| RF-04 | La sección Nosotros muestra solo "¿Qué es Image Bio Pro?" con el texto que pase el grupo. | "llevaría uno que lleve 'Nosotros' y nada más, '¿Qué es Image Bio Pro?'… No habría como más cosas" |
| RF-05 | La sección Contacto ("Haz contacto") tiene el formulario clásico, con correo. | "nada más sería 'Haz contacto', ¿no? El formulario clásico que viene, ¿no? Correo y así" |
| RF-06 | La sección Aliados muestra a las personas del grupo con su nombre, su foto y una reseña. | "vendría como el nombre de las personas que estamos en el grupo"; "quedaría pendiente subir las fotografías o los nombres"; "'Fulano de tal' es esto" |
| RF-07 | Las infografías se muestran como cuadros; al dar clic, se abre una ventana grande que despliega la imagen y el texto, como un blog. | "le apucha aquí y automáticamente en esta página sale grande esta ventana y despliega información"; "Casi como si fuera blog" |
| RF-08 | El título de cada infografía va fuera de la imagen. | "¿esto ya vendría dentro de la imagen, verdad? — No, eso sí puede ir… afuera" |
| RF-09 | El sitio muestra unos 4 videos cortos de YouTube que se reproducen en la misma página. | "lo que ellos quieren es que aquí mismo aparezca esa imagen de YouTube"; "Van a ser más o menos como cuatro videos… cortos de cuatro minutos" |

### Página de inteligencia artificial y cuentas

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-10 | La página de inteligencia artificial tiene una imagen de fondo, una sección para subir la imagen y un botón para analizarla. | "solo sería… como una imagen… de fondo"; "una sección que es para *upload image*"; "el botón de *enter*… O analizar" |
| RF-11 | La página de inteligencia artificial puede tener algún parámetro ajustable, si hace falta. | "O algún parámetro que se requiera modificar… iríamos viendo si es necesario o si no" |
| RF-12 | La página de inteligencia artificial lleva infografías como complemento, para que no se vea vacía. | "la página de inteligencia artificial se va a ver como muy sencillita, entonces… necesita tener como un poquito de relleno… Y van a ser infografías" |
| RF-13 | Para usar la red neuronal hay que iniciar sesión. | "Debe ser una página que tenga… que se pueda loguear para… la red neuronal" |
| RF-14 | Una persona se registra con su correo electrónico y con eso puede entrar. La cuenta sirve solo para tener acceso. | "con un correo electrónico quedaría"; "simplemente 'regístrate' y ya ingresa"; "así es como para que tengan una cuenta" |

### Análisis de imágenes

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-15 | El sistema cuenta cuántas células hay en la imagen. | "Contar las células, cuántas células hay en esa imagen" |
| RF-16 | El sistema no cuenta los puntos y líneas del fondo, que son ruido del microscopio. | "hay algunos puntos que están como muy al fondo… son solamente ruido del microscopio"; "esas líneas no contarían" |
| RF-17 | El sistema mide cuánto mide cada célula. | "hay que medir eh pues cuánto miden cada uno de ellos" |
| RF-18 | El sistema genera la gráfica de distribución de tamaños, tipo campana de Gauss. | "haría una gráfica como tipo Gauss"; "gráfica de distribución" |
| RF-19 | El sistema clasifica las células por color y dice cuántas son anaranjadas y cuántas rojas. | "clasificar cuántas anaranjadas son y cuántas rojas son" |
| RF-20 | Los resultados se pueden descargar en CSV y en PDF. | "descargar en CSV o en Excel"; "Sí, se puede descargar en CSV y en PDF" |
| RF-21 | El modelo se puede volver a entrenar y subir al sitio cuando haya más imágenes u otro tipo de células. | "Ahí sí se tiene que poner a entrenar y… subirle el modelo"; "si… son otro tipo de células, se tiene que volver a entrenar" |

## Requisitos no funcionales

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RNF-01 | El diseño es sencillo: sin muchos colores ni un nivel de detalle alto de diseño. FEMEXER es solo referencia de estructura. | Sobre FEMEXER: "tiene como muchos colores"; "tampoco nosotros queremos que lleve algo así como mucho tema a ese nivel de detalle" |
| RNF-02 | El formato de los resultados es flexible: si la gráfica se complica, basta con un archivo de texto con el conteo y las medidas. | "si ve complicado… graficar… no importa. Con que me dé este txt… 'Células'… medidas"; "si a usted se le facilita más fácil un TXT, un CSV, adelante" |
| RNF-03 | Los servicios se contratan en el plan justo, sin pagar de más. El hosting (por ejemplo Hostinger) se puede pagar por año. | "¿Cuál plan necesito?… no necesitas de más… O sea, lo justo"; "Anualmente se puede" |
| RNF-04 | Google Colab se paga en el plan barato mientras se trabaja con unas 10 imágenes, y en el más caro cuando lleguen las 50. | "en esta que tenemos las 10 imágenes paguemos el más barato y ya cuando sean las 50 imágenes paguemos el más caro" |
| RNF-05 | El avance debe poder mostrarse por etapas, y el primer entregable es el sitio en línea. | "sería más fácil para mí poder justificar y decir: '¿Sabes qué? Ya avanzamos en A, B, C'"; "quieren ver el primer entregable que es el sitio web… como que ya está en línea" |

## Restricciones

- **Fecha:** el sitio web y los avances de la red neuronal, para finales de octubre: "como por ahí del 29 o 30 de octubre". El correo posterior del cliente lo fijó el 28 de octubre.
- **Datos:** por ahora hay una sola imagen ("Es la única que me han compartido de momento"). El modelo inicial se arma con unas 10 imágenes y solo sirve como esqueleto ("de antemano no nos va a servir como de mucho"). El entrenamiento real será con unas 50 imágenes.
- **Las imágenes de ejemplo** son de espermatozoides teñidos "más o menos" en rojo, amarillo y naranja. El tono de las imágenes oficiales puede ser "mucho más sutil".
- **El modelo no aprende solo** una vez en línea: hay que reentrenarlo aparte.

## Fuera de alcance

- **Distinguir control contra tratamiento** (o tejido sano contra enfermo): "esto que le estoy planteando es perspectiva, o sea esto no es parte del proyecto".
- **Red neuronal con imágenes y datos AnnData:** "sería un proyecto aparte"; el cliente solo pidió saber si es viable.

## Pendientes

Lo que en la reunión quedó sin respuesta o ambiguo:

| Pendiente | Qué se dijo | Requisitos afectados |
|---|---|---|
| ¿Los análisis de cada usuario son privados o los ve todo el grupo? | El cliente preguntó si serían individuales o compartidos y no se respondió. Tu propuesta: privados. | RF-13, RF-14 |
| Unidad de medida del tamaño | El ejemplo del cliente usó milímetros, pero solo como ilustración. Tu propuesta: micrómetros. | RF-17, RF-18 |
| ¿Dónde van los videos? | "más abajo de esto, o sea, de esta infografía… o en Contacto, o en Aliados, perdón" | RF-09 |
| ¿Contacto lleva solo el formulario o también los datos del área? | "El formulario clásico que viene, ¿no? Correo y así." Tu propuesta: ambas cosas. | RF-05 |
| ¿Hace falta algún parámetro ajustable en la página de IA? | "iríamos viendo si es necesario o si no" | RF-11 |
| ¿Qué significa biológicamente el color anaranjado o rojo? | No se explicó; el tono puede ser más sutil en las imágenes oficiales. | RF-19 |
| Fotos, nombres, textos, infografías y videos | El grupo los va a pasar. | RF-04 a RF-09 |
