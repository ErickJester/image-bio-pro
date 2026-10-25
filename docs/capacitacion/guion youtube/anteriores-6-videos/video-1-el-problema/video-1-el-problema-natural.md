# Guion del video 1 de 6: El problema (versión natural)

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos. La apertura (diapositivas 2, 3 y 4) está escrita para que hables desde el inicio, sin que nadie te presente.

[Diapositiva · BioImage-Repro UAM]

> Idea central: Todo el curso gira alrededor de un solo proyecto, BioImage-Repro UAM. La portada se queda en pantalla mientras te presentas y agradeces; en la siguiente diapositiva empiezas a explicar qué es el proyecto.

Buenas tardes a todos. Mi nombre es Ángel Frausto Robles, soy ponente y parte del equipo que desarrolló este sitio web. Soy egresado de la Escuela Superior de Cómputo del Instituto Politécnico Nacional, especializado en temas de visión por computadora e inteligencia artificial.

Quiero agradecer a la doctora Sheila y al doctor Saúl la oportunidad de presentar este proyecto tan importante para la universidad.

[Diapositiva · ¿Qué es BioImage-Repro UAM?]

> Idea central: BioImage-Repro UAM es un proyecto de la UAM que lleva la inteligencia artificial a la docencia, la investigación, la difusión de la cultura y el servicio a la comunidad universitaria.

En esta serie de videos les voy a platicar de BioImage-Repro UAM, un proyecto que la Universidad Autónoma Metropolitana está impulsando para que la inteligencia artificial llegue a lo que se hace todos los días en la universidad: dar clases, investigar, preservar y difundir la cultura, y también vincularse con la comunidad y servirle.

Quizás se pregunten qué es, exactamente, BioImage-Repro UAM. Bueno, es una plataforma web nueva, pensada para meter las ideas más recientes de la inteligencia artificial en esas mismas tareas dentro de la UAM Iztapalapa. Dicho de otro modo, es la nueva era de la inteligencia artificial puesta al servicio de la comunidad universitaria.

[Diapositiva · Los cuatro módulos]

> Idea central: Son cuatro módulos: el primero el problema y las bases teóricas, el segundo cómo aprende una computadora, el tercero el sitio funcionando y el cuarto datos, entrenamiento y despliegue.

Este proyecto lo voy a presentar a lo largo de cuatro módulos. Antes que nada, les platico lo que vamos a ir viendo en ellos.

En el primer módulo empezamos por el problema que intentamos resolver, y les platicaré las bases teóricas que ocupamos para diseñar el sitio web.

En el segundo módulo, y lo resumo en una palabra, vemos cómo aprende una computadora, que es la esencia de una red neuronal artificial.

En el tercer módulo les enseño cómo funciona esta plataforma web. Una vez que entendimos el problema y exploramos las bases teóricas, ahora sí toca mostrar el sistema.

Y en el cuarto módulo veremos un par de ejemplos con datos, cómo se entrena la red neuronal y cómo es el despliegue de la información.

Quisiera pedirles que me den la oportunidad de cautivarlos para poder presentarles el sitio web en el tercer módulo. Me gustaría que primero tuvieran todo el background, todas las bases teóricas que nos permitieron desarrollar este sitio, para que cuando lo visiten sepan el trabajo y el enfoque de inteligencia artificial que utilizó esta plataforma. Espero que me puedan acompañar en estos cuatro módulos.

[Diapositiva · La agenda de este módulo]

> Idea central: En este módulo: el problema, qué es una imagen digital, algunas definiciones de inteligencia artificial y el comienzo de las redes neuronales. El sitio funcionando se presenta en el tercer módulo.

La agenda de este primer módulo: primero quisiera presentarles el problema, y después comenzamos explicando qué es una imagen digital.

Después de la imagen digital vamos a poner en orden algunas definiciones de inteligencia artificial, y con eso empezamos con las redes neuronales: qué es una neurona, qué es una capa y cómo se arma una red.

Cada módulo se divide en videos de unos 20 minutos. Este primer módulo son seis videos, y en cada uno vamos a ir avanzando por estos temas.

[Diapositiva · La inteligencia artificial en la educación y la investigación]

> Idea central: La inteligencia artificial puede analizar imágenes aprendiendo de ejemplos y no de reglas escritas, y lo hace sin cansarse. En este curso se ve aplicada a un problema real de biología de la reproducción.

Empiezo con una pregunta, y no hace falta que la contesten en voz alta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Hay muchas respuestas. Una, la que nos interesa hoy, es analizar imágenes. Una persona mira una imagen y reconoce lo que hay en ella. Un programa que aprendió de muchos ejemplos puede hacer algo parecido... y puede hacerlo una y otra vez, sin cansarse.

Bueno, antes de seguir hay que aclarar qué es eso de aprender de ejemplos, porque es la idea que sostiene todo el curso. Normalmente, cuando uno quiere que una computadora haga algo, le escribe reglas: si pasa esto, haz aquello. Eso funciona de maravilla para una calculadora o una hoja de cálculo, donde las reglas son exactas. Pero reconocer un espermatozoide en una imagen con reglas exactas es casi imposible. A ver, ¿cómo describirían ustedes la forma de una cabeza, con todas sus variaciones de tamaño, de orientación y de brillo? Cada regla que escribieran se rompería con la siguiente imagen.

Entonces se hace otra cosa. Se le muestran a la computadora muchos ejemplos ya resueltos: imágenes donde una persona marcó a mano dónde están los espermatozoides. El programa ajusta por sí mismo lo que necesita para reproducir esas marcas. A eso se le llama aprender de ejemplos, y a lo que resulta de ese proceso se le llama modelo. Cómo sucede ese ajuste lo vemos con calma más adelante en este módulo. Por ahora basta con recordar que al modelo le dimos ejemplos en lugar de reglas.

Las imágenes vienen de muchas fuentes, y una de las más importantes en las ciencias de la vida es la microscopía. Con un microscopio vemos células, por ejemplo espermatozoides, y vemos cómo cambian de tamaño y de forma bajo ciertas condiciones. Cada imagen trae información, pero alguien tiene que sacarla: contar, medir, comparar.

Las imágenes que vamos a usar vienen de la microscopía de fluorescencia, y en un momento les explico en qué consiste.

Lo que busco con este curso es que vean cómo se aplica la inteligencia artificial a un problema real de biología de la reproducción. Entonces, eh, para verlo en concreto, vamos a seguir un caso de estudio, o sea, un ejemplo: contar y medir espermatozoides en imágenes de microscopio.

No hace falta ser experto en nada. Si saben programar, van a ver cómo se arma el sistema. Y si vienen de biología, van a ver cómo se mide lo que ya conocen.

Esto tiene sentido en un entorno universitario. En la docencia, una herramienta que analiza imágenes le permite a quien está aprendiendo ver, con sus propios datos, cómo se pasa de una imagen a una medida. En la investigación, el conteo y la medición dejan de depender de horas de trabajo manual y de la mirada de una sola persona. Y en la difusión de la cultura científica, un sitio abierto a la comunidad muestra que la inteligencia artificial es una herramienta que se puede usar, revisar y entender.

Por eso, a lo largo de los módulos vamos a ver el sitio funcionando y también las ideas que hay debajo. Así cualquiera de ustedes puede razonar sobre qué hace el sistema, cuándo confiar en él y cuándo mirar con más cuidado. Esa es la ventaja de conocer las bases: dejan de ser una caja negra.

[Diapositiva · Microscopía de fluorescencia]

> Idea central: En fluorescencia, la célula se tiñe con un colorante que devuelve la luz en otro color. Por eso brilla sobre un fondo oscuro y es fácil de distinguir.

Veamos primero qué tipo de imágenes vamos a usar, porque no todas vienen del mismo entorno. Trabajamos con microscopía de fluorescencia.

Las células se tiñen con un colorante especial, un fluoróforo. Ese colorante tiene una propiedad curiosa: cuando recibe luz de cierto color, la absorbe, y un instante después devuelve luz de otro color. El microscopio ilumina la muestra con la luz que el colorante absorbe y, al mirar, filtra todo lo demás para dejar pasar solo la que el colorante devuelve.

El resultado es una imagen muy particular. Lo teñido brilla y lo demás queda oscuro. En nuestras imágenes las cabezas de los espermatozoides se ven rojas o anaranjadas, las colas verde amarillento y el fondo casi negro.

Para la computadora esto es una gran ayuda: separar un objeto del fondo resulta más fácil cuando el objeto tiene números altos y el fondo números bajos. Más adelante vemos qué es una imagen digital y por qué esto importa tanto.

También existen imágenes de fondo claro, donde la muestra se ve oscura sobre un fondo iluminado. Se ven distintas, así que para cada tipo hay un modelo distinto. Hoy nos concentramos en fluorescencia, que es el caso más claro para entender las ideas.

[Diapositiva · El caso de estudio]

> Idea central: Una imagen de fluorescencia muestra manchas brillantes sobre fondo oscuro, y cada una es la cabeza de un espermatozoide. Contarlas a simple vista es posible, pero medir cada una ya no.

Les muestro cómo se ve el problema. Esta es una imagen de fluorescencia: manchas brillantes de colores sobre un fondo oscuro. Cada mancha es la cabeza de un espermatozoide, y a veces se alcanza a ver una línea que sale de ella, la cola. Ahora pregunto, sin esperar respuesta: ¿cuántos hay en esta imagen? Lo primero que haría cualquiera es contarlos con la vista, uno por uno. Y si además hay que medir cada uno, ya no basta con mirar.

En la imagen hay cabezas de distintos tonos, unas más anaranjadas, otras más rojizas. Hay colas que salen como líneas delgadas. Hay zonas donde las células se tocan y colas que se cruzan con otras cabezas. Si me pidieran contarlas, yo empezaría por una esquina y avanzaría célula por célula, y a la mitad me preguntaría si ya conté esta o aquella.

Y contar es lo más sencillo. Lo siguiente sería medir. ¿Qué tan grande es cada cabeza? ¿Qué tanto varían entre sí? ¿Cambian de tamaño cuando cambia una condición del experimento? Esas son las preguntas que interesan en una investigación, y para contestarlas hay que medir cada célula, una por una, en cada imagen.

[Diapositiva · Qué se quiere medir]

> Idea central: Del problema salen tres cosas que medir: cuántas cabezas hay, qué tamaño tiene cada una y cómo se distribuyen los tamaños.

Veamos qué queremos obtener de cada imagen, porque de ahí sale todo el diseño del sistema.

Primero, el conteo: cuántas cabezas hay. Es el número más directo y el que más se usa para comparar muestras.

Segundo, el tamaño de cada cabeza. Como las cabezas son curvas, una sola medida no alcanza, así que se miden dos: el área, que es cuánto espacio ocupa, y el largo. El área se obtiene contando los píxeles que ocupa la cabeza, y los píxeles se convierten a micras con una escala que veremos más adelante.

Tercero, la distribución de tamaños. En lugar de quedarnos con un solo número, queremos ver cómo se reparten las medidas: cuántas cabezas son pequeñas, cuántas medianas, cuántas grandes. Esa distribución suele parecerse a una campana, la famosa campana de Gauss, y de ella salen dos números que vamos a usar mucho: la media, que es el valor típico, y la desviación estándar, que dice qué tanto se alejan las demás del valor típico.

Todo eso tiene que poder llevarse a otro lado. Por eso los resultados se exportan en un archivo CSV, para trabajarlos en una hoja de cálculo, y en un informe en PDF, para compartirlos.

Conteo, tamaño y distribución: eso es lo que el sistema entrega por cada imagen. Y todo depende de algo previo, saber dónde está cada cabeza.

[Diapositiva · Media y desviación estándar, con un ejemplo]

> Idea central: La media es el valor típico y la desviación estándar dice qué tanto se alejan los demás. Dos grupos con la misma media pueden ser muy distintos.

Ya nombramos dos números que van a aparecer mucho: la media y la desviación estándar. Veámoslos con un ejemplo pequeño, para que dejen de ser solo palabras.

Supongamos que medimos el área de cinco cabezas, en micras cuadradas, y obtenemos: dos, dos punto dos, uno punto ocho, dos punto cuatro y uno punto seis. La media es el promedio de siempre. Se suman los cinco valores, que dan diez, y se divide entre cinco. La media es dos. Ese es el valor típico.

Ahora queremos saber qué tanto se parecen entre sí. Para eso se mide cuánto se aleja cada valor de la media. Las diferencias son: cero, cero punto dos, menos cero punto dos, cero punto cuatro y menos cero punto cuatro. Si las promediáramos tal cual, los positivos y los negativos se cancelarían, así que primero se elevan al cuadrado: cero, cero punto cero cuatro, cero punto cero cuatro, cero punto dieciséis y cero punto dieciséis. Se suman y dan cero punto cuarenta. Se promedian, dividiendo entre cuatro, que es uno menos el número de datos, y da cero punto uno. Por último se saca la raíz cuadrada, que da más o menos cero punto tres. Esa es la desviación estándar.

Ahora un segundo grupo de cinco cabezas: uno punto nueve, dos, dos, dos punto uno y dos. Su media también es dos, pero sus valores están muy pegados. Con la misma cuenta, la desviación estándar es de más o menos cero punto cero siete.

Los dos grupos tienen la misma media, dos, y sin embargo son muy distintos: en uno las cabezas varían bastante y en el otro casi no varían. Si solo reportáramos la media, no nos daríamos cuenta. La desviación estándar nos dice qué tan dispersos están los datos.

Por eso el sistema entrega las dos cosas, y por eso la gráfica de la distribución de tamaños es tan útil: muestra de un vistazo cuál es el valor típico y qué tanto se reparte el resto.

[Diapositiva · Para qué sirven estas medidas en una investigación]

> Idea central: Con las imágenes se comparan condiciones: se mide cada grupo y se compara cómo cambian el número y el tamaño de las células. Interpretar la diferencia es trabajo de quien investiga.

¿Para qué sirven estos números en una investigación? Para comparar condiciones, y eso le da sentido a todo el trabajo.

Un experimento típico compara condiciones. Se toma una muestra en una condición, por ejemplo sin tratamiento, y otra en una condición distinta. De cada muestra se toman varias imágenes, y de cada imagen salen un conteo, una lista de tamaños, una media y una desviación estándar. Con esos números se pregunta si la condición cambió algo. ¿Hay más o menos células? ¿Son más grandes o más pequeñas? ¿Varían más o menos entre sí?

Para contestar con seriedad hace falta repetir. Una sola imagen puede ser rara por casualidad. Varias imágenes por condición, y varias muestras por condición, permiten distinguir una diferencia real de una variación normal. Y para saber si una diferencia es lo bastante grande como para tomarla en serio se usan pruebas estadísticas, que se aplican con los datos que el sistema entrega en el archivo CSV.

Nuestro sistema cuenta, mide y entrega los datos de forma uniforme y verificable. No interpreta. Decidir si una diferencia es significativa, qué la causa y qué implica biológicamente le corresponde a quien conoce la biología. El sistema es un instrumento, como una balanza: da el peso, y no decide si el resultado del experimento es bueno o malo.

Por eso importa que el instrumento sea estable: si no lo es, las diferencias que aparezcan podrían venir del instrumento y no de la condición. Con un método de medición uniforme, lo que se ve en los datos es lo que de verdad cambió en la muestra.

[Diapositiva · Contar y medir a mano]

> Idea central: Contar y medir a mano es lento, repetitivo y cambia según quién lo haga: tres personas cuidadosas pueden dar tres conteos distintos de la misma imagen. Un sistema que lo haga siempre igual hace falta.

Ahora sí, el problema. Contar y medir a mano toma mucho tiempo, es repetitivo y el resultado cambia según quién lo haga. Una sola imagen puede traer decenas o cientos de células, y muchas están encimadas o pegadas, así que cada quien traza la frontera entre una y otra en un lugar distinto. El ojo no tiene una regla fija. En la diapositiva puse tres conteos de la misma imagen, hechos por tres personas distintas. Son números de ejemplo, no de una medición real, pero la idea es esa: tres personas cuidadosas pueden llegar a tres resultados diferentes.

Y no se trata solo de contar. Para la investigación muchas veces lo que importa es el tamaño: cuánto mide cada célula, cuánto varía de una a otra y cómo cambia entre una condición y otra. Medir a mano exige trazar cada contorno con cuidado y leer el resultado, una y otra vez, para cientos de células en muchas imágenes. Un sistema que haga ese trabajo siempre igual deja de ser un lujo y se vuelve una necesidad.

Pensemos en dos personas que cuentan la misma imagen con todo cuidado. Una decide que dos cabezas muy pegadas son una sola, porque no ve el estrechamiento entre ellas. La otra sí lo ve y cuenta dos. Ninguna se equivocó por descuido; cada una aplicó su criterio. Pero sus números ya no coinciden, y comparar sus resultados deja de ser confiable.

Con las medidas pasa algo parecido. Para medir una cabeza a mano hay que decidir dónde termina el borde, y el borde de una célula brillante no es una línea nítida sino una transición de brillo. Una persona traza el contorno un poco por dentro y otra un poco por fuera, y esa diferencia, que parece mínima, cambia el área de forma apreciable, porque el área crece con el cuadrado del tamaño.

Y hay un tema de registro. Cuando se mide a mano, rara vez queda constancia de cómo se midió: dónde se trazó cada contorno, qué criterio se siguió. Un sistema automático puede guardar la imagen marcada, y cualquiera puede abrirla y ver exactamente qué se midió.

Por todo eso buscamos que la misma imagen dé siempre el mismo resultado, sin importar quién la analice, y que ese resultado se pueda revisar.

[Diapositiva · Un día de trabajo sin el sistema]

> Idea central: Con cuentas sencillas se ve que el trabajo manual no escala: unas pocas decenas de imágenes ya significan miles de células y medio día de trabajo.

A ver, pongamos números al problema. Son ilustrativos, y sirven para ver el orden de magnitud.

Un experimento pequeño, con treinta imágenes. Cada imagen, como dijimos, tiene del orden de ciento cincuenta cabezas. Treinta por ciento cincuenta son cuatro mil quinientas células. Para medir cada una a mano hay que localizarla, trazar su contorno con cuidado y anotar el resultado. Si cada célula tomara solo diez segundos, que ya es poquísimo, serían cuarenta y cinco mil segundos. Doce horas y media de trabajo sin descanso, sin contar los errores y sin comparar con nadie.

Ahora imaginen que el experimento tiene varias condiciones y que cada condición se repite. Esas treinta imágenes se vuelven cientos. Y si alguien quiere repetir el análisis con otro criterio de medición, el trabajo empieza de nuevo.

El otro lado de la cuenta es la calidad. Doce horas de trabajo repetitivo no se hacen con la misma atención de principio a fin. Hay cansancio, hay distracciones, y el criterio cambia sin que uno se dé cuenta. Medir la célula número cuatro mil con el mismo cuidado que la número uno es muy difícil para cualquiera.

Un sistema automático cambia las dos cuentas. Procesa una imagen en unas decenas de segundos, sin cansarse y con el mismo criterio. Treinta imágenes toman unos minutos. Y si se quiere repetir un análisis, se repite en el mismo tiempo.

El valor está en la velocidad y también en que el resultado es comparable. Dos personas que analizan sus imágenes con el mismo sistema miden con la misma regla, y eso permite comparar entre laboratorios y entre experimentos.

[Diapositiva · El camino de una imagen a un número]

> Idea central: Un mapa del recorrido: la imagen entra, la red encuentra las cabezas, el código mide cada una y salen los números, la gráfica, el CSV y el PDF.

Antes de meternos a los detalles, un mapa de a dónde vamos, para que cada pieza que veamos tenga su lugar.

El recorrido empieza con una imagen. Una persona la sube al sitio, y lo primero que pasa es que la imagen se prepara: se le da el tamaño y el formato que la red espera.

Después entra la red neuronal. Su trabajo es encontrar las cabezas y trazar el contorno de cada una. Esa es la única parte que se basa en aprendizaje.

Con los contornos en la mano, entra el código convencional. Para cada contorno cuenta los píxeles que encierra y, con la escala, los convierte en micras cuadradas: eso es el área. Mide el largo. Y luego junta todas las cabezas de la imagen y calcula el conteo, la media y la desviación estándar.

Con todo eso se arman los resultados que mencionamos: la imagen marcada con los contornos, la tabla con una fila por cabeza, la gráfica de tamaños y los archivos para descargar.

Fíjense que hay una parte que aprende y otra que calcula. La que aprende es la red, y por eso necesita ejemplos y entrenamiento. La que calcula es el código, y por eso es preciso, repetible y fácil de comprobar.

De todo este mapa, hoy vemos las piezas para entender la primera parte: qué es una imagen para una computadora, y qué es una red neuronal y cómo aprende. El recorrido completo, con el sitio funcionando, llega en el tercer módulo.

Pero antes de ver cómo se resuelve, tenemos que regresarnos a lo básico: qué es una imagen, y qué es una imagen digital.
