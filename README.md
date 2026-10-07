# Image Bio Pro

Sitio web bilingüe (español/inglés) con un clasificador de imágenes de microscopio. El usuario sube una foto de fluorescencia de una muestra de espermatozoides y el sistema detecta las cabezas, las cuenta, mide su tamaño, muestra la distribución de tamaños y clasifica cada cabeza por color.

Proyecto desarrollado para un grupo de investigación de la UAM Unidad Xochimilco.

> **Estado:** en planeación. Aún no hay código. El primer entregable (sitio en línea y avances del clasificador con un modelo de muestra) está previsto para el 29 o 30 de octubre de 2026.

## Qué hace

### Las imágenes

Microscopía de fluorescencia sobre fondo negro, probablemente de espermatozoides de roedor (cabeza en forma de gancho, de unos 8 µm en ratón). En cada imagen aparecen:

- **Cabezas** en rojo o anaranjado. Son lo que se cuenta y se mide.
- **Colas (flagelos)** en verde-amarillo, como líneas largas. No se cuentan.
- **Manchas rojas difusas** grandes, probablemente otras células o material fuera de foco. No se cuentan.
- **Cabezas encimadas** entre sí o sobre las colas, que hay que separar.

### Clasificador de imágenes

- **Detección:** localiza cada cabeza y obtiene su contorno, ignorando colas y manchas.
- **Conteo:** número de cabezas en la imagen.
- **Tamaño:** mide cada cabeza en micrómetros (µm), la unidad habitual en espermatozoides. Como las cabezas son curvas, se reportan el área y la longitud a lo largo de la curva hasta acordar cuál usar.
- **Distribución de tamaños:** gráfica tipo campana de Gauss con la frecuencia de cada tamaño.
- **Clasificación por color:** cuenta cuántas cabezas son rojas y cuántas anaranjadas, a partir de la proporción de rojo y verde medida dentro de cada contorno.
- **Exportación:** resultados descargables en CSV y PDF, con el conteo y las medidas de cada cabeza.

### Sitio web

- Título *Image Bio Pro* y menú tipo hamburguesa con Inicio, Nosotros, Aliados, Contacto y la página de Inteligencia Artificial.
- Selector de idioma EN/ES.
- **Nosotros:** qué es Image Bio Pro.
- **Aliados:** personas del grupo, con nombre y foto, en tarjetas.
- **Contacto:** formulario con nombre, correo y mensaje.
- **Infografías:** tarjetas que se despliegan para mostrar texto con imagen, como un blog informativo. El título va fuera de la imagen.
- **Videos:** unos cuatro videos de YouTube de unos cuatro minutos, incrustados en la propia página.
- **Página de IA:** imagen de fondo, carga de imagen y botón para analizarla. Si hacen falta parámetros ajustables, se agregan después.
- **Cuentas:** registro e inicio de sesión con correo electrónico, sin vincularlo a Gmail. Los análisis de cada usuario son privados: solo los ve quien los hizo.
- **Contenido:** el cliente lo entrega y lo irá actualizando con el tiempo. Mientras tanto, los textos e imágenes se llenan con Lorem Ipsum y marcadores de posición.
- Estilo sencillo y funcional. La página FEMEXER sirve solo de guía de estructura, no de diseño.

## Cómo está planteado

```
Navegador  ->  Flask (páginas, cuentas, carga de imagen)  ->  Red de segmentación (PyTorch)
                          |                                          |
                          +->  Base de datos (SQLite)                +->  Medición y color por cabeza
                                                                     |
                                                                     +->  Gráfica, CSV y PDF
```

### Modelo

- **Una sola red neuronal de segmentación por instancias**, partiendo de un modelo preentrenado y ajustándolo con las imágenes del cliente (*transfer learning*). Opción principal: YOLO de segmentación (Ultralytics). Alternativa: Mask R-CNN de torchvision, según la licencia (ver pendientes).
- La red detecta solo la clase "cabeza". El color y el tamaño se **miden** dentro de cada contorno con OpenCV y numpy, para que el resultado sea verificable. Si el cliente define un criterio de clasificación que no sea solo el color, la red se reentrena con dos clases.
- **Datos para entrenar:** cada imagen tiene del orden de 150 cabezas, así que 10 imágenes ya dan más de mil ejemplos anotados.
- **Anotación:** con CVAT o Label Studio, que no publican los datos. Alguien del grupo valida las anotaciones.
- **Entrenamiento:** en Google Colab. En el servidor solo se hace inferencia, en CPU, del orden de un segundo por imagen.
- **Reentrenamiento:** el modelo no aprende en línea. Para nuevas imágenes, otras tinciones u otro tipo de célula hay que reentrenar en Colab y volver a subir los pesos.

### Sitio

- **Flask** con plantillas Jinja2 y **Bootstrap**. Sin framework de frontend.
- **Cuentas:** Flask-Login, con contraseñas cifradas.
- **Formularios:** Flask-WTF, con protección CSRF. El formulario de contacto envía correo por SMTP.
- **Base de datos:** SQLite con Flask-SQLAlchemy.
- **Gráficas:** Chart.js en la página y matplotlib para el PDF.
- **PDF:** fpdf2. **CSV:** módulo `csv` de Python.
- **Videos:** `<iframe>` de YouTube.

### Despliegue

- **VPS** con Ubuntu, Nginx como proxy inverso, Gunicorn y HTTPS con Certbot. El hosting compartido no sirve, porque no puede correr Flask con PyTorch.
- Tamaño recomendado: 2 vCPU y 2 a 4 GB de RAM.
- Ajustes necesarios: timeout de Gunicorn de unos 120 s, `client_max_body_size` de Nginx de unos 20 MB, y limitar los hilos de PyTorch por proceso.
- Capacidad estimada: cientos de visitantes navegando y varios análisis a la vez. Para un grupo de investigación sobra. Se confirma midiendo en el servidor.

## Servicios

Los contrata el cliente, con la recomendación del desarrollador para no pagar de más.

- **VPS:** unos 100 a 250 MXN al mes, según el proveedor.
- **Dominio:** unos 200 a 400 MXN al año.
- **Google Colab:** con este tamaño de datos basta el plan económico (unos 300 MXN). Solo si se queda corto se pasa al de unos 1,100 MXN al mes.

## Datos

- Hasta ahora el cliente solo ha compartido una imagen de ejemplo, en JPEG por WhatsApp: comprimida y sin escala.
- Primera entrega: un modelo esqueleto entrenado con unas 10 imágenes. Sirve para mostrar el flujo completo y **no tiene validez científica**.
- Entrenamiento real: con un siguiente lote de unas 50 imágenes que generará el cliente, probablemente hacia enero de 2027.
- Las imágenes del cliente no se suben a este repositorio.

## Capacitación

El proyecto incluye 10 horas de capacitación en línea para el cliente y de 5 a 10 alumnos: uso del sistema, cómo se construyó y cómo reentrenar el modelo. El temario y los materiales están en [`docs/capacitacion/`](docs/capacitacion/README.md).

## Posibles extensiones

Fuera del alcance actual. El cliente las plantea como perspectiva.

- **Control contra tratamiento:** una CNN de clasificación binaria que distinga muestras de control (sanas) de muestras con tratamiento, según la forma, el tamaño y la distribución de tamaños de las células.
- **Modelo multimodal:** combinar las imágenes con datos numéricos de la misma muestra (AnnData/Scanpy). Sería un proyecto aparte, solo el modelo, sin plataforma. El cliente pidió saber si es viable y qué tan difícil sería.

## Pendientes por definir

- **Tinciones:** qué marca el rojo y qué marca el verde.
- **Significado del anaranjado:** qué indica biológicamente una cabeza anaranjada. En la imagen de ejemplo las anaranjadas se concentran donde hay muchas colas encimadas, así que parte del color podría ser mezcla por superposición.
- **Imágenes originales:** archivos del microscopio (por ejemplo TIFF) sin compresión, con el aumento usado o una barra de escala para convertir píxeles a µm.
- **Tamaño:** si se reporta el área, la longitud a lo largo de la curva o ambas. Confirmar que la unidad es µm.
- **Licencia:** Ultralytics es AGPL-3.0, que obliga a publicar el código del sitio si se sirve en línea. Si el cliente no lo acepta, se usa Mask R-CNN (licencia BSD).
- **Traducción:** el cliente pidió la API de Google Traductor. Como son pocos textos, se propone un archivo de traducciones ES/EN, que traduce mejor los términos científicos y no tiene costo.
- Correo al que llegarán los mensajes del formulario de contacto.
- Dominio definitivo del sitio.

## Estructura prevista

```
app/         sitio en Flask: rutas, plantillas, estilos y lógica de análisis
model/       notebooks de entrenamiento y pesos del modelo
docs/        documentación del proyecto y material de capacitación
```

La estructura puede cambiar al empezar el desarrollo.

## Desarrollo

Instrucciones de instalación y ejecución: pendientes, se agregan cuando exista el primer código.

## Autor

Ing. Angel Frausto Robles
