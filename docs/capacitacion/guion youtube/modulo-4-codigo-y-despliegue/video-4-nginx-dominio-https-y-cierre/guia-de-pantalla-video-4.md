# Guía de pantalla del módulo 4, video 4: Nginx, dominio, HTTPS y cierre

Este video no lleva mazo. Se graba la pantalla: la terminal, el editor y el navegador, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se escribe un comando o se abre un archivo (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, lo que se espera ver en cada orden y las cifras que el guion debe respetar. Si cambian los archivos de Nginx, el dominio o el certificado, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | Qué hace Nginx | Editor | `deploy/nginx-http.conf`, de la línea 3 a la 24 |
| 2 | El dominio | Panel del dominio, terminal | Registros A y `nslookup` del dominio y de `www` |
| 3 | HTTPS y el certificado | Terminal, editor, navegador | Certbot, `deploy/nginx.conf`, cambiar de configuración y el candado |
| 4 | Comprobar desde fuera | Terminal | `curl -I`, `openssl` y la prueba del puerto 8000 |
| 5 | Renovar, actualizar y respaldar | Terminales | `crontab`, `git push`, `git pull` con `docker compose up -d --build` y el respaldo |
| 6 | El cierre del curso | Navegador | Las páginas Videos y Contacto del sitio |

## Antes de grabar

- Una terminal en la computadora (Git Bash, para la orden de `openssl`) y otra con la sesión SSH ya abierta en el servidor.
- El editor con `deploy/nginx-http.conf` y `deploy/nginx.conf`, con números de línea y letra grande. Los comentarios de las primeras líneas de los dos archivos mandan a un documento de `docs/`: el guion empieza después (línea 3 en el primero y línea 5 en el segundo).
- **Qué no debe salir en pantalla:** la IP del servidor (también aparece en la salida de `nslookup`), el usuario, el correo del certificado y el contenido del `.env`.
- Para el tramo del dominio, el panel de quien administra el nombre, con la IP cubierta.
- Si se graba la emisión del certificado desde cero, hace falta un servidor y un dominio de prueba. Let's Encrypt limita cuántos certificados da por dominio, y repetir la prueba con el dominio real puede dejar al sitio sin poder renovar por un tiempo.
- El navegador con `https://imagebiopro.cloud`, `/videos` y `/contacto`. La página de Contacto muestra un correo y un teléfono públicos; confirmar que se pueden enseñar. Las capturas de referencia están en `figuras/`.

## Qué se espera en cada orden

Marcado como **real** lo que se comprobó el 30/10/2026 contra el sitio publicado, desde esta computadora. Marcado como **por confirmar** lo que corre en el servidor: aquí no hay acceso a él.

| Orden | Qué se espera | Estado |
|---|---|---|
| `nslookup imagebiopro.cloud` y `nslookup www.imagebiopro.cloud` | La dirección del servidor en las dos | Real |
| `curl -I https://imagebiopro.cloud` | `HTTP/1.1 200 OK` y `Server: nginx/1.27.5` | Real |
| `curl -I http://imagebiopro.cloud/algo?x=1` | `301 Moved Permanently` y `Location: https://imagebiopro.cloud/algo?x=1` | Real |
| `curl -I https://www.imagebiopro.cloud` | `301 Moved Permanently` y `Location: https://imagebiopro.cloud/` | Real |
| `openssl s_client` y `openssl x509` | `subject=CN=imagebiopro.cloud`; emisor Let's Encrypt; del `Oct 22 03:12:59 2026 GMT` al `Jan 20 03:12:58 2027 GMT`; nombres `imagebiopro.cloud` y `www.imagebiopro.cloud` | Real |
| `curl -I --max-time 10 http://imagebiopro.cloud:8000` | No contesta: `curl: (28) Connection timed out after 10005 milliseconds` | Real desde esta red |
| `docker run … certbot/certbot certonly …` | La emisión del certificado | Por confirmar |
| `docker compose up -d nginx` tras borrar `NGINX_CONF` | Nginx arranca con HTTPS | Por confirmar |
| `crontab -e`, `git pull`, respaldo con `tar` | Sin salida llamativa; el respaldo deja un archivo `datos-AAAA-MM-DD.tar.gz` | Por confirmar |
| `docker compose logs nginx` y `nginx -t` | Los registros de Nginx; la prueba de la configuración | Por confirmar |

## Cifras que el guion usa

- Certificado: emitido el 22 de octubre de 2026 y con vencimiento el 20 de enero de 2027 (89 días y 24 horas); Let's Encrypt; cubre `imagebiopro.cloud` y `www.imagebiopro.cloud`.
- `deploy/nginx-http.conf`: 24 líneas, escucha en el puerto 80, nombre `_`, `location /.well-known/acme-challenge/` con raíz `/var/www/certbot`, reenvío a `http://web:8000` con cuatro encabezados, límite de subida de 300 MB y 1800 segundos de espera.
- `deploy/nginx.conf`: 53 líneas, tres bloques `server`: puerto 80 con validación de Certbot y redirección 301 a `https://imagebiopro.cloud$request_uri` (líneas 6 a 17); `www` en 443 con redirección al dominio sin `www` (20 a 29); el sitio en 443 con `http2`, certificado y llave en `/etc/letsencrypt/live/imagebiopro.cloud/`, TLS 1.2 y 1.3, límite de 300 MB y reenvío a `web` (31 a 53).
- Renovación programada: `0 3 1 * *` (día 1 de cada mes, 3:00), Certbot `renew -q` y reinicio de Nginx. Certbot solo renueva si faltan menos de 30 días.
- Actualización: `git pull` y `docker compose up -d --build` en `~/imagebio`. Los modelos y el `.env` no están en Git.
- Respaldo: contenedor `alpine` con el volumen `imagebio_datos` y `tar czf` con la fecha en el nombre.
- El sitio tiene 15 videos del curso en dos secciones (`Red neuronal` y `Sitio web`) y un formulario de contacto con nombre, correo y mensaje.

## Líneas que nombra el guion

| Archivo | Líneas |
|---|---|
| `deploy/nginx-http.conf` | bloque `server` 3 a 24; puerto 4; nombre 5; límite de subida 7 y 8; reto de Certbot 10 a 12; reenvío 14 a 23 (`proxy_pass` 15, encabezados 16 a 19); espera 20 a 22 |
| `deploy/nginx.conf` | puerto 80 6 a 17; `www` 20 a 29; sitio 31 a 53 (certificado 36 y 37, TLS 38, límite 41, reenvío 43 a 52) |

Los números cuentan desde la primera línea de cada archivo, que es un comentario.

## Cosas que el guion dice con cuidado

- **Las órdenes del servidor no se probaron.** Certbot, `cron`, `git pull`, el respaldo, `nginx -t` y los registros hay que correrlos al grabar y ajustar el guion si algo difiere.
- **El comando de Certbot de la guía de despliegue lleva un solo `-d`.** El certificado real cubre dos nombres, así que el guion dice una opción `-d` por cada nombre (el dominio y `www`). Hay que corregir la guía de `docs/despliegue.md` para que coincida.
- **La renovación mensual deja poco margen.** Con un certificado de 90 días y Certbot renovando solo a menos de 30 días, una revisión al mes funciona por coincidencia de fechas (el 1 de enero quedan 19 días, y se renueva), pero a veces la revisión cae justo cuando faltan unos 30 días, no renueva y la siguiente ya llega con el certificado vencido. El guion lo menciona como mejora pendiente (revisar cada semana) y no cambia la línea del `cron`.
- **El enlace de recuperación de contraseña se arma con el protocolo que ve Flask.** El código no usa `X-Forwarded-Proto` (no hay `ProxyFix`), así que el enlace puede salir con `http` y pasar por la redirección a `https`. El guion lo menciona como pendiente.
- **El formulario de Contacto guarda el mensaje en la base de datos y no avisa a nadie.** El guion lo dice así («el mensaje se guarda en el sitio»). Falta definir quién los lee.
- **La página de Videos aún tiene marcadores de posición** y el orden de los videos 8 a 11 en `app/sitio.py` sigue siendo el anterior al cambio de orden del módulo 3. El guion solo dice que los videos se publican ahí.
- **El error del CNAME de `www` viene de las notas del proyecto**, no de una prueba de hoy. El guion lo cuenta como se anotó; confirmar los detalles al grabar.
- **El puerto 8000.** Desde esta red no contestó, lo cual no prueba cómo está configurado el servidor. El guion dice qué se espera y qué hacer si contesta.
- **No se muestran los documentos del proyecto.** La guía de despliegue de `docs/` se usó como fuente, pero no se abre en pantalla.
- **El guion queda en unos 13 minutos de habla**, por debajo de los 20 previstos, aunque cierra el curso. Si se quiere más tiempo, el candidato natural es un recorrido de todo el sistema con las capturas de los módulos 3 y 4 al hacer el resumen.
