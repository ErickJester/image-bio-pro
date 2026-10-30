# Guion del módulo 3, video 1 de 4: Backend (versión natural)

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Abre el módulo 3: empieza con la frase que lo une con el módulo 2 y presenta el módulo.

*5,565 palabras, unos 31.8 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar: el entorno de Python

El Python global de este equipo no trae las extensiones de Flask que usa el sitio, así que hay que crear un entorno aparte, una sola vez. Un entorno virtual (venv) es una carpeta, `.venv`, con su propia copia de las bibliotecas del proyecto: lo que se instala ahí no cambia el Python global, que se usa en otros proyectos. Se crea con `--system-site-packages` para que reutilice lo que ya está instalado (Flask, OpenCV, NumPy, PyTorch, Matplotlib y Pillow) y solo se instale lo que falta.

- `python -m venv --system-site-packages .venv` crea el entorno, en la carpeta del proyecto. La carpeta `.venv` ya está en `.gitignore`.
- `.\.venv\Scripts\python.exe -m pip install flask-login==0.6.3 flask-sqlalchemy==3.1.1 flask-wtf==1.3.0 fpdf2==2.8.9 pytest` instala lo que falta.
- `.\.venv\Scripts\Activate.ps1` activa el entorno en la terminal. Con él activo, en pantalla se ven `python run.py`, `flask --app run routes` y `python -m pytest` tal como los dice el guion. Si PowerShell bloquea el script por la política de ejecución, se usan las rutas completas, por ejemplo `.\.venv\Scripts\python.exe run.py`.
- No se usa `pip install -r requirements.txt` en el Python global: fija versiones (por ejemplo `numpy==2.5.4`) que cambiarían las de otros proyectos.

[Pantalla 1 · Qué pasa al subir una imagen]

> Idea central: Al pulsar analizar, el navegador manda una petición y el servidor contesta con una redirección a la página de resultados. En medio hay un camino: Nginx, Gunicorn, Flask, el modelo, la medición, la base de datos y el PDF. Este video recorre ese camino, menos el modelo y la medición, que son los dos siguientes.

> En pantalla: Navegador con la cuenta de prueba ya iniciada y la pestaña de red de las herramientas de desarrollo (F12) abierta, con la opción de conservar el registro activa. Pulsa Probar con la imagen de ejemplo y señala las dos peticiones que salen: un POST a `/analizar/prueba` con respuesta 302 y un GET a `/resultados/N` con respuesta 200.

Bienvenidos al módulo 3. En el módulo 2 vimos cómo ve una imagen una red convolucional, cómo trabaja Mask R-CNN, cómo la transferencia ahorra fotos y cómo se anotan y se miden los datos. Todo eso termina en un archivo: el modelo entrenado, con casi 44 millones de pesos guardados.

Pero un archivo de modelo, solo, no hace nada. Hace falta un sitio donde alguien suba una foto y reciba números. De eso trata el módulo 3.

Son cuatro videos. En este, el primero, vemos el backend. Es la parte del sitio que corre en el servidor, donde nadie la ve. En el segundo, cómo el servidor usa el modelo con recortes de la foto. En el tercero, cómo se miden los contornos, de qué depende la escala y qué retos tuvo el proyecto. Y en el cuarto, el último, el sitio funcionando, por fuera y por dentro. Esa es la parte que se ve en el navegador. Se llama frontend.

Por eso hoy vemos el sitio por detrás, antes de recorrerlo completo. Lo usamos solo lo necesario para ver qué ocurre al subir una imagen. La demostración completa, con calma, la dejamos para el final del módulo.

[Acción: navegador con la cuenta de prueba iniciada; F12, pestaña de red, conservar el registro]

Cuando alguien pulsa analizar, pasan muchas cosas en pocos segundos. Y casi ninguna se ve.

Antes de seguir, dos palabras que vamos a usar todo el video. Una petición es lo que el navegador le manda al servidor. Quiero esta página, o toma esta imagen. Una respuesta es lo que el servidor devuelve. Y las peticiones tienen un método. GET quiere decir pedir algo, como una página. POST quiere decir enviar datos, como una imagen o un formulario.

[Acción: pulsa Probar con la imagen de ejemplo]

Hagamos una prueba, con la pestaña de red del navegador abierta. Esa pestaña muestra cada petición que sale. Pulso el botón, y aparecen dos que nos importan.

La primera es un POST a analizar prueba. Su respuesta es un 302. Ese número es un código de estado, y el 302 quiere decir redirigir. El servidor no devuelve la página. Devuelve una instrucción: ve a esta otra dirección. La segunda es un GET a resultados, con el número del análisis. Esa sí devuelve la página, con un código 200, que quiere decir todo bien.

Detrás de esas dos líneas hay un camino de cuatro programas. El navegador habla primero con Nginx. Es un servidor web: el programa que recibe las visitas desde internet y las protege con HTTPS, que es el candado del navegador. Nginx sabe entregar páginas, pero no sabe ejecutar Python. Por eso se las pasa a Gunicorn, un servidor de aplicaciones de Python. Ese sí sabe, y atiende varias peticiones a la vez. Gunicorn llama a nuestra aplicación, hecha con Flask, un marco de trabajo para sitios web en Python. Flask comprueba que la persona haya iniciado sesión, y ejecuta la función de análisis.

Esa función le da la imagen al modelo. Recibe los contornos. Mide. Guarda los resultados en la base de datos, genera el PDF y manda al navegador a la página de resultados.

Este video recorre ese camino por dentro. Primero, con qué se escribe, cómo se crea la aplicación y qué rutas tiene. Después las cuentas y sus protecciones, la base de datos, la ruta de análisis y los reportes. Y al final, cómo se ejecuta todo y cómo se prueba. El modelo y la medición tienen su propio video cada uno.

[Pantalla 2 · Python y Flask]

> Idea central: El backend está escrito en Python, con Flask como marco de trabajo y unas pocas extensiones. Flask conecta direcciones con funciones; las bibliotecas hacen el resto. Las dependencias están en requirements.txt y PyTorch va aparte.

> En pantalla: Editor con `requirements.txt` abierto, y después `requirements-modelo.txt` y `run.py`. Señala cada biblioteca al nombrarla.

[Acción: editor, requirements.txt]

El backend está escrito en Python. Es un lenguaje de programación con fama de ser fácil de leer. Y domina la inteligencia artificial por las bibliotecas que se construyeron a su alrededor. Una biblioteca es una colección de programas ya escritos para una tarea, que uno puede usar en lugar de escribirla desde cero. Un proyecto como este no se programa entero. Se combinan bibliotecas muy buenas, y el trabajo propio está en unirlas con cuidado.

Esta es la lista, en el archivo requirements.txt. Significa requisitos. Cada línea es una biblioteca con su versión. El doble igual fija la versión exacta con la que se probó el sitio, para que mañana no cambie nada sin avisar.

Flask es el marco de trabajo, la base del sitio. Flask-Login lleva las sesiones, es decir, recuerda quién entró. Flask-WTF protege los formularios. Flask-SQLAlchemy conecta con la base de datos. OpenCV, NumPy y Pillow trabajan con imágenes: leerlas, recorrerlas como tablas de números y medir contornos. Matplotlib dibuja gráficas, y fpdf2 arma el PDF. Gunicorn es el servidor de aplicaciones que vimos. Y pytest corre las pruebas automáticas.

[Acción: requirements-modelo.txt]

PyTorch, la biblioteca de las redes neuronales, está en otro archivo, requirements-modelo.txt. Se instala aparte porque se baja de un repositorio especial, el de la versión para procesador. Es mucho más pequeña que la de tarjeta gráfica. El servidor no tiene tarjeta gráfica, y no la necesita para usar un modelo ya entrenado.

¿Y qué hace Flask? Una página web funciona con peticiones y respuestas. Flask permite decir, con pocas líneas de código, qué dirección corresponde a qué función. Si alguien entra al inicio, se ejecuta esta. Si alguien sube una imagen, se ejecuta aquella otra.

[Acción: abre run.py]

Y como Flask está escrito en Python, puede llamar directamente a la red neuronal, que también está en Python. El sitio y el modelo viven en el mismo programa. El archivo run.py es el arranque en tu computadora. Su primera línea importa la función crear app, que vamos a ver ahora. La tercera la ejecuta y guarda la aplicación en una variable. Y las dos últimas dicen: si este archivo se ejecuta directamente, enciende el servidor de pruebas de Flask, en modo de desarrollo.

[Pantalla 3 · Crear la aplicación]

> Idea central: crear_app construye la aplicación: reúne la configuración, crea las carpetas, enciende las extensiones y registra las tres secciones. Es una función y no una variable para que las pruebas puedan crear una aplicación nueva con otra configuración.

> En pantalla: Editor, `app/__init__.py`: la función `crear_app` (línea 9), la configuración (12 a 26), las carpetas (30 a 32), las extensiones (34 a 39) y los blueprints (41 a 48); después `app/extensiones.py` completo.

[Acción: abre app/__init__.py, función crear_app, línea 9]

El corazón del backend es una función. Se llama crear app y está en el archivo app/__init__.py. Una función que construye y devuelve la aplicación se llama, en programación, una fábrica. Hace cuatro cosas, de arriba abajo.

[Acción: línea 10: Flask(__name__, instance_relative_config=True)]

La línea 10 crea la aplicación. Flask, con el nombre del archivo, y una opción que le dice que use una carpeta llamada instance. Es para los archivos que cambian mientras el sitio funciona.

[Acción: líneas 12 a 26: la configuración]

Primero, la configuración, un conjunto de valores que controlan el sitio. En la línea 14 está la clave secreta. Sirve para firmar cosas, como la cookie de la sesión y los enlaces de recuperación, para que nadie pueda falsificarlos. No está escrita en el código. Se lee de una variable de entorno, que es un valor que vive en el sistema y no en los archivos. Si no existe, se usa un valor de desarrollo. Y en el servidor, el archivo de composición se niega a arrancar si no la define.

La línea 15 es la dirección de la base de datos: un archivo llamado imagebio.db dentro de instance. La línea 17 limita cada envío a 300 megabytes. Si alguien manda más, Flask responde con un error 413. La línea 18 es la primera opción propia del proyecto: el máximo de diez imágenes por análisis. Y de la 22 a la 25 están las rutas de tres carpetas de trabajo. Una para los PDF, una para las subidas temporales y una para las imágenes marcadas.

[Acción: líneas 27 y 28: if config]

La línea 27 permite sobrescribir cualquiera de esos valores al crear la aplicación. Eso lo usan las pruebas, como veremos.

[Acción: líneas 30 a 32: las carpetas]

Segundo, las carpetas. Este ciclo recorre las rutas y crea cada carpeta si no existe. La opción exist ok evita un error cuando la carpeta ya está.

[Acción: extensiones.py, líneas 1 a 3: los imports]

Tercero, las extensiones. Están en un archivo aparte, extensiones.py. Las tres primeras líneas son importaciones: traen de cada biblioteca la pieza que vamos a usar. Hay tres.

[Acción: extensiones.py, líneas 5 a 7: las tres extensiones]

La línea 5 crea db, la conexión con la base de datos, con SQLAlchemy. La línea 6 crea el administrador de sesiones, de Flask-Login. Y la línea 7 crea csrf, con CSRFProtect. CSRF son las siglas en inglés de falsificación de petición entre sitios. Es un ataque en el que una página ajena consigue que tu navegador mande una orden al sitio donde tienes la sesión abierta. CSRFProtect es lo que lo impide, y lo vemos completo en un tramo más adelante.

Aquí solo se crean, vacías. Y se crean en un archivo aparte para que cualquier otro archivo del proyecto pueda importarlas, sin que se enreden unos con otros.

[Acción: __init__.py, líneas 34 a 39: conectarlas a la aplicación]

De vuelta en crear app, las líneas 34 a 36 conectan las tres a la aplicación, con el método init app. La 37 dice a qué ruta mandar a quien intente entrar a una página privada sin sesión. Y la 38 y la 39 son el mensaje que verá.

[Acción: líneas 41 a 48 y 54 y 55]

Cuarto, las secciones. El sitio se divide en tres blueprints, que son grupos de rutas guardados cada uno en su archivo: el sitio público, las cuentas y el análisis. Se importan y se registran con register blueprint. Y en la línea 55, db.create all crea las tablas de la base de datos si todavía no existen. Ojo: no hay una herramienta de migraciones. Si algún día cambia una tabla, hay que cuidar la base que ya existe.

Falta explicar por qué esto es una función y no una aplicación suelta. Porque las pruebas necesitan crear una aplicación nueva. Con otra base de datos, otras carpetas y sin la protección de formularios, para que sean rápidas. Con una función, eso es llamarla con otra configuración.

[Pantalla 4 · Las rutas]

> Idea central: Hay 19 rutas propias, repartidas en tres blueprints: 7 del sitio público, 5 de cuentas y 7 de análisis. Cada ruta es una función con un decorador que dice su dirección y sus métodos; las privadas llevan login_required.

> En pantalla: Terminal con `flask --app run routes`; después el editor en `app/sitio.py`, `app/cuentas.py` y `app/analisis/rutas.py`, mirando solo los decoradores `@bp.route`.

[Acción: terminal, en la carpeta del proyecto: flask --app run routes]

Una ruta es una dirección del sitio con la función que la atiende. Esta es la lista completa. Flask la arma a partir del código. Cada fila dice la función, los métodos que acepta y la dirección. Hay 19 rutas propias, más una que sirve los archivos estáticos, como el CSS y las imágenes.

[Acción: abre app/sitio.py y muestra los decoradores]

Veamos cómo se escribe una. Esta línea con una arroba, @bp.route, es un decorador. Un decorador es una línea que se pone encima de una función para darle un comportamiento extra. Aquí convierte la función en la respuesta de una dirección. Y la palabra bp es el blueprint al que pertenece.

El sitio público tiene siete rutas. El inicio, Nosotros, Aliados, Infografías, Videos, Contacto y el aviso de privacidad. Son funciones cortas. Casi todas hacen una sola cosa: devolver una plantilla, una página con huecos que el servidor llena con datos. Las plantillas las vemos a fondo en el último video del módulo. La excepción es Contacto, que además recibe el formulario y guarda el mensaje.

[Acción: abre app/cuentas.py]

Las cuentas tienen cinco. Entrar, salir, perfil, olvidé mi contraseña y restablecer.

[Acción: abre app/analisis/rutas.py]

Y el análisis tiene siete. La página de inteligencia artificial, analizar, analizar la imagen de prueba, los resultados, la imagen marcada, el CSV y el PDF.

Fíjate en los métodos. Entrar acepta GET, para mostrar el formulario, y POST, para recibir lo que se llenó. Analizar solo acepta POST, porque solo tiene sentido si se envía una imagen. Y algunas direcciones llevan una parte variable, como el número del análisis. Escrita con int entre signos de menor y mayor, Flask exige que sea un número entero. Si no lo es, responde 404, que quiere decir no encontrado.

Las rutas privadas llevan además otro decorador, login_required, que significa inicio de sesión requerido. Si la persona no ha iniciado sesión, Flask la manda a la pantalla de entrada. Son ocho: salir, perfil, analizar, la prueba, y las cuatro que muestran o descargan resultados.

[Pantalla 5 · Cuentas]

> Idea central: Al crear una cuenta se guarda una huella de la contraseña y nunca la contraseña. Al iniciar sesión se compara la huella, y el mensaje de error es el mismo si falla el correo o la contraseña. Flask-Login recuerda quién entró, y destino_seguro impide que un enlace mande a la persona a otro sitio.

> En pantalla: Editor, `app/cuentas.py`: la ruta `entrar` (línea 26), el registro (36 a 53), el inicio de sesión (55 a 59) y `destino_seguro` (19); después `app/modelos.py`, las líneas 20 a 24 y el cargador de usuario (54).

[Acción: abre cuentas.py, ruta entrar, línea 26]

La ruta entrar sirve para dos cosas: iniciar sesión y crear cuenta. Acepta GET y POST.

[Acción: líneas 31 a 34: leer el formulario]

Si la petición es un POST, las líneas 32 a 34 leen lo que llegó del formulario. request.form es el conjunto de campos enviados. Un campo oculto, accion, dice cuál de los dos formularios se envió. Y al correo se le quitan los espacios con strip y se pasa a minúsculas con lower. Así, Ana arroba ejemplo y ana arroba ejemplo son la misma cuenta.

[Acción: líneas 36 a 46: las comprobaciones del registro]

Para crear una cuenta hay una cadena de comprobaciones. Que no falte ningún dato. Que el correo tenga una arroba. Que la contraseña tenga al menos ocho caracteres. Y que no exista ya una cuenta con ese correo. Si alguna falla, flash deja un aviso de color y la página se vuelve a mostrar.

[Acción: líneas 47 a 53: crear el usuario]

Si todo está bien, se crea el usuario. La línea 47 recorta el nombre a 120 caracteres y el correo a 254. Son los límites de las columnas de la base. La 48 guarda la contraseña, y ahora vemos cómo. La 49 agrega el usuario a la sesión de la base de datos, y la 50, con commit, confirma el guardado. Hasta ese momento, nada está guardado de verdad. La 51 inicia la sesión de esa persona, y la 53 la manda a la página a la que iba.

[Acción: abre modelos.py, líneas 20 a 24]

Ahora, lo importante es lo que no se guarda. La contraseña nunca se guarda. Esta función de la línea 21 calcula una huella de la contraseña, y guarda solo la huella. Una huella, que en programación se llama hash, es el resultado de una operación que va en un solo sentido. De la contraseña se obtiene la huella, pero de la huella no se puede volver a la contraseña. Además, la función agrega un dato aleatorio, para que dos personas con la misma contraseña tengan huellas distintas. El campo se llama clave cifrada, aunque en rigor no es un cifrado. Un cifrado se puede revertir. Una huella, no.

Para saber si una contraseña es correcta, la función de la línea 24 calcula la huella de lo que se escribió y la compara con la guardada.

[Acción: cuentas.py, líneas 54 a 59: el inicio de sesión]

En el inicio de sesión se busca al usuario por su correo y se revisa la contraseña. Si todo va bien, login user inicia la sesión. Y si la casilla de recordar viene marcada, la sesión dura más. Si algo falla, el mensaje es siempre el mismo: correo o contraseña incorrectos. No dice cuál de los dos. Así nadie puede usar el formulario para averiguar qué correos están registrados.

[Acción: modelos.py, línea 54]

Y para recordar quién entró se usa Flask-Login. Al iniciar sesión, deja en el navegador una cookie, un pequeño dato guardado por el sitio, firmada con la clave secreta. En cada petición, esta función, cargar usuario, recibe el número que viene en la cookie y busca a la persona en la base de datos. Eso es lo que hace que current user exista en el código y en las plantillas.

[Acción: cuentas.py, líneas 19 a 23: destino_seguro]

Y un detalle de seguridad. Cuando alguien intenta entrar a una página privada, el sitio lo manda a iniciar sesión y, al terminar, lo regresa a donde iba. Esa dirección viaja dentro de la dirección web, en un parámetro que se llama next. Así que alguien podría armar un enlace que, después de iniciar sesión, lleve a otro sitio. La función destino seguro lo evita. Solo acepta direcciones que empiecen con diagonal y no traigan dominio. Cualquier otra cosa lleva a la página de análisis.

[Pantalla 6 · Protección CSRF]

> Idea central: Cada formulario lleva un token que solo conoce el sitio, y todo POST sin token válido se rechaza antes de llegar a la función. Así una página ajena no puede hacer que tu navegador mande una orden en tu nombre.

> En pantalla: Editor, `app/extensiones.py` y `app/__init__.py` línea 35; después navegador, F12, pestaña Elementos, para ver el campo oculto `csrf_token` de un formulario, y la consola con una petición POST sin token.

[Acción: editor, extensiones.py, y __init__.py línea 35]

Volvamos a CSRF, que mencionamos hace un momento. Ocupa dos líneas de código. Se crea en extensiones.py, y se enciende con csrf punto init app, en la línea 35. Y protege algo muy concreto.

Imagina que tienes la sesión iniciada en este sitio. En otra pestaña abres una página maliciosa. Esa página puede hacer que tu navegador mande una petición al sitio. Por ejemplo, la de cerrar sesión, o la de analizar algo. Y tu navegador adjunta tu cookie de sesión, porque así funcionan las cookies: se mandan solas a su sitio. El servidor ve una petición con una sesión válida y la cumple. Tú no la pediste, pero el servidor no lo sabe. Eso es un ataque de falsificación de petición entre sitios.

[Acción: navegador, F12, pestaña Elementos: busca el campo oculto csrf_token en el formulario de salir]

La defensa es un token. Un token es una cadena de caracteres que funciona como una llave de un solo propósito. Cada formulario del sitio lleva este campo oculto, con un valor que el sitio genera para tu sesión. Una página ajena puede mandar la petición, pero no conoce ese valor. Todo POST que llegue sin un token válido se rechaza antes de llegar a la función de la ruta.

[Acción: consola: fetch('/salir', {method: 'POST'}).then(r => r.status). Debe dar 400. Di que es una forma de comprobarlo y que no es algo que haga el visitante]

Podemos comprobarlo. Desde la consola del navegador, que es una forma de hacer peticiones a mano, mando una petición para cerrar sesión, pero sin el token. No es algo que haga un visitante. Es solo una manera de probarlo. La respuesta es 400, petición incorrecta. Y la sesión sigue abierta.

En las pruebas automáticas esta protección se apaga, porque no hay un navegador que reciba el token. Es una de las configuraciones que cambia la función crear app.

[Pantalla 7 · Recuperar la contraseña]

> Idea central: El enlace de recuperación es un token firmado que lleva el número del usuario y un pedazo de su contraseña actual. Dura una hora y deja de servir en cuanto la contraseña cambia, sin guardar nada en la base de datos. La respuesta es la misma exista o no la cuenta, y el correo sale por SMTP con datos del archivo .env.

> En pantalla: Editor, `app/cuentas.py`: `_serializador`, `_token` y `_usuario_del_token` (78 a 95), `olvide` (98 a 117) y `restablecer` (120 a 137); después `app/correo.py` y el archivo `docker-compose.yml`, líneas 16 a 20.

[Acción: cuentas.py, líneas 78 a 84: el serializador y el token]

Recuperar la contraseña es la parte más delicada de las cuentas. Y se resolvió con una idea sencilla: el enlace se firma, no se guarda.

Un enlace de recuperación lleva un token. Y este token se arma con una biblioteca que se llama itsdangerous, que significa podría ser peligroso. El serializador de la línea 78 convierte datos en un texto y los firma con la clave secreta del sitio. Firmar quiere decir calcular una marca que depende de los datos y de la clave. Si alguien cambia aunque sea una letra del token, la marca ya no coincide, y el sitio lo descarta. El parámetro salt es un texto que separa usos. Un token hecho para recuperar contraseñas no sirve para ninguna otra cosa.

Dentro del token van dos datos. El número del usuario y los últimos diez caracteres de la huella de su contraseña actual. Y la firma lleva también la hora en que se creó.

[Acción: líneas 87 a 95: revisar el token]

Al abrir el enlace, el sitio hace tres comprobaciones. Que la firma sea válida. Que no hayan pasado 3,600 segundos, una hora. Y que esos diez caracteres coincidan con los de la huella actual. Si la persona cambia su contraseña, la huella cambia, y el mismo enlace deja de servir. Por eso solo se puede usar una vez, sin que el sitio guarde ninguna lista de enlaces.

[Acción: cuentas.py, líneas 98 a 117: olvide]

La pantalla de olvidé mi contraseña tiene dos decisiones. Una: la respuesta es la misma si el correo existe y si no. Siempre dice que, si está registrado, se manda un enlace. Así no sirve para descubrir quién tiene cuenta. La otra: si el envío falla, y solo entonces, avisa que no se pudo enviar y da el correo de contacto.

[Acción: abre correo.py, líneas 11 a 13: configurado]

El envío está en un archivo aparte, correo.py. Primero, una función revisa que existan tres variables de entorno: el servidor de correo, el usuario y la clave. Si falta alguna, no se intenta nada.

[Acción: líneas 16 a 36: enviar]

Después, la función enviar arma el mensaje con EmailMessage: asunto, remitente, destinatario y texto. Luego abre una conexión con smtplib, una biblioteca que viene con Python. SMTP es el protocolo con el que se envían correos. La conexión se cifra con starttls, para que el contenido no viaje a la vista. El inicio de sesión usa una contraseña de aplicación. Es una clave especial que el proveedor, en este caso Gmail, genera para que un programa pueda enviar correos sin usar tu contraseña personal. Y los espacios se quitan, porque Google la muestra en grupos de cuatro letras. Si algo sale mal, la función devuelve falso en lugar de romper la página.

[Acción: docker-compose.yml, líneas 16 a 20]

Esas variables llegan del archivo .env del servidor, a través del archivo de composición, que es el que arranca los contenedores. El archivo .env no está en Git, que es donde se guarda el código. Ahí viven las claves.

[Pantalla 8 · La base de datos]

> Idea central: La base de datos es SQLite, un archivo dentro de instance. Tiene tres tablas, Usuario, Analisis y Mensaje, definidas como clases de Python con SQLAlchemy. Los resultados de cada análisis se guardan como JSON dentro de una sola columna.

> En pantalla: Editor, `app/modelos.py`: las tres clases (10, 27 y 45) y la propiedad `resultados`; después el explorador de archivos en la carpeta `instance`.

[Acción: abre modelos.py]

Una base de datos es donde un sitio guarda lo que no debe perderse. Las cuentas, los análisis, los mensajes. La nuestra es SQLite. No hay un servidor de base de datos aparte. Es un solo archivo, imagebio.db, dentro de la carpeta instance. Para un sitio con pocos usuarios y un solo proceso, alcanza. Y se respalda copiando un archivo.

Las tablas se definen como clases de Python, con SQLAlchemy. Esa técnica se llama mapeo objeto relacional. Una clase es una tabla, y cada atributo es una columna. Así, el código trabaja con objetos de Python y la biblioteca traduce a la base de datos. Hay tres.

[Acción: señala la clase Usuario, líneas 10 a 15]

Usuario. Cada línea es una columna. El id es la llave primaria: un número único para cada fila. El nombre y la clave no pueden quedar vacíos. El correo es único, para que no haya dos cuentas iguales, y tiene un índice. Un índice funciona como el índice de un libro: permite encontrar un correo rápido, sin leer toda la tabla. Y la fecha de creación se llena sola con la hora del momento.

[Acción: líneas 17 y 18: la relación]

La relación de la línea 17 conecta cada usuario con sus análisis, y los ordena del más nuevo al más viejo. Es lo que usa la pantalla de Mis análisis, que lista los análisis de cada persona.

[Acción: señala la clase Analisis, línea 27, y la propiedad resultados]

Analisis. Dice de quién es, con una llave foránea, que es una columna que apunta a la llave de otra tabla, aquí la del usuario. También cuándo se hizo, el nombre del PDF y los resultados. Y aquí hay una decisión de diseño. Los resultados completos, con la lista de imágenes, sus contornos y sus medidas, se guardan en una sola columna de texto, en formato JSON. JSON es una forma de escribir datos como texto, con listas y diccionarios, que se puede guardar y volver a leer sin perder nada. La propiedad de la línea 37 hace esa lectura: convierte el texto otra vez en un diccionario de Python.

¿Por qué así? Porque lo que importa es volver a mostrar el análisis igual que al hacerlo, y su forma cambia según las imágenes que haya. La contrapartida es que no se pueden hacer consultas con SQL sobre cada medida. Para este proyecto no hace falta.

[Acción: señala la clase Mensaje, línea 45]

Y Mensaje guarda lo que llega por el formulario de contacto.

[Acción: explorador de archivos, carpeta instance]

En la carpeta instance están la base de datos y las tres carpetas de trabajo: pdfs, marcadas y subidas. En el servidor, toda la carpeta es un volumen de Docker, que es un espacio de almacenamiento que sobrevive aunque se reconstruya el sitio. Así, actualizar el programa no borra los datos.

[Pantalla 9 · La ruta analizar]

> Idea central: La ruta analizar valida antes de trabajar: que haya imágenes, que no pasen de diez y que la extensión sea permitida. Guarda cada imagen con un nombre generado, la analiza y la borra en un bloque finally, pase lo que pase.

> En pantalla: Editor, `app/analisis/rutas.py`: la ruta `analizar` (líneas 33 a 63), con las validaciones (39 a 49), el nombre con `uuid` (51 a 56) y el `try/finally` (58 a 61); después `analizar_prueba` (66 a 73).

[Acción: rutas.py, ruta analizar, líneas 33 a 37]

Llegamos a la ruta que hace el trabajo. Es solo POST, y lleva login required. La línea 36 toma los archivos del campo imagenes, request.files, y se queda solo con los que traen nombre. La 37 lee el máximo de la configuración.

[Acción: líneas 39 a 49: las validaciones]

Antes de hacer nada, se valida. Que haya al menos una imagen. Que no pasen del máximo de diez. Y que todas tengan una extensión permitida: BMP, PNG, TIFF o JPG. Si algo falla, flash deja un aviso, y redirect regresa a la página de análisis.

Y hay que decirlo claro. La comprobación mira el nombre del archivo, no su contenido. Si alguien sube un texto con extensión PNG, pasa esta validación. Es la función de medición la que descubre que no se puede abrir como imagen, y avisa.

[Acción: líneas 51 a 56: el nombre generado]

Después, un detalle de seguridad. En el disco, cada imagen se guarda con un nombre generado: un identificador aleatorio de la biblioteca uuid, el número de la imagen y la extensión. El nombre que puso la persona no se usa para guardar. Solo para mostrar. Así nadie puede colar un nombre con rutas raras ni pisar el archivo de otro.

[Acción: líneas 57 a 61: guardar, analizar y borrar]

La línea 57 guarda la imagen. Y luego viene algo que importa para la privacidad: las imágenes no se conservan. Cada una se analiza dentro de un bloque try, y se borra en el finally. Un try y finally funciona así. El try intenta hacer algo, y el finally se ejecuta siempre, pase lo que pase. Si el análisis termina bien, se borra la imagen. Si falla, también. Así no queda ninguna imagen subida en el servidor.

[Acción: líneas 66 a 73: analizar_prueba]

La ruta de la imagen de ejemplo hace lo mismo, pero con un archivo que ya está en el sitio, en la carpeta static. Reutiliza la misma función de análisis. Ahí se ve el beneficio de separar las piezas.

[Pantalla 10 · Guardar y mostrar]

> Idea central: Con la lista de imágenes analizadas, _guardar_y_mostrar arma el diccionario de resultados, lo guarda como JSON, genera el PDF y redirige a la página de resultados. Responder con una redirección evita que recargar la página repita el análisis.

> En pantalla: Editor, `app/analisis/rutas.py`, función `_guardar_y_mostrar` (líneas 81 a 103); señala el diccionario (83 a 90), el guardado (91 a 93), el PDF (96 a 101) y la redirección (103). Después, navegador: recarga la página de resultados con F5.

[Acción: rutas.py, _guardar_y_mostrar, línea 81]

Con las imágenes ya analizadas, entra _guardar_y_mostrar. El guion bajo del inicio es una costumbre de Python. Indica que es una función de uso interno de este archivo.

[Acción: líneas 82 a 90: el diccionario]

Primero arma el diccionario de resultados, que es una colección de datos con nombre. Lleva la lista de imágenes y el promedio entre ellas. Y dos banderas. Una dice si el análisis fue provisional, porque faltaban los modelos y se usó la detección por color. La otra dice si se hizo con el modelo, que el sitio llama preliminar. De eso depende qué avisos muestra la página.

[Acción: líneas 91 a 93]

Segundo, lo guarda. Crea un registro de Analisis con el número de la persona y el diccionario convertido a texto JSON, con json dumps. Y lo confirma con commit. Al confirmar, la base le asigna su número.

[Acción: líneas 96 a 101]

Tercero, el PDF. Se genera con ese número, se guarda en la carpeta de PDF con el nombre analisis, el número y la extensión, y se anota el nombre en el registro, con un segundo commit.

[Acción: línea 103]

Y por último, no devuelve la página. Devuelve una redirección a la ruta de resultados. Es lo que vimos en la pestaña de red: un POST con respuesta 302, y luego un GET. Es un patrón muy usado, y tiene una razón práctica.

[Acción: navegador: recarga la página de resultados con F5]

Si la respuesta al POST fuera la página, al recargarla el navegador preguntaría si quieres reenviar el formulario. Y reenviar significaría analizar otra vez. Como la página es el resultado de un GET, recargar la muestra de nuevo, sin repetir el trabajo.

Hay una consecuencia que se nota. El análisis se hace dentro de la misma petición, y el navegador espera. Por eso el sitio muestra una cubierta de espera mientras se analiza, que veremos en el último video, y por eso el tiempo máximo es tan alto. No hay una cola de tareas aparte, que sería un programa que recibe los trabajos y los hace uno por uno por detrás. Es una decisión de simplicidad, y la vemos al final.

[Pantalla 11 · Cada quien ve lo suyo]

> Idea central: Cada análisis es de una persona: si no existe o es de otra, la respuesta es 404 y no 403, para no revelar que existe. Las imágenes marcadas solo se sirven si su nombre aparece en los resultados de ese análisis.

> En pantalla: Editor, `app/analisis/rutas.py`: `_analisis_propio` (líneas 106 a 111) e `imagen_marcada` (122 a 129). Después, navegador: cambia el número del análisis en la dirección por el de otra cuenta de prueba, o por uno que no exista.

[Acción: rutas.py, _analisis_propio, línea 106]

Todas las rutas que muestran o descargan un análisis empiezan igual, con una función corta: _analisis_propio. Busca el análisis por su número. Si no existe, o si es de otra persona, responde 404, con la función abort.

[Acción: navegador: cambia el número del análisis en la dirección por uno de otra cuenta o que no exista]

Fíjate en el código: 404, no 403. Un 403 quiere decir prohibido, y diría que ese análisis existe, pero que no es tuyo. Un 404 dice lo mismo en los dos casos: aquí no hay nada. Así nadie puede recorrer los números para averiguar cuántos análisis hay.

[Acción: editor, rutas.py, líneas 122 a 129]

Lo mismo con las imágenes marcadas. La ruta recibe el nombre del archivo, pero antes arma el conjunto de nombres permitidos: las dos copias marcadas de cada imagen de ese análisis. Si el nombre pedido no está en ese conjunto, 404. Y para servir el archivo usa send from directory, que además impide salirse de la carpeta con rutas como punto punto diagonal. Es un truco para llegar a archivos que no deberían verse.

Es una regla de oro: nunca confiar en lo que llega en la dirección. Siempre se verifica de quién es y qué se pidió.

[Pantalla 12 · CSV y PDF]

> Idea central: reportes.py genera el CSV al momento, con una fila por espermatozoide y una marca para que Excel lea los acentos, y el PDF al terminar el análisis, con fpdf2 y gráficas de matplotlib dibujadas sin ventana. Las fuentes básicas del PDF solo aceptan latin-1.

> En pantalla: Editor, `app/analisis/reportes.py`: `generar_csv` (líneas 18 a 28), el modo sin ventana de matplotlib (8), `_texto` (31 a 33), `_grafica_barras` (36 a 50) y `generar_pdf` (87 a 131); después las rutas `descargar_csv` y `descargar_pdf` en `rutas.py` (132 a 150).

[Acción: abre reportes.py, generar_csv, línea 18]

Los reportes están en el archivo reportes.py. El CSV es la pieza más simple. CSV quiere decir valores separados por comas. Es un texto en el que cada fila es una línea y las columnas se separan con comas, y se abre en cualquier hoja de cálculo. Aquí se escribe en memoria, con el módulo csv de Python: una fila de encabezados y una fila por espermatozoide. Imagen, número, área y largo en píxeles, y área y largo en micras.

[Acción: línea 28: la marca de orden de bytes]

Hay un detalle en la última línea. Antes del texto se agrega un carácter invisible, la marca de orden de bytes, que en inglés se llama BOM. Sirve para que Excel abra el archivo con la codificación correcta, y los acentos no salgan rotos.

El CSV no se guarda. Se genera cada vez que alguien lo descarga, a partir de los resultados guardados. Y la respuesta lleva una cabecera que le dice al navegador que es una descarga, no una página.

[Acción: línea 8 y líneas 36 a 50]

El PDF es otra cosa. Se genera una vez, al terminar el análisis. Usa fpdf2, y las gráficas las dibuja matplotlib. Fíjate en la línea 8. El modo Agg le dice a matplotlib que dibuje sin ventana, porque el servidor no tiene pantalla. La gráfica se dibuja en memoria como una imagen PNG, y se inserta en la página.

[Acción: líneas 31 a 33: _texto]

Y una limitación que viene de las fuentes básicas del PDF. Solo aceptan el alfabeto latín-1, que es un conjunto de caracteres de las lenguas de Europa occidental. Los acentos, la eñe, la micra y el cuadrado pasan sin problema. Pero cualquier carácter fuera de ese conjunto se cambia por un signo de interrogación. Eso es lo que hace la función _texto.

[Acción: líneas 87 a 131: generar_pdf]

El PDF lleva lo mismo que la pantalla. El usuario, la fecha, la nota de la escala, el aviso rojo si fue provisional, una página por imagen y, si hay varias, la gráfica del promedio.

[Acción: rutas.py, líneas 132 a 150]

En las rutas, el CSV se entrega como respuesta en el momento, y el PDF se lee de la carpeta con send from directory. Los dos exigen sesión, y los dos pasan por la comprobación de que el análisis sea tuyo.

[Pantalla 13 · Un proceso, cuatro hilos y las pruebas]

> Idea central: Gunicorn corre con un proceso y cuatro hilos, para que los modelos se carguen una sola vez, y con tiempo máximo de 1,800 segundos, igual que Nginx. Las pruebas con pytest recorren el flujo completo sin los modelos, y comprueban que el sitio funcione, no que el conteo sea científicamente correcto.

> En pantalla: Editor: la última línea de `Dockerfile` (23) y `deploy/nginx.conf`, líneas 41 y 49 a 51; después terminal: `python -m pytest`, y el editor en `tests/test_sistema.py` (líneas 55 a 58, fixture `app` 18 a 30 y análisis completo 82 a 108) y en `tests/test_modelo.py` (línea 59).

[Acción: Dockerfile, línea 23]

Para cerrar, cómo se ejecuta todo y cómo se prueba. El Dockerfile es la receta con la que se arma el contenedor del sitio. Su última línea es la orden con la que arranca: Gunicorn, con un worker y cuatro hilos. Un worker es un proceso, un programa en marcha. Un hilo es una línea de trabajo dentro de ese proceso.

¿Por qué solo un proceso? Porque cada modelo ocupa unos 176 megabytes en memoria, y varios procesos los duplicarían. Con uno solo, los modelos se cargan una vez. Y los cuatro hilos permiten que el resto del sitio siga respondiendo mientras un análisis usa el procesador.

El tiempo máximo, que en la orden se llama timeout, es de 1,800 segundos. Media hora. Porque analizar diez imágenes grandes con los modelos puede tardar varios minutos.

[Acción: nginx.conf, líneas 41 y 49 a 51]

Nginx tiene los mismos números. Una espera máxima de 1,800 segundos y un límite de 300 megabytes por envío, igual que Flask. Si uno de los tres fuera menor, cortaría el análisis antes que los demás.

Esto es una decisión de simplicidad, y sus límites son claros. No hay una cola de tareas. Mientras un análisis corre, otro tiene que esperar su turno, y la persona ve la cubierta de espera. Con pocas personas a la vez, funciona. Si el uso creciera mucho, el siguiente paso sería sacar el análisis a una cola, con procesos aparte.

[Acción: terminal: python -m pytest. Lee el resultado de ese día]

Y las pruebas. Una prueba automática es una función que ejecuta una parte del sitio y comprueba que haga lo esperado. Así, cada cambio se puede verificar en segundos. Con la orden python -m pytest se ejecutan todas. Este es el resultado de hoy.

[Acción: tests/test_sistema.py, líneas 55 a 58: una prueba sencilla]

Veamos una. Se llama prueba analizar requiere sesión. Usa un cliente de pruebas, que simula un navegador sin abrir uno. Manda un POST a analizar sin haber iniciado sesión. Y afirma, con assert, dos cosas: que la respuesta sea un 302, una redirección, y que lleve a la pantalla de entrar. Si el código cambiara y dejara pasar a alguien sin cuenta, esta prueba fallaría.

[Acción: tests/test_sistema.py, fixture app, líneas 18 a 30]

Antes de cada prueba, pytest ejecuta una preparación que se llama fixture. Esta crea la aplicación. Usa crear app con una configuración especial: una base de datos y carpetas temporales, para no tocar las reales, y sin protección de formularios, porque no hay navegador que reciba el token. Y la línea de arriba le dice que los modelos no existen. Así el análisis usa la detección provisional, rápida y sin PyTorch.

[Acción: tests/test_sistema.py, líneas 82 a 108: el análisis completo]

Con esa base, hay pruebas más grandes. Una registra una cuenta, sube dos imágenes, abre los resultados y descarga el CSV y el PDF. Otras comprueban lo que no debe pasar. Que un análisis ajeno dé 404. Que un formato no permitido se rechace. Que más de diez imágenes se rechacen. Que una redirección a otro sitio se bloquee. Y que el enlace de recuperación solo sirva una vez.

[Acción: tests/test_modelo.py, línea 59]

Y hay que decir lo que no comprueban. No dicen si el conteo es correcto, ni si la medición es buena. Comprueban que el sitio usa bien lo que le entrega el modelo. La prueba con los modelos reales existe, pero solo corre si se pide con una variable y si los archivos están. La calidad científica se evalúa aparte, con las imágenes anotadas, y es parte del trabajo con el cliente.

[Pantalla 14 · Lo que vimos y lo que sigue]

> Idea central: Vimos el camino de una imagen por el backend: Flask y sus extensiones, la aplicación, las rutas, las cuentas con sus protecciones, la base de datos, el análisis, los reportes y cómo se ejecuta y se prueba. En el siguiente video, el modelo: cómo se le da una foto y cómo se recogen sus respuestas.

> En pantalla: Vuelve al navegador, en la página de resultados del ejemplo, mientras das el resumen y te despides.

[Acción: vuelve al navegador, en la página de resultados]

Un resumen.

Vimos el camino que sigue una imagen. Nginx recibe la petición, Gunicorn la pasa a Flask, y Flask la dirige a una función según la dirección. Vimos cómo se crea la aplicación con una función fábrica, y cómo se organizan sus 19 rutas en tres secciones.

Vimos las protecciones. Las contraseñas se guardan como huella, que no se puede deshacer. El error de inicio de sesión no revela nada. Los formularios llevan un token contra la falsificación de peticiones entre sitios. El enlace de recuperación se firma, dura una hora y se vuelve inútil al cambiar la contraseña. Cada persona ve solo lo suyo, y todo lo que llega en la dirección se verifica.

Vimos la base de datos con sus tres tablas. La ruta de análisis, que valida, guarda con un nombre generado y borra la imagen siempre. Y los reportes en CSV y PDF. Y vimos cómo corre todo en el servidor, y qué comprueban las pruebas y qué no.

En el siguiente video entramos al modelo. En esta ruta, analizar le entrega la imagen a una función y recibe contornos. Qué pasa dentro de esa función, cómo se prepara la foto, cómo se corta en recortes y cómo se recogen las respuestas de la red, es el tema del siguiente video. Gracias por acompañarme.
