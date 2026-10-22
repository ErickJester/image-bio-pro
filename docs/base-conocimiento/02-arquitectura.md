# 02 · Arquitectura y tecnologías

## Flujo general
Navegador → Nginx → Gunicorn → aplicación Flask → modelo (detección) → medición → resultados (pantalla, CSV, PDF).

## Servidor y despliegue
- VPS de Hostinger, plan **KVM 1** (un núcleo de CPU). Cifras exactas de RAM y precio: [COMPLETAR].
- Ubuntu con Docker, Nginx como proxy, HTTPS con Certbot.
- Gunicorn con un solo proceso y 4 hilos, tiempo máximo de 1800 s por petición. Se usa un solo proceso porque cada modelo ocupa unos 176 MB en memoria y varios procesos los duplicarían.
- Nginx acepta envíos de hasta 300 MB.
- Solo hay inferencia en el servidor, en CPU. No hay GPU.

## Sitio web
- Flask con plantillas Jinja2 y Bootstrap.
- Flask-Login para sesiones; las contraseñas se guardan cifradas (mínimo 8 caracteres).
- Flask-WTF para protección CSRF.
- SQLite con SQLAlchemy como base de datos.
- Traducción de la interfaz con el servicio de Google.
- Gráficas en pantalla con Chart.js; gráficas del PDF con matplotlib y fpdf2.

## Modelos
- Red de segmentación por instancias **Mask R-CNN** de PyTorch/torchvision, entrenada en Google Colab (`entrenamiento/entrenar_mask_rcnn.ipynb`).
- Dos modelos de unos 176 MB cada uno, fuera de git: `fluorescencia.pt` (fondo oscuro, teselas de 512 px) y `campo_claro.pt` (fondo claro, teselas de 640 px con la foto reducida a la mitad).
- **Selección de modelo:** una regla de brillo, no aprendizaje. Si la mediana del máximo de R, G y B de la foto es mayor a 127, el fondo es claro y se usa campo claro; si no, fluorescencia.
- **Inferencia por teselas:** la foto se corta en recortes con traslape, la red procesa cada uno, se unen los contornos y se eliminan los repetidos del traslape.

## Medición
OpenCV y numpy, dentro de cada contorno:
- **Área:** número de píxeles de la máscara.
- **Largo:** lado mayor del rectángulo mínimo que encierra el contorno (`cv2.minAreaRect`).
- **Micras:** se dividen los píxeles entre una escala común de 60 px = 1 µm (el área entre 60²). La imagen marcada lleva una regla de 300 px, equivalente a 5 µm.
- **Histograma:** siempre 10 intervalos de igual ancho entre el mínimo y el máximo; con varias imágenes se usa un rango común para poder compararlas. El eje horizontal está en píxeles.

## Respaldo por umbral
Si faltan los modelos, el sitio usa una detección por umbral de color (OpenCV) y muestra un aviso rojo diciendo que el conteo no es confiable.

## Qué se guarda
Las imágenes subidas se **borran al terminar** el análisis. Se conservan los resultados, el PDF y una copia reducida de la imagen marcada, visibles solo para quien hizo el análisis.

## Pantalla de espera
Mientras se analiza, el sitio avisa que puede tardar de segundos a varios minutos; pasado un minuto añade "Tu análisis sigue en curso".
