# Guía de pantalla del módulo 4, video 3: Despliegue en la nube

Este video no lleva mazo. Se graba la pantalla: la terminal, el editor y el navegador, mientras se habla. En el guion, cada bloque `> En pantalla:` resume qué se abre y qué se hace en ese tramo, y las líneas `[Acción: …]` dentro del texto marcan en qué frase se cambia de pantalla, se escribe un comando o se abre un archivo (no se leen en voz alta). Esta guía junta lo que hay que preparar antes de grabar, lo que se espera ver en cada orden y las cifras que el guion debe respetar. Si cambia el Dockerfile, el archivo de Compose o el proceso de instalación, hay que cambiar el guion (las dos versiones) y esta guía.

## Tramos

| N.º | Tramo | Dónde | Qué se hace |
|---|---|---|---|
| 1 | Un servidor que siempre está encendido | Panel del proveedor | Se abre el panel de Hostinger, con la IP cubierta |
| 2 | El panel de Hostinger | Panel del proveedor | Cabecera y plan, métricas, datos de acceso, tarjetas, «Snapshots y respaldos» y «Consola web» |
| 3 | La clave SSH | Terminal, panel | `ssh-keygen`, los dos archivos, registrar la pública en «Clave SSH» y entrar con `ssh root@IP` |
| 4 | Preparar el servidor | Terminal del servidor | Instalar Docker, clonar el repositorio y crear el `.env` |
| 5 | Docker en tres ideas, y el Dockerfile | Editor | `Dockerfile`, de arriba abajo |
| 6 | Docker Compose | Editor, terminal | `docker-compose.yml`, el error de `config` y `docker-compose.override.yml` |
| 7 | Levantar el sitio | Terminales, navegador | `scp`, `up -d --build`, `ps`, `logs -f` y el sitio por IP |
| 8 | Lo que vimos y lo que sigue | Terminal del servidor | Repaso con `docker compose ps` en pantalla |

## Antes de grabar

- El panel de Hostinger abierto en la vista general del VPS (`hpanel.hostinger.com`, menú VPS), con la sesión iniciada. La IP aparece tres veces en esa pantalla: junto al usuario, en el comando de acceso y en «Detalles del VPS». Se cubre en todas.
- **En el panel no se pulsa:** «Reiniciar», «Restablecer contraseña», «Restablecer» de los respaldos, «Crear snapshot», «Mejorar plan» ni «Renovar». Todo el recorrido es mirar y señalar.
- Una terminal en la computadora y otra con la sesión SSH ya abierta en el servidor.
- Los modelos `fluorescencia.pt` y `campo_claro.pt` en la carpeta `model/` de la computadora, para el `scp`.
- El editor con `Dockerfile`, `docker-compose.yml` y `docker-compose.override.yml`, con números de línea y letra grande.
- Para la clave SSH, un par nuevo de práctica (se borra al terminar). Nunca se enseña la clave de uso real.
- **Qué no debe salir en pantalla, ni al grabar ni al editar:** la IP del servidor, el nombre del servidor (`srv…hstgr.cloud`), el correo de la cuenta, la clave privada y el contenido del `.env`. El usuario `root` sí se dice y se enseña.
- **No se ejecuta `docker compose config` con el `.env` real.** Imprime todos los valores ya resueltos, incluida la contraseña del correo. En el video solo se enseña la versión que falla por no haber `SECRET_KEY`, que no imprime valores.
- **Cambios previos en `docker-compose.yml`.** La línea 13 (comentario del temporizador) nombra a quien recibe el sitio, y la línea 35 (comentario de Nginx) manda a un documento de `docs/`. Antes de grabar hay que reescribir los dos comentarios o no enseñarlos. El guion salta de la línea 12 a la 14 y de la 34 a la 36. Cambiar el archivo es un cambio del proyecto y lleva versión; está sin hacer.
- Si se quiere grabar la instalación desde cero, hace falta un servidor nuevo, no el de producción.

## Qué se espera en cada orden

Marcado como **real** lo que se ejecutó el 30/10/2026 en esta computadora. Marcado como **por confirmar** lo que corre en el servidor: aquí no hay un servidor ni Docker en marcha, así que esas órdenes no se probaron.

| Orden | Qué se espera | Estado |
|---|---|---|
| `ssh-keygen -t ed25519 -C "demo-curso"` | `Generating public/private ed25519 key pair.`, la ruta de los dos archivos, la huella `SHA256:…` y un dibujo | Real. Privada de unos 400 bytes y pública de unos 90 |
| `openssl rand -hex 32` | 64 caracteres hexadecimales | Real |
| `ssh root@IP` | La primera vez, el aviso de autenticidad del servidor y la pregunta `yes/no` | Por confirmar (mensaje estándar de OpenSSH) |
| `curl -fsSL https://get.docker.com \| sh` | Los pasos de la instalación | Por confirmar |
| `docker compose config` sin `SECRET_KEY` | `error while interpolating services.web.environment.SECRET_KEY: required variable SECRET_KEY is missing a value: Define SECRET_KEY en el archivo .env` | Real |
| `scp model/… USUARIO@IP:~/imagebio/model/` | Una barra de avance por archivo | Por confirmar |
| `docker compose up -d --build` | La construcción de la imagen y el arranque de los dos contenedores | Por confirmar. No se ha medido cuánto tarda la primera vez |
| `docker compose ps` | Los dos servicios en marcha | Por confirmar |
| `docker compose logs -f web` | Mensajes de Gunicorn y del sitio | Por confirmar |
| Navegador, `http://IP` | El sitio, sin candado | Por confirmar |
| Panel de Hostinger, vista general | Ubuntu 26.04 LTS, estado «Funcionando», plan KVM 1; CPU 1 %, memoria 36 %, disco 8 GB de 50 GB; usuario SSH `root` | Real, visto el 30/10/2026. Los porcentajes cambian |
| Panel, tarjetas | Clave SSH (Administrar), Reglas del firewall 0, Snapshots y respaldos 1, Escáner de malware no instalado | Real, 30/10/2026 |
| Panel, «Snapshots y respaldos» | Respaldo automático cada semana (el último, del 29/10/2026, de 7.72 GB, con 30 minutos de restauración); ninguna snapshot manual | Real, 30/10/2026 |

## Cifras que el guion usa

- `Dockerfile`: 23 líneas. Base `python:3.12-slim`. Dos instalaciones en la línea 9: las bibliotecas y PyTorch para procesador. El proyecto calcula que la imagen crece alrededor de 1 GB (no se midió aquí).
- Gunicorn: 1 proceso, 4 hilos, tiempo de espera de 1800 segundos, puerto 8000; la aplicación sale de `app:crear_app()`. Nginx usa el mismo tiempo de espera.
- `docker-compose.yml`: 43 líneas, dos servicios (`web` y `nginx`) y tres volúmenes con nombre (`datos`, `certbot-web` y `certbot-certs`). `nginx` usa la imagen `nginx:1.27-alpine` y publica los puertos 80 y 443; `web` no publica ninguno.
- `docker-compose.override.yml`: 4 líneas; publica el puerto 8000 de `web`.
- Variables: `SECRET_KEY` obligatoria; `TORCH_HILOS` usa hasta 4 según los procesadores si no se define; cinco variables de correo (`MAIL_SERVIDOR`, `MAIL_PUERTO`, `MAIL_USUARIO`, `MAIL_REMITENTE` y `MAIL_CLAVE`); `NGINX_CONF` elige el archivo de Nginx (por defecto `nginx.conf`).
- Modelos: unos 176 MB cada uno; no están en Git.
- `SECRET_KEY` se usa para firmar la sesión de Flask y los enlaces de recuperación de contraseña (con `itsdangerous`).
- El proveedor es Hostinger y el sistema, Ubuntu 26.04 LTS. Plan KVM 1: 1 núcleo de CPU, 4 GB de memoria, 50 GB de disco y 4 TB de ancho de banda al mes; centro de datos en Boston (Estados Unidos); renovación automática activada. Los datos salen del panel visto el 30/10/2026 y conviene volver a mirarlos al grabar.
- Panel: usuario SSH `root`; el panel muestra el comando completo `ssh root@IP`. «Clave SSH» lista las claves de la cuenta (no solo de este servidor) y el formulario «Añadir clave SSH» pide solo el contenido de la clave. «Reglas del firewall» marca 0: en el panel no hay ningún firewall creado para este servidor (no dice nada de un firewall dentro del servidor).
- Respaldos del proveedor: automáticos cada semana, de todo el servidor, guardados aparte del servidor; «Restablecer» devuelve todo el servidor a ese punto. Se distinguen de una snapshot manual y del respaldo de los datos del sitio con `tar` que se ve en el video siguiente.

## Líneas que nombra el guion

| Archivo | Líneas |
|---|---|
| `Dockerfile` | base 1; variables 3 y 4; carpeta de trabajo 6; requisitos 8; instalación 9; código 11 y 12; volumen 14 y 15; puerto 17; arranque 19 a 23 |
| `docker-compose.yml` | `web` 2 a 23 (construir 3, reinicio 4, variables 5 a 20, `SECRET_KEY` 7, modelos 9, hilos 11 y 12, temporizador 14, correo 15 a 20, volúmenes 21 a 23); `nginx` 25 a 38 (imagen 26, puertos 30 a 32, configuración 36, certificado 37 y 38); volúmenes con nombre 40 a 43 |
| `docker-compose.override.yml` | 1 a 4 (puerto 8000 en la línea 4) |

## Cosas que el guion dice con cuidado

- **Las órdenes del servidor no se probaron.** Aquí no hay servidor ni Docker en marcha. Hay que correrlas al grabar y ajustar el guion si algo difiere (nombres de contenedores, mensajes, tiempos).
- **No se dan tiempos.** Solo «varios minutos» la primera construcción, sin cifra. Del servidor real no hay mediciones.
- **`curl … | sh`.** El guion avisa que es dar confianza a un script de internet y que aquí es el método que recomienda Docker.
- **El `override` está en Git.** Se baja al servidor y Compose lo suma solo, con lo que el puerto 8000 se publicaría en el servidor. El guion pide comprobar desde fuera que no responda y no afirma cómo está el servidor. Comprobación del 30/10/2026 desde esta red: `https://imagebiopro.cloud` respondió 200 desde Nginx y `http://imagebiopro.cloud:8000` no respondió (se cortó por tiempo). No prueba cómo está configurado el servidor (puede ser un cortafuegos o que ese archivo no esté).
- **Lo del panel es lo que se vio el 30/10/2026.** Hostinger cambia su interfaz y los porcentajes de uso cambian. El guion solo da los de ese día como ejemplo. Hay que mirar el panel real al grabar y ajustar el guion si algo difiere (nombres de menús, botones, cifras).
- **El firewall en 0 no prueba nada del servidor.** Solo dice que el panel no tiene un firewall creado. El guion lo dice así y remite a la comprobación desde fuera del siguiente video.
- **La clave de demostración.** Se crea y se borra durante la práctica. La huella y el dibujo cambian en cada clave.
- **`docker compose config` con el `.env` real imprime secretos.** Se enseña solo el error por clave faltante.
- **No se muestran los documentos del proyecto.** La guía de despliegue de `docs/` se usa como fuente, pero no se abre en pantalla.
- **El guion queda en unos 19.5 minutos de habla**, cerca de los 20 previstos, con el recorrido por el panel de Hostinger incluido. El video siguiente (Nginx, dominio, HTTPS, actualización y cierre) queda en unos 13.
