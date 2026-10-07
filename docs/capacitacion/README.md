# Capacitación

10 horas de capacitación para el cliente y un grupo de 5 a 10 alumnos. Cubre el uso del sistema y cómo se construyó, para que el grupo pueda usarlo, entender sus resultados y reentrenar el modelo sin depender del desarrollador.

## Participantes

- Perfil mixto: algo de programación y algo de biología.
- Por eso cada sesión parte de la intuición y del caso biológico antes de pasar al código, y el código se ejecuta ya escrito para que nadie se atore con la sintaxis.

## Modalidad

- En línea, por videollamada.
- 5 sesiones de 2 horas, a partir de las 18:00. La hora exacta de inicio la define el cliente.
- Cada sesión es mitad explicación y mitad práctica, con una pausa de 5 a 10 minutos a la mitad.
- Las prácticas se hacen en Google Colab: los participantes solo necesitan una cuenta de Google y abrir un enlace, sin instalar nada. Los enlaces se comparten antes de cada sesión.
- Todas las sesiones se graban.

## Calendario y temario

La capacitación se da después de construir el sistema (del 8 al 16 de octubre), así que empieza por el uso y termina por cómo se construyó. Fechas propuestas al cliente, por confirmar. El 28 de octubre queda libre para la entrega.

| Sesión | Fecha (2026) | Tema | Práctica |
|---|---|---|---|
| 1 | Sábado 17 de octubre | Panorama del proyecto y uso del sistema: cuentas, carga de imagen, lectura de resultados, exportación a CSV y PDF. Límites: calidad de imagen, escala en µm y validez del modelo. | Cada participante analiza imágenes en el sitio y exporta resultados. |
| 2 | Martes 20 de octubre | Imágenes digitales y medición: píxeles, canales de color, fluorescencia, escala en µm, contornos, área, longitud y color rojo/verde. Repaso breve de Python y Colab. | Medir cabezas en un notebook. |
| 3 | Jueves 22 de octubre | Redes neuronales: qué es una red convolucional, explicada con intuición. Transfer learning y segmentación por instancias con YOLO. | Correr el modelo y revisar qué detecta y qué no. |
| 4 | Sábado 24 de octubre | Datos y entrenamiento: anotación en CVAT, conjuntos de entrenamiento, validación y prueba, métricas y sobreajuste. Por qué importa la cantidad de imágenes. | Anotar imágenes y reentrenar el modelo siguiendo la guía. |
| 5 | Martes 27 de octubre | Construcción del sitio y cierre: arquitectura (navegador, Flask, modelo y base de datos), servidor y actualización del modelo en producción. Etapas posteriores del proyecto. | Recorrido por el código y preguntas abiertas. |

La sesión 4 es la más importante para el grupo: el modelo no aprende solo, y saber reentrenarlo es lo que le da independencia.

## Pendientes con el cliente

- Confirmar las fechas propuestas.
- Hora de inicio de las sesiones.
- Número de participantes.
- Plataforma de videollamada y quién envía el enlace.

## Materiales

Se preparan a partir del trabajo de desarrollo, no por separado. El material de cada sesión se termina a más tardar el día anterior.

- [ ] Manual de usuario, corto y con capturas (sesión 1).
- [ ] Notebook de medición (sesión 2).
- [ ] Notebook del modelo de segmentación (sesión 3).
- [ ] Guía y notebook de anotación y reentrenamiento (sesión 4).
- [ ] Recorrido del código del sitio (sesión 5).
- [ ] Diapositivas por sesión.
- [ ] Grabaciones de las sesiones.
