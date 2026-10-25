# 01 · Resumen del proyecto

**Cómo usar esta base:** el asistente responde preguntas en vivo durante una exposición por videollamada. El público son unas 6 o 7 personas (quizá hasta 40) de distintas áreas de la universidad, y la sesión se graba y se publica en redes. Las respuestas deben ser breves, concretas y en lenguaje sencillo. Si la pregunta es muy técnica, dar la idea general y ofrecer verla al final. No afirmar nada que no esté en estos archivos; si falta el dato, decir "dato no disponible". Los datos marcados con [COMPLETAR] se desconocen.

## Qué es
BioImage-Repro UAM es un sitio web bilingüe (español e inglés) que analiza fotografías de microscopía de espermatozoides. Detecta cada espermatozoide, los cuenta, mide su área y su largo, dibuja la distribución de tamaños en un histograma y exporta los resultados en CSV y PDF.

## Problema que resuelve
Contar y medir a mano es lento y repetitivo, y el resultado cambia según quién lo haga. El sitio aplica siempre el mismo procedimiento a la misma imagen.

## Para quién
Se hizo para un grupo de investigación de la UAM Iztapalapa. En la exposición se presenta como **caso de estudio de inteligencia artificial** para la comunidad universitaria: contar espermatozoides es el ejemplo, no el único uso posible de la técnica.

## Objetivo
Que una persona suba sus fotos, sin programar, y obtenga conteo, medidas, histograma y reportes reproducibles.

## Alcance logrado
- Cuentas privadas con contraseña cifrada.
- Hasta 10 imágenes por análisis (300 MB por envío; formatos BMP, PNG, TIFF; JPG con aviso).
- Conteo, área y largo por espermatozoide, con media y desviación estándar.
- Histograma por imagen y de promedios entre imágenes.
- Imagen marcada y numerada, con zoom y detalle al pasar el mouse.
- Descarga de CSV y de un PDF único; sección "Mis análisis".
- Imagen de ejemplo sintética para probar sin subir nada.

## Fuera de alcance o pendiente
El sitio no interpreta resultados ni es un analizador general de células. El color se calcula pero no se muestra. No mide de cabeza a cola. No avisa si la imagen no es de espermatozoides. La comparación control contra tratamiento es una posible extensión.

## Datos del proyecto
- Desarrollador: Ing. Angel Frausto Robles.
- Entrega: 28 de octubre de 2026.
- Exposición en cuatro sesiones de dos horas (ocho en total): 23 de octubre (6 a 8 pm), 24 de octubre (9 a 11 am), 26 de octubre (6 a 8 pm) y 27 de octubre (6 a 8 pm).
  1. El problema y el sitio: caso de estudio, por qué una plataforma web, imagen digital, demostración y resultados.
  2. Cómo aprende la red: umbral como primer intento, red convolucional, aprendizaje, descenso del gradiente, Mask R-CNN y transfer learning.
  3. Cómo funciona por dentro: servidor Flask, inferencia, medición, retos y cómo se resolvieron.
  4. Datos, anotación en CVAT, reentrenamiento en Colab, despliegue (VPS, Docker, Nginx) y cierre.

## Tres principios del proyecto
1. **No suponer:** si falta un dato, el sitio lo declara.
2. **La red localiza, el código mide:** las medidas se calculan con código determinista dentro de cada contorno.
3. **Reproducibilidad:** la misma imagen da el mismo resultado.
