# Plan del módulo 4: código y despliegue

Plan para escribir los guiones de los cuatro videos del módulo 4 (videos 12 a 15 del curso). Está hecho leyendo el cuaderno `entrenamiento/entrenar_mask_rcnn.ipynb` (versión 0.5.1), `Dockerfile`, `docker-compose.yml`, `deploy/nginx.conf`, `deploy/nginx-http.conf` y `docs/despliegue.md`.

## Qué es el módulo

- Cierra el curso. El módulo 3 mostró el sitio y su código; este muestra de dónde sale el modelo y cómo llega el sitio a internet.
- Cuatro videos de unos 20 minutos (unas 3,300 a 3,500 palabras cada uno). Cada uno abre con una frase que lo une con el anterior. El video 1 une con el módulo 3 (el sitio ya funciona, falta ver de dónde viene el modelo).
- Mismo formato que el módulo 3: guion humanizado y guion natural con su Word, `[Acción: …]` dentro del texto, guía de pantalla con los comandos probados y artifact con capturas reales. Se graba la pantalla, sin mazo.
- No hay taller de práctica. El cuaderno y los comandos se muestran en demostración.
- Los títulos y las descripciones cortas de los videos 12 a 15 todavía no están en `app/sitio.py` (`_VIDEOS`); hay que agregarlos.

## Vista general

| Video | Título propuesto | Qué es | Qué se muestra |
|---|---|---|---|
| 12 (módulo 4, video 1) | El cuaderno de Colab, primera parte | De los datos a los recortes de entrenamiento | `entrenamiento/entrenar_mask_rcnn.ipynb`, pasos 1 a 6 |
| 13 (video 2) | El cuaderno de Colab, segunda parte | De la red al modelo exportado | El mismo cuaderno, pasos 7 a 11 y «Mejorar el modelo» |
| 14 (video 3) | Despliegue en la nube | Del VPS a los contenedores | `Dockerfile`, `docker-compose.yml`, terminal con SSH |
| 15 (video 4) | Nginx, dominio, HTTPS y cierre | Que el sitio se vea en internet, y el cierre del curso | `deploy/nginx.conf`, `deploy/nginx-http.conf`, registros DNS, Certbot |

## Videos 12 y 13: el cuaderno de Colab

**Material:** el cuaderno tiene 32 celdas y unas 950 líneas de código. No se puede leer línea por línea en dos videos de 20 minutos. El criterio es el mismo que en el módulo 3: se enseña dónde está cada cosa, se explica la que importa y se señala la que no hace falta entender.

**Se muestra con `MODO_PRUEBA = True`.** Entrena dos épocas muy cortas (`EPOCAS`, `RECORTES_POR_EPOCA`, `VALIDAR_CADA` y `GUARDAR_CADA` quedan en 2, 16, 1 y 1) y escribe en una carpeta con sufijo `_prueba`, así que no se mezcla con una corrida real. El entrenamiento completo (60 épocas) no se corre en el video.

### Video 12: primera parte (pasos 1 a 6, celdas 0 a 16, unas 470 líneas)

> **Estado (30 de octubre de 2026):** guion en las dos versiones, Word y guía de pantalla terminados en `guion youtube/modulo-4-codigo-y-despliegue/video-1-cuaderno-de-colab-primera-parte/`. Falta confirmar en Colab, con las fotos del laboratorio, las salidas de las celdas 8 y 10 (258 y 45 espermatozoides, 66 y 2 en la validación).

**Objetivo:** que se vea cómo un cuaderno convierte fotos y etiquetas en recortes listos para entrenar, y por qué cada decisión protege contra un error.

**Frase de unión:** el módulo 3 terminó con el sitio funcionando; el sitio usa dos archivos `.pt`. Este video enseña de dónde salen.

| Tramo | Contenido | Dónde |
|---|---|---|
| 1 | Qué es un cuaderno de Colab (celdas de texto y de código, GPU gratuita, Drive) y qué hace este | Celda 0 (introducción) |
| 2 | Paso 1, entorno: comprobar la GPU, conectar Drive | Celdas 1 a 3 |
| 3 | Paso 2, configuración: `PERFIL` (fluorescencia, campo claro o mixto), `NOMBRE_CORRIDA`, `MODO_PRUEBA` y el resto de valores ajustables en una sola celda | Celdas 4 y 5 |
| 4 | Paso 3, leer las etiquetas de CVAT en formato COCO y comprobar que cuadren con las fotos; se detiene antes de gastar GPU | Celdas 7 y 8 |
| 5 | Paso 4, separar entrenamiento y validación (10 fotos o más: fotos completas; menos de 10: una franja de cada foto con margen) | Celdas 9 y 10 |
| 6 | Paso 5, preparar las fotos una sola vez y guardarlas como `.npy`; la misma preparación se usa en el servidor | Celdas 11 y 12 |
| 7 | Paso 6, recortes y aumento de datos (volteos, giros, zoom, brillo, ruido) y la revisión visual del contorno verde | Celdas 13 a 16 |
| 8 | Cierre: lo que ya está listo y lo que sigue | |

**Une con:** módulo 2 video 4 (datos, anotación en CVAT, validación) y módulo 3 video 2 (la misma preparación en el servidor).

### Video 13: segunda parte (pasos 7 a 11 y mejorar, celdas 17 a 31, unas 480 líneas)

> **Estado (30 de octubre de 2026):** guion en las dos versiones, Word y guía de pantalla terminados en `guion youtube/modulo-4-codigo-y-despliegue/video-2-cuaderno-de-colab-segunda-parte/`. Las celdas 18 a 30 se corrieron en CPU en modo de prueba (sin pesos de COCO) para comprobar el formato de las salidas; falta correrlas en Colab. Falta decidir qué cifras del modelo de fluorescencia son las vigentes (la documentación y el archivo `model/fluorescencia.pt` no coinciden).

**Objetivo:** que se vea cómo se construye la red a partir de una ya entrenada, cómo se entrena y se mide, y cómo queda el archivo que va al servidor.

| Tramo | Contenido | Dónde |
|---|---|---|
| 1 | Paso 7, la red: Mask R-CNN preentrenada con COCO, una sola clase («cabeza»), anclas de 20 a 576 px, entrada sin reescalar, hasta 300 detecciones por tesela | Celdas 17 y 18 |
| 2 | Paso 8, cómo se mide: validar igual que en producción; precisión, exhaustividad, F1 y AP50; el umbral de 50 % de coincidencia | Celdas 19 y 20 |
| 3 | Paso 9, entrenar: SGD con calentamiento, precisión mixta, `mejor.pt` y `ultimo.pt`, y qué pasa si Colab se corta | Celdas 21 a 23 |
| 4 | Paso 10, resultados: las gráficas de pérdida y de validación, el sobreajuste, las fotos con lo que encontró la red | Celdas 24 a 28 |
| 5 | Paso 11, exportar `modelo_cabezas.pt` (pesos y configuración), comprobar que carga en CPU y medir cuánto tarda una tesela | Celdas 29 y 30 |
| 6 | Mejorar el modelo (más fotos, más variadas, otra corrida) y cómo se copia el modelo al servidor | Celda 31 |
| 7 | Cierre: el modelo llega a la carpeta `model/` y el video 14 lo lleva a internet | |

**Une con:** módulo 2 video 2 (Mask R-CNN), video 3 (transferencia) y video 4 (curvas y sobreajuste); módulo 3 video 2 (el archivo que carga el servidor).

## Videos 14 y 15: despliegue

**Material:** ya existe vivido en el proyecto y escrito en `docs/despliegue.md`. El VPS es de Hostinger con Ubuntu, el dominio es `imagebiopro.cloud`, y el certificado vence en enero de 2027.

### Video 14: despliegue en la nube

> **Estado (30 de octubre de 2026):** guion en las dos versiones, Word y guía de pantalla terminados en `guion youtube/modulo-4-codigo-y-despliegue/video-3-despliegue-en-la-nube/`. Quedó en unos 19.5 minutos, con un tramo nuevo que recorre el panel de Hostinger (visto el 30/10/2026) antes de la clave SSH. Las órdenes que corren en el servidor no se probaron: falta grabarlas en un servidor.

**Objetivo:** llegar de un VPS vacío a los dos contenedores corriendo, entendiendo qué es cada pieza.

| Tramo | Contenido | Dónde |
|---|---|---|
| 1 | Qué es un VPS y por qué hace falta (el sitio tiene que estar encendido siempre) | Panel del proveedor |
| 1b | El panel de Hostinger: plan, métricas, datos de acceso (usuario `root`), tarjetas, respaldos y la consola web | Panel del proveedor |
| 2 | La clave SSH: la pública va al servidor, la privada no sale de la computadora; una clave por uso | Terminal |
| 3 | Preparar el servidor: instalar Docker, clonar el repositorio, crear `.env` con `SECRET_KEY` | Terminal, `docs/despliegue.md` sección 1 |
| 4 | Docker en tres ideas: imagen (la receta), contenedor (el programa corriendo) y volumen (donde viven los datos) | `Dockerfile` (23 líneas) |
| 5 | Docker Compose: un archivo que levanta `web` y `nginx` con un comando; el volumen `datos`, la carpeta `model/` montada en solo lectura | `docker-compose.yml` (43 líneas) |
| 6 | Copiar los modelos con `scp` (no están en Git) y levantar con `docker compose up -d --build`; `ps` y `logs` | Terminal, sección 2 |
| 7 | Cierre: el sitio responde por IP, sin dominio ni HTTPS todavía | |

**Frase de unión:** el video 13 terminó con los dos `.pt`; ahora hay que ponerlos en un servidor.

### Video 15: Nginx, dominio, HTTPS y cierre

> **Estado (30 de octubre de 2026):** guion en las dos versiones, Word y guía de pantalla terminados en `guion youtube/modulo-4-codigo-y-despliegue/video-4-nginx-dominio-https-y-cierre/`. Se agregó un tramo de comprobación desde fuera (con salidas reales contra el sitio publicado). Quedó en unos 13 minutos. Las órdenes del servidor no se probaron.

**Objetivo:** que el sitio se abra con un nombre y con candado, y cerrar el curso.

| Tramo | Contenido | Dónde |
|---|---|---|
| 1 | Qué hace Nginx (recibe las visitas y se las pasa a Gunicorn) y por qué hay dos archivos: `nginx.conf` con HTTPS y `nginx-http.conf` sin él | `deploy/nginx.conf`, `deploy/nginx-http.conf` |
| 2 | El dominio: un registro A que apunta a la IP; el error real del registro CNAME de `www` que chocaba con el A | Panel del dominio |
| 3 | HTTPS con Let's Encrypt y Certbot; por qué Nginx no arranca sin certificado y cómo se resolvió | Terminal, sección 3 |
| 4 | Renovación con una tarea programada (el certificado dura 90 días) | `crontab` |
| 5 | Actualizar el sitio: `git push` en la computadora y `git pull` más `docker compose up -d --build` en el servidor; el respaldo de `datos` | Sección 4 y 5 |
| 6 | Cierre del curso: las tres ideas (la red localiza, el código mide, las personas verifican), dónde están los materiales y cómo mandar preguntas por escrito | |

## Cosas que los guiones deben decir con cuidado

1. **No se corre el entrenamiento completo.** Solo `MODO_PRUEBA`. No se dan métricas de la red como si salieran del video; si se muestran, que sean las de la corrida real que haya en Drive y con su nombre.
2. **Pocas fotos.** El cuaderno dice que con pocas fotos la validación es inestable. El guion no presenta el AP50 como una garantía.
3. **Los tiempos en el servidor.** `docs/despliegue.md` dice que hay que medirlos en el VPS real. No se da ninguno que no se haya medido.
4. **Nada secreto en pantalla.** La clave privada, el contenido de `.env`, la IP y el correo del certificado se tapan o se sustituyen. Se graba con una clave SSH de demostración.
5. **La escala sigue provisional.** No se vuelve a presentar como calibración.
6. **No se muestran los documentos del proyecto** (`docs/`). Lo que explican se dice hablando. Se acordó con el módulo 3.

## Decisiones que hacen falta

1. **El cuaderno en Colab o en local.** Para grabar el video 12 hace falta abrir Colab con Drive y una carpeta `datos/` con fotos y etiquetas. Hay que decidir con qué fotos se graba y si se puede mostrar la corrida real.
2. **El servidor de demostración.** Para el video 14 se necesita un VPS donde se pueda mostrar el proceso desde cero sin tocar el de producción. Opciones: (a) un VPS temporal, (b) grabar sobre el real mostrando solo `ps`, `logs` y el contenido de los archivos, sin repetir la instalación. Con (b) el video no enseña el paso a paso.
3. **El reparto del cuaderno.** Se propone cortar entre el paso 6 y el paso 7 porque las líneas quedan casi parejas (470 y 480). Falta confirmar contra el cuaderno al escribir el guion.
4. **Cuánto del cierre del curso va al video 15.** Propuesta: dos o tres minutos al final, con las tres ideas y la lista de materiales.
5. **Los títulos de `_VIDEOS`.** Hay que confirmar los de los videos 12 a 15 y también el orden de los videos 8 a 11 en `app/sitio.py` (sigue el orden anterior al cambio del módulo 3).

## Orden de trabajo propuesto

Mismo recorrido que el módulo 3, un video a la vez y en orden:

1. Revisar el cuaderno celda por celda y anotar cifras (líneas, parámetros, valores por defecto).
2. Guion humanizado.
3. Guion natural.
4. Word de los dos.
5. Guía de pantalla: preparación, comandos o celdas probadas y cifras.
6. Artifact con capturas reales.
7. Comprobar que las dos versiones traen las mismas cifras y las mismas acciones.

Los videos 12 y 13 se escriben juntos, porque el segundo continúa el cuaderno. Los 14 y 15 también, porque comparten el servidor y el repositorio.
