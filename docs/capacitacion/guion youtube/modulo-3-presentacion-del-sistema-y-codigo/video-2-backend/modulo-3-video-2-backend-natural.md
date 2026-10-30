# Guion del módulo 3, video 2 de 4: Backend (versión natural)

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

*3,594 palabras, unos 20.5 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

[Pantalla 1 · Qué pasa al subir una imagen]

> Idea central: Al pulsar analizar, el navegador manda una orden y el servidor contesta con una redirección a la página de resultados. En medio hay un camino: Nginx, Gunicorn, Flask, el modelo, la medición, la base de datos y el PDF. Este video recorre ese camino, menos el modelo y la medición, que son los dos siguientes.

> En pantalla: Navegador con la cuenta de prueba ya iniciada y la pestaña de red de las herramientas de desarrollo (F12) abierta, con la opción de conservar el registro activa. Pulsa Probar con la imagen de ejemplo y señala las dos peticiones que salen: un POST a `/analizar/prueba` con respuesta 302 y un GET a `/resultados/N` con respuesta 200.

[Acción: navegador con la cuenta de prueba iniciada; F12, pestaña de red, conservar el registro]

En el video anterior vimos el sitio como lo ve una persona. Y la parte que se ve en el navegador, el frontend. Hoy cruzamos al otro lado. Cuando alguien pulsa analizar, pasan muchas cosas en pocos segundos. Y casi ninguna se ve.

[Acción: pulsa Probar con la imagen de ejemplo]

Hagamos una prueba, con la pestaña de red del navegador abierta. Pulso el botón de probar con la imagen de ejemplo. Y aparecen dos peticiones que nos importan.

La primera es un POST a analizar prueba. Su respuesta es un 302, que quiere decir redirigir. La segunda es un GET a resultados, con el número del análisis. Esa sí devuelve la página. O sea: el navegador manda la orden, el servidor trabaja, y le contesta: ve a esta otra dirección.

Detrás de esas dos líneas hay un camino. El navegador habla con Nginx, que recibe las visitas desde internet. Nginx se las pasa a Gunicorn, el programa que ejecuta Python y atiende varias peticiones a la vez. Gunicorn llama a la aplicación Flask. Flask comprueba que la persona haya iniciado sesión y ejecuta la función de análisis.

Esa función le da la imagen al modelo. Recibe los contornos. Mide. Guarda los resultados en la base de datos, genera el PDF y manda al navegador a la página de resultados.

Este video recorre ese camino por dentro. Primero, con qué se escribe, cómo se crea la aplicación y qué rutas tiene. Después las cuentas y sus protecciones, la base de datos, la ruta de análisis y los reportes. Y al final, cómo se ejecuta todo y cómo se prueba. El modelo y la medición tienen su propio video cada uno.

[Pantalla 2 · Python y Flask]

> Idea central: El backend está escrito en Python, con Flask como marco de trabajo y unas pocas extensiones. Flask conecta direcciones con funciones; las bibliotecas hacen el resto. Las dependencias están en requirements.txt y PyTorch va aparte.

> En pantalla: Editor con `requirements.txt` abierto, y después `requirements-modelo.txt` y `run.py`. Señala cada biblioteca al nombrarla.

[Acción: editor, requirements.txt]

El backend está escrito en Python. Es un lenguaje con fama de ser fácil de leer. Y domina la inteligencia artificial por las bibliotecas que se construyeron a su alrededor: colecciones de programas ya escritos para tareas comunes. Un proyecto como este no se escribe desde cero. Se combinan bibliotecas muy buenas, y el trabajo propio está en unirlas con cuidado.

Aquí están las del sitio, en el archivo requirements.txt. Flask, el marco para hacer sitios web. Flask-Login, que lleva las sesiones. Flask-WTF, que protege los formularios. Flask-SQLAlchemy, que conecta con la base de datos. OpenCV, NumPy y Pillow trabajan con las imágenes. Matplotlib y fpdf2 hacen las gráficas y el PDF. Gunicorn es el servidor de Python. Y pytest corre las pruebas.

[Acción: requirements-modelo.txt]

PyTorch está en otro archivo, requirements-modelo.txt. Se instala aparte porque se baja de un repositorio especial, el de la versión para procesador. Es mucho más pequeña que la de tarjeta gráfica, y el servidor no tiene tarjeta gráfica.

¿Y qué hace Flask? Una página web funciona con peticiones y respuestas. El navegador pide una dirección. El servidor decide qué hacer, hace el trabajo y devuelve una respuesta, normalmente una página. Con Flask uno indica qué dirección corresponde a qué función. Si alguien entra al inicio, se ejecuta esta. Si alguien sube una imagen, se ejecuta aquella otra.

[Acción: abre run.py]

Y como Flask está escrito en Python, puede llamar directamente a la red neuronal, que también está en Python. El sitio y el modelo viven en el mismo programa. El archivo run.py tiene dos líneas útiles. Crea la aplicación y, si lo ejecutas, la enciende para probarla en tu computadora.

[Pantalla 3 · Crear la aplicación]

> Idea central: crear_app construye la aplicación: reúne la configuración, crea las carpetas, enciende las extensiones y registra las tres secciones. Es una función y no una variable para que las pruebas puedan crear una aplicación nueva con otra configuración.

> En pantalla: Editor, `app/__init__.py`: la función `crear_app` (línea 9), la configuración (12 a 26), las carpetas (30 a 32), las extensiones (34 a 39) y los blueprints (41 a 48); después `app/extensiones.py` completo.

[Acción: abre app/__init__.py, función crear_app, línea 9]

El corazón del backend es una función. Se llama crear_app y está en app/__init__.py. Hace cuatro cosas, y se leen de arriba abajo.

[Acción: líneas 12 a 26: la configuración]

Primero, la configuración. La clave secreta, que sirve para firmar las sesiones y los enlaces, sale de una variable de entorno. En el servidor, el archivo de composición se niega a arrancar si esa variable no está definida. Luego, el tamaño máximo de un envío, 300 megabytes. El máximo de imágenes por análisis, 10. Y las rutas de las carpetas donde se guardan los PDF, las imágenes marcadas y las subidas temporales.

[Acción: líneas 30 a 32: las carpetas]

Segundo, las carpetas. Todas viven dentro de una carpeta que se llama instance, y la función las crea si no existen. Ahí también está la base de datos.

[Acción: líneas 34 a 39 y extensiones.py]

Tercero, las extensiones. La base de datos, la protección de formularios y las sesiones se crean en un archivo aparte, extensiones.py, que tiene tres líneas útiles. Aquí solo se conectan a la aplicación. Se crean fuera para que cualquier archivo las pueda importar sin enredarse.

[Acción: líneas 41 a 48 y 54 y 55]

Y cuarto, las secciones. El sitio se divide en tres blueprints, que son grupos de rutas: el sitio público, las cuentas y el análisis. Cada uno vive en su archivo. Al final, db.create_all crea las tablas si no existen. Ojo: no hay herramienta de migraciones. Si algún día cambia una tabla, hay que cuidar la base que ya existe.

¿Por qué una función y no una aplicación suelta? Porque las pruebas necesitan crear una aplicación nueva. Con otra base de datos, otras carpetas y sin protección de formularios. Con una función, eso es llamarla con otra configuración.

[Pantalla 4 · Las rutas]

> Idea central: Hay 19 rutas propias, repartidas en tres blueprints: 7 del sitio público, 5 de cuentas y 7 de análisis. Cada ruta es una función con un decorador que dice su dirección y sus métodos; las privadas llevan login_required.

> En pantalla: Terminal con `flask --app run routes`; después el editor en `app/sitio.py`, `app/cuentas.py` y `app/analisis/rutas.py`, mirando solo los decoradores `@bp.route`.

[Acción: terminal, en la carpeta del proyecto: flask --app run routes]

Esta es la lista completa de direcciones del sitio. Flask la arma a partir del código. Son 19 rutas propias, más una que sirve los archivos estáticos, como el CSS y las imágenes.

[Acción: abre app/sitio.py y muestra los decoradores]

El sitio público tiene siete. El inicio, Nosotros, Aliados, Infografías, Videos, Contacto y el aviso de privacidad. Son funciones cortas. Casi todas hacen una sola cosa: devolver una plantilla. La excepción es Contacto, que además recibe el formulario y guarda el mensaje.

[Acción: abre app/cuentas.py]

Las cuentas tienen cinco. Entrar, salir, perfil, olvidé mi contraseña y restablecer.

[Acción: abre app/analisis/rutas.py]

Y el análisis tiene siete. La página de inteligencia artificial, analizar, analizar la imagen de prueba, los resultados, la imagen marcada, el CSV y el PDF.

Una ruta es una función con una línea encima, el decorador. Esa línea dice la dirección y los métodos que acepta. Entrar acepta GET, para mostrar el formulario, y POST, para recibirlo. Algunas direcciones llevan una parte variable, como el número del análisis. Si se escribe con int, Flask exige que sea un número y responde 404 si no lo es.

Las rutas privadas llevan otro decorador, login_required. Si la persona no ha iniciado sesión, Flask la manda a la pantalla de entrada. Son ocho: salir, perfil, analizar, la prueba, y las cuatro que muestran o descargan resultados.

[Pantalla 5 · Cuentas]

> Idea central: Al crear una cuenta se guarda una huella de la contraseña y nunca la contraseña. Al iniciar sesión se compara la huella, y el mensaje de error es el mismo si falla el correo o la contraseña. Flask-Login recuerda quién entró, y destino_seguro impide que un enlace mande a la persona a otro sitio.

> En pantalla: Editor, `app/cuentas.py`: la ruta `entrar` (línea 26), el registro (36 a 53), el inicio de sesión (55 a 59) y `destino_seguro` (19); después `app/modelos.py`, las líneas 20 a 24 y el cargador de usuario (54).

[Acción: abre cuentas.py, ruta entrar, línea 26]

La ruta entrar sirve para dos cosas: iniciar sesión y crear cuenta. Distingue cuál por un campo oculto del formulario.

[Acción: líneas 36 a 53: el registro]

Para crear una cuenta hay una cadena de comprobaciones. Que no falte nada. Que el correo tenga arroba. Que la contraseña tenga al menos ocho caracteres. Y que el correo no exista ya. El correo se limpia y se pasa a minúsculas, para que Ana y ana sean la misma cuenta. Si todo está bien, se crea el usuario y entra de una vez.

[Acción: abre modelos.py, líneas 20 a 24]

Lo importante es lo que no se guarda. La contraseña nunca se guarda. Se guarda una huella, calculada con una función de Werkzeug, que no se puede deshacer. El campo se llama clave cifrada, aunque en rigor no es un cifrado. Un cifrado se puede revertir. Una huella no. Para saber si una contraseña es correcta, se calcula su huella y se compara con la guardada.

[Acción: cuentas.py, líneas 55 a 59: el inicio de sesión]

En el inicio de sesión pasa lo mismo. Y si falla, el mensaje es siempre el mismo: correo o contraseña incorrectos. No dice cuál de los dos. Así nadie puede usar el formulario para averiguar qué correos están registrados.

[Acción: modelos.py, línea 54]

Para recordar quién entró se usa Flask-Login. Al iniciar sesión, deja una cookie firmada con la clave secreta. En cada petición, una función que se llama cargar usuario recibe el número guardado y busca a la persona en la base de datos. Eso es lo que hace que current user exista en el código y en las plantillas.

[Acción: cuentas.py, línea 19]

Y un detalle de seguridad. Cuando alguien intenta entrar a una página privada, el sitio lo manda a iniciar sesión y, al terminar, lo regresa a donde iba. Esa dirección viaja en la dirección web. Así que alguien podría armar un enlace que lleve a otro sitio. Por eso existe destino seguro. Solo acepta direcciones que empiezan con diagonal y no traen dominio. Cualquier otra cosa lleva a la página de análisis.

[Pantalla 6 · Protección CSRF]

> Idea central: Cada formulario lleva un token que solo conoce el sitio, y todo POST sin token válido se rechaza antes de llegar a la función. Así una página ajena no puede hacer que tu navegador mande una orden en tu nombre.

> En pantalla: Editor, `app/extensiones.py` y `app/__init__.py` línea 35; después navegador, F12, pestaña Elementos, para ver el campo oculto `csrf_token` de un formulario, y la consola con una petición POST sin token.

[Acción: editor, extensiones.py, y __init__.py línea 35]

La protección CSRF ocupa dos líneas de código. Se crea en extensiones.py y se enciende en crear_app. Y protege algo muy concreto.

Imagina que tienes la sesión iniciada en este sitio. En otra pestaña abres una página maliciosa. Esa página puede hacer que tu navegador mande una orden al sitio. Y tu navegador adjunta tu sesión, porque así funcionan las cookies. El sitio ve una orden con una sesión válida y la cumple. Eso es un ataque de falsificación de petición entre sitios.

[Acción: navegador, F12, pestaña Elementos: busca el campo oculto csrf_token en el formulario de salir]

La defensa es el token. Cada formulario del sitio lleva este campo oculto. Su valor lo genera el sitio para tu sesión, y una página ajena no lo puede conocer. Todo POST que llegue sin un token válido se rechaza antes de llegar a la función de la ruta.

[Acción: consola: fetch('/salir', {method: 'POST'}).then(r => r.status). Debe dar 400. Di que es una forma de comprobarlo y que no es algo que haga el visitante]

Podemos comprobarlo. Desde la consola mando una petición para cerrar sesión, pero sin el token. La respuesta es 400, petición incorrecta. Y la sesión sigue abierta.

En las pruebas automáticas esta protección se apaga, porque no hay un navegador que reciba el token. Es una de las configuraciones que cambia la función crear_app.

[Pantalla 7 · Recuperar la contraseña]

> Idea central: El enlace de recuperación es un token firmado que lleva el número del usuario y un pedazo de su contraseña actual. Dura una hora y deja de servir en cuanto la contraseña cambia, sin guardar nada en la base de datos. La respuesta es la misma exista o no la cuenta, y el correo sale por SMTP con datos del archivo .env.

> En pantalla: Editor, `app/cuentas.py`: `_serializador`, `_token` y `_usuario_del_token` (78 a 95), `olvide` (98 a 117) y `restablecer` (120 a 137); después `app/correo.py` y el archivo `docker-compose.yml`, líneas 16 a 20.

[Acción: cuentas.py, líneas 78 a 95]

Recuperar la contraseña es la parte más delicada de las cuentas. Y se resolvió con una idea sencilla: el enlace se firma, no se guarda.

El enlace lleva un token, armado con una biblioteca que se llama itsdangerous. Dentro van dos datos. El número del usuario y los últimos diez caracteres de la huella de su contraseña actual. Todo se firma con la clave secreta del sitio, y la firma lleva la hora.

Al abrir el enlace, el sitio verifica la firma. Comprueba que no hayan pasado 3,600 segundos, una hora. Y compara esos diez caracteres con los de la huella actual. Si la persona cambia su contraseña, la huella cambia, y el mismo enlace deja de servir. Por eso solo se puede usar una vez, sin que el sitio guarde ninguna lista de enlaces.

[Acción: cuentas.py, líneas 98 a 117]

La pantalla de olvidé mi contraseña tiene dos decisiones. Una: la respuesta es la misma si el correo existe y si no. Siempre dice que, si está registrado, se manda un enlace. Así no sirve para descubrir quién tiene cuenta. La otra: si el envío falla, y solo entonces, avisa que no se pudo enviar y da el correo de contacto.

[Acción: abre correo.py]

El envío está en un archivo aparte, correo.py. Usa smtplib, que viene con Python. Se conecta al servidor de correo, activa el cifrado, inicia sesión con una contraseña de aplicación y manda el mensaje. Todos los datos salen de variables de entorno: servidor, puerto, usuario, remitente y clave. Si falta alguna, la función no intenta nada y devuelve falso.

[Acción: docker-compose.yml, líneas 16 a 20]

Esas variables llegan del archivo .env del servidor, a través del archivo de composición. El .env no está en Git. Ahí viven las claves.

[Pantalla 8 · La base de datos]

> Idea central: La base de datos es SQLite, un archivo dentro de instance. Tiene tres tablas, Usuario, Analisis y Mensaje, definidas como clases de Python con SQLAlchemy. Los resultados de cada análisis se guardan como JSON dentro de una sola columna.

> En pantalla: Editor, `app/modelos.py`: las tres clases (10, 27 y 45) y la propiedad `resultados`; después el explorador de archivos en la carpeta `instance`.

[Acción: abre modelos.py]

La base de datos es SQLite. No hay un servidor de base de datos aparte. Es un archivo, imagebio.db, dentro de la carpeta instance. Para un sitio con pocos usuarios y un solo proceso, alcanza. Y se respalda copiando un archivo.

Las tablas se definen como clases de Python, con SQLAlchemy. Una clase es una tabla, y cada atributo es una columna. Hay tres.

[Acción: señala la clase Usuario, línea 10]

Usuario. Nombre, correo, que es único y tiene índice, la huella de la contraseña y la fecha de creación.

[Acción: señala la clase Analisis, línea 27, y la propiedad resultados]

Analisis. De quién es, cuándo se hizo, el nombre del PDF y los resultados. Y aquí hay una decisión de diseño. Los resultados completos, con la lista de imágenes, sus contornos y sus medidas, se guardan en una sola columna de texto, como JSON. Una propiedad, resultados, lo convierte otra vez en diccionario.

¿Por qué así? Porque lo que importa es volver a mostrar el análisis igual que al hacerlo, y su forma cambia según las imágenes que haya. La contrapartida es que no se pueden hacer consultas con SQL sobre cada medida. Para este proyecto no hace falta.

[Acción: señala la clase Mensaje, línea 45]

Y Mensaje guarda lo que llega por el formulario de contacto.

[Acción: explorador de archivos, carpeta instance]

En la carpeta instance están la base de datos y las tres carpetas de trabajo: pdfs, marcadas y subidas. En el servidor, toda la carpeta es un volumen de Docker. Así, reconstruir el sitio no borra los datos.

[Pantalla 9 · La ruta analizar]

> Idea central: La ruta analizar valida antes de trabajar: que haya imágenes, que no pasen de diez y que la extensión sea permitida. Guarda cada imagen con un nombre generado, la analiza y la borra en un bloque finally, pase lo que pase.

> En pantalla: Editor, `app/analisis/rutas.py`: la ruta `analizar` (líneas 33 a 63), con las validaciones (39 a 49), el nombre con `uuid` (51 a 56) y el `try/finally` (58 a 61); después `analizar_prueba` (66 a 73).

[Acción: rutas.py, ruta analizar, línea 33]

Llegamos a la ruta que hace el trabajo: analizar.

[Acción: líneas 36 a 49: las validaciones]

Antes de hacer nada, se valida. Que haya al menos una imagen. Que no pasen del máximo de diez. Y que todas tengan una extensión permitida: BMP, PNG, TIFF o JPG. Si algo falla, la función deja un aviso y regresa a la página de análisis.

Y hay que decirlo claro. La comprobación mira el nombre del archivo, no su contenido. Si alguien sube un texto con extensión PNG, pasa esta validación. Es la función de medición la que descubre que no se puede abrir como imagen, y avisa.

[Acción: líneas 51 a 56: el nombre generado]

Después, un detalle de seguridad. En el disco, cada imagen se guarda con un nombre generado: un identificador aleatorio de la biblioteca uuid, el número de la imagen y la extensión. El nombre que puso la persona no se usa para guardar. Solo para mostrar. Así nadie puede colar un nombre con rutas raras ni pisar el archivo de otro.

[Acción: líneas 58 a 61: try y finally]

Luego viene lo que dijimos en el video anterior: las imágenes no se conservan. Cada una se analiza dentro de un bloque try, y se borra en el finally. El finally se ejecuta siempre. Si el análisis termina bien, y también si falla. Así no queda ninguna imagen subida en el servidor.

[Acción: líneas 66 a 73: analizar_prueba]

La ruta de la imagen de ejemplo hace lo mismo, pero con un archivo que ya está en el sitio. Reutiliza la misma función de análisis. Ahí se ve el beneficio de separar las piezas.

[Pantalla 10 · Guardar y mostrar]

> Idea central: Con la lista de imágenes analizadas, _guardar_y_mostrar arma el diccionario de resultados, lo guarda como JSON, genera el PDF y redirige a la página de resultados. Responder con una redirección evita que recargar la página repita el análisis.

> En pantalla: Editor, `app/analisis/rutas.py`, función `_guardar_y_mostrar` (líneas 81 a 103); señala el diccionario (83 a 90), el guardado (91 a 93), el PDF (96 a 101) y la redirección (103). Después, navegador: recarga la página de resultados con F5.

[Acción: rutas.py, _guardar_y_mostrar, línea 81]

Con las imágenes ya analizadas, entra _guardar_y_mostrar.

[Acción: líneas 82 a 90: el diccionario]

Primero arma el diccionario de resultados. Lleva la lista de imágenes y el promedio entre ellas. Y dos banderas. Una dice si el análisis fue provisional, porque faltaban los modelos y se usó la detección por color. La otra dice si se hizo con el modelo, que el sitio llama preliminar. De eso depende qué avisos muestra la página.

[Acción: líneas 91 a 93]

Segundo, lo guarda. Crea un registro de Analisis con el número de la persona y el diccionario convertido a JSON, y lo confirma con commit. Al confirmar, la base le asigna su número.

[Acción: líneas 96 a 101]

Tercero, el PDF. Se genera con ese número, se guarda en la carpeta de PDF con el nombre analisis, el número y la extensión, y se anota el nombre en el registro, con un segundo commit.

[Acción: línea 103]

Y por último, no devuelve la página. Devuelve una redirección a la ruta de resultados. Es lo que vimos en la pestaña de red: un POST con respuesta 302, y luego un GET. Es un patrón muy usado, y tiene una razón práctica.

[Acción: navegador: recarga la página de resultados con F5]

Si la respuesta al POST fuera la página, al recargarla el navegador preguntaría si quieres reenviar el formulario. Y reenviar significaría analizar otra vez. Como la página es el resultado de un GET, recargar la muestra de nuevo, sin repetir el trabajo.

Hay una consecuencia que se nota. El análisis se hace dentro de la misma petición. El navegador espera. Por eso existe la cubierta de espera que vimos, y por eso el tiempo máximo es tan alto. No hay una cola de tareas aparte. Es una decisión de simplicidad, y la vemos al final.

[Pantalla 11 · Cada quien ve lo suyo]

> Idea central: Cada análisis es de una persona: si no existe o es de otra, la respuesta es 404 y no 403, para no revelar que existe. Las imágenes marcadas solo se sirven si su nombre aparece en los resultados de ese análisis.

> En pantalla: Editor, `app/analisis/rutas.py`: `_analisis_propio` (líneas 106 a 111) e `imagen_marcada` (122 a 129). Después, navegador: cambia el número del análisis en la dirección por el de otra cuenta de prueba, o por uno que no exista.

[Acción: rutas.py, _analisis_propio, línea 106]

Todas las rutas que muestran o descargan un análisis empiezan igual, con una función corta: _analisis_propio. Busca el análisis por su número. Si no existe, o si es de otra persona, responde 404.

[Acción: navegador: cambia el número del análisis en la dirección por uno de otra cuenta o que no exista]

Fíjate en el código: 404, no 403. Un 403 diría que ese análisis existe, pero que no es tuyo. Un 404 dice lo mismo en los dos casos: aquí no hay nada. Así nadie puede recorrer los números para averiguar cuántos análisis hay.

[Acción: editor, rutas.py, líneas 122 a 129]

Lo mismo con las imágenes marcadas. La ruta recibe el nombre del archivo, pero antes arma el conjunto de nombres permitidos: las dos copias marcadas de cada imagen de ese análisis. Si el nombre pedido no está en ese conjunto, 404. Y para servir el archivo usa send_from_directory, que además impide salirse de la carpeta con rutas como punto punto diagonal.

Es una regla de oro: nunca confiar en lo que llega en la dirección. Siempre se verifica de quién es y qué se pidió.

[Pantalla 12 · CSV y PDF]

> Idea central: reportes.py genera el CSV al momento, con una fila por espermatozoide y una marca para que Excel lea los acentos, y el PDF al terminar el análisis, con fpdf2 y gráficas de matplotlib dibujadas sin ventana. Las fuentes básicas del PDF solo aceptan latin-1.

> En pantalla: Editor, `app/analisis/reportes.py`: `generar_csv` (líneas 18 a 28), el modo sin ventana de matplotlib (8), `_texto` (31 a 33), `_grafica_barras` (36 a 50) y `generar_pdf` (87 a 131); después las rutas `descargar_csv` y `descargar_pdf` en `rutas.py` (132 a 150).

[Acción: abre reportes.py, generar_csv, línea 18]

Los reportes están en el archivo reportes.py. El CSV es la pieza más simple. Se escribe en memoria, con el módulo csv de Python: una fila de encabezados y una fila por espermatozoide. Imagen, número, área y largo en píxeles, y área y largo en micras.

[Acción: línea 28: la marca de orden de bytes]

Hay un detalle en la última línea. Antes del texto se agrega un carácter invisible, la marca de orden de bytes. Sirve para que Excel abra el archivo con la codificación correcta, y los acentos no salgan rotos.

El CSV no se guarda. Se genera cada vez que alguien lo descarga, a partir de los resultados guardados. Y la respuesta lleva una cabecera que le dice al navegador que es una descarga.

[Acción: línea 8 y líneas 36 a 50]

El PDF es otra cosa. Se genera una vez, al terminar el análisis. Usa fpdf2, y las gráficas las dibuja matplotlib. Fíjate en la línea 8. El modo Agg le dice a matplotlib que dibuje sin ventana, porque el servidor no tiene pantalla. La gráfica se dibuja en memoria como una imagen PNG, y se inserta en la página.

[Acción: líneas 31 a 33: _texto]

Y una limitación que viene de las fuentes básicas del PDF. Solo aceptan el alfabeto latín-1. Los acentos, la eñe, la micra y el cuadrado pasan sin problema. Pero cualquier carácter fuera de ese conjunto se cambia por un signo de interrogación. Eso es lo que hace la función _texto.

[Acción: líneas 87 a 131: generar_pdf]

El PDF lleva lo mismo que la pantalla. El usuario, la fecha, la nota de la escala, el aviso rojo si fue provisional, una página por imagen y, si hay varias, la gráfica del promedio.

[Acción: rutas.py, líneas 132 a 150]

En las rutas, el CSV se entrega como respuesta en el momento, y el PDF se lee de la carpeta con send_from_directory. Los dos exigen sesión, y los dos pasan por la comprobación de que el análisis sea tuyo.

[Pantalla 13 · Un proceso, cuatro hilos y las pruebas]

> Idea central: Gunicorn corre con un proceso y cuatro hilos, para que los modelos se carguen una sola vez, y con tiempo máximo de 1,800 segundos, igual que Nginx. Las pruebas con pytest recorren el flujo completo sin los modelos, y comprueban que el sitio funcione, no que el conteo sea científicamente correcto.

> En pantalla: Editor: la última línea de `Dockerfile` (23) y `deploy/nginx.conf`, líneas 41 y 49 a 51; después terminal: `python -m pytest`, y el editor en `tests/test_sistema.py` (fixture `app`, líneas 18 a 30) y en `tests/test_modelo.py` (línea 59).

[Acción: Dockerfile, línea 23]

Para cerrar, cómo se ejecuta todo. Esta es la orden con la que arranca el sitio en el servidor. Gunicorn, con un proceso, que se llama worker, y cuatro hilos.

¿Por qué solo uno? Porque cada modelo ocupa unos 176 megabytes en memoria, y varios procesos los duplicarían. Con un solo proceso, los modelos se cargan una vez. Y los cuatro hilos permiten que el resto del sitio siga respondiendo mientras un análisis usa el procesador.

El tiempo máximo es de 1,800 segundos, media hora. Porque analizar diez imágenes grandes con los modelos puede tardar varios minutos. Nginx tiene el mismo número en sus tiempos de espera, y un límite de 300 megabytes por envío, igual que Flask.

[Acción: nginx.conf, líneas 41 y 49 a 51]

Esto es una decisión de simplicidad, y sus límites son claros. No hay una cola de tareas. Mientras un análisis corre, otro tiene que esperar su turno, y la persona ve la cubierta de espera. Con pocas personas a la vez, funciona. Si el uso creciera mucho, el siguiente paso sería sacar el análisis a una cola, con procesos aparte.

[Acción: terminal: python -m pytest. Lee el resultado de ese día]

Y las pruebas. Con la orden python -m pytest se ejecutan todas. Este es el resultado de hoy.

[Acción: tests/test_sistema.py, fixture app, líneas 18 a 30]

Las pruebas recorren el flujo completo con un cliente de pruebas de Flask, que simula un navegador. Una cuenta se registra, entra, sube una imagen, ve los resultados y descarga el CSV y el PDF. También comprueban lo que no debe pasar. Que un análisis ajeno dé 404. Que un formato no permitido se rechace. Que más de diez imágenes se rechacen. Que una redirección a otro sitio se bloquee. Que el enlace de recuperación solo sirva una vez.

Para que sean rápidas, el entorno de pruebas se crea sin los modelos, con una base de datos temporal y sin protección de formularios.

[Acción: tests/test_modelo.py, línea 59]

Y hay que decir lo que no comprueban. No dicen si el conteo es correcto, ni si la medición es buena. Comprueban que el sitio usa bien lo que le entrega el modelo. La prueba con los modelos reales existe, pero solo corre si se pide con una variable y si los archivos están. La calidad científica se evalúa aparte, con las imágenes anotadas, y es parte del trabajo con el cliente.

[Pantalla 14 · Lo que vimos y lo que sigue]

> Idea central: Vimos el camino de una imagen por el backend: Flask y sus extensiones, la aplicación, las rutas, las cuentas con sus protecciones, la base de datos, el análisis, los reportes y cómo se ejecuta y se prueba. En el siguiente video, el modelo: cómo se le da una foto y cómo se recogen sus respuestas.

> En pantalla: Vuelve al navegador, en la página de resultados del ejemplo, mientras das el resumen y te despides.

[Acción: vuelve al navegador, en la página de resultados]

Un resumen.

Vimos el camino que sigue una imagen. Nginx recibe la petición, Gunicorn la pasa a Flask, y Flask la dirige a una función según la dirección. Vimos cómo se crea la aplicación con una función, y cómo se organizan sus 19 rutas en tres secciones.

Vimos las protecciones. Las contraseñas se guardan como huella. El error de inicio de sesión no revela nada. Los formularios llevan un token contra la falsificación de peticiones. El enlace de recuperación se firma, dura una hora y se vuelve inútil al cambiar la contraseña. Cada persona ve solo lo suyo, y todo lo que llega en la dirección se verifica.

Vimos la base de datos con sus tres tablas. La ruta de análisis, que valida, guarda con un nombre generado y borra la imagen siempre. Y los reportes en CSV y PDF. Y vimos cómo corre todo en el servidor, y qué comprueban las pruebas y qué no.

En el siguiente video entramos al modelo. En esta ruta, analizar le entrega la imagen a una función y recibe contornos. Qué pasa dentro de esa función, cómo se prepara la foto, cómo se corta en recortes y cómo se recogen las respuestas de la red, es el tema del tercer video. Gracias por acompañarme.
