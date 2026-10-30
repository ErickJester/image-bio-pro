# Guion del módulo 3, video 4 de 4: Frontend, el sitio funcionando (versión natural)

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

*3,446 palabras, unos 19.7 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

[Pantalla 1 · El sitio completo]

> Idea central: Este es el último video del módulo 3. Ya vimos lo que pasa por detrás, en el backend, el modelo y la medición. Ahora se ve todo junto en el sitio funcionando: un recorrido como lo ve una persona y cómo está hecho el frontend, la parte que se ve.

> En pantalla: Navegador, con la página de inicio del sitio y sin sesión iniciada. No hace falta mostrar nada más mientras recuerdas los tres videos anteriores.

Este es el último video del módulo 3. En el primero vimos el backend: lo que pasa en el servidor cuando alguien sube una imagen. En el segundo, cómo el servidor usa el modelo con recortes de la foto. Y en el tercero, cómo se miden los contornos, de qué depende la escala y qué retos tuvo el proyecto. Todo eso ocurre por detrás, donde nadie lo ve.

[Acción: navegador, en la página de inicio del sitio, sin sesión iniciada]

Hoy lo vemos todo junto, desde donde lo ve una persona. El sitio funcionando. Gracias al sitio, un modelo entrenado, que de otro modo sería solo un archivo, queda al alcance de quien no programa.

Hoy va en dos partes. Primero un recorrido, como lo haría alguien que entra por primera vez: el inicio, la cuenta, el análisis de una imagen, los resultados y las descargas. Después abrimos el código de esas pantallas en el editor, para ver con qué están hechas. Esa parte se llama frontend. Es lo que corre en el navegador de cada persona.

[Pantalla 2 · Lo que ve el visitante]

> Idea central: Sin cuenta, el visitante ve el inicio, Nosotros, Aliados, Infografías, Videos y Contacto. El inicio cuenta el proyecto en tres capítulos que aparecen al bajar. Para analizar imágenes hace falta una cuenta.

> En pantalla: Navegador, página de inicio. Baja despacio para que aparezcan los tres capítulos y se vea la barra de avance arriba. Abre el menú de las tres rayas y recorre: Nosotros, Aliados, Infografías (abre una tarjeta en su ventana), Videos (reproductor, anterior y siguiente) y Contacto (solo el formulario, sin enviar nada). Termina otra vez en el inicio.

Empecemos como visitante, sin cuenta. En pantalla está la página de inicio. El nombre del proyecto, una frase que lo resume y un botón para analizar una imagen.

[Acción: baja despacio por el inicio; se ven los tres capítulos y la barra de avance arriba]

Al bajar, el inicio se cuenta en tres capítulos. El primero es el problema: contar y medir células a mano es lento y cambia según quién lo haga. El segundo es el recorrido de una imagen, en tres pasos. Subes la foto, la red localiza, el código mide. El tercero se llama resultados que se pueden revisar.

Cada capítulo aparece cuando llegas a él. Y una barra delgada, arriba, marca cuánto has recorrido de la página. Si tu sistema tiene activado el movimiento reducido, nada se anima. Todo se ve desde el principio.

[Acción: abre el menú de las tres rayas]

El menú se abre con el botón de las tres rayas. Tiene siete secciones: Inicio, Nosotros, Aliados, Infografías, Videos, Inteligencia Artificial y Contacto.

[Acción: entra a cada sección, en el orden en que las nombra: Nosotros, Aliados, Infografías (abre una tarjeta), Videos (reproductor y botones) y Contacto (solo el formulario, sin enviar nada)]

Nosotros cuenta qué es el proyecto. Aliados muestra a las personas que participan. Infografías abre cada tarjeta en una ventana, con su imagen y su texto. Videos reúne los del curso, con un reproductor, botones de anterior y siguiente, y una marca de visto que se guarda solo en tu navegador. Y Contacto tiene un formulario. Sus mensajes se guardan en la base de datos.

[Acción: vuelve al inicio]

Todo esto se ve sin iniciar sesión. Lo que no se puede es analizar imágenes. Eso viene ahora.

[Pantalla 3 · Español e inglés]

> Idea central: El sitio está en español y en inglés. El selector ES o EN, arriba a la derecha, usa el traductor de Google. Los nombres propios y los nombres de archivo se marcan para que no se traduzcan.

> En pantalla: Haz clic en EN, arriba a la derecha, y deja que la página se recargue en inglés; baja un poco para que se note. Señala el nombre del proyecto, BIOIMAGE-REPRO UAM, en el encabezado: no cambia. Vuelve a ES.

[Acción: señala ES y EN; haz clic en EN, deja que la página se recargue en inglés y baja un poco]

En la esquina superior derecha están las letras ES y EN. Si eliges EN, todo el sitio pasa al inglés. El menú, los textos, los botones, los avisos.

No tradujimos el sitio a mano. Usa el traductor de Google, que se agrega a la página con un script. Pero el selector es nuestro, no el de Google. Cuando eliges un idioma, guarda una cookie con el par de idiomas y recarga la página. El traductor la lee al cargar. Así, el español sigue siendo el idioma original de todo el contenido, y el inglés es una traducción automática.

[Acción: con el inglés activo, señala BIOIMAGE-REPRO UAM en el encabezado: no cambia]

Esa traducción tiene un riesgo. Hay textos que no deben traducirse. El nombre del proyecto, BioImage-Repro UAM. O el nombre de una imagen que subió alguien. En esos elementos el código lleva una clase que se llama notranslate. Le dice al traductor que los deje como están. Más adelante la volvemos a ver.

[Acción: vuelve a ES]

Y hay que decirlo claro. Una traducción automática no es una traducción revisada. Para un sitio de investigación es una solución práctica, y cumple con tener dos idiomas. Pero los textos importantes convendría revisarlos.

[Pantalla 4 · Crear la cuenta y entrar]

> Idea central: Analizar imágenes requiere cuenta, gratis y con solo un correo. La pantalla Mi cuenta tiene dos columnas: iniciar sesión y crear cuenta, con contraseña de al menos 8 caracteres. Quien olvida su contraseña recibe un enlace por correo que dura una hora.

> En pantalla: Pulsa Inteligencia Artificial: el sitio lleva a Mi cuenta. Muestra las dos columnas sin llenar nada. Pulsa ¿Olvidaste tu contraseña? y enseña esa pantalla; regresa. Crea la cuenta de prueba (nombre, correo de prueba y una contraseña de prueba de ocho caracteres o más) y deja que entre. Arriba a la derecha señala tu nombre y el botón de salir.

[Acción: pulsa Inteligencia Artificial en el menú; el sitio lleva a Mi cuenta]

Al pulsar el botón de analizar, el sitio pide una cuenta. Es gratis. Basta un correo. La pantalla se llama Mi cuenta y tiene dos columnas.

[Acción: señala la columna izquierda y luego la derecha, sin llenar nada]

A la izquierda, iniciar sesión: correo, contraseña y una casilla para que el sitio recuerde el equipo. A la derecha, crear cuenta: nombre, correo y una contraseña de al menos ocho caracteres. Si falta algo, o el correo ya existe, aparece un aviso arriba, en un recuadro de color. Y al crear la cuenta, entras de una vez.

[Acción: pulsa ¿Olvidaste tu contraseña? y muestra esa pantalla; regresa a Mi cuenta]

Debajo del botón de entrar hay un enlace: olvidaste tu contraseña. Lleva a una pantalla donde escribes tu correo. El sitio te manda un enlace para elegir una contraseña nueva, y ese enlace dura una hora. La respuesta es la misma exista o no esa cuenta, para no revelar quién está registrado. Para mandar el correo, el servidor necesita tener configurado el suyo. Si no lo tiene, el sitio lo avisa.

[Acción: crea la cuenta de prueba, con una contraseña de prueba, y deja que entre; señala tu nombre y el botón de salir]

Ya dentro, arriba a la derecha aparece tu nombre, que lleva a tu perfil, y el botón de salir. Ahí están tus análisis. Los vemos al final del recorrido.

[Pantalla 5 · Analizar una imagen]

> Idea central: La pantalla de análisis recibe hasta 10 imágenes en BMP, PNG o TIFF; JPG se acepta con aviso. Hay un botón para probar con una imagen de ejemplo. Mientras se analiza, una cubierta con barra de progreso avisa que puede tardar, y pasado un minuto dice que el análisis sigue en curso.

> En pantalla: Pantalla Analizar imagen. Señala el cuadro para elegir imágenes y los dos botones: Analizar y Probar con la imagen de ejemplo. Para el aviso de formato, elige un archivo que no sea imagen (un `.txt`) y pulsa Analizar; lee el aviso. Para la cubierta de espera: el ejemplo termina en menos de un segundo, así que abre la consola (F12) y pega `document.getElementById('cubierta-analisis').classList.add('visible'); document.getElementById('aviso-espera').hidden = false`; enseña la cubierta con su barra y el aviso del minuto, y recarga la página antes de seguir. Pulsa Probar con la imagen de ejemplo.

[Acción: pantalla Analizar imagen]

Con la sesión iniciada, la sección Inteligencia Artificial muestra la pantalla de análisis. En el centro hay un cuadro para elegir imágenes, hasta diez a la vez. Los formatos son BMP, PNG o TIFF. El JPG también se acepta, pero el sitio avisa que pierde calidad. La compresión puede alterar los bordes.

[Acción: señala el botón Analizar y el de Probar con la imagen de ejemplo]

Debajo hay dos botones. Uno para analizar. Otro para probar con la imagen de ejemplo, una imagen dibujada por computadora. Sirve para ver todo el recorrido sin subir nada propio.

[Acción: elige un archivo .txt y pulsa Analizar; muestra el aviso]

Si eliges un archivo de otro formato, o más de diez imágenes, el sitio no analiza nada. Explica el motivo en un aviso.

[Acción: abre la consola (F12) y pega: document.getElementById('cubierta-analisis').classList.add('visible'); document.getElementById('aviso-espera').hidden = false. Se ve la cubierta con su barra y el aviso del minuto. Di que es una forma de enseñarla, no algo que haga el visitante. Recarga la página]

Al pulsar analizar, aparece una cubierta con una barra de progreso en movimiento. El texto avisa que es normal que tarde, desde unos segundos hasta varios minutos, y que no cierres la página. La razón es que el modelo corre en el procesador del servidor, no en una tarjeta gráfica, y una foto grande se corta en muchas teselas. Si pasa un minuto, la cubierta agrega otro aviso: tu análisis sigue en curso. Sin ese aviso, alguien podría pensar que la página se quedó trabada.

[Acción: pulsa Probar con la imagen de ejemplo]

Y algo importante. Las imágenes que subes no se conservan. El servidor las borra en cuanto termina de analizarlas. Guarda los resultados, el PDF y una copia reducida de la imagen marcada.

[Pantalla 6 · Los resultados]

> Idea central: La pantalla de resultados muestra, por imagen, sus datos, el conteo, el área media con su desviación estándar, el largo, la distribución de tamaños y una tabla con cada espermatozoide. Con la imagen de ejemplo cuenta 41, con un área media de 0.08 micras cuadradas (301.8 píxeles cuadrados).

> En pantalla: Pantalla Resultados del análisis, con la imagen de ejemplo. Recorre de arriba abajo, señalando con el cursor lo que nombras: nombre y fecha, aviso azul de la escala, datos del archivo, aviso verde, los tres números (41, 0.08 y 0.02), los mismos datos en píxeles, el histograma y la tabla.

[Acción: pantalla Resultados del análisis; señala cada parte al nombrarla]

Cuando termina, el sitio muestra los resultados. Usemos la imagen de ejemplo.

[Acción: señala el nombre, la fecha y el aviso azul de la escala]

Arriba están tu nombre y la fecha. Y un aviso azul con la escala. Para estandarizar el tamaño, se usa la misma en todas las imágenes: 60 píxeles por micra. Esa escala es provisional. Su origen lo vimos en el video anterior.

[Acción: señala los datos del archivo y el aviso verde]

Cada imagen tiene su bloque. Primero, los datos del archivo. El formato, que es PNG. El tamaño, 1200 por 900 píxeles. El modo de color y el peso, unos 134 kilobytes. Después, un aviso verde que dice que la imagen se analizó con éxito.

[Acción: señala el 41, el 0.08 y el 0.02]

A la derecha de la imagen están los tres números principales. El primero es el conteo: 41 espermatozoides. El segundo es el área media, y el tercero su desviación estándar. Los dos van en micras cuadradas: 0.08 y 0.02.

[Acción: señala los datos en píxeles]

Debajo, en letra más chica, vienen los mismos datos en píxeles. El área media es de 301.8 píxeles cuadrados, con una desviación estándar de 55.9. Y el largo medio es de 28.6 píxeles, que en micras son 0.48.

[Acción: baja hasta el histograma y después hasta la tabla]

Más abajo, la distribución de tamaños. Es una gráfica de barras: cuántos espermatozoides caen en cada intervalo de área. Y al final, una tabla con una fila por espermatozoide. Su número, su área y su largo, en píxeles y en micras.

Todos estos números salen del código, no de la red. Eso lo vimos en el video de medición.

[Pantalla 7 · Revisar a mano]

> Idea central: La imagen marcada permite revisar cada contorno. Con un clic se abre un visor con zoom, con rueda, arrastre y botones. Al pasar el cursor sobre un espermatozoide sale su detalle: número, área y largo.

> En pantalla: Señala la regla de 300 píxeles abajo a la izquierda de la imagen marcada. Pasa el cursor sobre dos o tres espermatozoides para que se vea el recuadro con número, área y largo. Haz clic en la imagen para abrir el visor: acerca con la rueda hacia un espermatozoide, arrastra, doble clic, y los botones de acercar, alejar, imagen entera y tamaño real. Pasa el cursor por un espermatozoide dentro del visor. Cierra el visor.

[Acción: sube a la imagen marcada; señala un contorno con su número y la regla de 300 píxeles]

A la izquierda de los números está la imagen marcada. Cada espermatozoide trae su contorno en blanco con un borde oscuro, y un número. Abajo a la izquierda hay una regla de 300 píxeles. Con la escala del sitio, equivale a 5 micras.

Esta imagen sirve para revisar. El sitio no dice que su resultado sea perfecto. Dice que se puede verificar.

[Acción: haz clic en la imagen para abrir el visor; rueda, arrastre, doble clic y botones, en el orden en que los nombra]

Por eso, al pulsar la imagen se abre un visor a pantalla completa. Con la rueda del ratón acercas y alejas. Arrastrando, te mueves. Con doble clic te acercas, o vuelves a la vista completa. Hay también botones para acercar, alejar, ver la imagen entera y ver el tamaño real, un píxel de la imagen por cada píxel de pantalla. En una pantalla táctil, dos dedos acercan y alejan.

[Acción: pasa el cursor sobre un espermatozoide dentro del visor y deja visible el recuadro; cierra el visor y repítelo en la página]

Y hay un detalle que se agradece. Si pasas el cursor sobre un espermatozoide, en la página o dentro del visor, aparece un recuadro con su número, su área y su largo, en píxeles y en micras. Si un contorno te parece dudoso, ves sus medidas al momento, sin buscar su fila en la tabla.

Esa revisión es lo que permite aplicar lo que dijimos en el módulo 2. El modelo es preliminar, y sus resultados se revisan con la imagen enfrente.

[Pantalla 8 · Varias imágenes, descargas e historial]

> Idea central: Con varias imágenes, el sitio agrega el promedio de la distribución. Los resultados se descargan en CSV y PDF, y se pueden imprimir. En su perfil, cada persona ve solo sus análisis anteriores.

> En pantalla: Antes de grabar, sube tres copias de `app/static/muestras/prueba.png` con otros nombres para tener un análisis con varias imágenes (con una sola no sale la gráfica del promedio); ábrelo desde Mis análisis y baja hasta la gráfica del promedio. En el final de la página señala los cuatro botones, descarga el CSV y ábrelo un momento en una hoja de cálculo, y descarga el PDF y enséñalo. Pulsa Imprimir y cancela. Luego pulsa tu nombre, arriba a la derecha, y muestra Mis análisis. Para la última frase, cambia en la dirección el número del análisis por el de otra cuenta de prueba, o por uno que no exista, y muestra la respuesta de que no existe.

[Acción: pasa a un análisis de tres imágenes hecho antes de grabar; baja hasta la gráfica del promedio]

Si subes varias imágenes, cada una tiene su bloque. Y al final el sitio agrega el promedio entre ellas: una gráfica con el número promedio de espermatozoides por intervalo de tamaño. Para poder compararlas, todas usan los mismos intervalos, tomados del mínimo y el máximo de todo el conjunto.

[Acción: baja al final de la página y señala los cuatro botones]

Al final de la página hay cuatro botones. Imprimir, descargar el PDF, descargar el CSV y analizar otras imágenes.

[Acción: pulsa Descargar CSV y ábrelo en una hoja de cálculo]

El CSV es una tabla con una fila por espermatozoide, para abrirla en una hoja de cálculo.

[Acción: pulsa Descargar PDF y ábrelo]

El PDF es un reporte con las imágenes marcadas, los números y las gráficas.

[Acción: pulsa Imprimir, muestra la vista limpia y cancela]

Y al imprimir, la página se limpia sola. Quita el encabezado, el pie y los botones, y deja lo que importa.

[Acción: pulsa tu nombre, arriba a la derecha; muestra Mis análisis y sus enlaces al PDF y al CSV]

Por último, el perfil. Si pulsas tu nombre arriba a la derecha, aparece Mis análisis. Una tabla con la fecha y hora, los nombres de las imágenes y los enlaces al PDF y al CSV de cada análisis. Cada persona ve solo los suyos.

[Acción: en la barra de direcciones cambia el número del análisis por el de otra cuenta de prueba, o por uno que no exista, y muestra la respuesta]

Si alguien intenta abrir el análisis de otra persona escribiendo su número en la dirección, el sitio responde que no existe.

[Acción: cambia al editor]

Hasta aquí, el recorrido. Ahora veamos cómo está hecho.

[Pantalla 9 · Cómo está hecho el frontend]

> Idea central: El frontend son plantillas HTML con Jinja2 que Flask llena con datos, Bootstrap para el diseño, una hoja de estilos propia, dos archivos de JavaScript y Chart.js para la gráfica. No hay framework de frontend. Son 15 plantillas.

> En pantalla: Cambia al editor, con el explorador de archivos abierto en `app/`. Despliega `templates/` (la base y las carpetas `sitio`, `cuentas` y `analisis`) y `static/` (`estilos.css`, `sitio.js`, `videos.js`). En `base.html` señala la línea de Bootstrap 5.3.3 (línea 10) y, en `analisis/resultados.html`, la de Chart.js 4.4.1 (línea 145): las dos vienen de internet.

[Acción: editor, con el explorador de archivos abierto en app]

El frontend de este sitio es sencillo, a propósito. No hay un framework como React o Vue. Las páginas las arma el servidor. Flask toma una plantilla, la llena con datos y manda al navegador el HTML terminado.

Las piezas son cinco.

[Acción: despliega templates y static, y señala cada archivo al nombrarlo]

Las plantillas, en HTML con Jinja2, que es el lenguaje de plantillas de Flask. Bootstrap, versión 5.3.3, que da el diseño base: la rejilla, los botones, los avisos y las ventanas. Una hoja de estilos propia, estilos.css, de unas 1,200 líneas, con el aspecto del proyecto. Dos archivos de JavaScript: sitio.js, con unas 270 líneas, y videos.js, con unas 90. Y Chart.js, versión 4.4.1, que dibuja las gráficas.

[Acción: base.html, línea 10 (Bootstrap), y resultados.html, línea 145 (Chart.js)]

Bootstrap y Chart.js se cargan desde internet, de una red de distribución de archivos. No se guardan en el proyecto.

[Acción: en templates: la base, sitio (8), cuentas (4) y analisis (2)]

Las plantillas son 15, en tres carpetas. Una plantilla base, y debajo ocho en la carpeta del sitio, cuatro en cuentas y dos en análisis. Con eso está todo.

¿Por qué sin framework? Porque no hace falta. Casi todo el contenido se arma en el servidor, el JavaScript solo se usa para unos comportamientos puntuales, y un sitio así se entiende abriendo los archivos. Además, Flask corre en el mismo proceso de Python que el modelo, así que no hay una segunda aplicación que mantener. Eso lo vimos en los videos anteriores.

[Pantalla 10 · La plantilla base]

> Idea central: base.html define el esqueleto de todas las páginas con bloques que las demás llenan. El menú sale de una lista de rutas, los avisos salen de flash, y cada formulario lleva su token CSRF. Las demás plantillas la extienden.

> En pantalla: Abre `app/templates/base.html`. En este orden: los bloques `titulo` (línea 6), `contenido` (80) y `scripts` (115); la lista de páginas con su ciclo y `url_for` (líneas 60 a 64); los avisos con `get_flashed_messages` (líneas 71 a 76); y la parte de la sesión con `current_user` (47) y el campo oculto `csrf_token` (50). Abre un momento `analisis/ia.html` para ver su primera línea, `extends`.

[Acción: abre base.html]

Veamos el código. En pantalla está el archivo base.html, y lo primero que hay que notar son los bloques.

[Acción: señala los bloques titulo (línea 6), contenido (80) y scripts (115)]

Una plantilla base define el esqueleto de la página: encabezado, menú, pie. Y en medio, unos huecos con nombre. Un bloque para el título, uno para el contenido y uno para los scripts.

[Acción: abre un momento analisis/ia.html, señala su primera línea, extends, y vuelve a base.html]

Las demás plantillas empiezan con una línea, extends base.html, y llenan solo esos huecos.

[Acción: líneas 60 a 64: el ciclo y url_for]

El menú no está escrito a mano siete veces. Hay una lista de pares, la ruta y el texto, y un ciclo la recorre. Para cada una, la función url_for calcula la dirección a partir del nombre de la ruta. Así, si una dirección cambia en Python, el menú no se rompe. Y una comparación con la ruta actual marca como activa la página en que estás.

[Acción: líneas 71 a 76: get_flashed_messages]

Los avisos de colores salen de una función de Flask que se llama flash. El servidor deja un mensaje y su categoría, por ejemplo éxito o peligro. La plantilla base los dibuja como recuadros de Bootstrap. Por eso funcionan igual en todas las páginas.

[Acción: línea 47 (current_user) y línea 50 (csrf_token)]

Y la sesión. La plantilla pregunta si la persona está autenticada. Si lo está, muestra su nombre y el botón de salir. Si no, el enlace para iniciar sesión. Ese botón de salir es un formulario con un campo oculto, el token CSRF. El servidor lo revisa para saber que la petición salió de su propio sitio.

[Pantalla 11 · Una plantilla con datos]

> Idea central: resultados.html recibe los resultados como datos y los recorre con ciclos y condiciones de Jinja2. Los datos se escapan automáticamente, y las direcciones se calculan con url_for. Una misma plantilla sirve para una imagen o para diez.

> En pantalla: Abre `app/templates/analisis/resultados.html`: el ciclo por imagen (línea 25), la condición de si hubo espermatozoides (40), el ciclo de las filas de la tabla (94) y un valor entre dobles llaves, por ejemplo `{{ img.nombre }}` (27). Señala `url_for` en el botón de descargar PDF (114).

[Acción: abre analisis/resultados.html]

La plantilla de resultados tiene 178 líneas. Es el mejor ejemplo de cómo se mezclan datos y HTML. El servidor le pasa dos cosas: el análisis y sus resultados, que son un diccionario con una lista de imágenes.

[Acción: línea 25 (ciclo por imagen), línea 40 (la condición) y línea 94 (las filas de la tabla)]

La plantilla recorre esa lista con un ciclo, una vez por imagen. Dentro, una condición pregunta si hubo espermatozoides. Solo en ese caso dibuja la imagen, los números y la tabla. Y otro ciclo, más adentro, escribe una fila de la tabla por cada espermatozoide. Por eso la misma plantilla sirve para una imagen o para diez. No sabe cuántas hay. Repite lo que le llega.

[Acción: línea 27: {{ img.nombre }}]

Los valores entran entre dobles llaves. Y un detalle importante: Jinja los escapa automáticamente. Si un nombre de archivo trae un signo menor o unas comillas, se muestran como texto. No se interpretan como código. Es una protección que viene con Flask y conviene no desactivar.

[Acción: línea 114: url_for en el botón del PDF]

Las direcciones de las imágenes y de las descargas también se calculan con url_for, a partir del número del análisis. Y las notas entre llaves y signos de número son comentarios. El navegador nunca los recibe.

Así se ve el patrón. El servidor decide qué datos hay. La plantilla decide cómo se dibujan. Las dos tareas no se mezclan.

[Pantalla 12 · La imagen con una zona por espermatozoide]

> Idea central: Sobre la imagen marcada hay un dibujo vectorial con un polígono invisible por espermatozoide, que lleva sus medidas en atributos. Un solo código en sitio.js muestra el detalle al pasar el cursor, y no hace falta pedirle nada al servidor.

> En pantalla: En `resultados.html`, líneas 48 a 58: el `<svg>`, el ciclo con `sort(attribute='area_px', reverse=true)` y el `<polygon>` con sus atributos `data-*`. Luego, en el navegador, abre las herramientas de desarrollo (F12), pestaña Elementos, y despliega el `<svg>` de la imagen marcada para ver los polígonos reales. Después abre `static/sitio.js`, en `iniciarDetalleEsperma` (línea 230).

[Acción: navegador: pasa el cursor sobre un espermatozoide]

Ahora, el recuadro que aparece al pasar el cursor. ¿Cómo sabe el navegador sobre qué espermatozoide estás?

[Acción: editor, resultados.html, líneas 48 a 58: el svg, el ciclo con sort y el polygon]

La plantilla pone, encima de la imagen, un dibujo vectorial, un SVG, del mismo tamaño. Dentro hay un polígono por cada espermatozoide, con los puntos de su contorno. Son invisibles, pero reciben el cursor.

[Acción: navegador, F12, pestaña Elementos: despliega el svg de la imagen marcada y muestra un polígono con sus atributos]

Cada polígono lleva además, como atributos, sus datos: el número, el área y el largo, en píxeles y en micras.

Dos detalles. Los contornos que guarda el sitio están simplificados, con muy pocos puntos por espermatozoide, para que la página no pese de más. Y se ordenan de los más grandes a los más chicos, así un espermatozoide pequeño que quede dentro de uno grande sigue siendo alcanzable.

[Acción: editor, sitio.js, iniciarDetalleEsperma, línea 230]

Del lado del navegador hay una sola función en sitio.js. Escucha cuando el cursor entra a un elemento, busca si es una de esas zonas, lee sus atributos y llena el recuadro con el texto. Lo coloca cerca del cursor. Si no cabe a la derecha o abajo, lo pone del otro lado.

Lo más importante: al pasar el cursor, no se le pide nada al servidor. Todos los datos ya venían con la página. Por eso responde al instante, aunque la conexión sea lenta.

Es un ejemplo de una idea general. Cuando algo se puede resolver con datos que ya están en la página, es mejor no ir a buscarlos.

[Pantalla 13 · El visor con zoom]

> Idea central: El visor es una ventana a pantalla completa de Bootstrap con una imagen que se acerca y se mueve cambiando su transformación. El código lleva la cuenta de la escala y la posición, y atiende la rueda, el arrastre y el gesto de dos dedos con eventos del puntero.

> En pantalla: En `static/sitio.js`, `iniciarVisorZoom` (línea 121): las variables de escala y posición, `aplicar` (141) con la transformación `translate` y `scale` (143) y `zoomEn` (154). Vuelve al navegador y abre el visor para que se vea lo que hace ese código.

[Acción: sitio.js, iniciarVisorZoom, línea 121]

El visor es otro ejemplo, y es la parte más larga de sitio.js. Es una ventana de Bootstrap a pantalla completa, con una imagen dentro.

[Acción: líneas 141 a 143: aplicar y la transformación translate y scale]

Para acercar y mover no se cambian los píxeles de la imagen. Se le aplica una transformación de CSS, que traslada y escala. El código guarda tres números: la escala, que va de uno hasta doce, y la posición de la esquina de la imagen. Cada vez que cambian, aplica la transformación.

[Acción: línea 154: zoomEn]

La parte delicada es acercar. Con la rueda, no se debe acercar hacia el centro. Se debe acercar hacia el punto donde está el cursor. Para eso, la función de zoom recalcula la posición, de modo que el punto bajo el cursor se quede fijo mientras todo crece alrededor. También limita el movimiento, para que no queden huecos en los bordes.

El arrastre y el gesto de dos dedos usan los eventos del puntero, que sirven igual para ratón y para pantallas táctiles. Con un puntero, se mueve la imagen. Con dos, el código mide la distancia entre ellos y acerca o aleja según cambie.

[Acción: navegador: abre el visor y acerca con la rueda]

Y la ventana se prepara para la imagen ampliada. El sitio guarda dos copias de la imagen marcada. Una reducida, de hasta 1,400 píxeles de lado, para la página y el PDF. Y otra más grande, de hasta 2,800, para el visor. Así el zoom muestra más detalle sin hacer pesada la página.

Cuando el visor se abre, se copia dentro de él la capa de zonas. Por eso el recuadro de detalle también funciona ahí.

[Pantalla 14 · La gráfica]

> Idea central: Las gráficas las dibuja Chart.js con datos que la plantilla escribe dentro del JavaScript con el filtro tojson. El histograma es de barras con borde marcado y está en píxeles. La misma información está en la tabla.

> En pantalla: En `resultados.html`: el `<canvas>` (línea 82), la función `graficaBarras` (152) y su llamada con `| tojson` (171). Luego, en el navegador, abre el código fuente de la página (Ctrl+U), busca `graficaBarras(` y muestra los números ya escritos dentro del JavaScript. Termina con la gráfica y la tabla Detalle por espermatozoide en pantalla.

La distribución de tamaños es una gráfica de barras. La dibuja Chart.js. Lo interesante es cómo le llegan los datos.

[Acción: editor, resultados.html: canvas (línea 82), función graficaBarras (152) y su llamada con tojson (171)]

En la plantilla hay un elemento de lienzo, un canvas, por cada gráfica, con su identificador. Más abajo, un bloque de script define una función que recibe el identificador, los bordes de los intervalos y las frecuencias. Y al llamarla, la plantilla escribe los números dentro del JavaScript con el filtro tojson de Jinja2.

[Acción: navegador, Ctrl+U: busca graficaBarras( y muestra los números ya escritos dentro del JavaScript]

Antes de llegar al navegador, el código ya dice: gráfica de barras, estos bordes, estas frecuencias, los de esta imagen. Una vez más, el servidor decide qué datos hay, y el navegador solo los dibuja.

[Acción: vuelve a la página y señala las barras y el eje horizontal]

Dos decisiones de diseño. Las barras tienen un relleno claro y un borde marcado, para que se distingan sin depender solo del color. Y el eje horizontal está en píxeles, aunque el resto del sitio dé las medidas en micras, porque los intervalos se calculan sobre el área en píxeles.

[Acción: señala la tabla Detalle por espermatozoide]

Y una de accesibilidad. Cada gráfica lleva una descripción para lectores de pantalla, que remite a la tabla de detalle. Los mismos datos están de las dos formas. Quien no pueda ver la gráfica, tiene la tabla.

[Pantalla 15 · Detalles que importan]

> Idea central: Varios detalles hacen que el sitio sea usable por más personas: enlace para saltar al contenido, textos alternativos, avisos que leen los lectores de pantalla, una versión para imprimir, el respeto al movimiento reducido y un diseño que se adapta al celular.

> En pantalla: Muéstralo funcionando. Recarga la página y pulsa Tab una vez para que aparezca el enlace de saltar al contenido. Pulsa Ctrl+P para la vista de impresión, sin encabezado ni botones. Con F12 y el modo dispositivo, ancho de celular (390 px), enseña el diseño adaptable. En `static/estilos.css` señala las variables del inicio (`:root`, línea 4), la regla de impresión (943) y la de movimiento reducido (962). Para `notranslate`, `base.html` línea 33 y `resultados.html` línea 27.

Para cerrar la parte técnica, unos detalles que no se ven a primera vista, pero cuentan.

[Acción: recarga la página y pulsa Tab una vez: aparece el enlace de saltar al contenido]

Primero, el teclado. Lo primero de la página es un enlace escondido, que aparece al recibir el foco, para saltar al contenido. Quien navega con teclado no tiene que pasar por todo el menú en cada página.

Segundo, los lectores de pantalla. Las imágenes llevan texto alternativo, los botones de zoom tienen nombre, y la cubierta de espera tiene un rol de estado que anuncia su mensaje sin interrumpir. Si pasa un minuto, el aviso adicional también se anuncia.

[Acción: Ctrl+P: muestra la vista de impresión y cancela; en estilos.css, regla de impresión (línea 943)]

Tercero, imprimir. Una regla de estilo para impresión oculta el encabezado, el pie, los botones, el recuadro de detalle y las zonas del cursor. Lo que sale en papel es el reporte.

[Acción: estilos.css, línea 962: prefers-reduced-motion]

Cuarto, el movimiento. Quien tiene activada la opción de reducir animaciones no ve ni las apariciones del inicio ni la barra de progreso en movimiento.

[Acción: F12, modo dispositivo, ancho de 390 px; en estilos.css, las variables del inicio (:root, línea 4)]

Quinto, el celular. Unas reglas de estilo cambian el tamaño de las letras, los márgenes y el logo según el ancho de la pantalla. Y todos los colores y espacios salen de unas variables al inicio de la hoja de estilos, no de valores sueltos en cada componente. Cambiar el azul del sitio es cambiar una línea.

[Acción: base.html, línea 33, y resultados.html, línea 27: notranslate]

Y una más, la que vimos con el idioma. La clase notranslate marca el nombre del proyecto y los nombres de archivo para que el traductor no los toque.

Son detalles pequeños. Pero la diferencia entre una página que funciona y una que se puede usar suele estar en ellos.

[Pantalla 16 · Lo que vimos y lo que sigue]

> Idea central: Vimos el sitio funcionando, de la cuenta a los resultados, y su frontend: plantillas con Jinja2, Bootstrap, JavaScript puntual y Chart.js. Con esto termina el módulo 3. En el módulo 4, el cuaderno de Colab con el que se entrena el modelo y el despliegue del sitio en la nube.

> En pantalla: Vuelve al navegador, en el inicio del sitio, sin nada más abierto. Es la última pantalla mientras das el resumen y te despides.

[Acción: vuelve al navegador, en el inicio del sitio]

Un resumen.

Vimos el sitio como lo ve una persona. El inicio, el menú, el cambio de idioma, la cuenta con su recuperación de contraseña, el análisis de una imagen con su espera, los resultados con el conteo y las medidas, la revisión con el visor y el detalle por espermatozoide, las descargas y el historial.

Y vimos con qué está hecho. Un frontend sin framework. Plantillas de Jinja2 que Flask llena con datos. Bootstrap para el diseño. Una hoja de estilos con variables. Y un JavaScript pequeño para las partes que cambian en el navegador: el idioma, el visor, el recuadro de detalle y la espera. Una plantilla base con bloques, que las demás extienden. Los datos de cada gráfica escritos con tojson. Y unos detalles de accesibilidad, de impresión y de celular.

Con esto termina el módulo 3. Vimos el sitio por detrás, con el backend, el modelo y la medición. Y ahora lo vimos por delante, con su frontend.

Falta lo que lo hace posible. Cómo se entrenó la red, y cómo se puso el sitio en internet para que cualquiera lo pueda visitar. Eso es el módulo 4: el cuaderno de Colab con el que se entrena el modelo, y el despliegue del sitio en la nube.

Gracias por acompañarme.
