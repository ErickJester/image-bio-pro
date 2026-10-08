# Ingeniería de software — Qué hacer después del boceto

Fecha: 7 de octubre de 2026. Lección transversal: aplica a todo el proyecto, no a un módulo.

## Qué aprendimos

Con el boceto terminado, la pregunta fue: según la ingeniería de software, ¿qué se hace primero?

## Conceptos nuevos

### Prototipo de baja fidelidad

El boceto no es el inicio del sitio: es un **prototipo de baja fidelidad**, una herramienta para **validar requisitos**, es decir, confirmar con el cliente que se entendió qué quiere antes de construirlo.

Los errores más caros en software son los de requisitos: construir bien algo que no era. Mover una caja gris en el boceto cuesta minutos; cambiar algo ya programado cuesta horas. Pasó en este mismo proyecto: el primer boceto tenía elementos que nadie pidió y le faltaba la sección de infografías y videos.

### Validación de requisitos

Mandar el boceto al cliente **junto con las preguntas pendientes**. Sus respuestas se vuelven el acuerdo de requisitos. Si después pide algo distinto, es un **cambio de alcance**, no un error del desarrollador.

### Desarrollo guiado por riesgo

Empezar por **lo que más probablemente salga mal**, no por lo más fácil.

| Parte | Riesgo | Por qué |
|---|---|---|
| Sitio web (páginas, menú, contacto) | Bajo | Ya se sabe cómo se ve; trabajo conocido |
| Cuentas, PDF, CSV | Bajo-medio | Hay librerías y tutoriales |
| Despliegue en el VPS | Medio | Siempre aparecen sorpresas del servidor |
| Detectar y medir cabezas en las imágenes | **Alto** | No se sabe si funciona bien con estas imágenes: colas encimadas, manchas, pocas imágenes |

### Spike

Un experimento corto para responder "¿se puede?" antes de comprometerse. Aquí: tomar la imagen real y ver qué tan bien se detectan y miden las cabezas (módulos 2 y 3). Si sale mal, se sabe el día 9 y no el 27.

### Esqueleto que camina (*walking skeleton*)

La versión más delgada del flujo completo, de punta a punta: subir imagen → análisis básico → ver resultado, **ya publicada en el servidor**. Fea pero completa. Sirve para que las piezas se integren desde el principio y para que el cliente vea algo real funcionando.

### Desarrollo incremental

Sobre el esqueleto se agrega una mejora a la vez, cada una funcionando antes de pasar a la siguiente (modelo YOLO, cuentas, PDF, contenido, traducción). Si el tiempo se acaba, lo que falta es lo menos importante y lo que existe funciona.

### Requisitos priorizados (historias de usuario)

Una lista de lo acordado, escrita como historias de usuario ("como investigador quiero subir una imagen para obtener el conteo") y con prioridad: **debe tener**, **debería tener**, **puede esperar**. Sirve para decidir qué recortar si el tiempo aprieta.

### Requisitos funcionales y no funcionales

Los requisitos se dividen en dos tipos:

- **Funcionales:** lo que el sistema **hace**. Ejemplo: "el sistema cuenta las cabezas detectadas".
- **No funcionales:** **cómo** lo hace o qué condiciones cumple: rapidez, seguridad, facilidad de uso, dónde corre. Ejemplo: "el análisis tarda como máximo unos 30 segundos".

Cada requisito lleva un identificador (RF-01, RNF-01…) para poder citarlo, y la frase del cliente de donde sale.

**Los requisitos salen del cliente, no del programador.** En la primera versión del documento se mezclaron decisiones técnicas propias (tiempos de respuesta, tamaño máximo de archivo, HTTPS, recuperar contraseña) con lo que pidió el cliente. Eso es un error: las decisiones técnicas son **diseño** y van aparte. Si un requisito no se puede rastrear a algo que dijo el cliente, no es un requisito, es una suposición. Lo ambiguo o sin respuesta va en una lista de **pendientes** para preguntarle, y las propuestas propias se marcan como propuestas.

Los del proyecto están en [`docs/requisitos.md`](../requisitos.md): 21 funcionales y 5 no funcionales, cada uno con su cita de la reunión, más restricciones, lo que queda fuera de alcance y los pendientes.

## Orden de trabajo que sale de esto

1. Mandar al cliente el PDF del boceto con las preguntas pendientes.
2. Terminar el módulo 1 y hacer el spike con la imagen real (módulos 2 y 3).
3. Armar el esqueleto que camina y publicarlo en el VPS.
4. Agregar incrementos en orden de prioridad.

## Lo que no entendí / dudas

-

## Cómo lo explicaría en la capacitación

> Primero hicimos un boceto para confirmar con el cliente qué quería, porque corregir un dibujo es barato y corregir código es caro. Luego atacamos lo más incierto, que era si la computadora podía reconocer y medir las cabezas, y después armamos una versión completa pero sencilla del sistema, que fuimos mejorando paso a paso.
