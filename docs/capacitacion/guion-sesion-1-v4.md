# Guion de la sesión 1: Introducción y comienzo de redes neuronales (versión 4, dos horas)

Image Bio Pro · Capacitación · viernes 23 de octubre de 2026, de 6:00 a 8:00 pm

Esta sesión es la primera de cuatro. Presenta el problema, la idea de imagen digital, algunas definiciones de inteligencia artificial y las bases de las redes neuronales. Las redes convolucionales y cómo se aprovecha una red entrenada para otra cosa se ven en la sesión 2; el sitio funcionando se ve en la sesión 3; datos, entrenamiento y despliegue, en la sesión 4.

## Cómo usar este guion

Todo lo que no va entre corchetes ni en un recuadro se dice tal cual está escrito, al pie de la letra. En azul van los cambios de diapositiva. En el recuadro amarillo, debajo de cada diapositiva, va la idea central de esa diapositiva: no se dice en voz alta, sirve para ubicarse antes de hablar.

La portada la presenta Saúl y te cede la palabra. Tú empiezas en la diapositiva 2. La apertura es la que Saúl modeló, sin cambios.

Ritmo considerado: 175 palabras por minuto. El guion suma 21,440 palabras, unas 123 minutos de habla, es decir, las dos horas de la sesión. Está dividido en seis partes de unos 20 minutos cada una, pensadas para grabarse como seis videos. Si el tiempo se acaba antes de terminar, se dice «hasta aquí llegamos, mañana seguimos».

---

## Parte 1. El problema (video 1)

*3,709 palabras, unos 21.2 min de habla*

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

Vale la pena decir por qué esto importa en un entorno universitario. En la docencia, una herramienta que analiza imágenes permite que quien está aprendiendo vea, con sus propios datos, cómo se pasa de una imagen a una medida. En la investigación, permite que el conteo y la medición dejen de depender de horas de trabajo manual y de la mirada de una sola persona. Y en la difusión de la cultura científica, un sitio abierto a la comunidad muestra que la inteligencia artificial no es algo lejano, sino una herramienta que se puede usar, revisar y entender.

Por eso, a lo largo de las sesiones no solo vamos a ver el sitio funcionando. Vamos a ver las ideas que hay debajo, para que cualquiera de ustedes pueda razonar sobre qué hace el sistema, cuándo se puede confiar en él y cuándo conviene mirar con más cuidado. Esa es la ventaja de conocer las bases: dejan de ser una caja negra.

[Diapositiva · Microscopía de fluorescencia]

> Idea central: En fluorescencia, la célula se tiñe con un colorante que devuelve la luz en otro color. Por eso brilla sobre un fondo oscuro y es fácil de distinguir.

Antes de ver el problema, una explicación breve de qué tipo de imágenes vamos a usar, porque no todos vienen del mismo entorno. Trabajamos con microscopía de fluorescencia.

En esta técnica, las células se tiñen con un colorante especial, un fluoróforo. Ese colorante tiene una propiedad: cuando recibe luz de cierto color, la absorbe, y un instante después devuelve luz de otro color. El microscopio ilumina la muestra con la luz que el colorante absorbe y, al mirar, filtra todo lo demás para dejar pasar solo la luz que el colorante devuelve.

El resultado es una imagen muy particular. Lo que está teñido brilla, y lo que no está teñido queda oscuro. En nuestras imágenes, las cabezas de los espermatozoides aparecen en rojo o anaranjado, las colas en un verde amarillento, y el fondo es casi negro. Esto nos conviene muchísimo, porque hay un contraste enorme entre lo que queremos medir y lo que no.

Eso tiene una consecuencia para la computadora. Cuando hay mucho contraste, separar un objeto del fondo es más fácil, porque el objeto tiene números altos y el fondo números bajos. Más adelante vamos a ver qué es una imagen digital y por qué esto importa tanto.

También existen las imágenes de fondo claro, donde la muestra se ve oscura sobre un fondo iluminado. Se ven distintas, y por eso para cada tipo de imagen hay un modelo distinto. Hoy nos concentramos en fluorescencia, que es el caso más claro para entender las ideas.

[Diapositiva · El caso de estudio]

> Idea central: Una imagen de fluorescencia muestra manchas brillantes sobre fondo oscuro, y cada una es la cabeza de un espermatozoide. Contarlas a simple vista es posible, pero medir cada una ya no.

Les muestro cómo se ve el problema. Esta es una imagen de fluorescencia. Lo que ven son manchas de colores brillantes sobre un fondo oscuro. Cada mancha es la cabeza de un espermatozoide, y a veces se alcanza a ver una línea que sale de ella, que es la cola. Ahora pregunto, sin esperar respuesta: ¿cuántos hay en esta imagen? Lo primero que haría cualquiera es contarlos con la vista, uno por uno. Y si además hay que medir cada uno, ya no basta con mirar.

Fíjense en lo que hay en la imagen. Hay cabezas de distintos tonos, unas más anaranjadas, otras más rojizas. Hay colas, que salen de las cabezas como líneas delgadas. Hay zonas donde las células se tocan, y algunas cuyas colas se cruzan con otras cabezas. Si me pidieran contar cuántas cabezas hay, yo empezaría por una esquina y avanzaría célula por célula, y a la mitad me preguntaría si ya conté esta o aquella.

Y contar es lo más sencillo. Lo siguiente sería medir. ¿Qué tan grande es cada cabeza? ¿Qué tanto varían entre sí? ¿Cambian de tamaño cuando cambia una condición del experimento? Esas preguntas son las que interesan en una investigación, y para contestarlas hay que medir cada célula, una por una, en cada imagen.

[Diapositiva · Qué se quiere medir]

> Idea central: Del problema salen cuatro cosas que medir: cuántas cabezas hay, qué tamaño tiene cada una, cómo se distribuyen los tamaños y de qué color es cada cabeza.

Pongamos en claro qué queremos obtener de cada imagen, porque de ahí sale todo el diseño del sistema.

Lo primero es el conteo: cuántas cabezas hay. Es el número más directo y el que más se usa para comparar muestras.

Lo segundo es el tamaño de cada cabeza. Como las cabezas son curvas, no basta con una sola medida, y por eso se miden dos: el área, que es cuánto espacio ocupa la cabeza, y el largo. El área se obtiene contando los píxeles que ocupa, y los píxeles se convierten a micras con una escala que veremos más adelante.

Lo tercero es la distribución de tamaños. En lugar de quedarnos con un solo número, queremos ver cómo se reparten las medidas: cuántas cabezas son pequeñas, cuántas medianas, cuántas grandes. Esa distribución suele parecerse a una campana, la famosa campana de Gauss, y de ella se sacan dos números que usaremos mucho: la media, que es el valor típico, y la desviación estándar, que dice qué tanto se alejan las demás del valor típico.

Lo cuarto es el color. En estas imágenes, el color de la cabeza va de rojo a amarillo, y se mide a partir de la proporción de rojo y de verde dentro de cada contorno. Lo importante es que no son categorías separadas: es una escala continua, de la que usamos diez grados.

Y al final, todo eso se tiene que poder llevar a otro lado. Por eso los resultados se exportan en un archivo CSV, para trabajarlos en una hoja de cálculo, y en un informe en PDF, para compartirlos.

Esas cuatro cosas, conteo, tamaño, distribución y color, son lo que el sistema entrega por cada imagen. Y todas dependen de algo previo: saber dónde está cada cabeza.

[Diapositiva · Media y desviación estándar, con un ejemplo]

> Idea central: La media es el valor típico y la desviación estándar dice qué tanto se alejan los demás. Dos grupos con la misma media pueden ser muy distintos.

Hemos nombrado dos números que van a aparecer mucho: la media y la desviación estándar. Veámoslos con un ejemplo pequeño, para que dejen de ser palabras.

Supongamos que medimos el área de cinco cabezas, en micras cuadradas, y obtenemos: dos, dos punto dos, uno punto ocho, dos punto cuatro y uno punto seis. La media es el promedio de siempre: se suman los cinco valores, que dan diez, y se divide entre cinco. La media es dos. Es el valor típico.

Ahora queremos saber qué tanto se parecen entre sí. Para eso se mide cuánto se aleja cada valor de la media. Las diferencias son: cero, cero punto dos, menos cero punto dos, cero punto cuatro y menos cero punto cuatro. Si las promediáramos tal cual, los positivos y los negativos se cancelarían, así que primero se elevan al cuadrado: cero, cero punto cero cuatro, cero punto cero cuatro, cero punto dieciséis y cero punto dieciséis. Se suman, y dan cero punto cuarenta. Se promedian, dividiendo entre cuatro, que es uno menos el número de datos, y da cero punto uno. Y por último se saca la raíz cuadrada, que da más o menos cero punto tres. Esa es la desviación estándar.

Ahora un segundo grupo de cinco cabezas: uno punto nueve, dos, dos, dos punto uno y dos. Su media también es dos. Pero sus valores están muy pegados. Haciendo la misma cuenta, la desviación estándar es de más o menos cero punto cero siete.

Fíjense en lo que acabamos de ver. Los dos grupos tienen la misma media, dos, y sin embargo son muy distintos: en uno las cabezas varían bastante, en el otro casi no varían. Si solo reportáramos la media, no nos daríamos cuenta. La desviación estándar es lo que nos dice qué tan dispersos están los datos.

Por eso el sistema entrega las dos cosas, y por eso la gráfica de la distribución de tamaños es tan útil: porque muestra de un vistazo cuál es el valor típico y qué tanto se reparte el resto.

[Diapositiva · Para qué sirven estas medidas en una investigación]

> Idea central: Con las imágenes se comparan condiciones: se mide cada grupo y se compara cómo cambian el número y el tamaño de las células. Interpretar la diferencia es trabajo de quien investiga.

Conviene que veamos para qué se usan estos números en una investigación, porque da sentido a todo el trabajo.

Un experimento típico compara condiciones. Se toma una muestra en una condición, por ejemplo sin tratamiento, y otra en una condición distinta. De cada muestra se toman varias imágenes, y de cada imagen salen un conteo, una lista de tamaños, una media y una desviación estándar. Con esos números, se pregunta si la condición cambió algo: ¿hay más o menos células?, ¿son más grandes o más pequeñas?, ¿varían más o menos entre sí?

Para contestar con seriedad hace falta repetir. Una sola imagen puede ser rara por casualidad. Varias imágenes por condición, y varias muestras por condición, permiten distinguir una diferencia real de una variación normal. Y para saber si una diferencia es suficientemente grande como para tomarla en serio se usan pruebas estadísticas, que se aplican con los datos que el sistema entrega en el archivo CSV.

Es importante tener claro hasta dónde llega nuestro sistema. Cuenta, mide y entrega los datos de forma consistente y revisable. No interpreta. Decidir si una diferencia es significativa, qué la causa y qué implica biológicamente es una pregunta que le corresponde a quien conoce la biología detrás. El sistema es un instrumento, como una balanza: da el peso, y no decide si el resultado del experimento es bueno o malo.

Y por eso la consistencia es tan valiosa. Si el instrumento no es consistente, las diferencias que se encuentren podrían venir del instrumento y no de la condición. Un método de medición estable permite que lo que se vea en los datos sea lo que realmente cambió en la muestra.

[Diapositiva · Contar y medir a mano]

> Idea central: Contar y medir a mano es lento, repetitivo y cambia según quién lo haga: tres personas cuidadosas pueden dar tres conteos distintos de la misma imagen. Un sistema que lo haga siempre igual hace falta.

El problema es este: contar y medir a mano es lento, es repetitivo y cambia según quién lo haga. Una sola imagen puede traer decenas o cientos de células. Muchas están encimadas o pegadas unas a otras, y ahí es donde cada persona decide distinto dónde termina una y empieza la otra. El ojo no tiene una regla fija, y por eso cada persona decide distinto. En la diapositiva puse tres conteos de la misma imagen, de tres personas distintas. Son números de ejemplo, no de una medición real, pero la idea es esa: tres personas cuidadosas pueden llegar a tres resultados distintos.

Imaginen contar a mano cien células en una imagen, y luego repetirlo con muchas imágenes... este, cada persona contaría algo distinto, ¿no? Además, para la investigación muchas veces lo que importa es el tamaño: cuánto mide cada célula, cuánto varía de una a otra y cómo cambia ese tamaño entre una condición y otra. Medir cada célula a mano exige trazar su contorno con cuidado y leer el resultado, una y otra vez. Multipliquen eso por cientos de células en una imagen y por muchas imágenes. Un sistema que haga ese trabajo siempre de la misma manera deja de ser un lujo y se vuelve algo que de verdad hace falta.

Hay otra consecuencia que a veces se pasa por alto: el cansancio. Una persona que lleva una hora contando no mide igual que cuando empezó. Un programa no se cansa, y esa regularidad, para comparar imágenes entre sí, vale mucho.

Una cosa más sobre las imágenes. Trabajamos con dos tipos: las de fluorescencia, donde las células brillan sobre un fondo oscuro, y las de fondo claro, que se ven distinto porque el fondo ya no es oscuro. Para cada tipo tenemos un modelo distinto, y más adelante vamos a ver cómo el sitio elige el que corresponde.



Hay un caso que ilustra bien el problema. Pensemos en dos personas que cuentan la misma imagen con todo cuidado. Una decide que dos cabezas muy pegadas son una sola, porque no ve el estrechamiento entre ellas. La otra sí lo ve y cuenta dos. Ninguna se equivocó por descuido; cada una aplicó su criterio. Pero sus números ya no coinciden, y si esas dos personas trabajan en laboratorios distintos, o en semanas distintas, comparar sus resultados deja de ser confiable.

Pasa algo parecido con las medidas. Para medir el tamaño de una cabeza a mano hay que decidir dónde exactamente termina el borde, y el borde de una célula brillante no es una línea nítida sino una transición de brillo. Una persona puede trazar el contorno un poco por dentro y otra un poco por fuera, y esa diferencia, que parece mínima, cambia el área de forma apreciable, porque el área crece con el cuadrado del tamaño.

Y hay un tema de registro. Cuando se mide a mano, rara vez queda constancia de cómo se midió: dónde se trazó cada contorno, qué criterio se siguió. Un sistema automático puede guardar la imagen marcada, y cualquiera puede abrirla y ver exactamente qué se midió.

Por todo eso, el objetivo no es reemplazar el criterio de las personas, sino hacerlo consistente y repetible. Que la misma imagen dé siempre el mismo resultado, y que ese resultado se pueda revisar.

[Diapositiva · Un día de trabajo sin el sistema]

> Idea central: Con cuentas sencillas se ve que el trabajo manual no escala: unas pocas decenas de imágenes ya significan miles de células y medio día de trabajo.

Pongamos números al problema, para que no quede en una idea abstracta. Estos números son ilustrativos, y están hechos para que se vea el orden de magnitud.

Supongamos un experimento pequeño, con treinta imágenes. Cada imagen, como dijimos, tiene del orden de ciento cincuenta cabezas. Treinta por ciento cincuenta son cuatro mil quinientas células. Para medir cada una a mano hay que localizarla, trazar su contorno con cuidado y anotar el resultado. Si cada célula tomara solo diez segundos, que es muy poco, serían cuarenta y cinco mil segundos. Eso son doce horas y media de trabajo sin descanso, sin contar los errores y sin comparar con nadie.

Ahora imaginen que el experimento tiene varias condiciones, y que cada condición se repite. Treinta imágenes se convierten en cientos. Y si alguien quiere repetir el análisis con otro criterio de medición, el trabajo empieza de nuevo.

El otro lado de la cuenta es la calidad. Doce horas de trabajo repetitivo no se hacen con la misma atención de principio a fin. Hay cansancio, hay distracciones, y el criterio cambia sin que nos demos cuenta. Medir la célula número cuatro mil con el mismo cuidado que la número uno es muy difícil para cualquier persona.

Un sistema automático cambia esas dos cuentas. Procesa una imagen en unas decenas de segundos, sin cansarse, y lo hace siempre con el mismo criterio. Treinta imágenes toman unos minutos. Y cuando se quiere repetir un análisis, se repite en el mismo tiempo.

Fíjense que el valor no está solo en la velocidad. Está también en que el resultado es comparable. Dos personas que analizan sus imágenes con el mismo sistema están midiendo con la misma regla, y eso es lo que hace posible comparar entre laboratorios y entre experimentos.

[Diapositiva · El camino de una imagen a un número]

> Idea central: Un mapa del recorrido: la imagen entra, la red encuentra las cabezas, el código mide cada una y salen los números, la gráfica, el CSV y el PDF.

Antes de meternos a los detalles, conviene tener un mapa de a dónde vamos, para que cada pieza que veamos tenga un lugar.

El recorrido empieza con una imagen. Una persona la sube al sitio. Lo primero que pasa es que la imagen se prepara: se le da el tamaño y el formato que la red espera.

Después entra la red neuronal. Su trabajo es encontrar las cabezas y trazar el contorno de cada una. Esa es la única parte que se basa en aprendizaje.

Con los contornos en la mano, entra el código convencional. Para cada contorno, cuenta los píxeles que encierra, y con la escala los convierte en micras cuadradas: eso es el área. Mide el largo. Calcula el color a partir de la proporción de rojo y verde. Y luego junta todas las cabezas de la imagen y calcula el conteo, la media y la desviación estándar.

Finalmente se arman los resultados: una imagen marcada con los contornos, una tabla con una fila por cabeza, una gráfica de la distribución de tamaños, un archivo CSV para trabajar con los datos y un informe en PDF.

Si lo pensamos con calma, hay una parte que aprende y una parte que calcula. La que aprende es la red, y por eso necesita ejemplos, entrenamiento y todo lo que veremos hoy. La que calcula es el código, y por eso es preciso, repetible y se puede revisar.

Hoy nos vamos a concentrar en las piezas que hacen falta para entender la primera parte: qué es una imagen para una computadora, y qué es y cómo aprende una red neuronal. El recorrido completo, con el sitio funcionando, lo vemos en la tercera sesión.

Pero antes de ver cómo se resuelve, tenemos que regresarnos a lo fundamental: qué es una imagen, y qué es una imagen digital.

---

## Parte 2. Qué son las imágenes (video 2)

*3,653 palabras, unos 20.9 min de habla*

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

Hagamos el ejercicio de ponernos en el lugar de la computadora. Cuando ustedes miran una imagen, reconocen formas, bordes, colores, y casi sin esfuerzo saben qué es cada cosa. La computadora no recibe nada de eso. Recibe una lista ordenada de números y una indicación de cuántos hay por fila y cuántas filas son. Con esa información reconstruye la cuadrícula.

Por eso se habla de una matriz. Una matriz es simplemente una tabla de números organizada en filas y columnas, como una hoja de cálculo. Cada celda de esa tabla es un píxel, y el valor de la celda es lo que sabemos de ese punto. En la diapositiva ven un fragmento de siete por cinco, con treinta y cinco celdas. Si pudiéramos ver la imagen completa de esta manera, serían casi dos millones y medio de celdas.

Algo importante es que la computadora no tiene ninguna idea previa de lo que hay en la imagen. No sabe dónde empieza una célula ni dónde termina. Cualquier cosa que queramos que haga, contar, medir o reconocer, tiene que construirse a partir de esos números y de las relaciones entre ellos. Un píxel solo no dice nada. Lo que dice algo es cómo se comportan los números vecinos: dónde suben de golpe, dónde bajan, dónde se mantienen parecidos.

Esa idea, que lo importante son las relaciones entre píxeles vecinos, va a volver una y otra vez, y es justamente la base de cómo una red neuronal mira una imagen.

[Diapositiva · El color: tres números por píxel]

> Idea central: Una imagen a color guarda tres números por píxel, uno para el rojo, uno para el verde y uno para el azul. Un naranja intenso es mucho rojo, algo de verde y poco azul.

Hasta ahora hablamos de imágenes en tonos de gris, donde cada píxel tiene un solo número, el brillo. Pero nuestras imágenes tienen color, y el color añade una dimensión.

En una imagen a color, cada píxel guarda tres números en lugar de uno. Un número dice cuánto rojo tiene el píxel, otro cuánto verde y otro cuánto azul. Cada uno va, igual que el brillo, de cero a doscientos cincuenta y cinco. Estos tres números se llaman canales, y por eso se habla de los canales rojo, verde y azul. Mezclándolos en distintas proporciones se obtiene cualquier color que veamos en una pantalla.

Veamos un ejemplo. El naranja de una cabeza brillante podría tener doscientos cuarenta de rojo, ciento veintidós de verde y cuarenta y dos de azul. Mucho rojo, una cantidad media de verde y casi nada de azul. Si el color tuviera menos verde, por ejemplo treinta, se vería más rojo. Si tuviera más verde, por ejemplo doscientos, se vería más amarillo. Y esto es justamente lo que nos permite medir el color de cada cabeza: comparar cuánto rojo y cuánto verde hay dentro de su contorno.

Conviene tener en cuenta otra cosa. Una imagen de tres canales pesa tres veces más que una de un canal, porque guarda tres números por píxel. Y para muchas tareas, como encontrar dónde hay algo brillante, a veces basta con trabajar con el brillo, que es un solo número por píxel y se calcula combinando los tres canales.

Entonces, resumiendo: una imagen en gris es una tabla de números; una imagen a color son tres tablas del mismo tamaño apiladas, una por canal. Todo lo que se haga con una imagen se hace, finalmente, con esas tablas.

[Diapositiva · Resolución y tamaño del archivo]

> Idea central: Más píxeles significan más detalle, pero también más números que guardar. Una imagen de nuestro tamaño pesa unos siete megabytes sin comprimir.

Hablemos de la resolución, que es una palabra que se usa mucho y se entiende a medias. La resolución de una imagen digital es cuántos píxeles tiene, normalmente expresado como ancho por alto.

Una imagen típica de las que usamos mide mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Si multiplicamos, nos da un poco menos de dos millones y medio de píxeles, que algunas personas llaman dos punto cinco megapíxeles.

¿Qué cambia con la resolución? El detalle. Cada píxel representa un pedacito de lo que se fotografió, y mientras más píxeles hay, más pequeño es ese pedacito. Con pocos píxeles, la forma de una célula se describe con pocos cuadritos y su borde se ve escalonado. Con muchos píxeles, el borde se describe con más cuidado y la medida es más precisa. Por eso, cuando lo que importa es medir, conviene que las imágenes tengan buena resolución.

Pero más píxeles también significa más datos. Hagamos la cuenta del peso. Cada píxel de una imagen a color guarda tres números, y cada número ocupa un byte. Entonces, dos millones y medio de píxeles por tres bytes son más o menos siete millones y medio de bytes, que son unos siete megabytes. Eso es lo que pesa una de nuestras imágenes cuando se guarda sin comprimir. Si fuera en gris, pesaría la tercera parte.

Esto explica un fenómeno que seguramente han notado: las imágenes grandes tardan más en subirse, en abrirse y en procesarse. Para la computadora, procesar una imagen es recorrer esos millones de números, y cada operación que se haga por píxel se multiplica por dos millones y medio. Más adelante veremos cómo el sistema se organiza para manejar eso sin que la espera sea excesiva.

[Diapositiva · Una célula brillante son números altos]

> Idea central: En fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. Medir su área es contar cuántos píxeles ocupa.

Ahora pensemos en una imagen de fluorescencia. ¿Cómo se ve una célula dentro de esa tabla de números? Como una zona de números altos sobre un fondo de números bajos. La célula brilla, así que sus píxeles tienen valores grandes, y el fondo oscuro tiene valores pequeños. La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

Esto también nos dice cómo se mide el tamaño. En la diapositiva les muestro una célula pequeñita dibujada con números. Los doce cuadritos más brillantes, los que tienen el borde marcado, son la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles. Medir el área de una célula es contar cuántos píxeles ocupa. En una imagen real serán cientos de píxeles por célula, pero la idea es exactamente la misma. Más adelante, con la escala del sitio, esos píxeles se convierten en micras.

Una pregunta que seguramente se están haciendo: ¿y no bastaría con decir que todo píxel por encima de cierto valor es célula? Es una idea natural y es, de hecho, el primer intento que se suele hacer. Se llama umbralización: se elige un umbral y todo lo que lo supera se considera objeto. Funciona razonablemente cuando las células están separadas y bien iluminadas, pero falla cuando se tocan, cuando hay manchas brillantes que no son células, o cuando el brillo cambia de una imagen a otra. Más adelante, en esta misma sesión, vemos por qué no basta y cómo una red neuronal retoma esa idea y suma otros factores. Hoy les dejo solo la intuición de que la computadora, en el fondo, está comparando números.

Esta idea tiene una consecuencia muy práctica: separar lo que nos interesa del fondo se puede plantear como una pregunta sobre números. ¿Dónde están los números altos? ¿Dónde están los bajos? ¿Dónde hay un cambio brusco de uno a otro? El borde de una célula es, en la tabla, el lugar donde los valores pasan de bajos a altos en muy pocos píxeles.

Y de ahí se entiende por qué el borde importa tanto. Si el borde es nítido, en la tabla se ve un salto claro, y trazar el contorno es sencillo. Si el borde está borroso, los valores suben poco a poco, y es más difícil decir dónde termina exactamente la célula. Esa diferencia se va a notar enseguida en los formatos de archivo y en la medida.

[Diapositiva · El histograma: contar los brillos]

> Idea central: Un histograma cuenta cuántos píxeles hay de cada nivel de brillo. En fluorescencia, casi todos son oscuros y unos pocos son muy brillantes, y esa forma explica por qué un umbral parece funcionar.

Hay una forma muy útil de resumir una imagen, que se llama histograma. Es una gráfica que cuenta cuántos píxeles hay de cada nivel de brillo. En el eje horizontal van los valores, de cero a doscientos cincuenta y cinco, y en el vertical, cuántos píxeles tienen ese valor.

Para construirlo, se recorre la imagen píxel por píxel, y cada vez que se encuentra un valor, se suma uno a la columna correspondiente. Al final, las columnas altas son los valores más comunes y las bajas los poco comunes.

Veamos cómo es el histograma de una imagen de fluorescencia. Recordemos cómo es la imagen: casi todo es fondo oscuro, y unas pocas zonas son células brillantes. Entonces, el histograma tiene una columna altísima en los valores bajos, porque la inmensa mayoría de los píxeles son oscuros, y después una cola larga y baja hacia los valores altos, que corresponden a las células.

Esa forma explica por qué la idea del umbral parece funcionar. Si en el histograma hay una zona de valores bajos con muchísimos píxeles y una zona de valores altos con unos pocos, se podría trazar una línea en medio: de ahí hacia la izquierda es fondo, de ahí hacia la derecha son células.

Pero también explica por qué falla. Las células no son del mismo brillo: unas son más intensas que otras. Hay colas, que brillan menos que las cabezas pero más que el fondo. Hay manchas difusas con valores intermedios. Y los bordes de las células, donde el brillo baja poco a poco, producen valores intermedios que no pertenecen claramente a ningún grupo. En el histograma, todo eso rellena el espacio entre el fondo y las células, y no hay una línea limpia donde cortar.

Además, el histograma de una imagen puede ser distinto del de la siguiente, si cambió la iluminación o la exposición. Un umbral elegido para una puede no servir para la otra.

Esta es una herramienta que usaremos más adelante para entender qué ve la computadora, y es una buena manera de comprobar, antes de cualquier análisis, si una imagen está bien expuesta.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

> Idea central: BMP, PNG y TIFF guardan la imagen tal cual; JPG la comprime y puede mover los bordes, y con ellos el área. Conviene trabajar con los archivos originales del microscopio.

Un tema práctico: los formatos de archivo. No todos guardan la imagen igual. BMP, PNG y TIFF guardan la imagen tal cual. JPG la comprime para que pese menos, y al comprimirla puede mover los bordes de las células. Para medir, eso importa.

En la diapositiva tengo la misma célula dos veces: a la izquierda con el borde nítido y a la derecha con el borde difuminado y con bloques raros, que es lo que pasa con la compresión. ¿Por qué importa? Porque si el borde se difumina, el contorno cambia, y si el contorno cambia, cambia el área, y entonces cambian los números que nos interesan. El sitio acepta JPG, pero lo avisa. La recomendación es trabajar con los archivos originales del microscopio y evitar que pasen por aplicaciones de mensajería, que suelen comprimirlos sin que nos demos cuenta.

Un dato que ayuda a entender la diferencia: una imagen de las que usamos, guardada como BMP, pesa alrededor de siete megabytes, porque guarda todos sus píxeles sin comprimir. El mismo contenido en JPG puede pesar una fracción de eso, y ahí está el atractivo del JPG: ocupa menos. Pero ese ahorro de espacio se paga con fidelidad, y para medir, la fidelidad es justo lo que necesitamos.

Veámoslo con un poco más de detalle, porque este es uno de los errores más comunes y más fáciles de evitar.

La compresión es una forma de guardar la misma imagen en menos espacio. Hay dos grandes familias. La compresión sin pérdida guarda la imagen de forma más compacta, pero al abrirla se recupera exactamente cada número, sin cambiar ninguno. PNG y TIFF, bien usados, funcionan así. Y BMP, en la práctica, ni siquiera comprime: guarda todos los números tal cual.

La compresión con pérdida, que es la de JPG, hace otra cosa. Parte de la idea de que el ojo humano no nota ciertos cambios pequeños, y aprovecha eso para descartar información. Divide la imagen en bloques y simplifica cada bloque. El resultado ocupa mucho menos espacio, pero los números que se recuperan al abrir la imagen ya no son los originales, solo se parecen.

Para una fotografía de un paisaje, eso casi no importa. Para una imagen donde vamos a medir el borde de una célula, sí importa, porque la simplificación por bloques tiende a mover y a suavizar justo los bordes. Y hay un detalle que conviene recordar: cada vez que una imagen se guarda en JPG, se pierde un poco más. Si pasa por varias aplicaciones, cada una comprimiéndola otra vez, el daño se acumula.

Por eso la recomendación es sencilla. Trabajar con el archivo original que genera el microscopio o la cámara, sin pasarlo por aplicaciones de mensajería ni de redes sociales, que casi siempre lo comprimen para ahorrar espacio. Si necesitan reducir el peso, lo ideal es un formato sin pérdida. Y si solo tienen una versión en JPG, el sitio la acepta, pero lo avisa, porque la medida puede cambiar ligeramente.

[Diapositiva · Aumentos y micras]

> Idea central: Los aumentos del microscopio, 40X o 100X, cambian cuánto mide en la realidad cada píxel. Una micra es la milésima parte de un milímetro.

Pasemos ahora a una pregunta que parece trivial y no lo es: ¿cuánto mide una célula? Para contestarla necesitamos una unidad y una forma de pasar de píxeles a esa unidad.

La unidad natural es la micra, o micrómetro. Una micra es la milésima parte de un milímetro. Un cabello humano mide unas decenas de micras de grosor, y una cabeza de espermatozoide mide unas pocas micras. A esa escala, los milímetros resultan demasiado grandes, y por eso se usan las micras.

El problema es que una imagen digital no sabe nada de micras. Solo sabe de píxeles. Y cuántas micras representa un píxel depende de cómo se tomó la imagen. Un factor es el aumento del microscopio. Si se usa un aumento de cuarenta X, cada píxel cubre un pedazo de la muestra; si se usa uno de cien X, ese mismo píxel cubre un pedazo más pequeño, porque el objeto se ve más grande. Otros factores son el tipo de cámara y el tamaño de sus sensores.

Eso significa que dos imágenes que miden lo mismo en píxeles pueden representar tamaños reales muy distintos. Si comparáramos sus medidas en píxeles sin más, estaríamos comparando cosas que no son comparables.

Y el archivo no guarda este dato. Las imágenes que usamos no traen escrito cuánto mide cada píxel. Entonces hay dos caminos. Uno es suponer un valor y no decir nada, y el otro es declarar una escala y repetirla en todos los resultados. Nuestro sistema toma el segundo camino, y eso es lo que vemos en la siguiente diapositiva.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

> Idea central: Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno. El sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, y la declara en cada resultado.

La última idea de este bloque es la escala. Una imagen sabe cuántos píxeles mide, pero no sabe cuántas micras es cada píxel, es decir, cuánto mide en la realidad. Los archivos no guardan esa información. Además, las imágenes pueden venir de distintos aumentos, por ejemplo de cuarenta X y de cien X, y cada aumento cambia lo que representa un píxel. Si queremos comparar imágenes entre sí, necesitamos una forma de ponerlas en la misma medida.

Una imagen no sabe cuánto mide un píxel en la realidad. Por eso el sitio usa la misma escala en todas las imágenes, para estandarizar su tamaño, y cada resultado dice cuál. Esa escala es de sesenta píxeles por micra. Cada resultado dice qué escala se usó, y la imagen marcada trae una regla de trescientos píxeles que equivalen a cinco micras. No voy a entrar hoy en cómo se define esa escala; eso lo vemos en la tercera sesión, cuando veamos cómo funciona el sistema.

Veámoslo con números. Si sesenta píxeles son una micra, entonces un largo de sesenta píxeles es una micra de largo, y un largo de trescientos píxeles son cinco micras, que es justo la regla que va dibujada en la imagen. Con las áreas hay un paso más. Un área se mide en unidades cuadradas, así que una micra cuadrada son sesenta por sesenta píxeles, es decir, tres mil seiscientos píxeles. Si una célula ocupa tres mil seiscientos píxeles, su área es de una micra cuadrada; si ocupa la mitad, de media micra cuadrada. Por eso, en el sitio, las áreas en micras cuadradas pueden salir como números pequeños.

Y para ubicarnos en la unidad: una micra es la milésima parte de un milímetro. Es la medida natural para hablar de células, porque a esa escala los milímetros resultan demasiado grandes.

Detengámonos en por qué esta decisión es importante. Imaginen que el sitio no declarara la escala y que una persona midiera con él imágenes de cuarenta X y otra de cien X. Las dos obtendrían áreas en micras cuadradas, pero las de una estarían infladas o reducidas respecto de las de la otra, y nadie se enteraría. Los números parecerían precisos y no lo serían.

Al fijar una escala única para todas las imágenes, el sistema estandariza el tamaño: cualquier imagen se interpreta con la misma relación entre píxeles y micras. Eso permite comparar entre imágenes y entre personas. Y al declararla en cada resultado, quien lee un número sabe con qué regla se calculó. Si en el futuro se decide usar otra escala, o una por cada aumento, se puede cambiar y todo el mundo sabrá que cambió.

Un último detalle, que se entiende con un ejemplo. Dijimos que una micra cuadrada son sesenta por sesenta píxeles, tres mil seiscientos. Entonces, si una cabeza ocupa siete mil doscientos píxeles, su área es de dos micras cuadradas. Y si ocupa mil ochocientos, de media micra cuadrada. Con este tipo de cuentas, que cualquiera puede repetir con una calculadora, se pasa de lo que la computadora ve a lo que el investigador necesita.

[Diapositiva · Dos tipos de imagen, dos modelos]

> Idea central: Las imágenes de fluorescencia y las de fondo claro se ven distintas, y por eso hay un modelo entrenado para cada tipo.

Algo que mencionamos de pasada y que merece su propio momento: trabajamos con dos tipos de imágenes, y para cada una hay un modelo.

Las de fluorescencia son las que hemos visto: células brillantes sobre un fondo oscuro. Las de fondo claro son lo contrario: la muestra se ve oscura, o de un color, sobre un fondo iluminado. Las dos son imágenes digitales, tablas de números, pero los números se comportan de forma muy distinta. En una, lo que buscamos son valores altos rodeados de valores bajos. En la otra, la situación es la contraria.

Podría pensarse que basta con una sola red que lo aprenda todo. En principio se puede, pero tiene un costo. Una red que debe resolver dos problemas muy distintos necesita más ejemplos de cada uno y más capacidad, y suele rendir peor en ambos que dos redes especializadas. Por eso se entrenó un modelo para cada caso.

Esto tiene una consecuencia práctica para quien usa el sitio: hay que subir cada imagen al tipo que le corresponde, y el sitio elige el modelo adecuado. Más adelante, cuando veamos el sistema funcionando, lo vamos a ver en acción.

Y deja una enseñanza general. Un modelo no es una solución universal. Es una solución para el tipo de imágenes con las que se entrenó. Cuando cambian las condiciones, como otra tinción, otro microscopio o un tipo de célula distinto, hay que preguntarse si el modelo sigue siendo adecuado, y a veces la respuesta es que se necesita otro.

---

## Parte 3. La inteligencia artificial a nuestro alrededor, definiciones y palabras clave (video 3)

*3,279 palabras, unos 18.7 min de habla*

[Diapositiva · La inteligencia artificial a nuestro alrededor]

> Idea central: Sin darnos cuenta, usamos inteligencia artificial todos los días: al escribir, al buscar, al ver recomendaciones. Casi todo se basa en aprender de ejemplos.

Antes de ponernos con las definiciones, mirémosla donde ya vive. Seguramente todos los que estamos aquí usamos hoy, sin pensarlo, varias herramientas que funcionan con aprendizaje automático.

Cuando escriben un mensaje en el teléfono y les sugiere la siguiente palabra, hay un modelo que aprendió, de millones de textos, qué palabras suelen seguir a cuáles. Cuando el correo manda un mensaje a la carpeta de no deseados, hay un modelo que aprendió, de muchísimos correos que otras personas marcaron como basura, qué rasgos tiene un mensaje de ese tipo. Cuando una plataforma de video propone qué ver después, hay un modelo que aprendió de lo que miraron personas parecidas a ustedes.

Lo mismo con la voz. Cuando le dictan algo al teléfono y lo transcribe, un modelo aprendió a relacionar sonidos con palabras escuchando grandes cantidades de grabaciones transcritas. Cuando un traductor convierte una frase de un idioma a otro, aprendió de enormes colecciones de textos traducidos.

Y con las imágenes también. Cuando el teléfono agrupa las fotos por personas, o cuando una cámara enfoca sola la cara, hay modelos que aprendieron a reconocer rostros a partir de muchísimos ejemplos.

Fíjense en lo que tienen en común. En ningún caso alguien escribió una lista de reglas para reconocer una cara, una frase o un mensaje basura. Habría sido imposible, por la cantidad de casos y de excepciones. En todos los casos, lo que se hizo fue reunir muchos ejemplos y dejar que el sistema encontrara por sí mismo qué los distingue.

Esa es la idea que sostiene el resto de lo que vamos a ver. Y es útil tenerla presente por una razón: nos recuerda que estas herramientas no son mágicas ni inteligentes en el sentido humano. Son muy buenas para lo que vieron en sus ejemplos, y se equivocan de maneras que a veces resultan sorprendentes. Lo que vamos a hacer en este curso es ver cómo funciona esa idea con un caso que nos queda muy cerca: contar y medir células.

[Diapositiva · La inteligencia artificial con imágenes de células]

> Idea central: En biología, la inteligencia artificial ayuda a contar, medir y localizar estructuras en imágenes de microscopio. Su valor está en la rapidez y en la consistencia.

Pasemos de la vida diaria a las ciencias de la vida, que es donde nos interesa. ¿Para qué se usa la inteligencia artificial con imágenes de microscopio?

La tarea más directa es contar. Contar células, núcleos, bacterias o colonias en una imagen es algo que se hace constantemente en un laboratorio, y es tedioso. Un modelo que cuenta con un criterio fijo ahorra tiempo y evita la variación entre personas.

La segunda es localizar. Saber dónde está cada estructura dentro de la imagen permite medirla, seguirla en el tiempo si se toman varias imágenes, o estudiar cómo se distribuyen unas respecto de otras. Esta es la tarea que nos ocupa: encontrar cada cabeza de espermatozoide.

La tercera es medir. Una vez localizada una estructura, se puede obtener su tamaño, su forma o su intensidad. Con las mediciones de cientos de estructuras se pueden comparar condiciones y tratamientos.

La cuarta es clasificar. Decidir de qué tipo es una célula, o si una región se ve normal o alterada, a partir de su apariencia. Es una tarea muy estudiada, y los resultados dependen mucho de la calidad de los ejemplos con que se entrena el modelo.

Y hay una quinta, que es filtrar. Antes de que una persona revise cientos de imágenes, un modelo puede señalar cuáles merecen atención, y así se aprovecha mejor el tiempo de quien conoce el tema.

En todos los casos hay algo que se repite: la inteligencia artificial no sustituye el criterio de quien investiga. Hace de forma rápida y consistente una parte repetitiva del trabajo, y deja a la persona lo que requiere conocimiento: decidir qué preguntas hacer, interpretar los resultados y detectar cuándo algo no tiene sentido.

Y es importante decirlo con claridad: un resultado producido por un modelo es una medición, con sus márgenes de error, y no una verdad. Por eso, en un buen sistema, el resultado siempre se puede revisar. Esa idea nos va a acompañar en todas las sesiones.

[Diapositiva · Algunas definiciones de inteligencia artificial]

> Idea central: Inteligencia artificial, aprendizaje automático, redes neuronales y aprendizaje profundo son capas de un mismo campo, de lo más amplio a lo más específico.

Antes de entrar con las redes neuronales, conviene poner en orden algunas palabras, porque se mezclan muy seguido.

La inteligencia artificial es el campo más amplio: cualquier técnica que haga que una máquina realice tareas que se asocian con la inteligencia. El aprendizaje automático es la parte que aprende de ejemplos. Las redes neuronales son una técnica dentro del aprendizaje automático, y el aprendizaje profundo se refiere a redes con muchas capas, que les voy a explicar en un momento.

La idea que da nombre al aprendizaje automático se resume en una frase: en lugar de escribir las reglas, se muestran ejemplos y se deja que el sistema las encuentre. En la programación tradicional se entregan reglas y datos y salen las respuestas. En el aprendizaje automático se entregan datos y respuestas y salen las reglas. Es una inversión de flujo, y de ella depende todo lo que sigue.

Muchas familias de técnicas siguen esa idea, desde modelos estadísticos sencillos hasta arquitecturas muy complejas. Las redes neuronales son una de ellas y rinden especialmente bien con imágenes, sonido o texto, es decir, datos crudos con mucha estructura que no se describe fácilmente con unas pocas variables. Aquí vamos a usar una red de aprendizaje profundo, que es la técnica que mejor funciona con imágenes.

Para que no se mezclen, vale la pena verlas como círculos que se contienen unos a otros. El más grande es la inteligencia artificial. Dentro está el aprendizaje automático. Dentro de este, las redes neuronales. Y dentro de las redes neuronales, el aprendizaje profundo, que son las que tienen muchas capas.

Una consecuencia de esto es que no toda la inteligencia artificial aprende de ejemplos. Un programa que sigue reglas escritas por una persona, como un sistema que recomienda qué hacer si la temperatura sube de cierto valor, también se considera inteligencia artificial en el sentido amplio. Lo que distingue al aprendizaje automático es que las reglas no las escribe una persona, sino que se obtienen de los datos.

Otra consecuencia es que, cuando se habla de inteligencia artificial en los medios, casi siempre se está hablando de aprendizaje profundo, que es la rama que más ha avanzado en los últimos años con imágenes, sonido y texto. Es la que usamos aquí.

Les pido que se queden con una imagen sencilla, porque nos va a servir para el resto de las sesiones. En la programación tradicional, yo escribo las reglas y la computadora las aplica. En el aprendizaje automático, yo le doy ejemplos y la computadora descubre las reglas. Todo lo demás que vamos a ver son detalles de cómo hacerlo bien.

[Diapositiva · Palabras que vamos a escuchar]

> Idea central: Seis palabras para las cuatro sesiones: red neuronal, Google Colab, Python, Flask, modelo y servidor. Entrenamiento e inferencia se explican en la siguiente diapositiva.

Antes de seguir, les dejo en pantalla unas palabras que van a escuchar durante las cuatro sesiones. No las voy a leer todas, solo las que salen hoy.

Una red neuronal es un programa que aprende de ejemplos. Google Colab es un entorno para programar en la nube. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python. El sitio está hecho con las dos. El modelo es el archivo que guarda lo que la red aprendió. Y el servidor es la computadora donde el sitio está en línea, la que responde cuando alguien entra. También aparecen dos palabras que explico en la siguiente diapositiva, entrenamiento e inferencia, porque son las que más confunden y las que más importa distinguir.

[Diapositiva · Red neuronal]

> Idea central: Una red neuronal es un programa formado por muchas operaciones pequeñas conectadas, cuyos valores se ajustan a partir de ejemplos en lugar de escribirse a mano.

Empecemos por la palabra que más vamos a usar: red neuronal. Una red neuronal es un programa que aprende de ejemplos. Pero conviene aclarar qué significa eso con un poco más de cuidado.

Un programa tradicional es una lista de instrucciones: si pasa esto, haz aquello. Una red neuronal, en cambio, es una estructura de muchas operaciones muy pequeñas, conectadas entre sí, y cada operación tiene unos números que se pueden ajustar. Esos números se llaman pesos. Al principio, los pesos tienen valores cualquiera, y la red no sirve para nada. Después, mediante ejemplos, los pesos se van ajustando hasta que la red da buenas respuestas.

Por eso decimos que la red aprende. No aprende como una persona, no comprende lo que hace. Lo que ocurre es que, ejemplo tras ejemplo, sus pesos se acercan a valores que producen la respuesta correcta.

El nombre viene de una inspiración. Las neuronas del cerebro reciben señales y, según el total, se activan o no, y las neuronas artificiales hacen algo parecido, pero mucho más simple. Hay que tomar esa comparación con cautela. Una red neuronal artificial no es un cerebro, y el parecido es más bien de forma que de funcionamiento.

Una cosa más. Existen redes neuronales de muchos tamaños. Algunas tienen unas decenas de pesos y se pueden estudiar a mano. Las que se usan con imágenes tienen millones de pesos, y la que usamos nosotros tiene decenas de millones. Pero el principio es siempre el mismo: operaciones pequeñas, con pesos ajustables, que se ajustan con ejemplos.

En las próximas diapositivas vamos a construir una desde cero, empezando por su pieza más pequeña, para que se vea que no hay nada misterioso.

[Diapositiva · Google Colab]

> Idea central: Google Colab es un cuaderno de programación en la nube, con computadoras potentes disponibles desde el navegador. Ahí se entrenó el modelo.

La segunda palabra es Google Colab. Colab es un entorno para programar que funciona dentro del navegador. No hay que instalar nada en la computadora. Uno abre una página, escribe código en celdas, y el código se ejecuta en una computadora de Google, en la nube.

Eso tiene una ventaja que importa mucho para la inteligencia artificial. Entrenar una red neuronal exige muchísimo cálculo, y una computadora común puede tardar horas o días en una tarea que una máquina especializada hace en minutos. Colab permite usar esas máquinas más potentes, con mucha memoria y con tarjetas gráficas, que son especialmente buenas para este tipo de cálculo, sin comprarlas. Y es accesible, porque se puede empezar a usar sin costo y hay planes de pago si hace falta más capacidad.

La forma de trabajo es en cuadernos. Un cuaderno es un documento que mezcla texto explicativo y celdas de código, y se puede ejecutar celda por celda. Eso lo hace muy bueno para enseñar y para documentar, porque el que lo lee ve qué se hizo, en qué orden y con qué resultado.

En este proyecto, Colab es donde se entrena el modelo. El entrenamiento está escrito en un cuaderno que cualquier persona con el enlace puede abrir y ejecutar, y eso es parte de lo que decíamos sobre que todo se pueda repetir.

También hay que decir lo que Colab no es. No es donde vive el sitio. Cuando el entrenamiento termina, lo que sale es un archivo, y ese archivo se lleva al servidor donde está la página. Colab sirve para entrenar, y no para que las personas usen el modelo todos los días. Esa diferencia es justo la que veremos con entrenamiento e inferencia.

[Diapositiva · Python]

> Idea central: Python es el lenguaje de programación que se usa en casi toda la inteligencia artificial, gracias a sus bibliotecas. Aquí se usa para entrenar el modelo y para hacer el sitio.

La tercera palabra es Python. Python es un lenguaje de programación. Un lenguaje de programación es la forma en que le escribimos instrucciones a una computadora de manera que una persona pueda leerlas.

Python tiene fama de ser fácil de leer, porque sus instrucciones se parecen a frases en inglés y no obliga a escribir muchos símbolos. Pero la razón por la que domina la inteligencia artificial no es solo esa. Es que alrededor de Python se construyó un enorme conjunto de bibliotecas, que son colecciones de programas ya escritos para tareas comunes.

Algunas de esas bibliotecas son las que usamos en este proyecto. PyTorch es la biblioteca con la que se construye y se entrena la red neuronal. NumPy sirve para trabajar con tablas de números, como las imágenes que vimos hace un momento. OpenCV es una biblioteca especializada en imágenes, y con ella se miden los contornos y las áreas. Y Matplotlib se usa para hacer las gráficas.

Esto es importante porque nos dice algo sobre cómo se hace un proyecto como este. Nadie escribe todo desde cero. Se combinan bibliotecas muy buenas, cada una especializada en algo, y el trabajo propio está en unirlas con cuidado y en decidir cómo se usan.

Existen otros lenguajes que también se usan en inteligencia artificial, como C++ para las partes que necesitan máxima velocidad, pero Python es el que se usa para escribir y probar las ideas. Y hay una ventaja adicional: el mismo lenguaje sirve para entrenar la red y para hacer el sitio web, así que no hay que cambiar de herramienta entre una parte y la otra.

[Diapositiva · Flask]

> Idea central: Flask es una herramienta de Python para construir sitios web. Recibe lo que pide el navegador, hace el trabajo y devuelve la página.

La cuarta palabra es Flask. Flask es una herramienta, lo que en programación se llama un marco de trabajo, para hacer sitios web con Python.

Para entender qué hace, recordemos cómo funciona una página web. El navegador le manda una petición al servidor: quiero esta página, o quiero analizar esta imagen. El servidor tiene que recibir esa petición, decidir qué hacer con ella, hacer el trabajo y devolver una respuesta, que normalmente es una página que el navegador dibuja.

Flask se encarga de esa parte. Uno le indica, con unas pocas líneas de código, qué dirección de la página corresponde a qué función. Por ejemplo, que cuando alguien entra a la página de inicio se ejecute esta función y se muestre esta plantilla, y que cuando alguien sube una imagen se ejecute esa otra función que analiza la imagen.

Para armar las páginas se usan plantillas. Una plantilla es una página con huecos: el diseño es siempre el mismo, y los huecos se llenan con lo que corresponda en cada caso, como el nombre de la persona o la tabla de resultados. Este sitio usa plantillas y la biblioteca Bootstrap, que ayuda a que se vea bien tanto en una computadora como en un teléfono.

Flask también se encarga de cosas como las cuentas de las personas, para saber quién entró, y de guardar información en una base de datos. En este proyecto la base de datos es SQLite, una base de datos sencilla que vive en un archivo.

La razón por la que se eligió Flask es que es pequeño y claro. No obliga a aprender un montón de reglas, y permite que una persona entienda de principio a fin cómo está hecho el sitio. Y como está escrito en Python, puede llamar directamente a la red neuronal, que también está en Python. El sitio y el modelo hablan el mismo idioma.

[Diapositiva · Modelo]

> Idea central: El modelo es el archivo que guarda lo que la red aprendió: sus pesos. Por sí solo no hace nada, hace falta un programa que lo cargue y lo use.

La quinta palabra es modelo. Cuando una red termina de entrenarse, lo que se obtiene es un archivo. Ese archivo es el modelo.

¿Qué hay dentro? Básicamente, la estructura de la red y el valor de todos sus pesos. Los pesos son los números que se ajustaron durante el entrenamiento, y son lo que la red sabe. Si la red fuera una receta, el modelo sería la receta escrita, con todas las cantidades ya afinadas.

En el proyecto, el modelo es un archivo con extensión punto pt, que es el formato en el que PyTorch guarda sus modelos. Ese archivo contiene decenas de millones de números, y por eso ocupa bastante espacio, del orden de cientos de megabytes. Casi todo ese peso son los pesos.

Un modelo por sí solo no hace nada. Es como un libro cerrado: tiene todo adentro, pero nadie lo puede leer. Hace falta un programa que lo abra, lo cargue en la memoria y le dé una imagen para que responda. Eso es lo que hace el sitio, y lo que se llama inferencia.

Otra característica de un modelo es que está fijo. Una vez entrenado, sus pesos no cambian mientras se usa. Si mañana le damos mil imágenes para que las analice, seguirá siendo exactamente el mismo modelo, con exactamente los mismos pesos. No aprende de lo que analiza. Para que cambie, hay que entrenarlo otra vez aparte, y el resultado es un modelo nuevo, un archivo distinto.

Esto tiene una consecuencia que a veces sorprende: dos personas que analizan la misma imagen con el mismo modelo obtienen siempre el mismo resultado. Y eso es justo lo que queremos de un instrumento de medición.

[Diapositiva · Servidor]

> Idea central: El servidor es la computadora, siempre encendida y conectada a internet, donde vive el sitio y donde se usa el modelo cada vez que alguien sube una imagen.

La sexta palabra es servidor. Un servidor es una computadora, o un programa que corre en una computadora, cuyo trabajo es responder peticiones de otras computadoras.

No tiene nada de mágico. Es una computadora como cualquier otra, solo que está siempre encendida, conectada a internet y con un programa esperando a que alguien le pida algo. Cuando ustedes escriben la dirección de un sitio o hacen clic en un botón, su navegador manda una petición y el servidor contesta.

En este proyecto, el servidor es una computadora que se contrata en un servicio de alojamiento. Ahí está instalado el sitio, con sus páginas, sus cuentas y su base de datos. Y ahí también está el archivo del modelo. Cuando alguien sube una imagen, el servidor la recibe, la prepara, se la da al modelo, recibe los contornos, mide, arma los resultados y devuelve la página con todo.

Algo importante es que ese servidor no tiene una tarjeta gráfica especializada. Hace la inferencia con su procesador, que es el que tiene cualquier computadora. Eso es posible porque usar un modelo ya entrenado es mucho más ligero que entrenarlo. Un análisis tarda unas decenas de segundos, y no horas.

También hay programas que ayudan al servidor a trabajar bien. Uno de ellos recibe las peticiones de internet y las reparte, y otro corre el sitio en sí, de manera que pueda atender a varias personas a la vez. No hace falta que conozcamos los detalles ahora. Lo que sí conviene retener es la idea de que el servidor es el lugar donde las cosas realmente suceden, mientras que el navegador de cada persona es solo una ventana para ver y pedir.

Y de cómo se pone un servidor en internet, y qué cuidados requiere, hablaremos en la última sesión.

[Diapositiva · Cómo se ve un cuaderno de Colab]

> Idea central: Un cuaderno de Colab mezcla texto y celdas de código que se ejecutan una por una, y deja a la vista cada paso y su resultado.

Antes de pasar al entrenamiento, vale la pena imaginar cómo se ve un cuaderno de Colab, porque es donde ocurre.

Un cuaderno es un documento con dos tipos de bloques. Unos son de texto: explican qué se va a hacer y por qué. Otros son celdas de código: pequeñas porciones de programa que se pueden ejecutar de una en una. Debajo de cada celda aparece su resultado, que puede ser un número, una tabla, una gráfica o una imagen.

Esa forma de trabajo tiene una ventaja enorme: el proceso queda a la vista. Alguien que abre el cuaderno puede leer la explicación, ver el código, ejecutarlo y ver el resultado, paso a paso. No hay que adivinar qué se hizo.

El cuaderno de este proyecto está dividido en pasos numerados. Primero, el entorno y la configuración. Después se leen las etiquetas, que son las anotaciones, y se revisa que todo cuadre. Luego se separan las imágenes de entrenamiento de las de validación, y se preparan las imágenes y sus recortes. Más adelante se construye la red, partiendo de una ya entrenada, y se define cómo se mide si funciona. Después viene el entrenamiento propiamente dicho, donde se ve cómo baja la pérdida. Y al final se ven los resultados, con las imágenes y lo que encontró la red, y se exporta el modelo a un archivo.

Es posible ejecutar solo una parte, y eso sirve para probar. Se puede, por ejemplo, entrenar unos minutos con pocas imágenes solo para verificar que todo funciona antes de lanzar el entrenamiento completo.

Un cuaderno es, además, un registro. Si alguien quiere saber con qué datos y con qué decisiones se obtuvo un modelo, el cuaderno lo dice. Y si alguien quiere repetirlo, lo ejecuta. Eso es lo que significa que el proceso se pueda repetir, uno de los tres principios de los que hablaremos en la siguiente sesión.

El cuaderno lo vamos a abrir y recorrer juntos en la última sesión.

---

## Parte 4. Entrenamiento, inferencia y la neurona (video 4)

*3,658 palabras, unos 20.9 min de habla*

[Diapositiva · Entrenamiento aparte, inferencia en el servidor]

> Idea central: Entrenar es aprender la receta y se hace aparte, en Colab; la inferencia es cocinarla, y se hace en el servidor. Para mejorar el modelo no se toca el sitio, solo se cambia el archivo.

El desarrollo de la red tiene dos etapas, y están separadas a propósito. Primero se entrena en Google Colab y, después, cuando queremos analizar imágenes nuevas, usamos el modelo en el servidor. A eso se le llama inferencia, ¿va?

La primera etapa es el entrenamiento. Se hace en Colab, con imágenes que las personas ya marcaron a mano, y de ahí sale el archivo del modelo. La segunda etapa es la inferencia, que es usar el modelo ya entrenado para analizar imágenes nuevas. Eso se hace en el servidor, en el procesador de la computadora donde está el sitio.

Esto tiene una consecuencia práctica que vale la pena entender. Para mejorar el modelo no se toca el sitio. Se entrena aparte, se obtiene un archivo nuevo y se cambia ese archivo en el servidor. Son dos partes con cuidados distintos: la parte web se mantiene como cualquier sitio, y la parte de aprendizaje automático se mejora con datos.

Una comparación que ayuda: el entrenamiento es como aprender una receta, y la inferencia es como cocinarla las veces que haga falta. Aprender la receta lleva tiempo y esfuerzo, con muchos intentos y correcciones, y se hace una vez, o cada vez que se quiere mejorar. Cocinar con la receta ya aprendida es mucho más rápido y se repite todos los días. Con el sitio pasa igual: entrenar el modelo es lo pesado, y por eso se hace aparte, en Colab, donde hay más capacidad de cálculo. Usarlo para analizar una imagen es lo ligero, y por eso puede hacerse en el procesador del servidor del sitio.

Esta separación tiene una ventaja más. El sitio no necesita saber cómo se entrenó el modelo, solo necesita el archivo. Si mañana se entrena una versión mejor, se reemplaza el archivo y el sitio sigue funcionando igual.

Ahora que ya conocemos las palabras, podemos darle más sentido a las dos etapas. Las separamos porque son trabajos de naturaleza distinta, y cada una pide una máquina distinta.

El entrenamiento es un trabajo de mucho cálculo y poca frecuencia. Se hace una vez, o unas pocas veces. Necesita ver muchas veces los mismos ejemplos, y cada pasada ajusta millones de números. Para eso conviene una máquina potente, como las que ofrece Colab, con una tarjeta gráfica. Una vez terminado, no se repite hasta que haya una razón.

La inferencia es lo opuesto: poco cálculo, pero muchas veces. Cada vez que alguien sube una imagen, hay que hacer una pasada por la red, solo de ida, sin ajustar nada. Es mucho más barato, y se puede hacer en una máquina modesta.

Esa asimetría es lo que permite que el sistema funcione como funciona. El trabajo pesado se hace una vez, en el lugar adecuado, y el trabajo ligero se hace todos los días, en el servidor del sitio. Además, como el sitio solo necesita el archivo del modelo, se puede mejorar el modelo sin tocar el sitio, y se puede mantener el sitio sin tocar el modelo.

Una pregunta que suele aparecer es: ¿el modelo sigue aprendiendo mientras la gente lo usa? La respuesta es que no. Durante la inferencia, los pesos no cambian. Si algún día se quisiera mejorar el modelo, se reuniría un conjunto nuevo de imágenes, se entrenaría una versión aparte y se cambiaría el archivo. Mientras tanto, el modelo que está en el sitio es el que está.

[Diapositiva · Entrenamiento]

> Idea central: Entrenar es ajustar los pesos con ejemplos anotados. Necesita muchos cálculos, una máquina potente y se hace pocas veces.

Veamos cada etapa por separado, empezando por el entrenamiento.

Entrenar es el proceso de ajustar los pesos de la red con ejemplos. Para hacerlo se necesitan tres ingredientes. El primero son los ejemplos: imágenes con su respuesta correcta, que en nuestro caso son los contornos de cada cabeza dibujados por personas. El segundo es la red, con una estructura elegida y unos pesos iniciales. Y el tercero es una forma de ajustar, que es lo que vimos con la pérdida, el gradiente y la retropropagación.

Un detalle importante es que no se usan todas las imágenes para entrenar. Se separa una parte que la red no ve durante el entrenamiento, y que sirve después para comprobar si funciona con imágenes que no conoce. Es la diferencia entre estudiar con los ejercicios del libro y presentar un examen con ejercicios nuevos.

El entrenamiento tiene tres características que lo distinguen. Es costoso, porque cada pasada recorre millones de pesos para cada imagen. Es lento comparado con usar la red, y puede tardar de minutos a horas, según el tamaño del modelo y de los datos. Y es poco frecuente: se hace una vez para obtener el modelo, y se vuelve a hacer solo si hay una razón.

Por eso se hace en un entorno aparte. En nuestro caso, en Google Colab, donde se pueden usar máquinas con tarjeta gráfica. Y como está en un cuaderno, queda documentado: qué datos se usaron, qué decisiones se tomaron y qué resultado se obtuvo.

El producto del entrenamiento es el archivo del modelo. Es lo único que sale de ahí y lo único que necesita el sitio.

[Diapositiva · Inferencia]

> Idea central: Inferencia es usar el modelo ya entrenado para analizar una imagen nueva. Es una sola pasada, sin ajustar nada, y basta con el procesador de una computadora normal.

La segunda etapa es la inferencia. La palabra suena técnica, pero es sencilla: es usar el modelo ya entrenado para obtener una respuesta con una imagen nueva.

En la inferencia no se ajusta nada. La imagen entra, atraviesa las capas hacia adelante, y sale la respuesta. No hay pérdida, ni gradiente, ni retropropagación. Los pesos están fijos, tal como quedaron al terminar el entrenamiento.

Esto hace que sea mucho más ligera que el entrenamiento. Una sola pasada hacia adelante cuesta una fracción de lo que cuesta una pasada completa con ajuste. Y por eso se puede hacer en una computadora ordinaria, sin tarjeta gráfica, con el procesador común. Es lo que hace nuestro servidor.

También cambia la forma de pensar en el tiempo. En el entrenamiento, una hora más o menos no importa demasiado. En la inferencia, la persona está esperando con la página abierta, y cada segundo cuenta. Por eso se cuida que el modelo se cargue una sola vez, al iniciar el servidor, y que no haya que volver a leer el archivo con cada análisis.

Otra diferencia es la frecuencia. El entrenamiento sucede una vez, y la inferencia sucede cada vez que alguien usa el sitio. Para un modelo que se usa durante meses, se puede hacer miles de veces.

Y hay algo que se debe subrayar: la inferencia es determinista. Con el mismo modelo y la misma imagen, siempre se obtiene la misma respuesta. No hay azar en el uso. Eso es lo que queremos de un instrumento: que dos mediciones de la misma muestra coincidan.

Si lo juntamos con el entrenamiento: uno es el estudio, largo y costoso; el otro es el trabajo diario, rápido y repetible.

[Diapositiva · Fundamentos de redes neuronales]

> Idea central: Vamos de lo general a lo concreto: un problema, la idea que lo resuelve y al final el nombre técnico. Sin ecuaciones; cuando haya una, se dice con palabras qué hace.

Con esto ya podemos empezar con las redes neuronales. Voy de lo general a lo concreto: primero un problema que podemos imaginar, luego la idea que lo resuelve y al final el nombre técnico. No voy a usar ecuaciones. Cuando una idea tenga expresión matemática, les digo con palabras qué hace.

La meta de esta parte es que quede claro cómo responder tres preguntas: qué es una red neuronal, cómo aprende y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides. Las dos primeras las vemos hoy. La tercera, mañana.

Una advertencia antes de empezar, para que nadie se inquiete. Vamos a hablar de números, pesos, capas, y esas palabras pueden sonar intimidantes. Pero todo lo que vamos a ver se reduce a multiplicar, sumar y comparar. Si saben sumar y multiplicar, tienen todo lo necesario.

Y otra cosa: no voy a pedirles que memoricen nada. Lo que me interesa es que al terminar esta parte puedan explicar, con sus propias palabras, qué hay dentro de una red neuronal. Con eso, el resto del curso se va a entender mucho mejor.

[Diapositiva · El primer intento: el umbral]

> Idea central: La primera idea para contar es usar el brillo: todo píxel por encima de cierto valor es célula. Sirve como primera aproximación, pero las reglas se multiplican y se enredan.

Partamos del problema. Supongamos que hay que escribir un programa que reciba una imagen y diga cuántos espermatozoides hay. ¿Cómo se haría con un programa tradicional, escribiendo reglas explícitas?

La primera idea es usar el brillo. Los espermatozoides son brillantes sobre fondo oscuro, así que se podría decir que todo píxel con un brillo mayor a cierto valor pertenece a una célula. Luego se agrupan los píxeles vecinos en manchas, y cada mancha es una célula. Esa técnica se llama umbralización, y el sitio la incluye como respaldo.

Como primera aproximación sirve, pero los problemas aparecen pronto. Las colas también brillan y no se quieren contar. Hay manchas rojas difusas, más grandes y fuera de foco, que pasan el umbral sin ser espermatozoides. Hay células encimadas entre sí o sobre las colas de otras, y el umbral las une en una sola mancha. Además, el brillo de una imagen depende de la iluminación, de la exposición y de la tinción. Un umbral que funciona en una imagen puede fallar en la siguiente.

Se pueden seguir agregando reglas. Si la mancha es muy alargada, probablemente es una cola. Si es muy grande, probablemente es una mancha difusa. Si tiene forma de ocho, probablemente son dos células juntas y hay que partirla por el estrechamiento. Cada regla ayuda un poco y trae sus excepciones. La lista crece, se enreda, y cada extensión nueva obliga a modificar el programa, con el riesgo de romper lo que ya funcionaba.

Hay problemas en los que escribir las reglas a mano es muy difícil. Por eso se recurre al aprendizaje automático: en lugar de escribir las reglas, se muestran ejemplos y se deja que el sistema las encuentre. Y una de las técnicas que mejor lo hace con imágenes es la red neuronal.

Veamos con números por qué un umbral, que parece tan razonable, tiene tantos problemas. Tomemos una fila de diez píxeles, con estos valores de brillo: ocho, ocho, sesenta, ciento cuarenta, doscientos treinta, doscientos treinta, ciento cuarenta, sesenta, ocho, ocho. Es la forma típica de una célula: sube, llega a un máximo y baja.

Si ponemos el umbral en cien, los píxeles que lo superan son cuatro: los de ciento cuarenta y los dos de doscientos treinta. Entonces la célula mide, en esa fila, cuatro píxeles. Pero si bajamos el umbral a cincuenta, los de sesenta también pasan, y la célula mide seis píxeles. Con un cambio de cincuenta puntos en el umbral, el tamaño de la célula cambió en la mitad. Y no hay una respuesta correcta: ambos valores parecen razonables.

Ese es el primer problema, y es serio, porque lo que queremos es medir. Un método cuyo resultado depende de un número que alguien eligió sin una razón clara no es un buen instrumento de medición.

El segundo problema es que el umbral trata a todos los píxeles por igual. No distingue una cabeza de una cola, ni una cabeza de una mancha, porque lo único que mira es el brillo de cada píxel por separado. Y el tercero es que ignora la forma. Dos células pegadas se convierten en una mancha grande, porque el umbral no sabe que ahí había dos objetos.

Con reglas adicionales se pueden arreglar algunos casos. Pero cada regla es una decisión hecha a mano, con sus excepciones. Y este es el punto central: cuando el problema es complejo y las excepciones se multiplican, escribir reglas a mano deja de ser práctico. Necesitamos otra forma de plantearlo, y ahí aparece el aprendizaje automático.

[Diapositiva · Una red neuronal no entiende]

> Idea central: Una red neuronal no entiende qué es un espermatozoide. Es un reconocedor de patrones muy sofisticado, y eso sirve para razonar cuándo va a funcionar y cuándo no.

Antes de construir la red, hay otra idea previa que condiciona cómo se va a escuchar el resto. Una red neuronal no entiende qué es un espermatozoide. No tiene el concepto ni sabe de biología, no sabe qué es una célula ni para qué sirve contarla. Tiene una enorme colección de números ajustados, de modo que ante ciertos patrones de píxeles produce una salida que coincide con lo que las personas marcaron en los ejemplos. Es un reconocedor de patrones muy sofisticado y nada más.

Eso no le quita mérito; sirve para razonar sobre cuándo va a funcionar y cuándo no. Si le muestro una imagen parecida a las de su entrenamiento, va a funcionar. Si le muestro algo muy distinto, no tiene cómo saber que se equivoca y producirá una salida con la misma seguridad aparente.

Esto conviene decirlo con claridad porque tendemos a atribuirle a la red una comprensión que no tiene. Cuando una persona ve un espermatozoide, sabe qué es: tiene el concepto, sabe para qué sirve contarlos, entiende que una cola cortada sigue siendo parte de una célula. La red no sabe nada de eso. Lo único que tiene es una función muy complicada que recibe números y produce números.

Un buen ejemplo de esto es lo que pasa cuando se le muestra algo que nunca vio. Si le damos la imagen de otro tipo de tejido, no responde «esto no es lo que sé hacer». Responde con la misma seguridad, porque no tiene una forma de medir su propia ignorancia. Para ella, todo es una entrada y debe dar una salida.

Entonces, la confianza que podemos tener en una red depende de cuánto se parecen las imágenes nuevas a las imágenes con las que se entrenó. Si se parecen, la respuesta suele ser buena. Si no, no hay garantía. Y por eso, en este proyecto, el resultado siempre se puede revisar, y por eso insistimos en mirar la imagen marcada antes de confiar en un número.

Pensarlo así tiene una ventaja: nos quita el misterio. Una red neuronal no es una inteligencia oculta que decide. Es una máquina de reconocer patrones, muy buena, que hay que usar con criterio.

[Diapositiva · Del umbral a la red: qué cambia]

> Idea central: El umbral usa una regla fija sobre un píxel. La red usa millones de reglas ajustadas con ejemplos, que miran vecindarios. Cambia quién escribe las reglas.

Hagamos una comparación directa entre los dos enfoques que vimos, porque resume lo que ganamos con la red.

El umbral es una sola regla, escrita por una persona: un píxel con brillo mayor a tal valor es célula. Mira cada píxel por separado, sin importar sus vecinos. No distingue forma, ni tamaño, ni textura. Y su resultado depende de un número elegido a mano.

La red neuronal es una enorme colección de reglas, millones de pesos, que no escribió nadie: se obtuvieron ajustándolos con ejemplos. Combina muchos píxeles a la vez, no uno por uno. Puede distinguir una cabeza de una cola por su forma, y una cabeza de una mancha por su textura y sus bordes. Y no depende de un solo número elegido a mano, porque lo que se ajustó fueron todos sus pesos, y se ajustaron para que coincidan con lo que las personas marcaron.

Otra diferencia es cómo se corrigen los errores. Con el umbral, si falla en un caso, hay que agregar una regla, con el riesgo de romper otros casos. Con la red, si falla en un tipo de caso, se agregan ejemplos de ese caso y se entrena de nuevo.

Pero la red también tiene un costo. Necesita ejemplos anotados, necesita entrenamiento, y sus decisiones son más difíciles de explicar que una regla simple. No se puede apuntar a un lugar y decir: esta regla lo decidió. Por eso en este proyecto se separa lo que decide la red, que es dónde está cada cabeza, de lo que se calcula con código, que es todo lo demás, y de ahí viene la idea de que la red localiza y el código mide, que veremos con detalle más adelante.

Lo que queda claro es que el cambio de fondo no es de herramienta sino de método: en lugar de decirle a la computadora cómo hacer algo, le mostramos qué queremos y dejamos que descubra cómo.

[Diapositiva · La neurona artificial]

> Idea central: Una neurona artificial es una operación muy pequeña en cuatro pasos: recibe números, los multiplica por pesos, los suma y decide si se activa.

Ahora sí vamos a construir la idea de la red desde su pieza más pequeña, que es la neurona artificial. Es la pieza elemental, y aunque el nombre es más una inspiración histórica que una descripción fiel de la biología, es una operación muy pequeña que se describe en cuatro pasos.

Primero, recibe una lista de números, que son las entradas. Segundo, cada entrada se multiplica por otro número, que es su peso. Tercero, se suman los resultados. Y cuarto, a esa suma se le aplica una pequeña función que decide cuándo se activa la neurona. Eso es todo.

Un ejemplo simple para ver qué hace un peso: imaginen una neurona que decide si un punto de la imagen es rojo e intenso. Recibe tres entradas, la cantidad de rojo, de verde y de azul de un píxel. Para que dé una salida alta con un píxel muy rojo, se le asigna un peso grande y positivo a la entrada del rojo, y pesos pequeños o negativos a las otras dos. Un píxel muy rojo produce una suma muy grande y uno azul una suma muy pequeña.

Los pesos expresan qué le importa a la neurona. Un peso grande dice «esto me va a importar mucho», uno cercano a cero dice «me da igual», y uno negativo dice «esto me hace dudar». Falta un elemento, un número que se suma al final, que se llama sesgo. Desplaza el punto desde el cual la neurona empieza a activarse. Pueden imaginarlo como un interruptor sensible: los pesos deciden a qué se fija y el sesgo decide qué tan exigente es antes de encenderse.

El último paso, la función de activación, es lo que hace posible que las redes sean tan potentes. Si la neurona solo multiplicara y sumara, haría una operación lineal, y encadenar muchas operaciones lineales equivale a una sola. No importa cuántas capas se apilen, el resultado siempre sería tan limitado como el de una. La función de activación introduce una no linealidad. La más usada hoy es simple: si la suma es negativa, la salida es cero; si es positiva, la salida es la propia suma. La neurona se apaga si no recibe estímulo suficiente y responde de forma proporcional si lo recibe. Esa pequeña torcedura permite representar relaciones complicadas y no solo proporcionales.

Hagamos las cuentas de una neurona con números concretos, para que se vea que de verdad es solo multiplicar y sumar.

Retomemos el ejemplo de la neurona que busca píxeles rojos intensos. Para simplificar, expresamos cada canal entre cero y uno, dividiendo entre doscientos cincuenta y cinco. Le asignamos tres pesos: dos para el rojo, menos uno para el verde y menos uno para el azul. Y un sesgo de menos cero punto tres.

Probemos con un píxel naranja intenso, el de doscientos cuarenta, ciento veintidós y cuarenta y dos. En escala de cero a uno, son más o menos cero punto noventa y cuatro, cero punto cuarenta y ocho y cero punto diecisiete. Multiplicamos cada entrada por su peso: noventa y cuatro por dos da uno punto ochenta y ocho; menos cero punto cuarenta y ocho; y menos cero punto diecisiete. Sumamos: uno punto ochenta y ocho, menos cero punto cuarenta y ocho, menos cero punto diecisiete, da uno punto veintitrés. Y le restamos el sesgo, cero punto tres, y queda cerca de cero punto noventa y cuatro. La neurona responde con un número alto.

Probemos ahora con un píxel azul, de veinte, treinta y doscientos veinte. Las entradas son cero punto ocho, cero punto doce y cero punto ochenta y seis. El rojo aporta cero punto dieciséis, el verde resta cero punto doce y el azul resta cero punto ochenta y seis, y con el sesgo el total queda en menos uno punto doce. Es un número negativo, y la neurona, que se activa solo con valores positivos, responde cero.

Fíjense en lo que pasó. Sin que nadie le dijera la palabra rojo, esta neurona distingue un píxel rojo de uno azul, solo por cómo están puestos sus pesos. Y fíjense también en el sesgo. Si fuera menos uno en lugar de menos cero punto tres, el píxel naranja daría solo cerca de cero punto veinticuatro, una respuesta mucho más tímida. El sesgo es lo que decide qué tan exigente es la neurona antes de decir que sí.

Esto es todo lo que hace una neurona. Una operación de multiplicar, sumar y comparar. La potencia de una red no viene de que cada neurona sea inteligente, sino de que hay millones de ellas, bien ajustadas.

[Diapositiva · El sesgo, con un ejemplo]

> Idea central: El sesgo mueve el punto de activación. Con el mismo píxel y los mismos pesos, un sesgo más exigente apaga la neurona y uno más permisivo la deja encendida.

Dediquemos un momento más al sesgo, porque suele ser el elemento menos intuitivo de la neurona.

Pensemos en una neurona sencilla, que mira solo el brillo de un píxel, expresado entre cero y uno, y tiene un peso de uno. Sin sesgo, su cuenta es multiplicar el brillo por uno y aplicar la activación. Entonces, un píxel con brillo cero punto dos produce cero punto dos, uno con brillo cero punto cinco produce cero punto cinco, y uno con brillo cero punto nueve produce cero punto nueve. La neurona responde en proporción al brillo, desde el más tenue.

Ahora agreguemos un sesgo de menos cero punto seis. La cuenta es brillo por uno, menos cero punto seis. El píxel de cero punto dos da menos cero punto cuatro, y la activación lo convierte en cero. El de cero punto cinco da menos cero punto uno, y también queda en cero. Solo el de cero punto nueve da cero punto tres. Con ese sesgo, la neurona se queda callada con todo lo que sea tenue o medio, y solo responde ante lo muy brillante.

Fíjense que no cambiamos el peso, y sin embargo la neurona se comporta de otra manera. El sesgo funciona como una barrera: el estímulo tiene que superarla para que la neurona se encienda. Un sesgo muy negativo hace a la neurona muy exigente. Uno cercano a cero la hace permisiva.

Y el sesgo también es un número que la red aprende. Durante el entrenamiento se ajusta, igual que los pesos, hasta encontrar qué tan exigente debe ser cada neurona para que el conjunto funcione bien.

Esta idea tiene un parecido con el umbral que vimos antes. Un sesgo negativo con una activación que apaga todo lo que no lo supera es, en cierto modo, un umbral. La diferencia es que aquí el umbral no lo elige una persona a ojo: lo encuentra el entrenamiento, y es distinto para cada neurona.

---

## Parte 5. Activación, capas y cómo aprende una red (video 5)

*3,637 palabras, unos 20.8 min de habla*

[Diapositiva · La función de activación]

> Idea central: La activación introduce una torcedura en la suma: si el total es negativo la salida es cero, y si es positivo se deja pasar. Sin ella, apilar capas no serviría de nada.

Dediquemos unos minutos a la función de activación, porque es el paso más fácil de pasar por alto y uno de los más importantes.

Recordemos lo que hace la neurona hasta antes de este paso. Multiplica las entradas por los pesos y suma, y eso es una operación lineal. Una operación lineal es aquella en que, si duplico la entrada, se duplica la salida, y si sumo dos entradas, la salida es la suma de las salidas. Es una operación muy limitada.

Ahora, algo que parece sorprendente: si se encadenan varias operaciones lineales, el resultado sigue siendo una sola operación lineal. Pueden apilar diez capas, o cien, o mil, y si solo multiplican y suman, todo eso equivale a una única capa. La profundidad no aporta nada.

Aquí entra la función de activación. Después de multiplicar y sumar, se aplica una pequeña regla que rompe la linealidad. La que más se usa hoy es muy sencilla: si el resultado es negativo, la salida es cero; si es positivo, la salida es ese mismo número. Se le llama la rectificadora, porque rectifica los negativos.

En una gráfica, es una línea plana en cero hasta el origen, y luego una línea que sube en diagonal. Esa pequeña esquina es lo que lo cambia todo. Con ella, cada neurona tiene un comportamiento de encendido y apagado: no responde nada hasta que el estímulo supera cierto nivel, y a partir de ahí responde de forma proporcional.

Y al combinar muchas de estas esquinas en capas, la red puede dibujar relaciones tan complicadas como queramos: curvas, bordes, formas. Es la diferencia entre trazar con una sola regla recta y trazar con miles de segmentos pequeños que, juntos, siguen cualquier contorno.

Entonces, en resumen: los pesos deciden a qué se fija cada neurona, el sesgo decide qué tan exigente es, y la activación hace que la red pueda representar cosas que no son simples proporciones. Con esas tres ideas se entiende una neurona completa.

[Diapositiva · De la neurona a la capa y a la red]

> Idea central: Una neurona sola hace muy poco. Muchas neuronas forman una capa, las capas se apilan y eso es una red neuronal; con muchas capas se habla de aprendizaje profundo.

Una neurona sola hace muy poco: una decisión simple basada en una combinación ponderada. La potencia aparece al juntar muchas.

La siguiente escala es una capa: un conjunto de neuronas que reciben las mismas entradas pero con pesos distintos, de modo que cada una se fija en una combinación diferente. Cien neuronas mirando los mismos números, cada una con su criterio. La salida de la capa es la lista de las cien respuestas: cada neurona es una pregunta distinta a la entrada y la capa devuelve la lista de respuestas.

Luego se apilan las capas: la salida de una se convierte en la entrada de la siguiente. La primera capa son cien preguntas sobre los datos originales. La segunda capa no ve los datos originales, sino las respuestas de la primera, y hace sus propias preguntas sobre ellas. La tercera pregunta sobre las respuestas de la segunda, y así sucesivamente. Cada capa trabaja con un resumen más abstracto de la anterior.

Esa arquitectura es la red neuronal, y cuando tiene muchas capas se habla de aprendizaje profundo. Profundo, literalmente, por las capas apiladas. Si la visualizamos, hay una entrada, los números que describen el dato; una cascada de capas intermedias que los transforman una y otra vez; y una salida, que es la respuesta final. En un clasificador sencillo podría ser un número entre cero y uno que indique qué tan probable es que la imagen contenga un espermatozoide. En un modelo más elaborado, como el nuestro, la salida es más rica, pero el principio es el mismo.

Es natural preguntar cuántos pesos tiene una red como la nuestra, y son muchísimos. La red que usamos tiene decenas de millones de pesos. Que un modelo esté entrenado significa que cada uno de esos millones de números ya tiene un valor adecuado. Un modelo sin entrenar tiene los mismos pesos con valores arbitrarios y produce respuestas sin sentido. El entrenamiento es el proceso que encuentra los valores correctos.

Una comparación con el cerebro conviene tomarla con cautela. El concepto nació de la idea de que las neuronas biológicas reciben señales, las ponderan y se activan según el total, pero una neurona artificial es mucho más simple que una biológica, y la red completa no funciona como un cerebro. Lo útil de la analogía son las muchas unidades simples que, en capas, producen comportamientos complejos. Sería un error pensar que, por llamarse neuronal, la red piensa o comprende.

Para resumir: una red neuronal es una cadena de capas. Cada capa toma números, los combina con pesos, aplica una pequeña no linealidad y pasa el resultado a la siguiente. Los pesos son lo que la red sabe. Falta ver cómo conseguir que esos pesos tomen valores útiles.

Para ver cómo se arma una red completa y que no quede en el aire, recorramos una muy pequeña, con números, en la siguiente diapositiva.

Pero antes, una pregunta que suelen hacer: ¿cuántas capas y cuántas neuronas debe tener una red? No hay una respuesta única. Es una decisión de diseño que depende del problema. Una red con pocas neuronas no tiene capacidad suficiente para capturar las relaciones complejas. Una con demasiadas puede aprender detalles que no sirven, y tarda más en entrenarse y en usarse. Por eso, en la práctica, se parte de arquitecturas que ya se probaron en problemas parecidos, y se ajustan.

Otra pregunta frecuente es qué hace cada capa. En una red que trabaja con imágenes, las primeras capas tienden a responder a cosas muy sencillas, como bordes y cambios de brillo. Las capas siguientes combinan esas respuestas para detectar formas, como curvas o esquinas. Y las últimas combinan formas para reconocer objetos completos. Nadie le dice a la red que haga eso; es lo que resulta útil, y por eso es lo que el entrenamiento termina encontrando. Es una jerarquía: de lo simple a lo complejo.

[Diapositiva · Una capa con tres criterios]

> Idea central: Tres neuronas con los mismos datos y distintos pesos dan tres respuestas distintas: cada una es una pregunta diferente sobre la entrada.

Veamos una capa pequeña con números, para ver cómo cada neurona se fija en algo distinto.

Tomemos el píxel naranja de siempre, con rojo en cero punto noventa y cuatro, verde en cero punto cuarenta y ocho y azul en cero punto diecisiete. Y construyamos una capa de tres neuronas que reciben esos tres números.

La primera neurona tiene pesos de dos para el rojo, y de menos uno para el verde y para el azul. Es la que ya vimos: pregunta qué tan rojo es el píxel. Con este píxel, su respuesta es alta, alrededor de uno punto dos antes del sesgo.

La segunda neurona tiene pesos de menos uno para el rojo, dos para el verde y menos uno para el azul. Pregunta qué tan verde es. Con nuestro píxel, la cuenta es menos cero punto noventa y cuatro, más cero punto noventa y seis, menos cero punto diecisiete, que da menos cero punto quince. Es negativo, y la activación lo convierte en cero. Respuesta: no es verde.

La tercera neurona tiene pesos de uno para cada color, y un sesgo de menos uno. Suma los tres canales, que en nuestro píxel dan uno punto cincuenta y nueve, y le resta uno. Da cero punto cincuenta y nueve. Pregunta qué tan brillante es el píxel en conjunto, y la respuesta es moderadamente alta.

La salida de la capa es la lista de las tres respuestas: alta, cero y moderada. Esa lista dice cosas sobre el píxel que el número original no decía de forma directa: es rojizo, no es verdoso, y tiene brillo considerable.

Ahora imaginen cien neuronas, cada una con sus propios pesos, mirando la misma entrada. Cada una responde a una combinación diferente. La capa entrega cien respuestas, y la siguiente capa puede combinarlas para preguntar cosas más elaboradas. Los pesos de cada neurona no los escribe nadie: los encuentra el entrenamiento, y por eso cada neurona termina especializándose en lo que resulta útil.

[Diapositiva · Una red pequeña, a mano]

> Idea central: Una red pequeña con dos entradas, dos neuronas ocultas y una salida se calcula con cuatro multiplicaciones y unas sumas. Una red grande hace lo mismo, millones de veces.

Para quitarle todo misterio, calculemos a mano una red muy pequeña. Tiene dos entradas, dos neuronas en una capa intermedia y una neurona de salida.

Supongamos que las dos entradas valen uno y dos. La primera neurona de la capa intermedia tiene los pesos uno y uno, y sesgo cero. Multiplica uno por uno, dos por uno, suma, y da tres. Como es positivo, la activación lo deja pasar: la salida de esta neurona es tres.

La segunda neurona tiene los pesos uno y menos uno, y sesgo cero. Multiplica uno por uno, dos por menos uno, suma, y da menos uno. Es negativo, y la activación lo convierte en cero. Esta neurona queda apagada.

Ahora la neurona de salida. Recibe las respuestas de la capa anterior: tres y cero. Tiene los pesos dos y uno, y un sesgo de menos uno. Multiplica tres por dos, que son seis, y cero por uno, que es cero. Suma seis. Le resta el sesgo, uno, y queda cinco. Esa es la respuesta de la red.

Eso es todo. Cuatro multiplicaciones en la capa intermedia, dos más en la salida, unas sumas y una regla de activación. Ahora imaginen esto con millones de neuronas, en decenas de capas. No cambia el tipo de operación; cambia la cantidad. Y esa cantidad es la que permite que la red capture patrones muy sutiles.

Hay algo más que se puede ver en este ejemplo. Si cambiamos uno solo de los pesos, la respuesta final cambia. Por ejemplo, si el segundo peso de la primera neurona fuera tres en lugar de uno, esa neurona daría uno más seis, que son siete, y la respuesta final sería trece en lugar de cinco. Entrenar una red es precisamente buscar los valores de todos esos pesos que hacen que la respuesta sea la correcta para los ejemplos que tenemos.

[Diapositiva · Profundidad: por qué importan las capas]

> Idea central: Con una sola capa la red solo puede combinar entradas de forma simple. Apilar capas permite construir ideas sobre otras ideas.

Retomemos la pregunta de por qué se apilan capas, con un ejemplo cotidiano.

Imaginen que quieren describir qué es una casa a alguien que nunca ha visto una. Podrían empezar por las piezas más simples: líneas rectas, ángulos, superficies planas. Con esas piezas, describen partes: una puerta es un rectángulo con una manija, una ventana es un rectángulo con un cruce adentro, un techo es un triángulo sobre un rectángulo. Y con las partes describen el objeto: una casa es una puerta, ventanas y un techo, acomodados de cierta manera.

Fíjense que cada nivel de la descripción se apoya en el anterior. No se describe una casa directamente con líneas rectas, sino pasando por partes. Esa es la idea de las capas apiladas: cada capa toma lo que hizo la anterior y construye algo un poco más elaborado.

Una red de una sola capa tendría que describir la casa directamente a partir de los píxeles. Es posible en teoría, pero necesitaría un número enorme de neuronas para cubrir todas las combinaciones posibles. Con varias capas, cada una resuelve un pedazo pequeño y el conjunto resuelve el problema completo con muchos menos recursos.

También es verdad que más capas no siempre es mejor. Cada capa agrega pesos que ajustar, y una red muy profunda con pocos ejemplos puede aprender de memoria en lugar de generalizar. Hay un equilibrio, y encontrarlo es parte del diseño. Por eso se parte de arquitecturas probadas en problemas parecidos, en lugar de inventar la estructura desde cero.

En resumen: la profundidad permite construir ideas complejas a partir de ideas simples, y ese es el motivo por el que el aprendizaje profundo funciona tan bien con datos que tienen estructura, como las imágenes.

[Diapositiva · Cómo aprende una red]

> Idea central: La red aprende por ensayo y corrección: predice, mide cuánto se equivocó, ajusta los pesos y repite. La respuesta correcta la ponen las personas, al anotar las imágenes.

¿Cómo aprende la red? ¿Cómo se puede lograr que millones de pesos tomen valores útiles? En pocas palabras, es un proceso de ensayo y corrección, bastante parecido a cómo aprendemos las personas.

Primero, la red hace una predicción con los pesos que tiene en ese momento. Segundo, se compara con la respuesta correcta que alguien proporcionó a mano, y se mide cuánto se equivocó. Tercero, se ajustan un poco los pesos en la dirección que habría reducido el error. Y cuarto, se repite con otro ejemplo, y así miles de veces.

Antes de entrenar, los pesos son arbitrarios. Si le damos una imagen, la red responde, pero la respuesta es casi aleatoria: con una imagen de cientos de espermatozoides podría marcar regiones al azar. Para mejorar, la red necesita saber cuánto se equivocó. Esa medida se llama función de pérdida, un número que resume la distancia entre lo que la red predijo y lo que debió predecir. Si marca justo los espermatozoides que las personas marcaron, la pérdida es pequeña; si marca otras cosas o se le escapa mucho, es grande. La pérdida solo tiene que cumplir dos condiciones: ser más baja mientras mejor sea la predicción y poder calcularse de forma automática.

Sobre el origen de las respuestas correctas, esto tiene consecuencias prácticas. No las da la red ni el desarrollador, las dan las personas. Alguien tuvo que mirar cada imagen de entrenamiento y marcar con un contorno cada espermatozoide. A ese trabajo se le llama anotación o etiquetado, y es la fuente de lo que el modelo aprende. En nuestro caso, se hizo con una herramienta llamada CVAT. Lo importante es que el modelo solo puede aprender a reproducir lo que las personas marcaron. Si las marcas tienen errores, aprende los errores; si siguen un criterio, aprende ese criterio. Un modelo es, en cierto sentido, un espejo comprimido de las anotaciones.

Hay una cosa que vale la pena notar en estos cuatro pasos. Ninguno requiere que alguien le explique a la red qué es un espermatozoide. Lo único que se necesita son ejemplos con su respuesta correcta y una forma de medir qué tan lejos estuvo la red de esa respuesta. Todo lo demás es mecánico: predecir, comparar, ajustar, repetir.

Y es mecánico a una escala enorme. Una sola pasada por una imagen ajusta millones de pesos, y el proceso completo repite eso miles y miles de veces. Ningún ser humano podría hacerlo a mano, y esa es una buena razón para que lo haga la computadora. Pero conviene entender el ciclo, porque cuando algo sale mal casi siempre se debe a uno de sus pasos: ejemplos que no representan bien el problema, una medida de error mal elegida, o un ajuste demasiado brusco.

[Diapositiva · Pesos al azar: el punto de partida]

> Idea central: Antes de entrenar, los pesos tienen valores al azar y la red responde sin sentido. El entrenamiento los mueve poco a poco hasta que dan buenas respuestas.

Hablemos del punto de partida, porque es una pregunta que suele quedar sin contestar: ¿con qué valores empieza una red?

Cuando se crea una red nueva, sus pesos tienen valores que se eligen al azar, dentro de rangos razonables. No hay otra opción, porque todavía no sabemos cuáles son los buenos. Si todos empezaran con el mismo valor, todas las neuronas de una capa harían lo mismo y se ajustarían igual, y la red no podría especializarse. El azar rompe esa simetría y permite que cada neurona tome su propio camino.

Con esos valores, la red hace predicciones sin sentido. Si le damos una imagen, marcará regiones que no corresponden a nada. La pérdida es alta. Es lo que esperamos, y es el estado desde el cual empieza todo.

A partir de ahí, cada ajuste mueve un poco los pesos en la dirección que reduce el error. Al principio, los cambios son enormes en efecto, porque cualquier mejora cuenta. Después se vuelven más finos.

Un detalle que sorprende a muchas personas: como el punto de partida es al azar, dos entrenamientos de la misma red con los mismos datos no dan exactamente el mismo resultado. Son parecidos, con una calidad comparable, pero no idénticos. Hay una forma de controlar esto, que consiste en fijar la semilla del generador de números al azar, de modo que siempre se obtengan los mismos valores iniciales, y por eso en un cuaderno bien documentado se anota esa semilla.

Otro detalle es que no empezar de cero cambia mucho. Si en lugar de pesos al azar se parte de pesos que ya vienen de un entrenamiento anterior, la red ya sabe hacer algunas cosas útiles desde el primer momento. Es una técnica que se usa mucho y de la que hablaremos en la siguiente sesión.

Por ahora quédense con esto: una red sin entrenar no es una red mala, es una red que todavía no aprendió. Todo lo que sabe, lo sabrá porque se le mostró.

[Diapositiva · Anotar imágenes: de dónde salen las respuestas]

> Idea central: Alguien tiene que dibujar el contorno de cada cabeza en las imágenes de entrenamiento. La red solo puede aprender lo que esas personas marcaron, con sus aciertos y sus errores.

Hablemos de la parte más humana del proceso, porque es la que menos se ve y la que más pesa: la anotación.

Para entrenar la red hace falta, como dijimos, un conjunto de imágenes con la respuesta correcta. Esa respuesta no existe sola. Alguien la tiene que crear. En nuestro caso, una persona abre cada imagen en una herramienta de anotación, y para cada cabeza dibuja su contorno, punto por punto, con el cursor. Es un trabajo lento y exigente.

La herramienta que se usó se llama CVAT. Es un programa pensado para anotar imágenes, que permite dibujar polígonos sobre los objetos y exportar el resultado en un formato que la red puede leer. Tiene una ventaja importante: no publica los datos, de modo que las imágenes de la investigación se quedan donde deben.

Es útil recordar las cantidades. Cada imagen tiene del orden de ciento cincuenta cabezas, así que anotar una imagen son ciento cincuenta contornos. Con diez imágenes, ya son más de mil quinientos. Parece mucho trabajo, pero fíjense que es muy poco frente a los millones de ejemplos que necesitaría una red entrenada desde cero. Y hay una forma de ahorrar ejemplos de la que hablaremos mañana.

Lo más delicado de la anotación es el criterio. ¿Qué cuenta como una cabeza? ¿Una mancha difusa sí o no? ¿Una cabeza parcialmente tapada por una cola? ¿Dos cabezas pegadas se dibujan juntas o por separado? Cada decisión que se toma al anotar es una decisión que la red va a aprender. Si una persona anota de una manera y otra de otra, la red recibe señales contradictorias.

Por eso es recomendable que alguien del grupo valide las anotaciones, y que haya un criterio escrito. Una red entrenada con anotaciones cuidadosas y consistentes funciona bien. Una entrenada con anotaciones descuidadas aprende el descuido.

Es una buena razón para recordar que los modelos no son neutros. Reflejan las decisiones de quienes los enseñaron.

[Diapositiva · Con respuestas y sin respuestas]

> Idea central: Aprender con ejemplos que traen su respuesta se llama aprendizaje supervisado. Es el que usamos, y por eso necesitamos anotar las imágenes.

Hay una distinción que ayuda a ubicar lo que hacemos dentro del panorama más amplio del aprendizaje automático.

Hay formas de aprendizaje en las que a la computadora se le dan ejemplos con la respuesta correcta incluida. A esto se le llama aprendizaje supervisado, porque alguien supervisa: ya dijo cuál es la respuesta. Un ejemplo es darle mil imágenes, cada una con la etiqueta perro o gato, para que aprenda a distinguirlos. El nuestro es de este tipo: le damos imágenes con el contorno de cada cabeza ya dibujado.

Hay otras formas en las que no se da la respuesta. A esto se le llama aprendizaje no supervisado. La computadora recibe datos sin etiquetas y tiene que encontrar por sí misma estructura en ellos, por ejemplo, agrupar imágenes parecidas sin que nadie le haya dicho cuáles son las categorías. Es útil cuando se quiere explorar datos, pero no sirve para una tarea tan precisa como trazar el contorno de una célula.

Y hay una tercera, el aprendizaje por refuerzo, donde el sistema aprende probando acciones y recibiendo premios o castigos, como en un juego. Es lo que se usa, por ejemplo, para enseñar a una máquina a jugar ajedrez o a controlar un robot.

Para nuestro problema, el supervisado es el adecuado, porque sabemos exactamente qué queremos: que la red encuentre cabezas. Y su costo es el que ya vimos: alguien tiene que anotar las imágenes. Cada contorno dibujado a mano es una respuesta correcta que la red usa para ajustarse.

Esto explica por qué la calidad de las anotaciones pesa tanto. En el aprendizaje supervisado, las respuestas son la fuente de todo lo que la red aprende. Si son buenas, la red puede ser buena. Si no lo son, no hay entrenamiento que lo compense.

[Diapositiva · La función de pérdida]

> Idea central: La pérdida es un número que resume qué tan mal lo hizo la red. Cuanto más cerca de la respuesta correcta, más baja; el entrenamiento consiste en bajarla.

Hablemos con más detalle de la medida del error, que se llama función de pérdida. Es la brújula del entrenamiento: sin ella, la red no sabría si va mejorando o empeorando.

Una pérdida es un número que se calcula comparando lo que la red predijo con lo que las personas marcaron. Para que sirva, necesita cumplir dos condiciones. La primera es que sea más baja mientras mejor sea la predicción. La segunda es que se pueda calcular de forma automática, para cada ejemplo, sin intervención de nadie.

En un problema muy sencillo, como adivinar el tamaño de una célula, la pérdida podría ser la diferencia entre el tamaño que adivinó la red y el real, elevada al cuadrado. Si la red dice cinco y la respuesta era cuatro, la pérdida es uno. Si dice siete, es nueve. Un error grande castiga mucho más que uno pequeño.

En una red como la nuestra, que debe encontrar cabezas y trazar su contorno, la pérdida combina varias medidas: si la red acertó en que ahí había una cabeza, qué tan bien quedó su ubicación y qué tanto coincide el contorno que dibujó la red con el que dibujó la persona. Todas se suman en un solo número, y ese es el que se intenta reducir.

Algo importante: la pérdida nos dice qué tan bien se ajusta la red a las respuestas que le dimos, no qué tan bien entiende el problema. Si las respuestas contienen errores, la red aprende a reproducirlos, y la pérdida puede ser muy baja a pesar de eso. Por eso es tan importante el trabajo de las personas que anotan las imágenes. Su cuidado y su criterio se convierten en el límite de lo que la red puede aprender.

Durante el entrenamiento, normalmente se ve una gráfica de la pérdida a lo largo del tiempo. Al principio es alta y baja deprisa. Después baja cada vez más despacio, y se estabiliza. Esa gráfica es una de las formas de saber si el entrenamiento va bien.

---

## Parte 6. Descenso del gradiente, retropropagación y cierre (video 6)

*3,504 palabras, unos 20.0 min de habla*

[Diapositiva · Ajustar: el descenso del gradiente]

> Idea central: Ajustar los pesos es como bajar una montaña con niebla: en cada paso se avanza hacia donde el suelo baja más. El tamaño del paso es la tasa de aprendizaje.

El siguiente paso es ajustar, que es la parte más ingeniosa. Imaginen que están en una montaña con una niebla densa y quieren llegar al valle más bajo, pero no ven el paisaje; solo sienten la inclinación del suelo bajo los pies. En cada paso avanzan un poquito hacia donde el suelo baja más. No saben dónde está el valle, pero siguiendo la pendiente descendente llegan poco a poco a un lugar bajo.

Esa imagen es literalmente el algoritmo con que se entrena la red, el descenso del gradiente. La altura del terreno es la pérdida, la posición es el conjunto de todos los pesos, la inclinación del suelo es el gradiente, que indica, para cada peso, en qué dirección moverlo para que la pérdida baje, y el tamaño del paso se llama tasa de aprendizaje. Con un paso demasiado grande se puede saltar por encima del valle y rebotar sin llegar nunca. Con uno muy pequeño se avanza tan lento que el entrenamiento no termina en tiempo razonable. Elegir el tamaño del paso es una de las decisiones que se toman antes de entrenar, y esas decisiones se llaman hiperparámetros.

Detengámonos un momento en la palabra gradiente, porque suena complicada y la idea es sencilla. El gradiente es, para cada peso, una indicación de hacia dónde moverlo y qué tan sensible es la pérdida a ese movimiento. Si al subir un poquito un peso la pérdida sube, el gradiente nos dice que hay que bajarlo. Y si al subirlo la pérdida baja, que hay que subirlo.

Volviendo a la montaña con niebla: no vemos el paisaje, pero sentimos la inclinación del terreno bajo los pies. En una montaña con dos direcciones, norte-sur y este-oeste, la inclinación nos dice cuánto sube o baja el suelo en cada una, y avanzamos en la combinación que más baja. En nuestra red hay decenas de millones de direcciones, una por cada peso, y el gradiente nos da la inclinación en todas a la vez.

Otra observación útil: nada garantiza que el valle al que llegamos sea el más profundo de toda la montaña. Podemos caer en un hueco intermedio. En la práctica, con redes grandes, estos huecos suelen ser suficientemente buenos, y por eso el método funciona. Pero explica por qué dos entrenamientos del mismo modelo con puntos de partida distintos pueden dar resultados ligeramente distintos.

Este procedimiento no es nuevo ni exclusivo de la inteligencia artificial. Es una técnica clásica de optimización, que se usa en ingeniería y en estadística para encontrar los valores que minimizan una cantidad. Lo que cambió es la escala: ahora se aplica a modelos con decenas de millones de parámetros y con cantidades enormes de datos.

[Diapositiva · Tasa de aprendizaje e hiperparámetros]

> Idea central: La tasa de aprendizaje es el tamaño del paso. Las decisiones que se toman antes de entrenar, como esta, se llaman hiperparámetros y se eligen probando.

Hablemos del tamaño del paso, que se llama tasa de aprendizaje, y que es de las decisiones más delicadas del entrenamiento.

Si el paso es demasiado grande, pasa lo que le pasaría a alguien que quiere bajar a un valle dando zancadas enormes: pasa por encima del fondo y llega al otro lado, más arriba de donde estaba. Después vuelve a pasarse. La pérdida, en vez de bajar, sube o rebota sin parar, y el entrenamiento nunca se estabiliza.

Si el paso es demasiado pequeño, la red sí baja, pero tan despacio que el entrenamiento tardaría una eternidad, o se agota el tiempo antes de llegar a un buen lugar. Con una máquina que se paga por tiempo de uso, eso también cuesta dinero.

El paso ideal está entre los dos, y no hay una fórmula que lo dé de antemano. Se prueba. Se entrena un poco con un valor, se ve cómo baja la pérdida, y se ajusta. Es común empezar con pasos más grandes al principio y reducirlos conforme la red se acerca al fondo.

La tasa de aprendizaje es un ejemplo de lo que se llama un hiperparámetro. Un hiperparámetro es una decisión que se toma antes de entrenar y que no la aprende la red. La diferencia con un peso es esta: los pesos los ajusta el entrenamiento, mientras que los hiperparámetros los elige la persona. Otros ejemplos son cuántas veces se recorren los datos, cuántos ejemplos se usan en cada ajuste, o cuántas capas tiene la red.

Es importante saber que existen, porque cuando se dice que un modelo se entrenó de cierta manera, parte de esa manera son sus hiperparámetros. Y por eso el cuaderno de entrenamiento se comparte con su configuración: para que cualquiera pueda repetir el entrenamiento con las mismas decisiones.

[Diapositiva · Retropropagación: repartir el error]

> Idea central: La retropropagación calcula cuánto contribuyó cada peso al error, yendo hacia atrás desde la salida, capa por capa. Se parece a revisar los tiros fallados de Batalla naval.

También hay que preguntarse cómo se calcula la pendiente con decenas de millones de pesos. Existe una técnica, la retropropagación, que aprovecha que la red es una cadena de operaciones simples para calcular de forma eficiente cuánto contribuyó cada peso al error. Se llama así porque el cálculo va hacia atrás: parte del error en la salida y retrocede capa por capa, repartiendo la responsabilidad.

Una forma de verlo es con el juego de Batalla naval. Al principio la red señala casi al azar, como cuando uno dispara a ciegas. Conforme se avanza por las capas, el peso del error va aumentando, como las piezas blancas que marcan los tiros que no dieron en el blanco. La retropropagación es ir desde el fondo, desde donde el error es más grande, hacia atrás, para ver cuál fue el origen, que era la aleatoriedad del principio.

Así, ensayo tras ensayo, los pesos van tomando valores útiles, y una red que empezó respondiendo al azar termina marcando los espermatozoides. Cómo mira una imagen una red convolucional, y cómo se aprovecha una red entrenada para otra cosa, lo vemos mañana.

Veamos la idea con una analogía más cercana. Imaginen una cadena de montaje con varias estaciones, y al final sale un producto defectuoso. Nadie sabe en cuál estación se cometió el error. Una persona revisa el producto y, caminando hacia atrás, va preguntando: ¿esta estación lo hizo bien? ¿La anterior? Y así identifica cuánto contribuyó cada una al defecto, y le pide a cada una que corrija lo suyo, un poco, en la dirección correcta.

La retropropagación hace exactamente eso con la red. El error aparece al final, en la salida. Desde ahí se calcula cuánto del error se debe a cada neurona de la última capa, luego a cada neurona de la capa anterior, y así hacia atrás hasta la entrada. Con eso se sabe, para cada peso, en qué dirección moverlo.

Lo que hace posible que esto sea eficiente es que una red es una cadena de operaciones simples, y la contribución de cada una se calcula con reglas elementales. Sin esa técnica, entrenar redes tan grandes sería prácticamente imposible. Con ella, una sola pasada hacia atrás da el gradiente de todos los pesos a la vez.

Y es el momento de unir las piezas. Un ciclo completo de entrenamiento es: la imagen entra, la red predice con los pesos actuales, se calcula la pérdida, la retropropagación reparte el error hacia atrás, el descenso del gradiente mueve un poco cada peso, y se pasa a la siguiente imagen. Eso, muchas veces, es lo que llamamos entrenar.

[Diapositiva · Lotes, iteraciones y épocas]

> Idea central: En cada ajuste se usa un lote de imágenes. Una iteración es un ajuste; una época es una pasada completa por todos los ejemplos. Se hacen muchas épocas.

Hay tres palabras que aparecen constantemente cuando se habla de entrenar una red, y que conviene distinguir: lote, iteración y época.

Imaginemos que tenemos cien imágenes de entrenamiento. En teoría, podríamos calcular el error de las cien y hacer un solo ajuste de los pesos. Pero eso es lento y gasta mucha memoria. En la práctica, se reparte el conjunto en pequeños grupos. Cada grupo es un lote. Por ejemplo, si cada lote tiene cuatro imágenes, las cien imágenes se reparten en veinticinco lotes.

Un ajuste de los pesos, hecho con un lote, es una iteración. Entonces, para pasar por las cien imágenes con lotes de cuatro, se hacen veinticinco iteraciones.

Y una pasada completa por todas las imágenes, en este caso las veinticinco iteraciones, es una época. Una época no suele bastar. La red necesita ver los mismos ejemplos muchas veces para ajustar sus pesos con cuidado, así que el entrenamiento se repite por varias épocas, y en cada una la pérdida baja un poco más.

Una forma de recordarlo es con el estudio de un examen. El lote es el montón de ejercicios que resuelves antes de revisar tus errores. La iteración es cada vez que revisas y corriges. Y la época es cada vez que terminas todos los ejercicios del libro. No se aprende a la primera vuelta, sino repasando muchas veces.

También hay que tener cuidado: demasiadas épocas pueden hacer que la red se aprenda de memoria los ejemplos, incluidos sus defectos, y que luego funcione mal con imágenes nuevas. Por eso, durante el entrenamiento, se separan algunas imágenes que la red nunca usa para ajustarse, y se miden con ellas los resultados. Ese tema, el de cuándo parar y cómo comprobar que la red de verdad generaliza, lo veremos en la última sesión.

[Diapositiva · Semillas y repetibilidad]

> Idea central: Como el entrenamiento usa azar, para poder repetirlo se fija una semilla y se documentan las decisiones. Así otra persona puede obtener el mismo modelo.

Hay una consecuencia práctica del azar en el entrenamiento que conviene tener presente: la repetibilidad.

En un entrenamiento hay varias cosas que dependen del azar. Los pesos iniciales se eligen al azar. El orden en que se presentan las imágenes se baraja en cada época. Y algunas técnicas que se usan para que la red generalice mejor también incluyen azar, como alterar ligeramente las imágenes en cada pasada.

Los computadores no generan azar de verdad. Generan secuencias de números que lo parecen, a partir de un valor inicial que se llama semilla. Con la misma semilla, la secuencia es siempre la misma. Y eso es una herramienta muy valiosa: si fijamos la semilla, el entrenamiento se vuelve repetible. Con los mismos datos, las mismas decisiones y la misma semilla, otra persona obtiene el mismo resultado.

Esto es importante en ciencia. Un resultado que no se puede repetir es difícil de defender. Si alguien afirma que un modelo funciona de cierta manera, otra persona debería poder reproducir el entrenamiento y comprobarlo.

En la práctica, repetir exactamente puede ser más delicado de lo que parece, porque ciertas operaciones en las tarjetas gráficas no son estrictamente deterministas. Aun así, lo que se busca es que los resultados sean comparables y que todo lo demás, los datos, las decisiones y el código, esté documentado.

Por eso, cuando el entrenamiento está en un cuaderno compartido, el cuaderno guarda esas decisiones: los hiperparámetros, la separación de las imágenes, la semilla. Quien lo abre sabe qué se hizo y puede hacerlo otra vez. Es el tercero de los principios que mencionamos: que todo se pueda repetir.

Y vale una advertencia de sentido común. Que un entrenamiento sea repetible no significa que sea correcto. Se puede repetir un entrenamiento malo tantas veces como se quiera. La repetibilidad es la condición para poder revisarlo, no una garantía de que esté bien.

[Diapositiva · Un entrenamiento de ejemplo: la pérdida bajando]

> Idea central: Durante el entrenamiento, la pérdida empieza alta, baja rápido al principio y se estabiliza. Esa curva es la forma de saber si el entrenamiento va bien.

Veamos cómo se ve un entrenamiento desde fuera. Los números que voy a dar son ilustrativos: sirven para entender la forma, y no son los de nuestro modelo.

Imaginemos que, antes de entrenar, la pérdida vale dos. La red responde casi al azar, y por eso el error es grande. Después de la primera época, la pérdida baja a uno punto dos. Después de la segunda, a cero punto ocho. De la tercera, a cero punto seis. De la cuarta, a cero punto cinco. De la quinta, a cero punto cuarenta y cinco.

Fíjense en la forma. Al principio, la pérdida baja muchísimo en cada época: de dos a uno punto dos, casi un punto. Después baja cada vez menos: de cero punto cinco a cero punto cuarenta y cinco son solo cinco centésimas. La curva es muy inclinada al principio y se va aplanando.

Esa forma es la esperada, y se entiende bien. Al principio la red está lejos de una buena respuesta y cualquier ajuste mejora mucho. Cuando ya está cerca, cada ajuste aporta poco. Cuando la curva se aplana, significa que la red ya aprendió casi todo lo que podía aprender de esos datos y con esas decisiones, y no tiene sentido seguir.

Esa gráfica sirve también para detectar problemas. Si la pérdida no baja, hay algo mal: quizá la tasa de aprendizaje es demasiado grande, o los datos tienen un problema. Si baja y luego sube, probablemente el paso fue excesivo. Si baja mucho en los datos de entrenamiento, pero no en las imágenes que la red nunca vio, es señal de que se está aprendiendo los ejemplos de memoria.

Quien entrena una red pasa mucho tiempo mirando esta curva. Es como el termómetro del entrenamiento: no dice todo, pero avisa si algo va mal.

[Diapositiva · Repaso: lo que hace una red]

> Idea central: Una red neuronal es una cadena de capas con pesos ajustables, que se ajustan con ejemplos mediante pérdida, gradiente y retropropagación. No hay comprensión: hay números ajustados.

Hagamos un repaso de lo que vimos en esta parte, para que se quede la imagen completa.

Empezamos con una neurona: recibe números, los multiplica por pesos, los suma, agrega un sesgo y aplica una activación. Con muchas neuronas se forma una capa, y con capas apiladas, una red. Cuando tiene muchas capas, hablamos de aprendizaje profundo.

Una red recién creada no sirve de nada, porque sus pesos son arbitrarios. Para que aprenda, se le muestran ejemplos que alguien anotó, se calcula con una función de pérdida qué tan lejos estuvo, y se reparte el error hacia atrás con la retropropagación. Con el descenso del gradiente se mueve cada peso un poco en la dirección que baja el error, con un paso cuyo tamaño es la tasa de aprendizaje. Y eso se repite durante muchas épocas.

Lo más importante, quizás, es lo que no hay. No hay comprensión, no hay reglas escritas a mano para reconocer espermatozoides, ni hay nada misterioso. Hay números ajustados con paciencia a partir de ejemplos, y por eso la calidad de los ejemplos y la revisión de las personas son tan importantes.

Con estas ideas ya tenemos las bases de qué es una red neuronal y cómo aprende. Mañana vamos a ver cómo mira una imagen una red como la nuestra, y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides. El lunes vamos a ver cómo se usa todo esto en un sitio funcionando, y el martes, cómo se prepararon los datos, cómo se entrenó y cómo se publicó.

[Diapositiva · Límites y cuidados al usar un modelo]

> Idea central: Un modelo funciona bien con imágenes parecidas a las de su entrenamiento. Con otras puede fallar sin avisar, y por eso se revisa siempre la imagen marcada.

Para cerrar esta parte, hablemos de los límites, porque conocerlos es lo que permite usar bien una herramienta.

El primer límite es el dominio. Un modelo funciona bien con imágenes parecidas a las que se usaron para entrenarlo: el mismo tipo de microscopio, la misma tinción, el mismo tipo de célula, un brillo y una nitidez comparables. Cuando las imágenes se alejan de eso, el rendimiento puede bajar, y no hay una alarma que avise.

El segundo es que el modelo no duda. Marca lo que cree que es una cabeza con el mismo aspecto con que marca una perfecta. No hay una luz que se prenda cuando está confundido. La revisión humana es, por eso, parte del proceso y no un lujo.

El tercero son los errores de dos tipos. Puede marcar algo que no es una cabeza, como una mancha o un trozo de cola. Y puede dejar sin marcar una cabeza que sí está. Los segundos son más difíciles de notar, porque no hay contorno que mirar. Por eso conviene mirar la imagen entera y no solo lo marcado.

El cuarto es que el modelo refleja los datos con los que se entrenó. Si había pocos ejemplos de cierta situación, la red la maneja peor. Mejorarlo requiere más ejemplos, más variados y mejor anotados, y un nuevo entrenamiento aparte.

Y el quinto es que un buen resultado en unas imágenes no garantiza uno bueno en todas. Hay que verificar con imágenes propias.

Nada de esto le quita valor al sistema. Un instrumento de laboratorio también tiene su rango de uso, y saber cuál es parte de saber usarlo. Lo que hace diferente a este es que muestra su trabajo: cada resultado trae la imagen marcada, para que cualquiera pueda comprobar si los contornos tienen sentido.

[Diapositiva · Preguntas que suelen surgir]

> Idea central: Respuestas breves a las dudas más comunes: la red no piensa, no necesita millones de imágenes si parte de una ya entrenada, puede equivocarse y se revisa.

Antes de cerrar, aprovecho para contestar algunas dudas que suelen aparecer cuando se explica esto por primera vez.

Una duda frecuente es si la red piensa. No. Calcula. Lo que parece comprensión es una consecuencia de un ajuste muy bien hecho. Es una distinción importante, porque nos recuerda que una red puede equivocarse con total aplomo.

Otra es cuántas imágenes hacen falta. Depende. Entrenando desde cero, muchísimas, decenas de miles o más. Pero cuando cada imagen tiene cientos de células, cada una aporta un ejemplo, y las cantidades necesarias son mucho menores. Mañana veremos otra forma de ahorrar ejemplos.

Otra es si la red puede equivocarse. Claro. Puede marcar algo que no es una cabeza, y puede dejar escapar una que sí lo es. Por eso el sistema muestra la imagen marcada, y por eso conviene revisarla. Hablaremos de esos errores con calma en la siguiente sesión.

Otra es por qué se necesita una tarjeta gráfica para entrenar. Porque entrenar es hacer una cantidad enorme de multiplicaciones y sumas parecidas entre sí, y las tarjetas gráficas están diseñadas para hacer muchas operaciones de ese tipo en paralelo. Un procesador común hace pocas cosas muy rápido; una tarjeta gráfica hace muchísimas cosas sencillas a la vez.

Otra es si la red mejora cuanto más se usa. No. Una vez entrenada, está fija. Para que mejore hay que entrenarla de nuevo, con más ejemplos o con mejores ejemplos.

Y otra, que es la más honesta, es si el resultado es siempre correcto. No, y nadie debería prometerlo. Es una herramienta de medición, con sus márgenes de error, como cualquier instrumento. Lo que sí podemos prometer es que es consistente y que se puede revisar.

[Diapositiva · Glosario de repaso]

> Idea central: Un repaso rápido de las palabras de hoy, una por una, para que queden a la mano.

Para terminar esta parte, un glosario rápido, con todas las palabras de hoy, en una frase cada una. Pueden usarlo como repaso.

Píxel: cada cuadrito de una imagen digital, con un número, o tres si es a color. Canal: cada una de las tablas de números de una imagen a color, la roja, la verde y la azul. Resolución: cuántos píxeles tiene una imagen. Histograma: una gráfica que cuenta cuántos píxeles hay de cada brillo.

Micra: la milésima parte de un milímetro. Escala: la relación entre píxeles y micras; en nuestro sistema es sesenta píxeles por micra, para todas las imágenes.

Inteligencia artificial: el campo amplio. Aprendizaje automático: lo que aprende de ejemplos. Red neuronal: una estructura de operaciones sencillas con pesos ajustables. Aprendizaje profundo: redes con muchas capas.

Neurona: multiplica entradas por pesos, suma, agrega un sesgo y aplica una activación. Capa: un conjunto de neuronas con las mismas entradas. Peso: un número ajustable; los pesos son lo que la red sabe. Sesgo: un número que decide qué tan exigente es una neurona. Activación: la regla que rompe la linealidad.

Pérdida: un número que mide qué tan lejos estuvo la red. Gradiente: la dirección en que hay que mover cada peso. Descenso del gradiente: bajar la pérdida paso a paso. Tasa de aprendizaje: el tamaño del paso. Hiperparámetro: una decisión que toma la persona antes de entrenar. Retropropagación: repartir el error hacia atrás. Lote, iteración y época: grupos de imágenes, un ajuste y una pasada completa.

Anotación: dibujar a mano las respuestas correctas. Aprendizaje supervisado: aprender con ejemplos que traen su respuesta. Semilla: el valor inicial del azar, que se fija para poder repetir un entrenamiento. Modelo: el archivo con los pesos. Entrenamiento: ajustar los pesos con ejemplos. Inferencia: usar el modelo ya entrenado.

Colab: el entorno para entrenar. Python: el lenguaje. Flask: la herramienta para el sitio. Servidor: la computadora donde vive el sitio.

[Diapositiva · Lo que vimos hoy]

> Idea central: El problema era contar y medir a mano; vimos qué es una imagen digital, algunas definiciones y las bases de las redes neuronales: neurona, capas y cómo aprenden.

Para cerrar, un resumen de lo que vimos. El problema era contar y medir a mano, que es lento y cambia según quién lo haga. Vimos qué es una imagen digital: una tabla de números, con sus formatos y su escala. Pusimos en orden algunas definiciones y las palabras que vamos a usar. Y vimos las bases de las redes neuronales: la neurona, la capa y la red, y cómo aprende una red ajustando sus pesos a partir de ejemplos.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Idea central: Hoy vimos qué es una red neuronal y cómo aprende. Mañana, sábado a las 9, vemos cómo mira una imagen una red convolucional y cómo se aprovecha una red entrenada para otra cosa; el lunes, el sitio funcionando, y el martes, datos, entrenamiento y despliegue.

Y una última idea para llevarse. Si hoy les quedó la impresión de que una red neuronal es una máquina de multiplicar y sumar, tienen razón, y es una buena impresión. Lo que la hace poderosa no es una inteligencia escondida, sino la cantidad de operaciones simples y el cuidado con el que se ajustan. Si se quedan con eso, entenderán por qué el sistema funciona, y también por qué conviene revisarlo.

Y termino con una pregunta que seguramente ya se hicieron: cómo sabe el sistema dónde hay un espermatozoide. Hoy vimos qué es una red neuronal y cómo aprende. Mañana, sábado a las nueve de la mañana, vamos a ver cómo mira una imagen una red como la nuestra, y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides.

El lunes vemos cómo funciona el sistema, con el sitio, y el martes, los datos, el entrenamiento y el despliegue en la nube. Si no alcanzamos a terminar algo de lo de hoy, lo retomamos en la siguiente sesión. Muchas gracias por su atención.

---

## Resumen de tiempos

| Parte | Palabras | Minutos de habla |
|---|---|---|
| El problema (video 1) | 3,709 | 21.2 |
| Qué son las imágenes (video 2) | 3,653 | 20.9 |
| La inteligencia artificial a nuestro alrededor, definiciones y palabras clave (video 3) | 3,279 | 18.7 |
| Entrenamiento, inferencia y la neurona (video 4) | 3,658 | 20.9 |
| Activación, capas y cómo aprende una red (video 5) | 3,637 | 20.8 |
| Descenso del gradiente, retropropagación y cierre (video 6) | 3,504 | 20.0 |
| Total | 21,440 | 122.5 |
