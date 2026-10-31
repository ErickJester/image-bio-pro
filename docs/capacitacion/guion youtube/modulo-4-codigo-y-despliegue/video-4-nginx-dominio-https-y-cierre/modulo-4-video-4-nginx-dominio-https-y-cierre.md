# Guion del módulo 4, video 4 de 4: Nginx, dominio, HTTPS y cierre

BioImage-Repro UAM · Módulo 4 · Capacitación en video

Se graba con la pantalla: la terminal, el editor y el navegador se muestran mientras hablas, sin mazo. Continúa del video anterior. Empieza con la frase que lo une con el video 3 del módulo.

*2,409 palabras, unos 13.8 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se escribe un comando o se abre un archivo. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- Una terminal en la computadora y otra con la sesión abierta en el servidor. Los archivos `deploy/nginx-http.conf` y `deploy/nginx.conf` abiertos en el editor, con números de línea.
- Cubrir la dirección IP, el usuario, el correo del certificado y el contenido del archivo `.env` en todo momento.
- Para enseñar los registros del dominio, el panel de quien administra el nombre, con la IP cubierta. Para el candado, el navegador con el sitio en HTTPS.
- Para el final, el navegador con las páginas Videos y Contacto del sitio.
- Si se graba la emisión del certificado desde cero, hace falta un servidor y un dominio de prueba, no los de producción: Let's Encrypt limita cuántos certificados da por dominio.

[Pantalla 1 · Qué hace Nginx]

> Idea central: El sitio ya responde por la dirección IP, pero sin nombre y sin candado. Nginx es la puerta de entrada: recibe todas las visitas y se las pasa a Gunicorn. En un servidor nuevo, todavía sin certificado, trabaja con una configuración solo de HTTP.

> En pantalla: El editor con `deploy/nginx-http.conf`, de arriba abajo.

[Acción: abre deploy/nginx-http.conf, líneas 3 a 24, saltando el comentario de arriba]

El video anterior terminó con el sitio funcionando pero con una dirección numérica y un aviso de sitio no seguro. Hoy lo arreglamos. Le ponemos un nombre y le ponemos candado y vemos cómo se actualiza. Y al final cerramos el curso.

Empecemos por Nginx que ya apareció como el segundo contenedor. Es un servidor web y aquí hace de puerta de entrada. Toda visita llega primero a él y él se la pasa a Gunicorn que ejecuta el sitio. A eso se le llama proxy inverso. Tiene sentido separar los dos oficios. Nginx se ocupa de lo que viene de internet como las conexiones y el cifrado que veremos enseguida y Gunicorn se ocupa de ejecutar el sitio.

Este archivo es la configuración de un servidor nuevo de solo HTTP. Es un bloque server que escucha en el puerto 80. Su nombre es un guion bajo que significa cualquier nombre porque todavía no hay dominio.

Dentro hay dos secciones. La primera es el acme challenge y la guardamos para el siguiente tramo porque es la que usa Certbot. La segunda es location barra y es la importante. Manda todo lo demás a web que es el servicio del sitio en el puerto 8000. Ese nombre web es el del servicio en Compose y funciona porque los dos contenedores comparten una red interna.

Junto con la petición se pasan cuatro encabezados. El nombre con el que se pidió el sitio y la dirección del visitante y la cadena de direcciones por las que pasó la petición. Y el protocolo original que es HTTP o HTTPS. Sin ellos el sitio solo vería a Nginx como visitante. Un detalle honesto. El código del sitio todavía no lee el último y por eso el enlace de recuperación de contraseña se arma con el protocolo que ve Flask y no con el original. Es un pendiente.

Al final aparecen dos números que ya conoces. Un límite de 300 megabytes por subida que equivale a diez imágenes sin compresión y 1,800 segundos de espera igual que en Gunicorn.

[Pantalla 2 · El dominio]

> Idea central: Un dominio es un nombre que se traduce en una IP, y eso lo guarda el DNS en registros. Un registro A apunta un nombre a una IP. El nombre con www también necesita su registro, y un CNAME en ese nombre chocaba con el registro A.

> En pantalla: El panel de registros DNS del dominio, con la IP cubierta, y la terminal con `nslookup`.

[Acción: panel del dominio: la lista de registros DNS; cubre la IP]

Toca ponerle nombre. Una dirección de números funciona pero nadie la recuerda y no se puede cifrar con un certificado. Para eso se compra un dominio y este proyecto usa imagebiopro punto cloud.

Un dominio es solo un nombre. Para que lleve al servidor hay que decirle a internet a qué dirección corresponde. Eso lo guarda el DNS que es una especie de agenda mundial y lo guarda en registros. En el panel de quien administra el dominio hay una lista. El que necesitamos se llama registro A y dice que este nombre corresponde a esta dirección. Se crea uno para el dominio apuntando a la IP del servidor.

Queremos además que funcione con www y aquí hubo un error real del proyecto. El nombre con www se había creado como un CNAME que es un registro que dice que un nombre es un alias de otro. Pero un nombre con CNAME no puede tener otros registros y chocaba con el registro A. La solución fue darle a www su propio registro A con la misma dirección.

Después de cambiar registros los cambios tardan un rato en llegar a todos lados. A eso se le llama propagación.

[Acción: terminal: nslookup del dominio y de www]

Para comprobar que ya está se le pregunta a internet. El comando nslookup con el nombre devuelve la dirección que le corresponde. Se hace con el dominio y se repite con www y las dos deben dar la dirección del servidor. Con eso sabemos que el nombre ya lleva al servidor aunque todavía sin candado.

[Pantalla 3 · HTTPS y el certificado]

> Idea central: HTTPS cifra la conexión y comprueba que el sitio es de quien dice. Para eso hace falta un certificado, que Let's Encrypt da gratis cuando se demuestra que el dominio es tuyo. Hay un problema de huevo y gallina: Nginx con HTTPS no arranca sin certificado, y el certificado se pide con Nginx arriba. Por eso hay dos archivos de configuración.

> En pantalla: Terminal en el servidor, con el comando de Certbot; el editor con `deploy/nginx.conf`; y el navegador con el sitio.

[Acción: terminal en el servidor: el comando de Certbot, sin correo real]

HTTPS hace dos cosas. Cifra la conexión para que nadie en el camino pueda leer lo que se manda como contraseñas o fotos. Y comprueba que el sitio es de quien dice ser. Para eso necesita un certificado que es un archivo que afirma con una firma que este nombre pertenece a este servidor.

Los certificados los emiten autoridades. Let's Encrypt es una que los da gratis con una condición. Hay que demostrarle que controlas el dominio. Y Certbot es el programa que hace el trámite. Aquí corre dentro de un contenedor y usa los dos volúmenes del certificado que vimos en Compose.

Funciona así. Certbot le dice a Let's Encrypt que quiere un certificado para un nombre. Let's Encrypt contesta pidiendo que se publique un archivo con cierto contenido en una dirección concreta del sitio bajo punto well-known acme challenge. Certbot lo escribe en uno de los volúmenes y Nginx lo sirve y Let's Encrypt lo lee desde internet y comprueba que es cierto. Si lo es entrega el certificado y Certbot lo guarda en el otro volumen.

Por eso existe el bloque de acme challenge que vimos en el archivo anterior. Sin él Nginx no podría servir ese archivo de prueba.

El comando es docker run con los dos volúmenes y la imagen de Certbot y la orden certonly con el método webroot. Se indica la carpeta compartida. Luego va el dominio con la opción d una vez por cada nombre que deba cubrir el certificado. Aquí son dos que son el dominio y www. Y al final un correo de contacto que se cubre al grabar.

Los volúmenes se llaman con el nombre de la carpeta del proyecto. Si tu carpeta se llama distinto el comando cambia y docker volume ls te dice los nombres reales.

[Acción: abre deploy/nginx.conf, líneas 5 a 17: el puerto 80 con HTTPS]

Con el certificado listo se pasa al otro archivo que es nginx punto conf y aquí aparece el huevo y la gallina. Este archivo apunta al certificado y si el certificado no existe Nginx se niega a arrancar. Por eso en un servidor nuevo se empieza con el archivo de solo HTTP y se pide el certificado. Solo entonces se cambia a este. Fue un error real del proyecto y es la razón de que haya dos archivos.

El primer bloque escucha en el puerto 80 y tiene dos funciones. Deja pasar la validación de Certbot para que la renovación siga funcionando. Y todo lo demás lo manda con una redirección permanente a la versión segura conservando la ruta que se pidió. Quien escriba la dirección con http termina en https sin darse cuenta.

[Acción: líneas 19 a 29: www]

El segundo bloque atiende a www en HTTPS. Usa el mismo certificado que cubre los dos nombres y redirige al dominio sin www. De modo que el sitio tiene una sola dirección oficial.

[Acción: líneas 31 a 53: el servidor con HTTPS]

Y el tercero es el sitio. Escucha en el puerto 443 con HTTP dos activado. Dice dónde están el certificado y su llave privada dentro del volumen. Y limita los protocolos a las dos versiones modernas de TLS que es el cifrado en el que se apoya HTTPS.

Lo que sigue es lo que ya vimos en el archivo anterior. El límite de subida y el reenvío a web con los cuatro encabezados y los 1,800 segundos. Es el mismo servidor ahora con cifrado. Ojo con otro dominio hay que cambiar los nombres en este archivo que aparecen en las rutas del certificado y en los nombres de los servidores.

[Acción: terminal en el servidor: borra la línea NGINX_CONF del .env y levanta nginx]

Para pasar a este archivo se borra del punto env la línea de NGINX_CONF. Con eso Compose usa el valor por defecto que es el archivo con HTTPS. Y se levanta solo el servicio de Nginx. No hay que reconstruir nada.

[Acción: navegador: https://imagebiopro.cloud, con el candado]

Y la comprobación. El navegador con la dirección segura y aparece el candado. Si se hace clic el certificado dice que lo emitió Let's Encrypt para el dominio. Y si escribes con http o con www te lleva a la dirección segura.

[Pantalla 4 · Comprobar desde fuera]

> Idea central: Un sitio no está bien porque tú lo ves bien desde adentro: se comprueba desde fuera. Que HTTPS responde, que HTTP y www redirigen, que el certificado trae las fechas y los nombres correctos y que el puerto 8000 no responde. Si algo falla, los primeros lugares donde mirar son los registros de Nginx y la prueba de su configuración.

> En pantalla: Terminal en la computadora con `curl -I`, `openssl` y la prueba del puerto 8000.

[Acción: terminal en la computadora: curl -I con la dirección https, con http y con www]

Antes de seguir una costumbre que vale la pena. Comprobar desde fuera. Que el sitio funcione en tu navegador no prueba demasiado porque el navegador guarda cosas. Así que se prueba con una orden que no guarda nada.

Es curl con la opción i mayúscula que pide solo las cabeceras de la respuesta. Con la dirección segura la primera línea dice 200 OK y otra indica que contestó nginx. Con la dirección http dice 301 movido permanentemente y una línea location con la dirección https. Si se le agrega una ruta y parámetros los conserva. Con www también da 301 hacia el dominio sin www. Así se ve de verdad que las redirecciones funcionan.

[Acción: terminal en la computadora: openssl, las fechas y los nombres del certificado]

Ahora el certificado. La orden de openssl se conecta al sitio y muestra lo que el servidor presenta. Hay que mirar tres cosas. Para quién es que es el dominio con www como segundo nombre. Quién lo emitió que es Let's Encrypt. Y las fechas que empiezan el 22 de octubre de 2026 y terminan el 20 de enero de 2027. Son 90 días menos unos minutos.

[Acción: terminal en la computadora: curl al puerto 8000, que no debe responder]

Y una última prueba de las que más importan y menos se hacen. Comprobar que lo que no debe estar abierto no lo está. Se le pide al puerto 8000 del servidor desde fuera y lo esperado es que no conteste. De modo que la orden se queda esperando y termina por tiempo. Si contestara el sitio tendría una puerta lateral sin Nginx y sin cifrado. Y habría que revisar el archivo override del video anterior y el cortafuegos del servidor.

Y si algo falla hay dos lugares donde mirar primero. Los registros de Nginx con docker compose logs nginx que dicen quién pidió qué y qué contestó el servidor. Y la prueba de la configuración con nginx guion t que revisa el archivo sin reiniciar nada y señala la línea exacta del error. Con esos dos casi todo se resuelve.

[Pantalla 5 · Renovar, actualizar y respaldar]

> Idea central: El certificado dura 90 días y se renueva con una tarea programada. Para actualizar el sitio basta con subir los cambios a Git desde la computadora, y bajarlos y reconstruir en el servidor; los modelos y el `.env` no están en Git y no cambian. Los datos viven en un volumen, y se respaldan aparte.

> En pantalla: Terminal en el servidor, con `crontab`, y terminal en la computadora y en el servidor para la actualización y el respaldo.

[Acción: terminal en el servidor: crontab -e, la línea de renovación]

El certificado no es para siempre. Dura 90 días. El que usa este sitio se emitió el 22 de octubre y vence el 20 de enero de 2027. Y si nadie lo renueva ese día el navegador empieza a avisar a todos que el sitio no es seguro.

Para eso hay una tarea programada. Se abre con crontab y se agrega una línea que dice en orden lo siguiente. A las tres de la mañana del día 1 de cada mes entra a la carpeta del proyecto y corre Certbot con la orden de renovar. Y si todo sale bien reinicia Nginx para que lea el certificado nuevo.

Renovar no significa renovar siempre. Certbot solo renueva si faltan menos de 30 días. De lo contrario no hace nada.

Y una observación. Una revisión al mes deja poco margen con un certificado de 90 días. Lo más habitual es revisar cada semana porque Certbot solo renueva cuando toca y revisar más veces no cuesta nada. Es una mejora pendiente.

[Acción: terminal en la computadora: git push]

Actualizar el sitio es más simple de lo que parece. Los cambios se hacen en el repositorio. En tu computadora haces tus cambios y los guardas con un commit y los subes con git push.

[Acción: terminal en el servidor: git pull y docker compose up -d --build]

Después en el servidor entras a la carpeta del proyecto. Git pull baja los cambios y docker compose up con las opciones que ya conoces reconstruye lo que cambió y reinicia lo necesario. Gracias al orden del Dockerfile si solo cambió el código la parte lenta de las dependencias no se repite.

Dos cosas no cambian con un pull. Son los modelos y el archivo punto env que no están en Git. Si hay un modelo nuevo se copia con scp y se reinicia el servicio web como vimos. Y los datos que son la base y los resultados están en su volumen y por eso reconstruir no los borra.

[Acción: terminal en el servidor: el respaldo con tar]

Esos datos conviene respaldarlos porque un volumen no es un respaldo. Si el servidor falla el volumen se va con él. Este comando monta el volumen de datos y la carpeta actual en un contenedor pequeño y comprime todo en un archivo con la fecha de hoy en el nombre. Después ese archivo hay que copiarlo a otro lugar fuera del servidor.

[Pantalla 6 · El cierre del curso]

> Idea central: El curso recorre un sistema completo, y se resume en tres ideas: la red localiza, el código mide y las personas verifican. Los videos están en la página Videos del sitio, y las preguntas por escrito se mandan desde la página de Contacto.

> En pantalla: El navegador con la página Videos, las dos secciones y los 15 videos; después la página de Contacto.

[Acción: navegador: la página Videos del sitio, con las dos secciones]

Llegamos al final y vale la pena un recorrido de todo el curso.

Empezamos con un problema que es contar y medir espermatozoides en fotos de microscopio. Vimos qué es una imagen digital y qué es una red neuronal y cómo aprende. Vimos cómo ve una imagen una red convolucional y cómo funciona Mask R-CNN y qué es el aprendizaje por transferencia y cómo se preparan los datos. Después vimos el sitio por dentro con el frontend y el backend y la inferencia y la medición. Y hoy el cuaderno donde se entrena y el servidor donde vive.

Si hubiera que quedarse con tres ideas serían estas.

La red localiza. Lo único que hace la red es trazar el contorno de cada espermatozoide. No cuenta y no mide y no interpreta.

El código mide. El área y el largo y la escala y el resumen y el histograma salen de código común. Ese código da siempre el mismo resultado con los mismos datos y se puede comprobar a mano.

Y las personas verifican. Hay falsos positivos. Hay espermatozoides juntos y colas que se marcan como espermatozoides. Hay una escala que sigue siendo provisional y una validación con pocas fotos. Por eso el resultado se revisa a ojo con la imagen marcada. El sitio mide y la lectura científica es del grupo de investigación.

Los videos se publican en esta página que es la de Videos del sitio y están en las dos secciones del curso.

[Acción: navegador: la página de Contacto]

Y si te queda una duda o encuentras un error hay un lugar para preguntar por escrito que es la página de Contacto. Se llena con el nombre y el correo y el mensaje. Y el mensaje se guarda en el sitio.

Gracias por acompañarme en este curso.
