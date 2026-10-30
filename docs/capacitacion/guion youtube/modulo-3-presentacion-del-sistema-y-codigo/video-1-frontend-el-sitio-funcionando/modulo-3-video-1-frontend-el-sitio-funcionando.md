# Guion del módulo 3, video 1 de 4: Frontend, el sitio funcionando

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Continúa del video anterior. Empieza con la frase que lo une con el video anterior.

*3,499 palabras, unos 20.0 min de habla*

[Diapositiva 1 · De la teoría al sitio]

> Idea central: El módulo 2 terminó con un modelo entrenado y unos datos. Un archivo de modelo no hace nada por sí solo: el sitio lo pone al alcance de quien no programa. Este video tiene dos partes: un recorrido por el sitio y cómo está hecho el frontend, la parte que se ve.

En el módulo 2 vimos cómo ve una red convolucional, cómo trabaja Mask R-CNN, cómo la transferencia ahorra fotos y cómo se anotan y se miden los datos. Todo eso termina en un archivo, el modelo entrenado, con casi 44 millones de pesos guardados. Y un archivo de modelo, por sí solo, no hace nada. Hace falta una página donde alguien suba una foto y reciba números.

De eso trata el módulo 3. Son cuatro videos. En este vemos el sitio funcionando y cómo está hecha la parte que se ve en el navegador, que se llama frontend. En el segundo, el backend: qué pasa del otro lado cuando se sube una imagen. En el tercero, cómo el servidor usa el modelo con recortes de la foto. Y en el cuarto, cómo se miden los contornos, de qué depende la escala y qué retos tuvo el proyecto.

Este video va en dos partes. En la primera hacemos un recorrido, como lo haría una persona que entra por primera vez: la página de inicio, la cuenta, el análisis de una imagen, los resultados y las descargas. En la segunda abrimos el código de esas pantallas, con fragmentos cortos, para ver con qué están hechas.

[Diapositiva 2 · Lo que ve el visitante]

> Idea central: Sin cuenta, el visitante ve el inicio, Nosotros, Aliados, Infografías, Videos y Contacto. El inicio cuenta el proyecto en tres capítulos que aparecen al bajar. Para analizar imágenes hace falta una cuenta.

Empecemos como visitante, sin cuenta. En pantalla está la página de inicio, con el nombre del proyecto, una frase que lo resume y un botón para analizar una imagen.

Al bajar, el inicio se cuenta en tres capítulos. El primero es el problema: contar y medir células a mano es lento y cambia según quién lo haga. El segundo es el recorrido de una imagen, en tres pasos: subes la foto, la red localiza y el código mide. El tercero se llama resultados que se pueden revisar. Cada capítulo aparece al llegar a él, y una barra delgada arriba marca cuánto se ha recorrido la página. Si la persona tiene activado el movimiento reducido en su sistema, nada se anima y todo queda visible desde el principio.

El menú se abre con el botón de las tres rayas. Tiene siete secciones: Inicio, Nosotros, Aliados, Infografías, Videos, Inteligencia Artificial y Contacto. Nosotros cuenta qué es el proyecto. Aliados muestra a las personas que participan. Infografías abre cada tarjeta en una ventana, con su imagen y su texto. Videos reúne los del curso, con un reproductor, los botones de anterior y siguiente, y una marca de visto que se guarda solo en el navegador de cada persona. Y Contacto tiene un formulario cuyos mensajes se guardan en la base de datos.

Todo esto se ve sin iniciar sesión. Lo que no se puede sin cuenta es analizar imágenes, y vamos a verlo.

[Diapositiva 3 · Español e inglés]

> Idea central: El sitio está en español y en inglés. El selector ES o EN, arriba a la derecha, usa el traductor de Google. Los nombres propios y los nombres de archivo se marcan para que no se traduzcan.

En la esquina superior derecha están las letras ES y EN. Al elegir EN, todo el sitio pasa al inglés: el menú, los textos, los botones y los avisos.

No tradujimos el sitio a mano. Usa el traductor de Google, que se agrega a la página con un script. El selector es nuestro, no el de Google: al elegir un idioma, guarda una cookie con el par de idiomas y recarga la página, y el traductor la lee al cargar. Así el español sigue siendo el idioma original de todo el contenido, y el inglés es una traducción automática.

Esa traducción tiene un riesgo, y se atiende. Hay textos que no deben traducirse: el nombre del proyecto, BioImage-Repro UAM, o el nombre de una imagen que subió alguien. En esos elementos el código lleva una clase que se llama notranslate, que le dice al traductor que los deje como están. Más adelante la volvemos a ver.

También hay que decirlo con claridad: una traducción automática no es una traducción revisada. Para un sitio de investigación es una solución práctica, que cumple con tener dos idiomas, pero los textos importantes convendría revisarlos.

[Diapositiva 4 · Crear la cuenta y entrar]

> Idea central: Analizar imágenes requiere cuenta, gratis y con solo un correo. La pantalla Mi cuenta tiene dos columnas: iniciar sesión y crear cuenta, con contraseña de al menos 8 caracteres. Quien olvida su contraseña recibe un enlace por correo que dura una hora.

Al pulsar el botón de analizar, el sitio pide una cuenta. Es gratis y basta con un correo. La pantalla se llama Mi cuenta y tiene dos columnas.

A la izquierda, iniciar sesión: correo, contraseña y una casilla para que el sitio recuerde el equipo. A la derecha, crear cuenta: nombre, correo y contraseña de al menos ocho caracteres. Si algo falta o el correo ya existe, aparece un aviso arriba, en un recuadro de color. Al crear la cuenta, la persona entra de una vez.

Debajo del botón de entrar hay un enlace: olvidaste tu contraseña. Lleva a una pantalla donde se escribe el correo, y el sitio manda un enlace para elegir una contraseña nueva. El enlace dura una hora. Y la respuesta es la misma exista o no esa cuenta, para no revelar quién está registrado. Para mandar el correo, el servidor necesita tener configurado su correo; si no lo tiene, el sitio lo avisa.

Una vez dentro, arriba a la derecha aparece el nombre de la persona, que lleva a su perfil, y el botón de salir. Ahí están sus análisis, que vemos al final del recorrido.

[Diapositiva 5 · Analizar una imagen]

> Idea central: La pantalla de análisis recibe hasta 10 imágenes en BMP, PNG o TIFF; JPG se acepta con aviso. Hay un botón para probar con una imagen de ejemplo. Mientras se analiza, una cubierta con barra de progreso avisa que puede tardar, y pasado un minuto dice que el análisis sigue en curso.

Con la sesión iniciada, la sección Inteligencia Artificial muestra la pantalla de análisis. En el centro hay un cuadro para elegir imágenes, hasta diez a la vez. Los formatos son BMP, PNG o TIFF. El JPG se acepta, pero el sitio avisa que pierde calidad, porque la compresión puede alterar los bordes. Debajo hay un botón para analizar y otro para probar con la imagen de ejemplo, que es una imagen dibujada por computadora y sirve para ver el recorrido completo sin subir nada propio.

Si se elige un archivo de otro formato, o más de diez imágenes, el sitio no analiza nada y explica el motivo en un aviso.

Al pulsar analizar, aparece una cubierta con una barra de progreso en movimiento. El texto avisa que es normal que tarde, desde unos segundos hasta varios minutos, y que no hay que cerrar la página. Esto se debe a que el modelo corre en el procesador del servidor, no en una tarjeta gráfica, y una foto grande se corta en muchas teselas. Y si pasa un minuto, la cubierta agrega otro aviso: tu análisis sigue en curso. Sin ese aviso, una persona podría pensar que la página se quedó trabada.

Las imágenes subidas no se conservan. El servidor las borra en cuanto termina de analizarlas, y guarda solo los resultados, el PDF y una copia reducida de la imagen marcada.

[Diapositiva 6 · Los resultados]

> Idea central: La pantalla de resultados muestra, por imagen, sus datos, el conteo, el área media con su desviación estándar, el largo, la distribución de tamaños y una tabla con cada espermatozoide. Con la imagen de ejemplo cuenta 41, con un área media de 0.08 micras cuadradas (301.8 píxeles cuadrados).

Cuando termina, el sitio muestra los resultados. Usemos la imagen de ejemplo. Arriba están el nombre de la persona y la fecha. Y un aviso azul con la escala: para estandarizar el tamaño, se usa la misma en todas las imágenes, 60 píxeles por micra. Esa escala es provisional y su origen se explica en el cuarto video del módulo.

Cada imagen tiene su bloque. Primero, sus datos de archivo: el formato, que es PNG, el tamaño, 1200 por 900 píxeles, el modo de color y el peso, unos 134 kilobytes. Después, un aviso verde que dice que la imagen se analizó con éxito.

A la derecha de la imagen están los tres números principales. El primero es el conteo: 41 espermatozoides. El segundo es el área media y el tercero su desviación estándar, los dos en micras cuadradas: 0.08 y 0.02. Debajo, en letra más chica, vienen los mismos datos en píxeles. El área media es de 301.8 píxeles cuadrados, con una desviación estándar de 55.9. El largo medio es de 28.6 píxeles, y en micras, 0.48.

Más abajo, la distribución de tamaños es una gráfica de barras: cuántos espermatozoides caen en cada intervalo de área. Y al final, una tabla con una fila por espermatozoide: su número, su área y su largo, en píxeles y en micras.

Todos esos números salen del código y no de la red, algo que vemos en el último video del módulo.

[Diapositiva 7 · Revisar a mano]

> Idea central: La imagen marcada permite revisar cada contorno. Con un clic se abre un visor con zoom, con rueda, arrastre y botones. Al pasar el cursor sobre un espermatozoide sale su detalle: número, área y largo.

A la izquierda de los números está la imagen marcada. Cada espermatozoide trae su contorno en blanco con un borde oscuro, y un número. Abajo a la izquierda hay una regla de 300 píxeles, que equivale a 5 micras con la escala del sitio.

La imagen sirve para revisar. El sitio no pretende que su resultado sea perfecto. Pretende que se pueda verificar. Por eso, al pulsar la imagen se abre un visor a pantalla completa. Con la rueda del ratón se acerca y se aleja, arrastrando se mueve, y con doble clic se acerca o se vuelve a la vista completa. Hay también botones para acercar, alejar, ver la imagen entera y ver el tamaño real, un píxel de la imagen por cada píxel de pantalla. En una pantalla táctil, dos dedos acercan y alejan.

Y hay un detalle que se agradece. Al pasar el cursor sobre un espermatozoide, sea en la página o dentro del visor, aparece un recuadro con su número, su área y su largo, en píxeles y en micras. Así, quien ve un contorno dudoso puede mirar sus medidas sin buscar la fila en la tabla.

Esa revisión es lo que permite aplicar lo que dijimos en el módulo 2: el modelo es preliminar, y sus resultados se revisan con la imagen enfrente.

[Diapositiva 8 · Varias imágenes, descargas e historial]

> Idea central: Con varias imágenes, el sitio agrega el promedio de la distribución. Los resultados se descargan en CSV y PDF, y se pueden imprimir. En su perfil, cada persona ve solo sus análisis anteriores.

Si se suben varias imágenes, cada una tiene su bloque, y al final el sitio agrega el promedio entre ellas: una gráfica con el número promedio de espermatozoides por intervalo de tamaño. Para poder compararlas, todas usan los mismos intervalos, tomados del mínimo y el máximo de todo el conjunto.

Al final de la página hay cuatro botones: imprimir, descargar el PDF, descargar el CSV y analizar otras imágenes. El CSV es una tabla con una fila por espermatozoide, para abrirla en una hoja de cálculo. El PDF es un reporte con las imágenes marcadas, los números y las gráficas. Al imprimir, la página se limpia sola: quita el encabezado, el pie y los botones, y deja lo que importa.

Por último, el perfil. Al pulsar el nombre arriba a la derecha aparece Mis análisis: una tabla con la fecha y hora, los nombres de las imágenes y los enlaces al PDF y al CSV de cada análisis. Cada persona ve solo los suyos. Si alguien intenta abrir el análisis de otra persona escribiendo su número en la dirección, el sitio responde que no existe.

Hasta aquí, el recorrido. Ahora veamos cómo está hecho.

[Diapositiva 9 · Cómo está hecho el frontend]

> Idea central: El frontend son plantillas HTML con Jinja2 que Flask llena con datos, Bootstrap para el diseño, una hoja de estilos propia, dos archivos de JavaScript y Chart.js para la gráfica. No hay framework de frontend. Son 15 plantillas.

El frontend de este sitio es sencillo a propósito. No hay un framework de frontend como React o Vue. Las páginas las arma el servidor: Flask toma una plantilla, la llena con datos y manda el HTML terminado al navegador.

Las piezas son cinco. Las plantillas, en HTML con Jinja2, que es el lenguaje de plantillas de Flask. Bootstrap, versión 5.3.3, que da el diseño base: la rejilla, los botones, los avisos y las ventanas. Una hoja de estilos propia, estilos.css, de unas 1,200 líneas, con el aspecto del proyecto. Dos archivos de JavaScript, sitio.js, con unas 270 líneas, y videos.js, con unas 90. Y Chart.js, versión 4.4.1, que dibuja las gráficas. Bootstrap y Chart.js se cargan desde internet, de una red de distribución de archivos, y no se guardan en el proyecto.

Las plantillas son 15, en tres carpetas. Hay una plantilla base, y debajo, ocho en la carpeta del sitio, cuatro en cuentas y dos en análisis. Con eso está todo.

¿Por qué sin framework? Porque no hace falta: casi todo el contenido se arma en el servidor, el JavaScript solo se usa para unos comportamientos puntuales, y un sitio así se entiende abriendo los archivos. Y como Flask corre en el mismo proceso de Python que el modelo, no hay una segunda aplicación que mantener. Lo vemos en los videos siguientes.

[Diapositiva 10 · La plantilla base]

> Idea central: base.html define el esqueleto de todas las páginas con bloques que las demás llenan. El menú sale de una lista de rutas, los avisos salen de flash, y cada formulario lleva su token CSRF. Las demás plantillas la extienden.

Veamos el código. En pantalla está el archivo base.html, y lo primero que hay que notar son los bloques. Una plantilla base define el esqueleto de la página, con encabezado, menú, pie, y en medio unos huecos con nombre: un bloque para el título, uno para el contenido y uno para los scripts. Las demás plantillas empiezan con una línea, extends base.html, y llenan solo esos huecos.

El menú no está escrito a mano siete veces. Hay una lista de pares, la ruta y el texto, y un ciclo la recorre. Para cada una, la función url_for calcula la dirección a partir del nombre de la ruta, de modo que si una dirección cambia en Python, el menú no se rompe. Y una comparación con la ruta actual marca como activa la página en que se está.

Los avisos de colores salen de una función de Flask que se llama flash. El servidor deja un mensaje y su categoría, por ejemplo éxito o peligro, y la plantilla base los dibuja como recuadros de Bootstrap. Por eso funcionan igual en todas las páginas.

Y la sesión. La plantilla pregunta si la persona está autenticada. Si lo está, muestra su nombre y el botón de salir; si no, el enlace para iniciar sesión. Ese botón de salir es un formulario con un campo oculto, el token CSRF, que el servidor revisa para saber que la petición salió de su propio sitio.

[Diapositiva 11 · Una plantilla con datos]

> Idea central: resultados.html recibe los resultados como datos y los recorre con ciclos y condiciones de Jinja2. Los datos se escapan automáticamente, y las direcciones se calculan con url_for. Una misma plantilla sirve para una imagen o para diez.

La plantilla de resultados, de 178 líneas, es el mejor ejemplo de cómo se mezclan datos y HTML. El servidor le pasa dos cosas: el análisis y sus resultados, que son un diccionario con una lista de imágenes.

La plantilla las recorre con un ciclo, una vez por cada imagen. Dentro, una condición pregunta si hubo espermatozoides, y solo en ese caso dibuja la imagen, los números y la tabla. Otro ciclo, más adentro, escribe una fila de la tabla por cada espermatozoide. Es la razón por la que la misma plantilla sirve para una imagen o para diez: la plantilla no sabe cuántas hay, solo repite lo que le llega.

Los valores entran entre dobles llaves. Un detalle importante: Jinja los escapa automáticamente. Si un nombre de archivo trae un signo menor o unas comillas, se muestran como texto y no se interpretan como código. Es una protección que viene con Flask y que conviene no desactivar.

Las direcciones de las imágenes y de las descargas también se calculan con url_for, a partir del número del análisis. Y las notas entre llaves y signos de número son comentarios que el navegador nunca recibe.

Así se ve el patrón: el servidor decide qué datos hay, y la plantilla decide cómo se dibujan. No se mezclan las dos tareas.

[Diapositiva 12 · La imagen con una zona por espermatozoide]

> Idea central: Sobre la imagen marcada hay un dibujo vectorial con un polígono invisible por espermatozoide, que lleva sus medidas en atributos. Un solo código en sitio.js muestra el detalle al pasar el cursor, y no hace falta pedirle nada al servidor.

Ahora, el recuadro que aparece al pasar el cursor. ¿Cómo sabe el navegador sobre qué espermatozoide está?

La plantilla pone, encima de la imagen, un dibujo vectorial, un SVG, del mismo tamaño. Dentro hay un polígono por cada espermatozoide, con los puntos de su contorno. Son invisibles, pero reciben el cursor. Cada polígono lleva además, como atributos, sus datos: el número, el área y el largo, en píxeles y en micras. Los contornos que guarda el sitio están simplificados, con muy pocos puntos por espermatozoide, para que la página no pese de más. Y se ordenan de los más grandes a los más chicos, de modo que un espermatozoide pequeño que quede dentro de uno grande siga alcanzable.

Del lado del navegador hay una sola función en sitio.js. Escucha cuando el cursor entra a un elemento de la página, busca si es una de esas zonas, lee sus atributos y llena el recuadro con el texto. Lo coloca cerca del cursor, y si no cabe a la derecha o abajo, lo pone del otro lado.

Lo más importante es que, al pasar el cursor, no se le pide nada al servidor. Todos los datos ya venían con la página. Por eso responde al instante, aun con una conexión lenta.

Y sirve de ejemplo de una idea general: cuando algo se puede resolver con datos que ya están en la página, es mejor no ir a buscarlos.

[Diapositiva 13 · El visor con zoom]

> Idea central: El visor es una ventana a pantalla completa de Bootstrap con una imagen que se acerca y se mueve cambiando su transformación. El código lleva la cuenta de la escala y la posición, y atiende la rueda, el arrastre y el gesto de dos dedos con eventos del puntero.

El visor es otro ejemplo, y es la parte más larga de sitio.js. Es una ventana de Bootstrap a pantalla completa, con una imagen dentro.

Para acercar y mover no se cambian los píxeles de la imagen. Se le aplica una transformación de CSS, que traslada y escala. El código guarda tres números: la escala, que va de uno hasta doce, y la posición de la esquina de la imagen. Cada vez que cambian, aplica la transformación.

La parte delicada es acercar. Con la rueda, no se debe acercar hacia el centro, sino hacia el punto donde está el cursor. Para eso la función de zoom recalcula la posición, de modo que el punto bajo el cursor se quede fijo mientras todo crece alrededor. También limita el movimiento, para que no queden huecos en los bordes.

El arrastre y el gesto de dos dedos usan los eventos del puntero, que sirven igual para ratón y para pantallas táctiles. Con un puntero, se mueve la imagen. Con dos, el código mide la distancia entre ellos y acerca o aleja según cambie. Y la ventana se prepara para la imagen ampliada: el sitio guarda dos copias de la imagen marcada, una reducida, de hasta 1,400 píxeles de lado, para la página y el PDF, y otra más grande, de hasta 2,800, para el visor. Así el zoom muestra más detalle sin hacer pesada la página.

Cuando el visor se abre, se copia dentro de él la capa de zonas, y por eso el recuadro de detalle también funciona ahí.

[Diapositiva 14 · La gráfica]

> Idea central: Las gráficas las dibuja Chart.js con datos que la plantilla escribe dentro del JavaScript con el filtro tojson. El histograma es de barras con borde marcado y está en píxeles. La misma información está en la tabla.

La distribución de tamaños es una gráfica de barras. La dibuja Chart.js, y lo interesante es cómo le llegan los datos.

En la plantilla hay un elemento de lienzo, un canvas, por cada gráfica, con su identificador. Más abajo, un bloque de script define una función que recibe el identificador, los bordes de los intervalos y las frecuencias. Y al llamarla, la plantilla escribe los números dentro del JavaScript con el filtro tojson de Jinja2. Antes de llegar al navegador, el código ya dice, por ejemplo, grafica de barras, los bordes de los intervalos y las frecuencias de esta imagen. Una vez más, el servidor decide qué datos hay y el navegador solo los dibuja.

Dos decisiones de diseño. Las barras tienen un relleno claro y un borde marcado, para que se distingan sin depender solo del color. Y el eje horizontal está en píxeles, aunque lo demás del sitio dé las medidas en micras, porque los intervalos se calculan sobre el área en píxeles.

Y una de accesibilidad: cada gráfica lleva una descripción para lectores de pantalla, que remite a la tabla de detalle. Los mismos datos están en las dos formas, y quien no pueda ver la gráfica tiene la tabla.

[Diapositiva 15 · Detalles que importan]

> Idea central: Varios detalles hacen que el sitio sea usable por más personas: enlace para saltar al contenido, textos alternativos, avisos que leen los lectores de pantalla, una versión para imprimir, el respeto al movimiento reducido y un diseño que se adapta al celular.

Para cerrar la parte técnica, unos detalles que no se ven a primera vista, pero que cuentan.

Primero, el teclado. Lo primero de la página es un enlace, escondido hasta que recibe el foco, para saltar al contenido. Quien navega con teclado no tiene que pasar por todo el menú en cada página.

Segundo, los lectores de pantalla. Las imágenes llevan texto alternativo, los botones de zoom tienen nombre, y la cubierta de espera tiene un rol de estado que anuncia su mensaje sin interrumpir. Si pasa un minuto, el aviso adicional también se anuncia.

Tercero, imprimir. Una regla de estilo para impresión oculta el encabezado, el pie, los botones, el recuadro de detalle y las zonas del cursor. Lo que sale en papel es el reporte.

Cuarto, el movimiento. Quien tiene activada la opción de reducir animaciones no ve ni las apariciones del inicio ni la barra de progreso en movimiento.

Quinto, el celular. Unas reglas de estilo cambian el tamaño de las letras, los márgenes y el logo según el ancho de la pantalla. Y todos los colores y espacios salen de unas variables al inicio de la hoja de estilos, no de valores sueltos en cada componente. Cambiar el azul del sitio es cambiar una línea.

Son detalles pequeños. Pero la diferencia entre una página que funciona y una que se puede usar suele estar en ellos.

[Diapositiva 16 · Lo que vimos y lo que sigue]

> Idea central: Vimos el sitio funcionando, de la cuenta a los resultados, y su frontend: plantillas con Jinja2, Bootstrap, JavaScript puntual y Chart.js. En el siguiente video, el backend: qué pasa del otro lado cuando se pulsa analizar.

Un resumen. Vimos el sitio como lo ve una persona: el inicio, el menú, el cambio de idioma, la cuenta con su recuperación de contraseña, el análisis de una imagen con su espera, los resultados con el conteo y las medidas, la revisión con el visor y el detalle por espermatozoide, las descargas y el historial.

Y vimos con qué está hecho. Un frontend sin framework: plantillas de Jinja2, que Flask llena con datos; Bootstrap para el diseño; una hoja de estilos con variables; y un JavaScript pequeño para las partes que cambian en el navegador, el idioma, el visor, el recuadro de detalle y la espera. Una plantilla base con bloques, que las demás extienden. Los datos de cada gráfica escritos con tojson. Y unos detalles de accesibilidad, de impresión y de celular.

En el siguiente video cruzamos al otro lado. Cuando alguien pulsa analizar, el navegador manda las imágenes, y algo del otro lado las recibe, las revisa, las analiza, guarda los resultados y devuelve la página que acabamos de ver. Eso es el backend, y lo recorremos ruta por ruta. Gracias por acompañarme.
