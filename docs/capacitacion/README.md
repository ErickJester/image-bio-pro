# Capacitación

10 horas de capacitación para el cliente y un grupo de 5 a 10 alumnos. Cubre el uso del sistema y cómo se construyó, para que el grupo pueda usarlo, entender sus resultados y reentrenar el modelo sin depender del desarrollador.

## Participantes

- Perfil mixto: algo de programación y algo de biología.
- Por eso cada sesión parte de la intuición y del caso biológico antes de pasar al código, y el código se ejecuta ya escrito para que nadie se atore con la sintaxis.

## Modalidad

- En línea, por videollamada.
- Las prácticas se hacen en Google Colab: los participantes solo abren un enlace, sin instalar nada.
- Todas las sesiones se graban.

## Temario

5 sesiones de 2 horas.

| Sesión | Tema | Contenido | Práctica |
|---|---|---|---|
| 1 | Uso del sistema | Qué hace y qué no. Cuentas, carga de imagen, lectura de resultados, exportación a CSV y PDF. Límites: calidad de imagen, escala en µm y validez del modelo. | Cada participante analiza imágenes y revisa los resultados. |
| 2 | Imágenes digitales y procesamiento clásico | Píxeles, canales de color, umbral, eliminación de ruido, conteo y medición, conversión de píxeles a µm. Repaso breve de Python y Colab. | Contar las células de la imagen de ejemplo paso a paso. |
| 3 | Redes neuronales | Qué es una red convolucional, explicada con intuición. Transfer learning. Cómo funcionan los modelos del sistema. | Correr el modelo de segmentación y compararlo con el método clásico. |
| 4 | Datos y entrenamiento | Anotación de imágenes. Conjuntos de entrenamiento, validación y prueba. Métricas. Sobreajuste. Por qué importa la cantidad de imágenes. | Reentrenar el modelo siguiendo la guía. |
| 5 | Construcción del sitio y cierre | Arquitectura: navegador, Flask, modelo y base de datos. Servidor y actualización del modelo en producción. Posibles extensiones. | Recorrido por el código y preguntas abiertas. |

La sesión 4 es la más importante para el grupo: el modelo no aprende solo, y saber reentrenarlo es lo que le da independencia.

## Calendario

- **Sesión 1:** después de la primera entrega (finales de octubre de 2026), con el sitio en línea.
- **Sesiones 2 a 5:** cuando el modelo esté entrenado con el lote real de imágenes.

## Materiales

Se preparan a partir del trabajo de desarrollo, no por separado.

- [ ] Manual de usuario, corto y con capturas.
- [ ] Notebook de procesamiento clásico (sesión 2).
- [ ] Notebook de redes neuronales (sesión 3).
- [ ] Guía y notebook de reentrenamiento (sesión 4).
- [ ] Diapositivas por sesión.
- [ ] Grabaciones de las sesiones.
