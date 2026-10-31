# Guion del módulo 4, video 3 de 4: Despliegue en la nube

BioImage-Repro UAM · Módulo 4 · Capacitación en video

Se graba con la pantalla: la terminal, el editor y el navegador se muestran mientras hablas, sin mazo. Continúa del video anterior. Empieza con la frase que lo une con el video 2 del módulo.

*3,434 palabras, unos 19.6 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se escribe un comando o se abre un archivo. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- Una terminal en la computadora y otra con la sesión abierta en el servidor, para no perder tiempo en el video.
- Los archivos `Dockerfile`, `docker-compose.yml` y `docker-compose.override.yml` abiertos en el editor, con números de línea.
- Cubrir la dirección IP del servidor, el usuario, la clave privada y el contenido del archivo `.env` en todo momento. No se muestra nunca el resultado de `docker compose config`: imprime los valores del `.env`.
- El panel de Hostinger abierto en la vista general del VPS, con la dirección IP cubierta: aparece junto al usuario, en el comando de acceso y en «Detalles del VPS». No pulsar «Reiniciar», «Restablecer contraseña», «Restablecer» de los respaldos, «Crear snapshot» ni «Mejorar plan». El nombre del servidor y el correo de la cuenta tampoco hace falta enseñarlos.
- Para la demostración de la clave SSH se usa una clave nueva, de práctica, que se borra al terminar. Nunca la clave de uso real.

[Pantalla 1 · Un servidor que siempre está encendido]

> Idea central: Un modelo y un sitio no sirven de nada si solo corren en tu computadora, que se apaga. Un VPS es una computadora que se renta a un proveedor, con una dirección pública y siempre encendida. En ella corre el sitio, que solo analiza fotos con el procesador y no necesita tarjeta gráfica.

> En pantalla: El panel del proveedor del VPS, con la dirección IP cubierta.

[Acción: abre el panel del proveedor del VPS; cubre la dirección IP]

El video anterior terminó con un archivo que es el modelo exportado de unos 176 megabytes. Pero un archivo no atiende a nadie. Para que una persona suba una foto y reciba sus resultados el sitio tiene que estar corriendo a todas horas en una computadora a la que cualquiera pueda llegar. La tuya no sirve para eso porque se apaga y cambia de red y no tiene una dirección fija en internet.

Para eso existe un VPS que es un servidor privado virtual. Es una computadora o más exactamente una porción de una que se renta a un proveedor. Está siempre encendida y tiene una dirección pública que es la IP y se maneja a distancia. El sitio de este proyecto vive en uno de Hostinger con Ubuntu que es una versión de Linux.

Hay algo que explica por qué basta un servidor modesto. En el servidor no se entrena nada. Eso se hizo en Colab. El servidor solo hace inferencia. Es decir recibe una foto y la pasa por el modelo y devuelve contornos. Y lo hace con el procesador sin tarjeta gráfica.

[Pantalla 2 · El panel de Hostinger]

> Idea central: El panel del proveedor resume el servidor: el sistema, el plan, el uso de recursos y los datos de acceso. Desde ahí se ven el usuario y el comando para entrar, se administran las claves SSH, se revisan el firewall y los respaldos y hay una terminal de emergencia en el navegador.

> En pantalla: El panel de Hostinger en la vista general del VPS: la cabecera, las métricas, los datos de acceso y las tarjetas. Después «Snapshots y respaldos» y el botón «Consola web». La dirección IP, cubierta.

[Acción: señala la cabecera de la vista general y baja a «Detalles del VPS» y «Detalles del plan»]

Esto es el panel de Hostinger en la vista general del servidor de este proyecto. Arriba aparecen el sistema instalado que es Ubuntu 26.04 y el plan que es KVM 1 y el estado que dice funcionando. KVM 1 es el plan más pequeño y ofrece un núcleo de procesador con 4 gigas de memoria y 50 gigas de disco y 4 terabytes de ancho de banda al mes. El centro de datos está en Boston en Estados Unidos. Más abajo el plan indica que la renovación automática está activada y por eso el servidor no se apaga por olvido.

[Acción: señala las métricas: uso de CPU, memoria, disco, tráfico y ancho de banda]

Debajo están las métricas. El procesador va en 1 por ciento y la memoria en 36 por ciento y el disco usa 8 de los 50 gigas. También se ven el tráfico entrante y el saliente y lo que se ha gastado del ancho de banda. Es lo primero que se mira cuando el sitio va lento o no responde. Son valores de este momento y cambian.

[Acción: señala los datos de acceso: usuario, IP y el comando ssh; cubre la IP]

Arriba están los datos para entrar al servidor. El usuario SSH es root que es el administrador de todo. Luego aparece la dirección IP que se cubre en el video. Y debajo está el comando completo que es ssh root arroba la IP con un icono para copiarlo. Es el comando que usaremos en un momento. Como root puede hacerlo todo conviene entrar con una clave SSH y cuidarla. También hay un botón para restablecer la contraseña de root si se olvida y no lo vamos a tocar.

[Acción: señala las tarjetas: Clave SSH, Reglas del firewall, Snapshots y respaldos y Escáner de malware]

Más abajo hay cuatro tarjetas con accesos directos. La de Clave SSH la veremos en la siguiente parte del video. Reglas del firewall marca cero porque en el panel del proveedor no hay ningún firewall creado para este servidor. Eso no dice si hay otro dentro del servidor y por eso lo comprobaremos desde fuera en el siguiente video. Snapshots y respaldos marca uno que es el respaldo semanal automático. Y el escáner de malware figura como no instalado.

[Acción: abre «Respaldos y monitoreo» y entra a «Snapshots y respaldos»]

En Snapshots y respaldos hay dos cosas distintas. La primera es el respaldo automático que hoy está programado cada semana y guarda una copia de todo el servidor. La lista muestra la fecha y el tamaño y el tiempo que tardaría en restaurarse que son unos 30 minutos. El botón restablecer devuelve todo el servidor a ese punto y por eso no se pulsa a la ligera. La segunda es la snapshot que es una captura del estado actual y la creas tú cuando quieres un punto de restauración. Por ejemplo antes de un cambio grande. Aquí no hay ninguna snapshot manual. Los respaldos se guardan aparte del servidor y los más viejos se reemplazan solos. Más adelante veremos también el respaldo de los datos del sitio que es el que hacemos nosotros.

[Acción: señala el botón «Consola web», arriba a la derecha]

Arriba a la derecha está el botón Consola web. Abre una terminal del servidor dentro del navegador sin instalar nada. Sirve para emergencias como cuando se pierde la clave o la conexión SSH no entra. Para trabajar de verdad se usa SSH desde tu computadora y eso es lo que sigue.

El trabajo de hoy tiene cuatro partes. Conectarnos al servidor de forma segura y prepararlo. Entender cómo se empaqueta el sitio con Docker. Y levantarlo. En el siguiente video le ponemos nombre y candado.

[Pantalla 3 · La clave SSH]

> Idea central: SSH es la forma segura de manejar un servidor a distancia. Se entra con un par de claves: la pública se deja en el servidor y la privada no sale nunca de tu computadora. Conviene una clave por uso, para poder retirar una sin afectar a las demás.

> En pantalla: Terminal en la computadora: `ssh-keygen`, los dos archivos de la clave, y después la conexión con `ssh`. El panel del proveedor, con la tarjeta de claves SSH.

[Acción: terminal: ssh-keygen, crea la clave de demostración]

Para entrar al servidor se usa SSH que es un programa que abre una terminal en la computadora de otro con la conexión cifrada. Se podría entrar con una contraseña pero es más seguro usar un par de claves.

Una clave es un archivo y el par son dos. La clave privada se queda en tu computadora y no sale de ahí nunca. La clave pública se deja en el servidor. Se parecen a una llave y un candado. El candado que es la pública se le puede dar a cualquiera y la llave que es la privada no. Cuando te conectas el servidor comprueba con matemáticas que tienes la llave que abre ese candado y la llave nunca viaja por la red.

Voy a crear un par de práctica. El comando es ssh-keygen con el tipo ed25519 que es el que se recomienda hoy y un comentario que dice para qué es la clave. Esta es solo para el video y la borraré al terminar.

[Acción: muestra los dos archivos de la clave y la primera parte de la pública]

Aparecen dos archivos. El que no tiene extensión es la clave privada y mide unos 400 bytes. El que termina en pub es la pública y mide menos de cien. Fíjate en cómo empieza la pública. Trae el tipo de clave y una cadena larga de letras y números y al final el comentario. Esa línea sí se puede compartir. Si por descuido compartieras la otra quien la tenga entraría a tu servidor y habría que borrar la clave y generar otra.

Una práctica útil es tener una clave por uso. Una para tu computadora de trabajo y otra para la de un compañero y otra para una automatización. Así si una se pierde o alguien deja el proyecto se retira solo esa y las demás no se tocan.

[Acción: abre el panel del proveedor, tarjeta «Clave SSH», «Administrar», y pega la clave pública]

La clave pública se registra en el servidor. En el panel se hace desde la tarjeta Clave SSH y su botón Administrar. Ahí aparece la lista de claves y el botón más Clave SSH que abre un formulario. Pide un solo dato que es el contenido de la clave y es un cuadro de texto donde se pega la línea completa de la pública. Luego se guarda con el botón Guardar. El panel incluso explica cómo generarla. Hay dos detalles. La lista pertenece a tu cuenta de Hostinger y no solo a este servidor y la propia pantalla pide eliminar las claves que no reconozcas. También puede hacerse a mano agregándola al archivo de claves autorizadas del servidor. De cualquier forma lo que se pega es siempre la pública.

[Acción: terminal: ssh root@IP, entra al servidor; cubre la IP]

Y ya podemos entrar. El comando es el que mostraba el panel que es ssh y luego root y una arroba y la dirección IP. El usuario es root porque es el que trae el servidor. La primera vez SSH pregunta si confías en la huella del servidor. Es una comprobación para saber que te conectas al servidor correcto y se contesta que sí una sola vez.

Observa que cambia la línea de comandos. Ya no es la de tu computadora. Todo lo que escribas desde aquí se ejecuta en el servidor.

[Pantalla 4 · Preparar el servidor]

> Idea central: En un servidor nuevo se hacen tres cosas, una sola vez: instalar Docker, bajar el código con Git y crear el archivo `.env` con la clave secreta del sitio. Ese archivo no va a Git ni a la imagen, porque guarda secretos.

> En pantalla: Terminal en el servidor: la instalación de Docker, `git clone`, y la creación del archivo `.env` sin mostrar su contenido.

[Acción: terminal en el servidor: instala Docker con la línea de get.docker.com]

Estamos dentro de un servidor vacío y lo primero es Docker. Se instala con una sola línea que descarga un script de la página oficial de Docker y lo ejecuta. Instala Docker y también Compose que es el plugin con el que levantaremos varios contenedores juntos.

Una advertencia honesta. Descargar un script de internet y ejecutarlo con permisos de administrador es cómodo pero es dar confianza. Aquí es el método que recomienda la propia Docker. Con otro programa conviene leer el script antes.

[Acción: git clone del repositorio y entra a la carpeta]

Después va el código. Se clona el repositorio con Git y se entra a la carpeta. Eso baja el código del sitio y los archivos de Docker y de Nginx. Lo que no baja son los modelos ni los secretos porque no están en Git. Los modelos pesan demasiado y los secretos no se suben a ningún repositorio.

[Acción: crea el archivo .env con SECRET_KEY, sin mostrar su contenido]

Falta el archivo de los secretos que se llama punto env. Esta línea lo crea con una sola variable que es la clave secreta del sitio. Sale de un comando de OpenSSL que genera 32 bytes al azar y los escribe como 64 caracteres.

¿Para qué sirve? Flask la usa para firmar. Firma la sesión que es la cookie que te mantiene conectado. Y firma también los enlaces de recuperación de contraseña para que nadie pueda fabricar uno. Si la clave se filtrara alguien podría hacerse pasar por otra persona. Por eso se genera en el servidor y es distinta de la de tu computadora y no se escribe en ningún lugar visible.

Fíjate en el signo. Esta primera línea usa un solo mayor que y eso crea el archivo o lo reemplaza.

[Acción: agrega NGINX_CONF=nginx-http.conf al .env]

La segunda línea agrega una variable más y usa dos signos mayor que que añaden al final sin borrar lo que había. Dice qué configuración de Nginx se va a usar. En un servidor nuevo todavía sin certificado se usa la versión de solo HTTP. Cuando haya certificado se quita esta línea y eso es la mitad del siguiente video.

El archivo punto env no se sube a Git porque está en la lista de archivos ignorados. Tampoco entra a la imagen de Docker porque está en la lista de ignorados de Docker.

[Pantalla 5 · Docker en tres ideas, y el Dockerfile]

> Idea central: Docker empaqueta el sitio con todo lo que necesita para correr igual en cualquier computadora. Son tres ideas: la imagen es la receta, el contenedor es el programa corriendo y el volumen es donde viven los datos, para que reconstruir no los borre. El Dockerfile es la receta de la imagen del sitio.

> En pantalla: El editor con el `Dockerfile`, de arriba abajo.

[Acción: abre el Dockerfile, líneas 1 a 12: la base y las dependencias]

Ahora Docker que se entiende con tres ideas.

La imagen es una receta ya cocinada. Es un paquete con Linux y Python y las bibliotecas y el código del sitio todo junto. Un contenedor es esa imagen corriendo. Es un programa vivo y aislado del resto del servidor y de una imagen se pueden levantar muchos contenedores. Y un volumen es un lugar donde viven los datos fuera del contenedor. Un contenedor se puede borrar y volver a crear mientras que los datos en un volumen se quedan.

Todo eso se define en un archivo de 23 líneas que es el Dockerfile. Es la receta de la imagen.

La primera línea dice de dónde se parte. De Python 3.12 en su versión slim que es una variante mínima. Las dos variables de entorno que siguen tienen un motivo cada una. Una hace que los mensajes del programa aparezcan al momento en los registros. La otra pide que pip no guarde su caché para que la imagen pese menos. Después viene la carpeta de trabajo dentro de la imagen.

Ahora un detalle importante que es el orden. Primero se copian solo los archivos de requisitos y se instalan las dependencias. El código se copia después. ¿Por qué? Docker guarda cada paso como una capa y la reutiliza si nada cambió. Si cambia el código pero no los requisitos la instalación que es lo más lento no se repite.

La línea 9 hace dos instalaciones. Primero las bibliotecas normales y luego PyTorch desde el índice de versiones para procesador sin tarjeta gráfica. Eso es lo que agranda la imagen. Según el propio proyecto crece alrededor de un gigabyte.

Luego se copian la carpeta del sitio y el archivo de arranque. Fíjate en lo que no se copia. Pruebas y documentos y scripts y modelos. Un archivo aparte llamado punto dockerignore los deja fuera igual que al punto env.

[Acción: líneas 14 a 17: el volumen y el puerto]

Las líneas 14 y 15 declaran un volumen en la carpeta instance donde viven la base de datos y los PDF y las imágenes marcadas. Todo lo que el sitio guarde ahí sobrevive cuando se reconstruye la imagen.

La línea 17 dice que el programa escucha en el puerto 8000. Ojo. Eso solo documenta y no abre nada hacia afuera. De eso se encarga Compose en un momento.

[Acción: líneas 19 a 23: Gunicorn]

Y la orden de arranque. Gunicorn es el servidor que ejecuta de verdad el sitio de Flask con varios hilos. Escucha en todas las direcciones del contenedor en el puerto 8000 con un solo proceso y cuatro hilos. Lo explican los comentarios. Los modelos son de cientos de megabytes y con un solo proceso se cargan una vez. Los análisis esperan turno porque solo uno usa el procesador a la vez. Y los hilos permiten que el resto del sitio siga respondiendo mientras tanto.

Hay además un tiempo de espera de 1,800 segundos que son media hora. Analizar diez imágenes grandes con los modelos puede tardar varios minutos. Es el mismo número que veremos en Nginx. Si uno de los dos fuera menor cortaría el análisis a medias.

La última parte entre comillas le dice a Gunicorn de dónde sacar la aplicación. Es la función que crea el sitio.

[Pantalla 6 · Docker Compose]

> Idea central: Compose es un archivo que describe varios contenedores y los levanta juntos con un comando. Aquí son dos: web, el sitio, y nginx, la puerta de entrada. El archivo define la configuración que llega del `.env`, los volúmenes con nombre, los modelos montados en solo lectura y qué puertos se abren hacia afuera. Un segundo archivo, para desarrollo, abre además el puerto 8000.

> En pantalla: El editor con `docker-compose.yml`, de arriba abajo; después la terminal, y por último `docker-compose.override.yml`.

[Acción: abre docker-compose.yml, líneas 1 a 12: el servicio web y su configuración]

La receta produce una imagen pero el sitio necesita más. Necesita configuración y datos y los modelos y una puerta hacia afuera. Para describir todo eso y levantar los contenedores juntos está Compose. Es un archivo de 43 líneas con dos servicios.

El primero es web que es el sitio. Se construye con el Dockerfile de esta carpeta. La línea reiniciar a menos que se detenga significa que si el programa se cae o el servidor se reinicia Docker lo vuelve a levantar solo salvo que tú lo hayas parado.

Luego están las variables de entorno. La primera que es la clave secreta usa una sintaxis que merece atención porque lleva un signo de interrogación. Significa que la variable es obligatoria y si falta Compose se niega a arrancar y muestra el mensaje que sigue. Así nadie levanta el sitio sin clave por descuido.

Siguen el lugar de los modelos dentro del contenedor y el número de hilos de PyTorch. Si no se define usa hasta cuatro según los procesadores del servidor. Y sigue una variable para que las bibliotecas de álgebra no usen varios hilos a la vez.

[Acción: líneas 14 a 23: el correo, los volúmenes y los modelos]

Hay una variable que solo sirve en desarrollo que es el temporizador de la pantalla de espera. Con la sintaxis de dos puntos y guion queda vacía si no está definida y en el servidor se deja sin definir.

Vienen luego cinco variables del correo con las que el sitio envía el mensaje de recuperación de contraseña. También salen del archivo punto env y si no se definen quedan vacías.

Ahora los volúmenes del servicio. El primero llamado datos es un volumen con nombre que se monta en la carpeta instance. Ahí está la base de datos que no se pierde cuando la imagen se reconstruye. El segundo es la carpeta model del proyecto montada en solo lectura. Son los modelos que copiaremos a mano. Que sea solo lectura quiere decir que el sitio puede leerlos pero no modificarlos. Como es una carpeta montada cambiar un modelo por otro no obliga a reconstruir la imagen. Se copia el archivo y se reinicia el servicio.

[Acción: líneas 25 a 43: Nginx y los volúmenes con nombre]

El segundo servicio es nginx que es la puerta de entrada. Usa una imagen oficial ya hecha en su versión alpine que es pequeña. Espera a que web esté listo. Y es el único que publica puertos hacia afuera. El 80 para HTTP y el 443 para HTTPS. El servicio web no publica ninguno así que solo se llega a él a través de Nginx por dentro de la red de Compose.

Su configuración se monta desde la carpeta deploy y el nombre del archivo sale de la variable que pusimos en el punto env. Si no está definida se usa la versión con HTTPS. Por eso en un servidor nuevo la ponemos en solo HTTP. Monta además dos volúmenes del certificado en solo lectura que veremos en el siguiente video.

Abajo están los tres volúmenes con nombre. Los datos y los dos del certificado. Docker los crea y los conserva aparte del código.

[Acción: terminal: docker compose config sin SECRET_KEY: el error]

Una prueba de lo de la clave obligatoria. Si le pido a Compose que revise el archivo sin que la clave exista se niega y el mensaje es el que escribimos. La orden config sirve para comprobar el archivo sin levantar nada. Pero ojo. Cuando la clave sí existe imprime todos los valores ya resueltos y eso incluye las contraseñas del punto env. Por eso esa salida no se muestra ni se pega en ningún chat.

[Acción: abre docker-compose.override.yml]

Hay un archivo más de cuatro líneas que es el override. Compose lo suma solo sin que se lo pidas y lo que hace es abrir el puerto 8000 del sitio hacia afuera. Sirve en tu computadora donde levantas y abres el puerto 8000 en el navegador sin pasar por Nginx.

Y aquí hay un cuidado. Ese archivo está en el repositorio y por eso también se baja al servidor y Compose lo suma ahí igualmente. En el servidor todo debería entrar por Nginx con HTTPS. Que el puerto 8000 quedara abierto a todo internet sería una puerta lateral. Conviene comprobar desde fuera del servidor que ese puerto no responda.

[Pantalla 7 · Levantar el sitio]

> Idea central: Se copian los modelos al servidor con `scp`, se levantan los contenedores con `docker compose up -d --build`, y se comprueba con `ps` que los dos estén corriendo y con `logs` que no haya errores. El sitio responde ya por la dirección IP.

> En pantalla: Terminal en la computadora para copiar los modelos; terminal en el servidor para levantar y comprobar; el navegador con la dirección IP.

[Acción: terminal en la computadora: scp de los dos modelos]

Falta lo que no está en Git que son los modelos. Se copian con scp que es copiar por SSH. Desde tu computadora se escribe el comando y los dos archivos y el destino. El destino es el usuario y la IP y la carpeta model del proyecto en el servidor. Cada archivo pesa unos 176 megabytes y por eso tarda un poco según tu conexión.

Si faltaran nada se rompe. El sitio arranca igual y usa la detección provisional por umbral de color y lo avisa en los resultados. Aun así conviene que estén antes de levantar.

[Acción: terminal en el servidor: docker compose up -d --build]

Ahora sí en el servidor. Docker compose up con dos opciones. La d significa en segundo plano para que no te deje la terminal ocupada y build pide que se construya la imagen. La primera vez tarda varios minutos porque baja Python e instala las bibliotecas y PyTorch. Las siguientes con las capas guardadas es mucho más rápido.

[Acción: docker compose ps]

Para comprobar docker compose ps muestra los dos servicios y su estado. Los dos deben decir que están corriendo y si alguno aparece reiniciándose algo falla.

[Acción: docker compose logs -f web; Ctrl+C para salir]

Y para ver por qué están los registros. Logs con la opción f va mostrando en tiempo real lo que escribe el sitio y es lo primero que se mira cuando algo no funciona. Con Control C se sale de los registros y los contenedores siguen corriendo.

[Acción: navegador: http://IP del servidor; cubre la IP]

Y la prueba final. En un navegador desde cualquier computadora se escribe la dirección IP del servidor y el sitio responde. Ahí está el mismo sitio que viste funcionar en el módulo 3 ahora corriendo en una computadora que no es la tuya.

[Pantalla 8 · Lo que vimos y lo que sigue]

> Idea central: Hay un servidor al que se entra con una clave, y en él corren dos contenedores definidos por dos archivos: el Dockerfile y el de Compose. Los datos y los modelos viven fuera de la imagen. Falta que el sitio tenga nombre y conexión segura: es el siguiente video.

> En pantalla: Vuelve a la terminal del servidor.

[Acción: vuelve a la terminal del servidor, con el resultado de docker compose ps]

Un repaso. Un servidor al que se entra con una clave pública y una privada. Una instalación que se hace una sola vez. Una imagen definida por una receta de 23 líneas. Dos contenedores definidos por un archivo de 43. Datos en un volumen. Modelos en una carpeta montada. Y secretos en un archivo que no está en Git.

El sitio ya responde pero con una dirección numérica y sin conexión segura y el navegador con razón lo marca como no seguro. En el siguiente video que es el último del curso le ponemos un nombre. Configuramos Nginx para que cifre la conexión con un certificado y cerramos todo el recorrido.

Gracias por acompañarme.
