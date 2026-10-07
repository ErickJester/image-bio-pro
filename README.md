# Image Bio Pro

Sitio web bilingüe (español/inglés) con un clasificador de imágenes de microscopio. El usuario sube una foto de una muestra de espermatozoides y el sistema cuenta las células, mide su tamaño, muestra la distribución de tamaños y clasifica las células por color.

Proyecto desarrollado para un grupo de investigación de la UAM Unidad Xochimilco.

> **Estado:** en planeación. Aún no hay código. El primer entregable (sitio en línea y avances del clasificador con un modelo de muestra) está previsto para el 29 o 30 de octubre de 2026.

## Qué hace

### Clasificador de imágenes

- **Entrada:** imagen de microscopio con espermatozoides teñidos en tonos rojo, amarillo y naranja.
- **Conteo:** cuenta las células (cada una aparece como una bolita anaranjada).
- **Descarte de ruido:** ignora los puntos y líneas del fondo, que son ruido del microscopio y no son células.
- **Tamaño:** mide cada célula en micrómetros (µm), la unidad habitual en espermatozoides. Falta confirmarla con el cliente.
- **Distribución de tamaños:** gráfica tipo campana de Gauss con la frecuencia de cada tamaño.
- **Clasificación por color:** cuenta cuántas células son anaranjadas y cuántas rojas, según la intensidad. En las imágenes oficiales la diferencia de tono puede ser más sutil.
- **Exportación:** resultados descargables en CSV y PDF. Como mínimo, un archivo con el conteo y las medidas de cada célula.

### Sitio web

- Título *Image Bio Pro* y menú tipo hamburguesa con Inicio, Nosotros, Aliados, Contacto y la página de Inteligencia Artificial.
- Selector de idioma EN/ES, con traducción automática mediante la API de Google Traductor.
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
Navegador  ->  Frontend  ->  API REST (Flask)  ->  Modelo (PyTorch)
                                    |
                                    +->  Reporte PDF / CSV
```

- **Frontend:** páginas del sitio, carga de imagen con `fetch` y despliegue de resultados.
- **Backend:** Flask como API REST. Recibe la imagen en base64, la convierte a tensor, corre el modelo y responde en JSON. También maneja el registro y el inicio de sesión.
- **Modelo:**
  - Segmentación por instancias para localizar y contar células.
  - Histograma de áreas para el tamaño y su distribución.
  - Clasificación de cada célula por color (anaranjada o roja).
- **Entrenamiento:** en Google Colab. En el servidor solo se hace inferencia, en CPU.
- **Reentrenamiento:** el modelo no aprende en línea. Para nuevas imágenes, otros tipos de célula u otras tinciones hay que reentrenar en Colab y volver a subir los pesos.
- **Despliegue:** VPS con Gunicorn y un proxy inverso, con HTTPS y dominio propio.

## Servicios

Los contrata el cliente, con la recomendación del desarrollador para no pagar de más.

- **Hosting y dominio:** plan tipo Hostinger, con pago anual de menos de 1,000 MXN.
- **Google Colab:** el plan económico (unos 300 MXN) para el modelo esqueleto con 10 imágenes y el plan de unos 1,100 MXN al mes cuando llegue el lote de 50 imágenes.

## Datos

- Hasta ahora el cliente solo ha compartido una imagen de ejemplo.
- Primera entrega: un modelo esqueleto entrenado con unas 10 imágenes. Sirve para mostrar el flujo completo y **no tiene validez científica**.
- Entrenamiento real: con un siguiente lote de unas 50 imágenes que generará el cliente, probablemente hacia enero de 2027. Está por ver si ese número alcanza.
- Las imágenes del cliente no se suben a este repositorio.

## Posibles extensiones

Fuera del alcance actual. El cliente las plantea como perspectiva.

- **Control contra tratamiento:** una CNN de clasificación binaria que distinga muestras de control (sanas) de muestras con tratamiento, según la forma, el tamaño y la distribución de tamaños de las células.
- **Modelo multimodal:** combinar las imágenes con datos numéricos de la misma muestra (AnnData/Scanpy). Sería un proyecto aparte, solo el modelo, sin plataforma. El cliente pidió saber si es viable y qué tan difícil sería.

## Pendientes por definir

- Confirmar con el cliente que la unidad de medida es micrómetros.
- Correo al que llegarán los mensajes del formulario de contacto.
- Dominio definitivo del sitio.

## Estructura prevista

```
frontend/    páginas, estilos y scripts del sitio
backend/     API en Flask y lógica de inferencia
model/       código de entrenamiento y pesos del modelo
docs/        documentación del proyecto
```

La estructura puede cambiar al empezar el desarrollo.

## Desarrollo

Instrucciones de instalación y ejecución: pendientes, se agregan cuando exista el primer código.

## Autor

Ing. Angel Frausto Robles
