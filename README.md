# Image Bio Pro

Sitio web bilingüe (español/inglés) con un clasificador de imágenes de microscopio. El usuario sube una foto de una muestra de espermatozoides y el sistema cuenta las células, mide su tamaño, muestra la distribución de tamaños y dice si la muestra parece de control o con tratamiento.

Proyecto desarrollado para un grupo de investigación de la UAM Unidad Xochimilco.

> **Estado:** en planeación. Aún no hay código. El primer entregable (sitio en línea con un modelo de muestra) está previsto para finales de octubre de 2026.

## Qué hace

### Clasificador de imágenes

- **Entrada:** imagen de microscopio con espermatozoides teñidos en tonos rojo, amarillo y naranja.
- **Conteo:** cuenta las células (cada una aparece como una bolita anaranjada).
- **Descarte de ruido:** ignora los puntos y líneas del fondo, que son ruido del microscopio y no son células.
- **Tamaño:** mide cada célula. La unidad (milímetros o micrómetros) está por confirmar con el cliente.
- **Distribución de tamaños:** gráfica tipo campana de Gauss con la frecuencia de cada tamaño.
- **Clasificación:** distingue muestras de **control** (sanas) de muestras **con tratamiento**, según forma, tamaño y si la cabeza "sale del agua".
- **Reporte en PDF:** resumen descargable con los resultados del análisis.

### Sitio web

- Menú superior con Inicio, Nosotros, Aliados, Contacto y la página de Inteligencia Artificial.
- Selector de idioma EN/ES, con traducción automática mediante la API de Google Traductor.
- **Nosotros:** qué es Image Bio Pro.
- **Aliados:** personas del grupo, con nombre y foto, en tarjetas.
- **Contacto:** formulario con nombre, correo y mensaje.
- **Infografías:** tarjetas que se despliegan para mostrar texto con imagen, como un blog informativo.
- **Videos:** unos cuatro videos cortos de YouTube incrustados en la propia página.
- **Página de IA:** carga de imagen y botón para analizarla.
- Estilo sencillo y funcional. La página FEMEXER sirve solo de guía de estructura, no de diseño.

## Cómo está planteado

```
Navegador  ->  Frontend  ->  API REST (Flask)  ->  Modelo (PyTorch)
                                    |
                                    +->  Reporte PDF
```

- **Frontend:** páginas del sitio, carga de imagen con `fetch` y despliegue de resultados.
- **Backend:** Flask como API REST. Recibe la imagen en base64, la convierte a tensor, corre el modelo y responde en JSON.
- **Modelo:**
  - Segmentación por instancias para localizar y contar células.
  - Histograma de áreas para el tamaño y su distribución.
  - Red convolucional (CNN) de clasificación binaria, control contra tratamiento.
- **Entrenamiento:** en Google Colab. En el servidor solo se hace inferencia, en CPU.
- **Despliegue:** VPS con Gunicorn y un proxy inverso, con HTTPS y dominio propio.

## Datos

- Hasta ahora el cliente solo ha compartido una imagen de ejemplo.
- Primera entrega: un modelo esqueleto entrenado con unas 10 imágenes. Sirve para mostrar el flujo completo y **no tiene validez científica**.
- Entrenamiento real: con un siguiente lote de unas 50 imágenes que generará el cliente. Está por ver si ese número alcanza.
- Las imágenes del cliente no se suben a este repositorio.

## Pendientes por definir

- Unidad de medida del tamaño de las células.
- Criterios exactos para distinguir control de tratamiento.
- Si el sitio tendrá inicio de sesión y qué podrá hacer cada usuario.
- Correo al que llegarán los mensajes del formulario de contacto.
- Dominio definitivo del sitio.
- Textos, fotos, infografías y enlaces de videos, que entrega el cliente.

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
