# Requisitos

Requisitos de Image Bio Pro tomados **solo de la transcripción de la reunión con el cliente**. Cada uno cita la frase de donde sale. Lo que no se dijo en la reunión no está aquí: las decisiones técnicas van en el [README](../README.md) y lo que quedó sin resolver está al final, en "Pendientes".

Versión del 7 de octubre de 2026 (primera reunión), ampliada el 12 de octubre con la reunión de requisitos del clasificador. Los requisitos RF-22 en adelante y RNF-06 en adelante salen de la segunda reunión; los cambios sobre la primera están en "Cambios respecto a la primera reunión".

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

## Segunda reunión: requisitos del sistema y del clasificador

Hablante 1 es el cliente; hablante 2, el desarrollador. Solo se toma como requisito lo que dijo o aceptó el cliente. Entre corchetes va el minuto de la transcripción.

### Mediciones y estadística

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-22 | Medida 1: la distancia que abarca la cabeza. | "El primer parámetro sería la distancia que hay de este punto a este punto" [04:37, "De cabeza"] |
| RF-23 | Medida 2: de la punta de la cabeza a la cola, siguiendo la forma de la célula aunque esté doblada. | "este está como doblado… Entonces puede ser que mida más… ¿se puede medir esta sección así?" [05:17]; "quedaría súper bien si se puede" [06:05] |
| RF-24 | Medida 3: la "distancia real", en línea recta. | "sería esta distancia que está acá… la tercera distancia. Digamos la distancia real" [06:05] |
| RF-25 | Medida 4: el área de la cabeza en píxeles. | "toda esta parte… tiene un cierto nivel de píxeles… 300 píxeles… 260 píxeles" [06:05, 07:41] |
| RF-26 | Por imagen, gráfica de distribución del tamaño de cabeza: eje horizontal el tamaño, eje vertical el número de células. | "una gráfica de distribución… N contra N, o sea número de datos… una frecuencia" [07:41, 10:39] |
| RF-27 | Con varias imágenes, una segunda gráfica con promedios: por cada tamaño, el promedio entre imágenes, usando el mínimo y el máximo encontrados en todas. | "a las de 200 hiciera un promedio… con base al mínimo y máximo que encuentre en todas las imágenes… Ya la gráfica con promedios" [11:08] |
| RF-28 | El sistema cuenta las células. | "el conteo de células… aquí son 4 células" [21:21]; "con el conteo de celdas cinco datos" [21:45] |
| RF-29 | El PDF y la pantalla muestran la media y la desviación estándar. | "la gráfica de distribución… Y la media. ¿Es posible que podamos imprimir la desviación estándar?" — "Sí, también" [36:40] |
| RF-30 | Cómo separar cabeza de cola lo define el modelo; el cliente sugiere como estrategia tomar como cabeza lo que quede dentro de un radio fijo (ejemplo: 1.5 µm) desde la punta, y validar manualmente con el conjunto de entrenamiento. | "Todo lo que aparezca en un radio de 1.5 micrómetros considérelo como cabeza" [18:57]; "tendríamos que validar… inclusive manual" [21:13]; "lo que dé el modelo" [18:00] |

### Clasificación por color

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-31 | Hay dos tipos de espermatozoides por color; rojo es sano y amarillo es enfermo. | "uno es… amarillo y otro es rojo" [24:32]; "rojo está sano y amarillo está enfermo" [48:59] |
| RF-32 | El color es una variable ordinal: el sistema reparte el color, del mínimo al máximo, en 10 grados equidistantes entre rojo y amarillo, y cada célula cae en uno. El grado 10 es completamente sano y el 1 completamente enfermo (el cliente dijo "o al revés"). | "dividir en 10 regiones de color, que va del amarillo al rojo… equidistantes" [57:12]; "categoría 10 es completamente sano… la categoría 1 es enfermo" [58:08] |
| RF-33 | El color se mide solo en la cabeza. Si dos cabezas se juntan, su color se promedia, con cierto error asociado. | "A partir de la cabeza solamente… ese color lo podemos promediar" [54:29, 54:45] |
| RF-34 | El resultado de color es el conteo y el porcentaje de células en cada grado. | "70 cabezas rojas, 30 amarillo rojizo… 70 entre 200…" [54:45]; "categoría 10, sano, sería por ejemplo 30%. Aquí 20%…" [58:56] |

### Entrada y avisos del sistema

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-35 | Se pueden subir hasta 10 imágenes a la vez, y puede ser menos. | "Ese ya le definimos desde ahorita, que suba 10 imágenes" [33:36]; "Pero máximo, ¿no?… uno, dos o tres" [35:59] |
| RF-36 | Mientras se analiza se muestra una barra de progreso o mensaje de que está trabajando. | "un diseño de que está cargando… Una barra de progreso. Sí" [34:26] |
| RF-37 | Si la imagen no es de espermatozoides, el sistema avisa que no corresponde. | "la imagen seleccionada no corresponde a una biopsia de espermatozoides" [41:48] |
| RF-38 | Si no encuentra espermatozoides o la calidad es mala, avisa que no es factible analizarla. | "aquí no hay espermatozoides, la imagen seleccionada es de mala calidad, no es factible analizar la imagen" [43:00] |
| RF-39 | Si todo salió bien, avisa que la imagen se analizó con éxito. | "Y la imagen fue analizada con éxito" [44:38] |
| RF-40 | Avisos (warnings) cuando el análisis se hizo pero no distinguió bien la clasificación, los tamaños o la forma; o contó pero no clasificó, o clasificó pero no contó. | "no distinguió bien la clasificación… los tamaños… la forma" [45:26]; "contabilizó pero no clasificó… o clasificó pero no contabilizó" [45:56] |
| RF-41 | Cuando el aviso indica que la red no funcionó para esa imagen, el sistema deja claro que no la analizó, en lugar de dar un resultado dudoso. | "para que la persona diga, ah no la analizó… si da un resultado va a decir, no sirve tu red neuronal" [46:29, 46:43] |
| RF-42 | La interfaz del análisis solo tiene el botón de ejecutar, sin modificaciones. | "nada más tendría el botón de ejecutar… no vamos a ponerle a hacer alguna modificación" [40:30] |

### Resultados, PDF e historial

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-43 | El resultado se imprime en pantalla y, hasta abajo, aparece la opción de imprimir. | "imprimir en pantalla… en el sitio web aparezca… y nada más hasta abajo aparezca imprimir" [36:18, 38:07] |
| RF-44 | Si se suben varias imágenes, sale un solo PDF con un análisis por imagen. | "Subió 10 imágenes, un solo PDF con 10 análisis" [35:48] |
| RF-45 | El PDF lleva: nombre del usuario, fecha y hora (muy importante), encabezado con logotipo, características de la imagen (metadatos), resultados, gráfica de distribución, media y desviación estándar. | "nombre del usuario, fecha… principalmente la fecha y hora… Le vamos a pasar el logotipo… metadatos de la imagen" [39:15, 40:30] |
| RF-46 | Se guarda el PDF de cada análisis en el servidor. | "el PDF sí se va a guardar" [37:21] |
| RF-47 | Las imágenes que suben los usuarios se borran al terminar el análisis. | "Que se borren las imágenes" [34:47]; "borrar los datos después de generar el PDF" [36:18] |
| RF-48 | En el perfil, "mis análisis" lista los análisis anteriores; al abrir uno se ve en pantalla igual que al hacerlo, solo para visualizar. | "yendo a mi perfil, mis análisis…"; "la pantalla sí puede retornar el display… nada más visualización" [37:36, 38:46] |

### Acceso y contenido

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RF-49 | El sitio se ve sin iniciar sesión; para analizar imágenes sí hay que entrar con usuario y contraseña, y quien no tenga cuenta la crea ahí. | "exclusivamente para el análisis de redes neuronales hay que entrar con usuario" [62:09]; "generes un usuario y un password" [62:34] |
| RF-50 | Cualquier persona se puede registrar, sin aprobación del administrador. | "que no requiera de la confirmación del administrador, solamente es mero trámite para el marketing" [65:16] |
| RF-51 | El usuario no puede ver el código de la red neuronal. | "no pueden ver nada de eso" [64:05] |
| RF-52 | El sitio ofrece una o unas pocas imágenes de prueba para que cualquiera pruebe sin subir las suyas, y descargue su PDF. Es una función de la etapa beta; en producción se deja una sola. | "que el usuario pruebe esa imagen… y ya descargue su propio PDF" [66:16]; "una funcionalidad temporal… ya después… nada más la dejemos con una sola" [66:42] |
| RF-53 | El pie de página lleva el aviso de privacidad 2026 y la licencia Creative Commons Attribution Non Commercial, y se parece al menú: Nosotros, Aliados, Contacto, etc. El texto lo da el cliente cuando el esqueleto esté listo. | "Consulte nuestro aviso de privacidad 2026… Creative Commons Attribution, Non Commercial… Eso es muy importante para nosotros" [69:49]; "ya nada más es meterle letra" [70:21] |

### No funcionales y restricciones nuevas

| ID | Requisito | Lo que se dijo |
|---|---|---|
| RNF-06 | Que el análisis tarde unos 2 o 3 minutos es aceptable e incluso deseado, por percepción comercial. | "sí queremos que se tarde un poquito, a lo mejor unos dos, tres minutos… es un tema comercial" [33:36] |
| RNF-07 | Las imágenes de entrada deben venir con la mayor calidad posible (formato del microscopio sin compresión, por ejemplo TIFF), no por WhatsApp. | "mantener la mayor calidad posible"; "evitar que sea en WhatsApp" [14:01, 29:45] |
| RNF-08 | El hosting es un solo VPS (Hostinger), contratado por 2 años, el plan más barato, de unos 2,000 a 2,500 pesos. El cliente deposita el dinero, avisando con 1 o 2 días de anticipación. No hay factura. Con un solo sitio basta. | "de dos años… entre 2,000 a 2,500" [72:42]; "avíseme con un día de anticipación o dos" [71:56]; "Una, con una es suficiente" [73:28] |
| RNF-09 | Si un dato cambia después (por ejemplo los colores), se permite un ajuste pequeño. | "si después me cambian la jugada, se puede hacer una ligera modificación" [01:09, 01:34] |

### Capacitación (reunión del 12 de octubre)

- Las 10 horas se dan este mes, incluidas 2 horas para revisar primero la presentación con el cliente; después, unas 5 a 8 horas. "estas 10 horas sí o sí se tienen que dar en este mes" [74:26].
- Primero el cliente quiere ver la presentación y hacer comentarios; debe ser más formal que un PDF y compartirse al final [74:58, 76:04].
- Público: 6 o 7 personas, nivel básico a intermedio en programación (dos con mucha experiencia: un físico matemático y un bioinformático). Contenido general de la parte de programación, sin la parte biológica; lenguaje profesional, sin comentarios que sugieran que no saben [76:04 a 80:00].
- Sesión grabada: el desarrollador aceptó [81:07].
- No es un taller con práctica: es explicar y mostrar un ejemplo (registrarse, subir, ver el resultado), "presentarlo al cliente" [86:03 a 86:47].
- El desarrollador pidió llevar el guion escrito y las 2 horas previas [84:53]. El cliente aceptó.

### Cambios respecto a la primera reunión

| Antes | Ahora |
|---|---|
| RF-19: contar "anaranjadas" y "rojas". | RF-31 a RF-34: rojo = sano, amarillo = enfermo, 10 grados ordinales; el cliente dejó de hablar de "anaranjado" como categoría. |
| RF-17: "cuánto mide cada célula" (sin definir). | RF-22 a RF-25: cuatro medidas (cabeza, punta a cola doblada, distancia real, área en píxeles). |
| RF-14: la cuenta sirve solo para acceso. | RF-46 y RF-48: ahora hay historial de PDF en el perfil. |
| RF-11: parámetro ajustable "si hace falta". | RF-42: solo el botón de ejecutar. |

## Restricciones

- **Fecha:** el sitio web y los avances de la red neuronal, para finales de octubre: "como por ahí del 29 o 30 de octubre". El correo posterior del cliente lo fijó el 28 de octubre.
- **Datos:** por ahora hay una sola imagen ("Es la única que me han compartido de momento"). El modelo inicial se arma con unas 10 imágenes y solo sirve como esqueleto ("de antemano no nos va a servir como de mucho"). El entrenamiento real será con unas 50 imágenes.
- **Formato de las imágenes de entrenamiento:** vienen en BMP, sin ninguna en JPG (dato del desarrollador, 14 de octubre; no lo dijo el cliente en las reuniones). Falta saber en qué formato subirán imágenes los usuarios del sitio (ver Pendientes).
- **Las imágenes de ejemplo** son de espermatozoides teñidos "más o menos" en rojo, amarillo y naranja. El tono de las imágenes oficiales puede ser "mucho más sutil".
- **El modelo no aprende solo** una vez en línea: hay que reentrenarlo aparte.

## Fuera de alcance

- **Distinguir control contra tratamiento** (o tejido sano contra enfermo): "esto que le estoy planteando es perspectiva, o sea esto no es parte del proyecto".
- **Red neuronal con imágenes y datos AnnData:** "sería un proyecto aparte"; el cliente solo pidió saber si es viable.

## Pendientes

Lo que sigue sin respuesta o ambiguo, de ambas reuniones:

| Pendiente | Qué se dijo | Requisitos afectados |
|---|---|---|
| Imágenes originales: formato, escala, peso y cantidad | Las de entrenamiento vienen en BMP. Falta confirmar el formato que usarán las personas al subir imágenes al sitio, la escala, el peso y la cantidad. El cliente las pidió por correo; fecha límite jueves o viernes, confirma el miércoles. Si no llegan, "volvemos a platicar sobre las fechas". | RF-22 a RF-30, RNF-07 |
| Unidad de las medidas: ¿píxeles o micrómetros? | El cliente habló de píxeles para el área y de micrómetros para el radio de la cabeza y la escala. | RF-22 a RF-27, RF-30 |
| ¿Se confirma el correo y se recupera la contraseña? | "esa parte ya no es tan necesaria, pero… es un tema de ventas"; el desarrollador habló del enlace de confirmación y el cliente no se opuso. | RF-14, RF-49, RF-50 |
| ¿Hay administrador con panel para ver y dar de baja usuarios? | El desarrollador lo preguntó; el cliente solo respondió que no requiere aprobación. "le llegaría la confirmación de que alguien ingresó" no aclara a quién. | RF-50 |
| ¿Los análisis de cada usuario son privados? | "mis análisis" lo planteó el desarrollador y el cliente lo aceptó, pero no habló de si otros los ven. | RF-48 |
| Cuántas imágenes de prueba y cuáles | "con una imagen o con dos, tres imágenes de prueba". | RF-52 |
| Qué extremo de la escala de 10 es el sano | "O al revés". | RF-32 |
| Imágenes de "basura" para reconocer lo que no es espermatozoide | El desarrollador las pidió como opcionales. | RF-37 |
| ¿Dónde van los videos? | "más abajo de esto, o sea, de esta infografía… o en Contacto, o en Aliados" | RF-09 |
| ¿Contacto lleva solo el formulario o también los datos del área? | "El formulario clásico que viene, ¿no? Correo y así." | RF-05 |
| Fotos, nombres, textos, infografías, videos, logotipo y texto del pie | El grupo los va a pasar; el desarrollador necesita 1 o 2 días por texto. | RF-04 a RF-09, RF-45, RF-53 |
| Horarios y fechas de la capacitación | El cliente los pasa la siguiente semana. | Capacitación |
