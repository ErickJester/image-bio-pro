# Guion de la sesión 1: Introducción y comienzo de redes neuronales (versión 3)

Image Bio Pro · Capacitación · viernes 23 de octubre de 2026, de 6:00 a 8:00 pm

Esta sesión es la primera de cuatro. Presenta el problema, la idea de imagen digital, algunas definiciones de inteligencia artificial y el comienzo de las redes neuronales. Las redes convolucionales y cómo se aprovecha una red entrenada para otra cosa se ven en la sesión 2; el sitio funcionando, en la sesión 3; datos, entrenamiento y despliegue, en la sesión 4.

## Cómo usar este guion

Todo lo que no va entre corchetes ni en un recuadro se dice tal cual está escrito, al pie de la letra. En azul van los cambios de diapositiva. En el recuadro amarillo, debajo de cada diapositiva, va la idea central de esa diapositiva: no se dice en voz alta, sirve para ubicarse antes de hablar.

La portada la presenta Saúl y te cede la palabra. Tú empiezas en la diapositiva 2. La apertura es la que Saúl modeló, sin cambios.

Ritmo considerado: 175 palabras por minuto. Cada bloque trae sus palabras y el tiempo que ocupan hablando. Si el tiempo se acaba antes de terminar, se dice «hasta aquí llegamos, mañana seguimos» y se retoma en la siguiente sesión.

---

## Bloque 1. Bienvenida

*471 palabras, unos 2.7 min de habla*

[Diapositiva · Image Bio Pro]

> Idea central: Todo el curso gira alrededor de un solo proyecto, Image Bio Pro. En la portada habla Saúl; tú tomas la palabra en la siguiente diapositiva.

[Diapositiva · ¿Qué es Image Bio Pro?]

> Idea central: Image Bio Pro es un proyecto de la UAM que lleva la inteligencia artificial a la docencia, la investigación, la difusión de la cultura y el servicio a la comunidad universitaria.

Buenas tardes a todos. Muchísimas gracias por la presentación, doctor Saúl. Muchas gracias también a los profesores, a la doctora Sheila y al doctor Saúl, por la oportunidad de poder presentar este proyecto tan importante para la universidad.

Me presento. Mi nombre es Ángel Frausto Robles, soy ponente y parte del equipo que desarrolló este sitio web. Soy egresado de la Escuela Superior de Cómputo del Instituto Politécnico Nacional, especializado en temas de visión por computadora e inteligencia artificial.

El día de hoy les voy a platicar de lo que es el proyecto Image Bio Pro, que está impulsando la Universidad Autónoma Metropolitana para promover proyectos de inteligencia artificial en el desempeño de las funciones de docencia, investigación y preservación y difusión de la cultura, así como de vinculación y servicio a la comunidad universitaria.

Quizás la primera pregunta que se hagan es: ¿qué es Image Bio Pro? Bueno, básicamente es una nueva plataforma web que tiene como objetivo incorporar los nuevos conceptos de inteligencia artificial para abordar, estudiar y apoyar las actividades de docencia, de investigación y de preservación y difusión de la cultura en la comunidad universitaria de la UAM Iztapalapa. Es la nueva era de la inteligencia artificial al servicio de la comunidad universitaria.

[Diapositiva · Las cuatro sesiones]

> Idea central: Son cuatro sesiones: hoy el problema y las bases teóricas, mañana cómo aprende una computadora, el lunes el sitio funcionando y el martes datos, entrenamiento y despliegue.

Este proyecto lo voy a presentar a lo largo de cuatro sesiones. Antes que nada, les platico lo que vamos a ir viendo en ellas.

En la primera sesión vamos a ver el problema que intentamos resolver, y les platicaré las bases teóricas que ocupamos para diseñar el sitio web.

En la segunda sesión vamos a ver, y lo resumo en una palabra, cómo aprende una computadora, que es la esencia de una red neuronal artificial.

En la tercera sesión vamos a ver cómo funciona esta plataforma web. Una vez que ya entendimos el problema y exploramos las bases teóricas, ahora sí les presentaré cómo funciona el sistema.

Y en la cuarta sesión veremos un par de ejemplos con datos, cómo se entrena la red neuronal y cómo es el despliegue de la información.

Quisiera pedirles que me den la oportunidad de cautivarlos para poder presentarles el sitio web en la tercera sesión. Me gustaría que primero tuvieran todo el background, todas las bases teóricas que nos permitieron desarrollar este sitio, para que cuando lo visiten sepan el trabajo y el enfoque de inteligencia artificial que utilizó esta plataforma. Espero que me puedan acompañar en estas cuatro sesiones.

[Diapositiva · La agenda de hoy]

> Idea central: Hoy: el problema, qué es una imagen digital, algunas definiciones de inteligencia artificial y el comienzo de las redes neuronales. El sitio funcionando se presenta en la tercera sesión.

La agenda del día de hoy: primero quisiera presentarles el problema, y después comenzamos explicando qué es una imagen digital.

Después de la imagen digital vamos a poner en orden algunas definiciones de inteligencia artificial, y con eso empezamos con las redes neuronales: qué es una neurona, qué es una capa y cómo se arma una red. El sitio funcionando lo vemos en la tercera sesión.

---

## Bloque 2. El problema

*979 palabras, unos 5.6 min de habla*

[Diapositiva · La inteligencia artificial en la educación y la investigación]

> Idea central: La inteligencia artificial puede analizar imágenes aprendiendo de ejemplos y no de reglas escritas, y lo hace sin cansarse. En este curso se ve aplicada a un problema real de biología de la reproducción.

Empiezo con una pregunta, y no hace falta que la contesten en voz alta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Hay muchas respuestas, y una de ellas, que es la que nos interesa hoy, es analizar imágenes. Una persona mira una imagen y reconoce lo que hay en ella. Un programa que aprendió de muchos ejemplos puede hacer algo parecido, y puede hacerlo muchas veces seguidas sin cansarse.

Vale la pena detenernos un momento en qué quiere decir aprender de ejemplos, porque es la idea que sostiene todo el curso. Tradicionalmente, cuando uno quiere que una computadora haga algo, le escribe reglas: si pasa esto, haz aquello. Eso funciona muy bien para una calculadora o para una hoja de cálculo, donde las reglas son exactas. Pero para reconocer un espermatozoide en una imagen, escribir las reglas es casi imposible. ¿Cómo describirían ustedes, con reglas exactas, la forma de una cabeza, con todas sus variaciones de tamaño, de orientación y de brillo? Cada vez que escribieran una regla, aparecería una imagen que la rompe.

En lugar de escribir las reglas, se le muestran a la computadora muchos ejemplos ya resueltos. Es decir, imágenes donde una persona marcó a mano dónde están los espermatozoides. El programa ajusta por sí mismo lo que necesita para reproducir esas marcas. A eso se le llama aprender de ejemplos, y a lo que resulta de ese proceso se le llama modelo. Cómo sucede ese ajuste lo vemos mañana con calma. Hoy solo necesitamos quedarnos con la idea de que el modelo no recibió reglas, recibió ejemplos.

Las imágenes vienen de muchas fuentes, y una de las más importantes en las ciencias de la vida es la microscopía. Con un microscopio podemos ver células, por ejemplo espermatozoides, y podemos ver cómo cambian de tamaño y de forma bajo ciertas condiciones. Cada imagen trae información, pero alguien tiene que sacarla: contar, medir, comparar.

Para quienes no han trabajado con fluorescencia, una explicación breve. En esta técnica las células se tiñen con un colorante que, al recibir cierta luz, la devuelve en otro color. Por eso en la imagen la célula brilla y el fondo queda oscuro: lo único que vemos es lo que está teñido. Eso nos conviene, porque hay mucho contraste entre la célula y el fondo. Más adelante, cuando veamos cómo mira una imagen la computadora, esto va a tener mucho sentido.

También conviene decir qué preguntas se contestan con estas imágenes. Quien estudia espermatozoides puede querer saber cuántos hay en una muestra, qué tan grandes son, si ese tamaño cambia cuando cambia una condición, y qué tanto varían unos de otros. Todas esas preguntas se contestan midiendo, y medir a mano, uno por uno, es justo lo que vamos a ver que se vuelve un problema.

Lo que busco con este curso es que vean cómo se aplica la inteligencia artificial a un problema real, de biología de la reproducción, y no en teoría. Entonces, eh, para entender cómo se aplica la inteligencia artificial, vamos a seguir un caso de estudio, o sea, un ejemplo concreto: contar y medir espermatozoides en imágenes de microscopio.

No hace falta ser experto en nada. Si saben programar, van a ver cómo se arma el sistema, y si vienen de biología, van a ver cómo se mide lo que ya conocen.

[Diapositiva · El caso de estudio]

> Idea central: Una imagen de fluorescencia muestra manchas brillantes sobre fondo oscuro, y cada una es la cabeza de un espermatozoide. Contarlas a simple vista es posible, pero medir cada una ya no.

Les muestro cómo se ve el problema. Esta es una imagen de fluorescencia. Lo que ven son manchas de colores brillantes sobre un fondo oscuro. Cada mancha es la cabeza de un espermatozoide, y a veces se alcanza a ver una línea que sale de ella, que es la cola. Ahora pregunto, sin esperar respuesta: ¿cuántos hay en esta imagen? Lo primero que haría cualquiera es contarlos con la vista, uno por uno. Y si además hay que medir cada uno, ya no basta con mirar.

[Diapositiva · Contar y medir a mano]

> Idea central: Contar y medir a mano es lento, repetitivo y cambia según quién lo haga: tres personas cuidadosas pueden dar tres conteos distintos de la misma imagen. Un sistema que lo haga siempre igual hace falta.

El problema es este: contar y medir a mano es lento, es repetitivo y cambia según quién lo haga. Una sola imagen puede traer decenas o cientos de células. Muchas están encimadas o pegadas unas a otras, y ahí es donde cada persona decide distinto dónde termina una y empieza la otra. El ojo no tiene una regla fija, y por eso cada persona decide distinto. En la diapositiva puse tres conteos de la misma imagen, de tres personas distintas. Son números de ejemplo, no de una medición real, pero la idea es esa: tres personas cuidadosas pueden llegar a tres resultados distintos.

Imaginen contar a mano cien células en una imagen, y luego repetirlo con muchas imágenes... este, cada persona contaría algo distinto, ¿no? Además, para la investigación muchas veces lo que importa es el tamaño: cuánto mide cada célula, cuánto varía de una a otra y cómo cambia ese tamaño entre una condición y otra. Medir cada célula a mano exige trazar su contorno con cuidado y leer el resultado, una y otra vez. Multipliquen eso por cientos de células en una imagen y por muchas imágenes. Un sistema que haga ese trabajo siempre de la misma manera deja de ser un lujo y se vuelve algo que de verdad hace falta.

Hay otra consecuencia que a veces se pasa por alto: el cansancio. Una persona que lleva una hora contando no mide igual que cuando empezó. Un programa no se cansa, y esa regularidad, para comparar imágenes entre sí, vale mucho.

Una cosa más sobre las imágenes. Trabajamos con dos tipos: las de fluorescencia, donde las células brillan sobre un fondo oscuro, y las de fondo claro, que se ven distinto porque el fondo ya no es oscuro. Para cada tipo tenemos un modelo distinto, y más adelante vamos a ver cómo el sitio elige el que corresponde.

Pero antes de ver cómo se resuelve, tenemos que regresarnos a lo fundamental: qué es una imagen, y qué es una imagen digital.

---

## Bloque 3. Qué son las imágenes

*1,332 palabras, unos 7.6 min de habla*

[Diapositiva · ¿Qué son las imágenes?]

> Idea central: Antes de hablar de redes hay que entender qué es una imagen para una computadora. Esa pregunta abre esta parte.

La primera pregunta que nos vamos a hacer es: ¿qué son las imágenes?

Una imagen es la categoría general. Abarca cualquier tipo de representación visual: un dibujo, una pintura, una captura, lo que sea. Una fotografía es un tipo de imagen: la que se captura con una cámara y registra la luz que llega a un sensor en un momento concreto. Toda fotografía es una imagen, pero no toda imagen es una fotografía. En microscopía todo lo que se genera se llama imagen, y por eso de aquí en adelante voy a hablar de imágenes, y en particular de imágenes digitales.

[Diapositiva · Una imagen digital es una tabla de números]

> Idea central: Para la computadora una imagen es una tabla de números, uno por píxel, de 0 (negro) a 255 (blanco). Una imagen grande son casi dos millones y medio de números.

Vamos con algo que parece muy básico y de lo que depende todo lo demás. La pregunta es: ¿qué es una imagen para una computadora?

Para la computadora, una imagen es, o sea, una tabla de números. Cada cuadrito, cada píxel, guarda cuánta luz tiene. Es una cuadrícula de cuadritos, y cada píxel guarda un número. En una imagen en tonos de gris, ese número es el brillo, y va de cero, que es negro, a doscientos cincuenta y cinco, que es blanco. Los números intermedios son los grises. En una imagen a color no es un número sino tres, uno para el rojo, otro para el verde y otro para el azul, y con la mezcla de los tres sale el color de ese cuadrito.

En la diapositiva tengo a la izquierda una imagen pequeña con un cuadro azul marcado, y a la derecha lo que hay dentro de ese cuadro, ampliado hasta que se ven los números. Son treinta y cinco cuadritos, siete por cinco. Fíjense en la parte de afuera: números bajos, casi negros. Y en el centro, números altos, hasta un doscientos cincuenta y cinco. Eso es lo que la computadora tiene delante cuando mira una imagen.

Una imagen grande, de las que usamos, tiene por ejemplo mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Hagan la cuenta: son casi dos millones y medio de cuadritos, cada uno con su número. La computadora los maneja todos a la vez sin problema, pero a un ojo humano eso no le dice nada. Lo que nosotros vemos como células, la computadora lo ve como un mar de números.

Un detalle sobre esos números del cero al doscientos cincuenta y cinco: tienen una razón. Cada píxel guarda su valor en un byte, que son ocho bits, y con ocho bits se pueden representar doscientos cincuenta y seis valores distintos. Por eso el rango empieza en cero y termina en doscientos cincuenta y cinco. Con esos doscientos cincuenta y seis niveles el ojo ve un degradado suave de negro a blanco, sin escalones. En una imagen a color son tres bytes por píxel, uno por cada color.

Y una idea más, la de resolución. Cuantos más píxeles tiene una imagen, más detalle puede guardar, porque cada cuadrito representa una zona más pequeña de lo que se fotografió. Una imagen con pocos píxeles se ve pixelada cuando se amplía, justamente porque los cuadritos ya no alcanzan a describir la forma. Por eso a las imágenes del microscopio les conviene tener muchos píxeles: para que la forma de cada célula quede descrita con detalle.

[Diapositiva · Una célula brillante son números altos]

> Idea central: En fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. Medir su área es contar cuántos píxeles ocupa.

Ahora pensemos en una imagen de fluorescencia. ¿Cómo se ve una célula dentro de esa tabla de números? Como una zona de números altos sobre un fondo de números bajos. La célula brilla, así que sus píxeles tienen valores grandes, y el fondo oscuro tiene valores pequeños. La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

Esto también nos dice cómo se mide el tamaño. En la diapositiva les muestro una célula pequeñita dibujada con números. Los doce cuadritos más brillantes, los que tienen el borde marcado, son la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles. Medir el área de una célula es contar cuántos píxeles ocupa. En una imagen real serán cientos de píxeles por célula, pero la idea es exactamente la misma. Más adelante, con la escala del sitio, esos píxeles se convierten en micras.

Una pregunta que seguramente se están haciendo: ¿y no bastaría con decir que todo píxel por encima de cierto valor es célula? Es una idea natural y es, de hecho, el primer intento que se suele hacer. Se llama umbralización: se elige un umbral y todo lo que lo supera se considera objeto. Funciona razonablemente cuando las células están separadas y bien iluminadas, pero falla cuando se tocan, cuando hay manchas brillantes que no son células, o cuando el brillo cambia de una imagen a otra. Más adelante, en esta misma sesión, vemos por qué no basta y cómo una red neuronal retoma esa idea y suma otros factores. Hoy les dejo solo la intuición de que la computadora, en el fondo, está comparando números.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

> Idea central: BMP, PNG y TIFF guardan la imagen tal cual; JPG la comprime y puede mover los bordes, y con ellos el área. Conviene trabajar con los archivos originales del microscopio.

Un tema práctico: los formatos de archivo. No todos guardan la imagen igual. BMP, PNG y TIFF guardan la imagen tal cual. JPG la comprime para que pese menos, y al comprimirla puede mover los bordes de las células. Para medir, eso importa.

En la diapositiva tengo la misma célula dos veces: a la izquierda con el borde nítido y a la derecha con el borde difuminado y con bloques raros, que es lo que pasa con la compresión. ¿Por qué importa? Porque si el borde se difumina, el contorno cambia, y si el contorno cambia, cambia el área, y entonces cambian los números que nos interesan. El sitio acepta JPG, pero lo avisa. La recomendación es trabajar con los archivos originales del microscopio y evitar que pasen por aplicaciones de mensajería, que suelen comprimirlos sin que nos demos cuenta.

Un dato que ayuda a entender la diferencia: una imagen de las que usamos, guardada como BMP, pesa alrededor de siete megabytes, porque guarda todos sus píxeles sin comprimir. El mismo contenido en JPG puede pesar una fracción de eso, y ahí está el atractivo del JPG: ocupa menos. Pero ese ahorro de espacio se paga con fidelidad, y para medir, la fidelidad es justo lo que necesitamos.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

> Idea central: Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno. El sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, y la declara en cada resultado.

La última idea de este bloque es la escala. Una imagen sabe cuántos píxeles mide, pero no sabe cuántas micras es cada píxel, es decir, cuánto mide en la realidad. Los archivos no guardan esa información. Además, las imágenes pueden venir de distintos aumentos, por ejemplo de cuarenta X y de cien X, y cada aumento cambia lo que representa un píxel. Si queremos comparar imágenes entre sí, necesitamos una forma de ponerlas en la misma medida.

Una imagen no sabe cuánto mide un píxel en la realidad. Por eso el sitio usa la misma escala en todas las imágenes, para estandarizar su tamaño, y cada resultado dice cuál. Esa escala es de sesenta píxeles por micra. Cada resultado dice qué escala se usó, y la imagen marcada trae una regla de trescientos píxeles que equivalen a cinco micras. No voy a entrar hoy en cómo se define esa escala; eso lo vemos en la tercera sesión, cuando veamos cómo funciona el sistema.

Veámoslo con números. Si sesenta píxeles son una micra, entonces un largo de sesenta píxeles es una micra de largo, y un largo de trescientos píxeles son cinco micras, que es justo la regla que va dibujada en la imagen. Con las áreas hay un paso más. Un área se mide en unidades cuadradas, así que una micra cuadrada son sesenta por sesenta píxeles, es decir, tres mil seiscientos píxeles. Si una célula ocupa tres mil seiscientos píxeles, su área es de una micra cuadrada; si ocupa la mitad, de media micra cuadrada. Por eso, en el sitio, las áreas en micras cuadradas pueden salir como números pequeños.

Y para ubicarnos en la unidad: una micra es la milésima parte de un milímetro. Es la medida natural para hablar de células, porque a esa escala los milímetros resultan demasiado grandes.

---

## Bloque 4. Definiciones y palabras clave

*643 palabras, unos 3.7 min de habla*

[Diapositiva · Algunas definiciones de inteligencia artificial]

> Idea central: Inteligencia artificial, aprendizaje automático, redes neuronales y aprendizaje profundo son capas de un mismo campo, de lo más amplio a lo más específico.

Antes de entrar con las redes neuronales, conviene poner en orden algunas palabras, porque se mezclan muy seguido.

La inteligencia artificial es el campo más amplio: cualquier técnica que haga que una máquina realice tareas que se asocian con la inteligencia. El aprendizaje automático es la parte que aprende de ejemplos. Las redes neuronales son una técnica dentro del aprendizaje automático, y el aprendizaje profundo se refiere a redes con muchas capas, que les voy a explicar en un momento.

La idea que da nombre al aprendizaje automático se resume en una frase: en lugar de escribir las reglas, se muestran ejemplos y se deja que el sistema las encuentre. En la programación tradicional se entregan reglas y datos y salen las respuestas. En el aprendizaje automático se entregan datos y respuestas y salen las reglas. Es una inversión de flujo, y de ella depende todo lo que sigue.

Muchas familias de técnicas siguen esa idea, desde modelos estadísticos sencillos hasta arquitecturas muy complejas. Las redes neuronales son una de ellas y rinden especialmente bien con imágenes, sonido o texto, es decir, datos crudos con mucha estructura que no se describe fácilmente con unas pocas variables. Aquí vamos a usar una red de aprendizaje profundo, que es la técnica que mejor funciona con imágenes.

[Diapositiva · Palabras que vamos a escuchar]

> Idea central: Seis palabras para las cuatro sesiones: red neuronal, Google Colab, Python, Flask, modelo y servidor. Entrenamiento e inferencia se explican en la siguiente diapositiva.

Antes de seguir, les dejo en pantalla unas palabras que van a escuchar durante las cuatro sesiones. No las voy a leer todas, solo las que salen hoy.

Una red neuronal es un programa que aprende de ejemplos. Google Colab es un entorno para programar en la nube. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python. El sitio está hecho con las dos. El modelo es el archivo que guarda lo que la red aprendió. Y el servidor es la computadora donde el sitio está en línea, la que responde cuando alguien entra. También aparecen dos palabras que explico en la siguiente diapositiva, entrenamiento e inferencia, porque son las que más confunden y las que más importa distinguir.

[Diapositiva · Entrenamiento aparte, inferencia en el servidor]

> Idea central: Entrenar es aprender la receta y se hace aparte, en Colab; la inferencia es cocinarla, y se hace en el servidor. Para mejorar el modelo no se toca el sitio, solo se cambia el archivo.

El desarrollo de la red tiene dos etapas, y están separadas a propósito. Primero se entrena en Google Colab y, después, cuando queremos analizar imágenes nuevas, usamos el modelo en el servidor. A eso se le llama inferencia, ¿va?

La primera etapa es el entrenamiento. Se hace en Colab, con imágenes que las personas ya marcaron a mano, y de ahí sale el archivo del modelo. La segunda etapa es la inferencia, que es usar el modelo ya entrenado para analizar imágenes nuevas. Eso se hace en el servidor, en el procesador de la computadora donde está el sitio.

Esto tiene una consecuencia práctica que vale la pena entender. Para mejorar el modelo no se toca el sitio. Se entrena aparte, se obtiene un archivo nuevo y se cambia ese archivo en el servidor. Son dos partes con cuidados distintos: la parte web se mantiene como cualquier sitio, y la parte de aprendizaje automático se mejora con datos.

Una comparación que ayuda: el entrenamiento es como aprender una receta, y la inferencia es como cocinarla las veces que haga falta. Aprender la receta lleva tiempo y esfuerzo, con muchos intentos y correcciones, y se hace una vez, o cada vez que se quiere mejorar. Cocinar con la receta ya aprendida es mucho más rápido y se repite todos los días. Con el sitio pasa igual: entrenar el modelo es lo pesado, y por eso se hace aparte, en Colab, donde hay más capacidad de cálculo. Usarlo para analizar una imagen es lo ligero, y por eso puede hacerse en el procesador del servidor del sitio.

Esta separación tiene una ventaja más. El sitio no necesita saber cómo se entrenó el modelo, solo necesita el archivo. Si mañana se entrena una versión mejor, se reemplaza el archivo y el sitio sigue funcionando igual.

---

## Bloque 5. Fundamentos de redes neuronales

*1,368 palabras, unos 7.8 min de habla*

[Diapositiva · Fundamentos de redes neuronales]

> Idea central: Vamos de lo general a lo concreto: un problema, la idea que lo resuelve y al final el nombre técnico. Sin ecuaciones; cuando haya una, se dice con palabras qué hace.

Con esto ya podemos empezar con las redes neuronales. Voy de lo general a lo concreto: primero un problema que podemos imaginar, luego la idea que lo resuelve y al final el nombre técnico. No voy a usar ecuaciones. Cuando una idea tenga expresión matemática, les digo con palabras qué hace.

La meta de esta parte es que quede claro cómo responder tres preguntas: qué es una red neuronal, cómo aprende y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides. Las dos primeras las vemos hoy. La tercera, mañana.

[Diapositiva · El primer intento: el umbral]

> Idea central: La primera idea para contar es usar el brillo: todo píxel por encima de cierto valor es célula. Sirve como primera aproximación, pero las reglas se multiplican y se enredan.

Partamos del problema. Supongamos que hay que escribir un programa que reciba una imagen y diga cuántos espermatozoides hay. ¿Cómo se haría con un programa tradicional, escribiendo reglas explícitas?

La primera idea es usar el brillo. Los espermatozoides son brillantes sobre fondo oscuro, así que se podría decir que todo píxel con un brillo mayor a cierto valor pertenece a una célula. Luego se agrupan los píxeles vecinos en manchas, y cada mancha es una célula. Esa técnica se llama umbralización, y el sitio la incluye como respaldo.

Como primera aproximación sirve, pero los problemas aparecen pronto. Las colas también brillan y no se quieren contar. Hay manchas rojas difusas, más grandes y fuera de foco, que pasan el umbral sin ser espermatozoides. Hay células encimadas entre sí o sobre las colas de otras, y el umbral las une en una sola mancha. Además, el brillo de una imagen depende de la iluminación, de la exposición y de la tinción. Un umbral que funciona en una imagen puede fallar en la siguiente.

Se pueden seguir agregando reglas. Si la mancha es muy alargada, probablemente es una cola. Si es muy grande, probablemente es una mancha difusa. Si tiene forma de ocho, probablemente son dos células juntas y hay que partirla por el estrechamiento. Cada regla ayuda un poco y trae sus excepciones. La lista crece, se enreda, y cada extensión nueva obliga a modificar el programa, con el riesgo de romper lo que ya funcionaba.

Hay problemas en los que escribir las reglas a mano es muy difícil. Por eso se recurre al aprendizaje automático: en lugar de escribir las reglas, se muestran ejemplos y se deja que el sistema las encuentre. Y una de las técnicas que mejor lo hace con imágenes es la red neuronal.

[Diapositiva · Una red neuronal no entiende]

> Idea central: Una red neuronal no entiende qué es un espermatozoide. Es un reconocedor de patrones muy sofisticado, y eso sirve para razonar cuándo va a funcionar y cuándo no.

Antes de construir la red, hay otra idea previa que condiciona cómo se va a escuchar el resto. Una red neuronal no entiende qué es un espermatozoide. No tiene el concepto ni sabe de biología, no sabe qué es una célula ni para qué sirve contarla. Tiene una enorme colección de números ajustados, de modo que ante ciertos patrones de píxeles produce una salida que coincide con lo que las personas marcaron en los ejemplos. Es un reconocedor de patrones muy sofisticado y nada más.

Eso no le quita mérito; sirve para razonar sobre cuándo va a funcionar y cuándo no. Si le muestro una imagen parecida a las de su entrenamiento, va a funcionar. Si le muestro algo muy distinto, no tiene cómo saber que se equivoca y producirá una salida con la misma seguridad aparente.

[Diapositiva · La neurona artificial]

> Idea central: Una neurona artificial es una operación muy pequeña en cuatro pasos: recibe números, los multiplica por pesos, los suma y decide si se activa.

Ahora sí vamos a construir la idea de la red desde su pieza más pequeña, que es la neurona artificial. Es la pieza elemental, y aunque el nombre es más una inspiración histórica que una descripción fiel de la biología, es una operación muy pequeña que se describe en cuatro pasos.

Primero, recibe una lista de números, que son las entradas. Segundo, cada entrada se multiplica por otro número, que es su peso. Tercero, se suman los resultados. Y cuarto, a esa suma se le aplica una pequeña función que decide cuándo se activa la neurona. Eso es todo.

Un ejemplo simple para ver qué hace un peso: imaginen una neurona que decide si un punto de la imagen es rojo e intenso. Recibe tres entradas, la cantidad de rojo, de verde y de azul de un píxel. Para que dé una salida alta con un píxel muy rojo, se le asigna un peso grande y positivo a la entrada del rojo, y pesos pequeños o negativos a las otras dos. Un píxel muy rojo produce una suma muy grande y uno azul una suma muy pequeña.

Los pesos expresan qué le importa a la neurona. Un peso grande dice «esto me va a importar mucho», uno cercano a cero dice «me da igual», y uno negativo dice «esto me hace dudar». Falta un elemento, un número que se suma al final, que se llama sesgo. Desplaza el punto desde el cual la neurona empieza a activarse. Pueden imaginarlo como un interruptor sensible: los pesos deciden a qué se fija y el sesgo decide qué tan exigente es antes de encenderse.

El último paso, la función de activación, es lo que hace posible que las redes sean tan potentes. Si la neurona solo multiplicara y sumara, haría una operación lineal, y encadenar muchas operaciones lineales equivale a una sola. No importa cuántas capas se apilen, el resultado siempre sería tan limitado como el de una. La función de activación introduce una no linealidad. La más usada hoy es simple: si la suma es negativa, la salida es cero; si es positiva, la salida es la propia suma. La neurona se apaga si no recibe estímulo suficiente y responde de forma proporcional si lo recibe. Esa pequeña torcedura permite representar relaciones complicadas y no solo proporcionales.

[Diapositiva · De la neurona a la capa y a la red]

> Idea central: Una neurona sola hace muy poco. Muchas neuronas forman una capa, las capas se apilan y eso es una red neuronal; con muchas capas se habla de aprendizaje profundo.

Una neurona sola hace muy poco: una decisión simple basada en una combinación ponderada. La potencia aparece al juntar muchas.

La siguiente escala es una capa: un conjunto de neuronas que reciben las mismas entradas pero con pesos distintos, de modo que cada una se fija en una combinación diferente. Cien neuronas mirando los mismos números, cada una con su criterio. La salida de la capa es la lista de las cien respuestas: cada neurona es una pregunta distinta a la entrada y la capa devuelve la lista de respuestas.

Luego se apilan las capas: la salida de una se convierte en la entrada de la siguiente. La primera capa son cien preguntas sobre los datos originales. La segunda capa no ve los datos originales, sino las respuestas de la primera, y hace sus propias preguntas sobre ellas. La tercera pregunta sobre las respuestas de la segunda, y así sucesivamente. Cada capa trabaja con un resumen más abstracto de la anterior.

Esa arquitectura es la red neuronal, y cuando tiene muchas capas se habla de aprendizaje profundo. Profundo, literalmente, por las capas apiladas. Si la visualizamos, hay una entrada, los números que describen el dato; una cascada de capas intermedias que los transforman una y otra vez; y una salida, que es la respuesta final. En un clasificador sencillo podría ser un número entre cero y uno que indique qué tan probable es que la imagen contenga un espermatozoide. En un modelo más elaborado, como el nuestro, la salida es más rica, pero el principio es el mismo.

Es natural preguntar cuántos pesos tiene una red como la nuestra, y son muchísimos. La Mask R-CNN que usamos tiene decenas de millones de pesos. Que un modelo esté entrenado significa que cada uno de esos millones de números ya tiene un valor adecuado. Un modelo sin entrenar tiene los mismos pesos con valores arbitrarios y produce respuestas sin sentido. El entrenamiento es el proceso que encuentra los valores correctos.

Una comparación con el cerebro conviene tomarla con cautela. El concepto nació de la idea de que las neuronas biológicas reciben señales, las ponderan y se activan según el total, pero una neurona artificial es mucho más simple que una biológica, y la red completa no funciona como un cerebro. Lo útil de la analogía son las muchas unidades simples que, en capas, producen comportamientos complejos. Sería un error pensar que, por llamarse neuronal, la red piensa o comprende.

Para resumir: una red neuronal es una cadena de capas. Cada capa toma números, los combina con pesos, aplica una pequeña no linealidad y pasa el resultado a la siguiente. Los pesos son lo que la red sabe. Falta ver cómo conseguir que esos pesos tomen valores útiles.

---

## Bloque 6. Cómo aprende la red

*690 palabras, unos 3.9 min de habla*

[Diapositiva · Cómo aprende una red]

> Idea central: La red aprende por ensayo y corrección: predice, mide cuánto se equivocó, ajusta los pesos y repite. La respuesta correcta la ponen las personas, al anotar las imágenes.

¿Cómo aprende la red? ¿Cómo se puede lograr que millones de pesos tomen valores útiles? En pocas palabras, es un proceso de ensayo y corrección, bastante parecido a cómo aprendemos las personas.

Primero, la red hace una predicción con los pesos que tiene en ese momento. Segundo, se compara con la respuesta correcta que alguien proporcionó a mano, y se mide cuánto se equivocó. Tercero, se ajustan un poco los pesos en la dirección que habría reducido el error. Y cuarto, se repite con otro ejemplo, y así miles de veces.

Antes de entrenar, los pesos son arbitrarios. Si le damos una imagen, la red responde, pero la respuesta es casi aleatoria: con una imagen de cientos de espermatozoides podría marcar regiones al azar. Para mejorar, la red necesita saber cuánto se equivocó. Esa medida se llama función de pérdida, un número que resume la distancia entre lo que la red predijo y lo que debió predecir. Si marca justo los espermatozoides que las personas marcaron, la pérdida es pequeña; si marca otras cosas o se le escapa mucho, es grande. La pérdida solo tiene que cumplir dos condiciones: ser más baja mientras mejor sea la predicción y poder calcularse de forma automática.

Sobre el origen de las respuestas correctas, esto tiene consecuencias prácticas. No las da la red ni el desarrollador, las dan las personas. Alguien tuvo que mirar cada imagen de entrenamiento y marcar con un contorno cada espermatozoide. A ese trabajo se le llama anotación o etiquetado, y es la fuente de lo que el modelo aprende. En nuestro caso, se hizo con una herramienta llamada CVAT. Lo importante es que el modelo solo puede aprender a reproducir lo que las personas marcaron. Si las marcas tienen errores, aprende los errores; si siguen un criterio, aprende ese criterio. Un modelo es, en cierto sentido, un espejo comprimido de las anotaciones.

[Diapositiva · Ajustar: el descenso del gradiente]

> Idea central: Ajustar los pesos es como bajar una montaña con niebla: en cada paso se avanza hacia donde el suelo baja más. El tamaño del paso es la tasa de aprendizaje.

El siguiente paso es ajustar, que es la parte más ingeniosa. Imaginen que están en una montaña con una niebla densa y quieren llegar al valle más bajo, pero no ven el paisaje; solo sienten la inclinación del suelo bajo los pies. En cada paso avanzan un poquito hacia donde el suelo baja más. No saben dónde está el valle, pero siguiendo la pendiente descendente llegan poco a poco a un lugar bajo.

Esa imagen es literalmente el algoritmo con que se entrena la red, el descenso del gradiente. La altura del terreno es la pérdida, la posición es el conjunto de todos los pesos, la inclinación del suelo es el gradiente, que indica, para cada peso, en qué dirección moverlo para que la pérdida baje, y el tamaño del paso se llama tasa de aprendizaje. Con un paso demasiado grande se puede saltar por encima del valle y rebotar sin llegar nunca. Con uno muy pequeño se avanza tan lento que el entrenamiento no termina en tiempo razonable. Elegir el tamaño del paso es una de las decisiones que se toman antes de entrenar, y esas decisiones se llaman hiperparámetros.

[Diapositiva · Retropropagación: repartir el error]

> Idea central: La retropropagación calcula cuánto contribuyó cada peso al error, yendo hacia atrás desde la salida, capa por capa. Se parece a revisar los tiros fallados de Batalla naval.

También hay que preguntarse cómo se calcula la pendiente con decenas de millones de pesos. Existe una técnica, la retropropagación, que aprovecha que la red es una cadena de operaciones simples para calcular de forma eficiente cuánto contribuyó cada peso al error. Se llama así porque el cálculo va hacia atrás: parte del error en la salida y retrocede capa por capa, repartiendo la responsabilidad.

Una forma de verlo es con el juego de Batalla naval. Al principio la red señala casi al azar, como cuando uno dispara a ciegas. Conforme se avanza por las capas, el peso del error va aumentando, como las piezas blancas que marcan los tiros que no dieron en el blanco. La retropropagación es ir desde el fondo, desde donde el error es más grande, hacia atrás, para ver cuál fue el origen, que era la aleatoriedad del principio.

Así, ensayo tras ensayo, los pesos van tomando valores útiles, y una red que empezó respondiendo al azar termina marcando los espermatozoides. Cómo mira una imagen una red convolucional, y cómo se aprovecha una red entrenada para otra cosa, lo vemos mañana.

---

## Bloque 7. Cierre y adelanto de la sesión 2

*188 palabras, unos 1.1 min de habla*

[Diapositiva · Lo que vimos hoy]

> Idea central: El problema era contar y medir a mano; vimos qué es una imagen digital, algunas definiciones y los primeros fundamentos de las redes neuronales.

Para cerrar, un resumen de lo que vimos. El problema era contar y medir a mano, que es lento y cambia según quién lo haga. Vimos qué es una imagen digital: una tabla de números, con sus formatos y su escala. Pusimos en orden algunas definiciones y las palabras que vamos a usar. Y empezamos con las redes neuronales: la neurona, la capa y la red, y cómo aprende una red ajustando sus pesos a partir de ejemplos.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Idea central: Hoy vimos qué es una red neuronal y cómo aprende. Mañana, sábado a las 9, vemos cómo mira una imagen una red convolucional; el lunes, el sitio funcionando, y el martes, datos, entrenamiento y despliegue.

Y termino con una pregunta que seguramente ya se hicieron: cómo sabe el sistema dónde hay un espermatozoide. Esa es la pregunta de mañana: cómo aprende una computadora. Hoy vimos qué es una red y cómo aprende en grandes rasgos. Mañana, sábado a las nueve de la mañana, vemos cómo mira una imagen una red convolucional y cómo se aprovecha una red entrenada para otra cosa.

El lunes vemos cómo funciona el sistema, con el sitio, y el martes, los datos, el entrenamiento y el despliegue en la nube. Si no alcanzamos a terminar algo de lo de hoy, lo retomamos en la siguiente sesión. Muchas gracias por su atención.

---

## Resumen de tiempos

| Bloque | Palabras | Minutos de habla |
|---|---|---|
| Bienvenida | 471 | 2.7 |
| El problema | 979 | 5.6 |
| Qué son las imágenes | 1,332 | 7.6 |
| Definiciones y palabras clave | 643 | 3.7 |
| Fundamentos de redes neuronales | 1,368 | 7.8 |
| Cómo aprende la red | 690 | 3.9 |
| Cierre y adelanto de la sesión 2 | 188 | 1.1 |
| Total | 5,671 | 32.4 |

Queda un margen amplio dentro de las dos horas para pausas al hablar, preguntas y los tiempos de cada diapositiva.
