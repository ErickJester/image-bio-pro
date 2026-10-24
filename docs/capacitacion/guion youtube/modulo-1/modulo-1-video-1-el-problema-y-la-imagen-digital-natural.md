# Guion del módulo 1, video 1 de 3: El problema y la imagen digital (versión natural)

Image Bio Pro · Módulo 1 · Capacitación en video

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos. La apertura está escrita para que hables desde el inicio, sin que nadie te presente.

[Diapositiva · Image Bio Pro]

> Idea central: Todo el curso gira alrededor de un solo proyecto, Image Bio Pro. La portada se queda en pantalla mientras te presentas y agradeces; en la siguiente diapositiva empiezas a explicar qué es el proyecto.

Buenas tardes a todos. Mi nombre es Ángel Frausto Robles, soy ponente y parte del equipo que desarrolló este sitio web. Soy egresado de la Escuela Superior de Cómputo del Instituto Politécnico Nacional, especializado en temas de visión por computadora e inteligencia artificial.

Quiero agradecer a la doctora Sheila y al doctor Saúl la oportunidad de presentar este proyecto tan importante para la universidad.

[Diapositiva · ¿Qué es Image Bio Pro?]

> Idea central: Image Bio Pro es un proyecto de la UAM que lleva la inteligencia artificial a la docencia, la investigación, la difusión de la cultura y el servicio a la comunidad universitaria.

En esta serie de videos les voy a platicar de Image Bio Pro, un proyecto que la Universidad Autónoma Metropolitana está impulsando para que la inteligencia artificial llegue a lo que se hace todos los días en la universidad: dar clases, investigar, preservar y difundir la cultura, y también vincularse con la comunidad y servirle.

Quizás se pregunten qué es, exactamente, Image Bio Pro. Bueno, es una plataforma web nueva, pensada para meter las ideas más recientes de la inteligencia artificial en esas mismas tareas dentro de la UAM Iztapalapa. Dicho de otro modo, es la nueva era de la inteligencia artificial puesta al servicio de la comunidad universitaria.

[Diapositiva · Los cuatro módulos]

> Idea central: Son cuatro módulos: el primero el problema y las bases teóricas, el segundo cómo aprende una computadora, el tercero el sitio funcionando y el cuarto datos, entrenamiento y despliegue.

Este proyecto lo voy a presentar a lo largo de cuatro módulos. Antes que nada, les platico lo que vamos a ir viendo en ellos.

En el primer módulo empezamos por el problema que intentamos resolver, y les platicaré las bases teóricas que ocupamos para diseñar el sitio web.

En el segundo módulo, y lo resumo en una palabra, vemos cómo aprende una computadora, que es la esencia de una red neuronal artificial.

En el tercer módulo les enseño cómo funciona esta plataforma web. Una vez que entendimos el problema y exploramos las bases teóricas, ahora sí toca mostrar el sistema.

Y en el cuarto módulo veremos un par de ejemplos con datos, cómo se entrena la red neuronal y cómo es el despliegue de la información.

Quisiera pedirles que me den la oportunidad de cautivarlos para poder presentarles el sitio web en el tercer módulo. Me gustaría que primero tuvieran todo el background, todas las bases teóricas que nos permitieron desarrollar este sitio, para que cuando lo visiten sepan el trabajo y el enfoque de inteligencia artificial que utilizó esta plataforma. Espero que me puedan acompañar en estos cuatro módulos.

[Diapositiva · La agenda de este módulo]

> Idea central: En este módulo: el problema, qué es una imagen digital, algunas definiciones de inteligencia artificial y las redes neuronales, en tres videos. El sitio funcionando se presenta en el tercer módulo.

La agenda de este primer módulo: primero quisiera presentarles el problema, y después comenzamos explicando qué es una imagen digital.

Con esa base, en el segundo video ponemos en orden algunas definiciones de inteligencia artificial y empezamos con las redes neuronales: qué es una neurona. En el tercero juntamos varias neuronas en capas y vemos cómo aprende una red.

Cada módulo se divide en videos de unos 20 minutos. Este primer módulo son tres videos, y en cada uno vamos a ir avanzando por estos temas.

[Diapositiva · La inteligencia artificial en la educación y la investigación]

> Idea central: La inteligencia artificial puede analizar imágenes aprendiendo de ejemplos y no de reglas escritas, y lo hace sin cansarse. En este curso se ve aplicada a un problema real de biología de la reproducción.

Empiezo con una pregunta, y no hace falta que la contesten en voz alta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Hay muchas respuestas. Una, la que nos interesa hoy, es analizar imágenes. Una persona mira una imagen y reconoce lo que hay en ella. Un programa que aprendió de muchos ejemplos puede hacer algo parecido... y puede hacerlo una y otra vez, sin cansarse.

Lo que busco con este curso es que vean cómo se aplica la inteligencia artificial a un problema real de biología de la reproducción. Entonces, eh, para verlo en concreto, vamos a seguir un caso de estudio, o sea, un ejemplo: contar y medir espermatozoides en imágenes de microscopio.

No hace falta ser experto en nada. Si saben programar, van a ver cómo se arma el sistema. Y si vienen de biología, van a ver cómo se mide lo que ya conocen.

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

Y contar es lo más sencillo. Lo siguiente sería medir. ¿Qué tan grande es cada cabeza? ¿Qué tanto varían entre sí? ¿Cambian de tamaño cuando cambia una condición del experimento? Esas son las preguntas que interesan en una investigación, y para contestarlas hay que medir cada célula, una por una, en cada imagen.

[Diapositiva · Qué se quiere medir]

> Idea central: Del problema salen tres cosas que medir: cuántas cabezas hay, qué tamaño tiene cada una y cómo se distribuyen los tamaños.

Veamos qué queremos obtener de cada imagen, porque de ahí sale todo el diseño del sistema.

Primero, el conteo: cuántas cabezas hay. Es el número más directo y el que más se usa para comparar muestras.

Segundo, el tamaño de cada cabeza. Como las cabezas son curvas, una sola medida no alcanza, así que se miden dos: el área, que es cuánto espacio ocupa, y el largo. El área se obtiene contando los píxeles que ocupa la cabeza, y los píxeles se convierten a micras con una escala que veremos más adelante.

Tercero, la distribución de tamaños. En lugar de quedarnos con un solo número, queremos ver cómo se reparten las medidas: cuántas cabezas son pequeñas, cuántas medianas, cuántas grandes. Esa distribución suele parecerse a una campana, la famosa campana de Gauss, y de ella salen dos números que vamos a usar mucho: la media, que es el valor típico, y la desviación estándar, que dice qué tanto se alejan las demás del valor típico.

Conteo, tamaño y distribución: eso es lo que el sistema entrega por cada imagen. Y todo depende de algo previo, saber dónde está cada cabeza.

[Diapositiva · Contar y medir a mano]

> Idea central: Contar y medir a mano es lento, repetitivo y cambia según quién lo haga: tres personas cuidadosas pueden dar tres conteos distintos de la misma imagen. Un sistema que lo haga siempre igual hace falta.

Ahora sí, el problema. Contar y medir a mano toma mucho tiempo, es repetitivo y el resultado cambia según quién lo haga. Una sola imagen puede traer decenas o cientos de células, y muchas están encimadas o pegadas, así que cada quien traza la frontera entre una y otra en un lugar distinto. El ojo no tiene una regla fija. En la diapositiva puse tres conteos de la misma imagen, hechos por tres personas distintas. Son números de ejemplo, no de una medición real, pero la idea es esa: tres personas cuidadosas pueden llegar a tres resultados diferentes.

Por eso buscamos que la misma imagen dé siempre el mismo resultado, sin importar quién la analice, y que ese resultado se pueda revisar.

[Diapositiva · El camino de una imagen a un número]

> Idea central: Un mapa del recorrido: la imagen entra, la red encuentra las cabezas, el código mide cada una y salen los números, la gráfica, el CSV y el PDF.

Antes de meternos a los detalles, un mapa de a dónde vamos, para que cada pieza que veamos tenga su lugar.

El recorrido empieza con una imagen. Una persona la sube al sitio, y lo primero que pasa es que la imagen se prepara: se le da el tamaño y el formato que la red espera.

Después entra la red neuronal. Su trabajo es encontrar las cabezas y trazar el contorno de cada una. Esa es la única parte que se basa en aprendizaje.

Con los contornos en la mano, entra el código convencional. Para cada contorno cuenta los píxeles que encierra y, con la escala, los convierte en micras cuadradas: eso es el área. Mide el largo. Y luego junta todas las cabezas de la imagen y calcula el conteo, la media y la desviación estándar.

Fíjense que hay una parte que aprende y otra que calcula. La que aprende es la red, y por eso necesita ejemplos y entrenamiento. La que calcula es el código, y por eso es preciso, repetible y fácil de comprobar.

De todo este mapa, en este módulo vemos las piezas para entender la primera parte: qué es una imagen para una computadora, y qué es una red neuronal y cómo aprende. El recorrido completo, con el sitio funcionando, llega en el tercer módulo.

Pero antes de ver cómo se resuelve, tenemos que regresarnos a lo básico: qué es una imagen, y qué es una imagen digital.

[Diapositiva · ¿Qué son las imágenes?]

> Idea central: Antes de hablar de redes hay que entender qué es una imagen para una computadora. Esa pregunta abre esta parte.

Una imagen es la categoría general. Cualquier representación visual: un dibujo, una pintura, una captura, lo que sea. Una fotografía es un tipo de imagen, la que se captura con una cámara y registra la luz que llega a un sensor en un momento concreto. O sea, toda fotografía es una imagen, pero no toda imagen es una fotografía. En microscopía todo lo que se genera se llama imagen, así que de aquí en adelante voy a hablar de imágenes, y en particular de imágenes digitales.

[Diapositiva · Una imagen digital es una tabla de números]

> Idea central: Para la computadora una imagen es una tabla de números, uno por píxel, de 0 (negro) a 255 (blanco). Una imagen grande son casi dos millones y medio de números.

Vamos con algo que parece muy básico, y de lo que depende todo lo demás. ¿Qué es una imagen para una computadora?

Para la computadora, una imagen es, o sea, una tabla de números: una cuadrícula de cuadritos, los píxeles, y cada uno guarda cuánta luz tiene. En una imagen en tonos de gris, ese número es el brillo. Va de cero, que es negro, a doscientos cincuenta y cinco, que es blanco. Los números de en medio son los grises. En una imagen a color no es un número sino tres: uno para el rojo, otro para el verde y otro para el azul. Con la mezcla de los tres sale el color de ese cuadrito.

En la diapositiva tengo, a la izquierda, una imagen pequeña con un cuadro azul marcado. A la derecha, lo que hay dentro de ese cuadro, ampliado hasta que se ven los números. Son treinta y cinco cuadritos, siete por cinco. Fíjense en la parte de afuera: números bajos, casi negros. Y en el centro, números altos, hasta un doscientos cincuenta y cinco. Eso es lo que la computadora tiene delante cuando mira una imagen.

Una imagen real de las nuestras tiene casi dos millones y medio de cuadritos, cada uno con su número. La computadora los maneja todos a la vez sin problema, pero a un ojo humano eso no le dice nada: lo que nosotros vemos como células, la computadora lo ve como un mar de números.

Un detalle sobre esos números del cero al doscientos cincuenta y cinco: tienen una razón. Cada píxel guarda su valor en un byte, que son ocho bits, y con ocho bits se pueden representar doscientos cincuenta y seis valores distintos. Por eso el rango empieza en cero y termina en doscientos cincuenta y cinco. Con esos doscientos cincuenta y seis niveles, el ojo ve un degradado suave de negro a blanco, sin escalones. En una imagen a color son tres bytes por píxel, uno por cada color.

Por eso se habla de una matriz. Una matriz es simplemente una tabla de números en filas y columnas, como una hoja de cálculo. Cada celda es un píxel, y su valor es lo que sabemos de ese punto. En la diapositiva ven un fragmento de siete por cinco, treinta y cinco celdas.

La computadora no tiene ninguna idea previa de lo que hay en la imagen. No sabe dónde empieza una célula ni dónde termina. Cualquier cosa que queramos que haga, contar, medir o reconocer, tiene que construirse a partir de esos números y de las relaciones entre ellos. Un píxel solo no dice nada. Lo que dice algo es cómo se comportan los vecinos: dónde suben de golpe, dónde bajan, dónde se parecen.

Esa idea, que lo que importa son las relaciones entre píxeles vecinos, va a volver una y otra vez. Es justo la base de cómo una red neuronal mira una imagen.

[Diapositiva · El color: tres números por píxel]

> Idea central: Una imagen a color guarda tres números por píxel, uno para el rojo, uno para el verde y uno para el azul. Un naranja intenso es mucho rojo, algo de verde y poco azul.

Hasta ahora hablamos de tonos de gris, donde cada píxel tiene un solo número, el brillo. Pero nuestras imágenes tienen color, y el color añade una dimensión.

En una imagen a color, cada píxel guarda tres números en lugar de uno. Uno dice cuánto rojo tiene, otro cuánto verde y otro cuánto azul. Cada uno va, igual que el brillo, de cero a doscientos cincuenta y cinco. Esos tres números se llaman canales, y por eso se habla de los canales rojo, verde y azul. Mezclándolos en distintas proporciones sale cualquier color que veamos en una pantalla.

Un ejemplo. El naranja de una cabeza brillante podría tener doscientos cuarenta de rojo, ciento veintidós de verde y cuarenta y dos de azul. Mucho rojo, un verde medio y casi nada de azul. Si tuviera menos verde, treinta por ejemplo, se vería más rojo. Con más verde, doscientos por ejemplo, se vería más amarillo. Con tres números, entonces, queda descrito el color de cada píxel.

Entonces: una imagen en gris es una tabla de números. Una imagen a color son tres tablas del mismo tamaño, apiladas, una por canal. Todo lo que se haga con una imagen se hace, al final, con esas tablas.

[Diapositiva · Resolución y tamaño del archivo]

> Idea central: Más píxeles significan más detalle, pero también más números que guardar. Una imagen de nuestro tamaño pesa unos siete megabytes sin comprimir.

Una imagen típica de las nuestras mide mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Si multiplicamos, nos da un poco menos de dos millones y medio de píxeles, lo que algunas personas llaman dos punto cinco megapíxeles.

¿Qué cambia con la resolución? El detalle. Cada píxel representa un pedacito de lo que se fotografió, y mientras más píxeles hay, más pequeño es ese pedacito. Con pocos píxeles, la forma de una célula se describe con pocos cuadritos y el borde se ve escalonado. Con muchos, el borde se describe con más cuidado y la medida es más precisa. Por eso, cuando lo que importa es medir, conviene tener buena resolución.

Pero más píxeles también son más datos. Hagamos la cuenta del peso. Cada píxel de una imagen a color guarda tres números, y cada número ocupa un byte. Dos millones y medio de píxeles por tres bytes son más o menos siete millones y medio de bytes, unos siete megabytes. Eso pesa una de nuestras imágenes sin comprimir. En gris pesaría la tercera parte.

[Diapositiva · Una célula brillante son números altos]

> Idea central: En fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. Medir su área es contar cuántos píxeles ocupa.

A ver, ahora pensemos en una imagen de fluorescencia. ¿Cómo se ve una célula dentro de esa tabla de números? Como una zona de números altos sobre un fondo de números bajos. La célula brilla, así que sus píxeles tienen valores grandes. El fondo oscuro tiene valores pequeños. La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

Esto nos dice también cómo se mide el tamaño. En la diapositiva les muestro una célula pequeñita dibujada con números. Los doce cuadritos más brillantes, los que tienen el borde marcado, son la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles. Medir el área de una célula es contar cuántos píxeles ocupa. En una imagen real serán cientos de píxeles por célula, pero la idea es exactamente la misma. Más adelante, con la escala del sitio, esos píxeles se convierten en micras.

Y eso tiene una consecuencia práctica: separar lo que nos interesa del fondo se puede plantear como una pregunta sobre números. ¿Dónde están los números altos? ¿Dónde los bajos? ¿Dónde hay un cambio brusco de uno a otro? El borde de una célula es, en la tabla, el lugar donde los valores pasan de bajos a altos en muy pocos píxeles.

De ahí se entiende por qué el borde importa tanto. Si es nítido, en la tabla se ve un salto claro y trazar el contorno es sencillo. Si está borroso, los valores suben poco a poco y cuesta más decir dónde termina exactamente la célula. Esa diferencia se va a notar enseguida en los formatos de archivo y en la medida.

[Diapositiva · El histograma: contar los brillos]

> Idea central: Un histograma cuenta cuántos píxeles hay de cada nivel de brillo. En fluorescencia, casi todos son oscuros y unos pocos son muy brillantes, y esa forma explica por qué un umbral parece funcionar.

Hay una forma muy útil de resumir una imagen: el histograma. Es una gráfica que cuenta cuántos píxeles hay de cada nivel de brillo. En el eje horizontal van los valores, de cero a doscientos cincuenta y cinco. En el vertical, cuántos píxeles tienen ese valor.

Para construirlo se recorre la imagen píxel por píxel, y cada vez que se encuentra un valor se le suma uno a la columna correspondiente. Al final, las columnas altas son los valores más comunes y las bajas los poco comunes.

¿Cómo es el histograma de una imagen de fluorescencia? Recordemos la imagen: casi todo es fondo oscuro, y unas pocas zonas son células brillantes. Entonces el histograma tiene una columna altísima en los valores bajos, porque la inmensa mayoría de los píxeles son oscuros. Y después, una cola larga y baja hacia los valores altos, que son las células.

Esta herramienta la vamos a usar más adelante para entender qué ve la computadora. Y sirve para comprobar, antes de cualquier análisis, si una imagen está bien expuesta.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

> Idea central: BMP, PNG y TIFF guardan la imagen tal cual; JPG la comprime y puede mover los bordes, y con ellos el área. Conviene trabajar con los archivos originales del microscopio.

Bueno, un tema práctico: los formatos de archivo. No todos guardan la imagen igual. BMP, PNG y TIFF la guardan tal cual. JPG la comprime para que pese menos, y al comprimirla puede mover los bordes de las células. Y para medir, eso importa.

En la diapositiva tengo la misma célula dos veces. A la izquierda, con el borde nítido. A la derecha, con el borde difuminado y con bloques raros, que es lo que pasa con la compresión. ¿Por qué importa? Porque si el borde se difumina, cambia el contorno. Si cambia el contorno, cambia el área. Y entonces cambian los números que nos interesan.

La compresión es una forma de guardar la misma imagen en menos espacio, y hay dos grandes familias. La compresión sin pérdida guarda la imagen de forma más compacta, pero al abrirla se recupera exactamente cada número, sin cambiar ninguno. PNG y TIFF, bien usados, funcionan así. Y BMP, en la práctica, ni siquiera comprime: guarda todos los números tal cual.

La compresión con pérdida, que es la de JPG, hace otra cosa. Parte de la idea de que el ojo humano no nota ciertos cambios pequeños, y aprovecha eso para descartar información. Divide la imagen en bloques y simplifica cada bloque. El resultado ocupa mucho menos espacio, pero los números que se recuperan al abrir la imagen ya no son los originales. Solo se parecen.

Por eso la recomendación es sencilla. Trabajar con el archivo original que genera el microscopio o la cámara, sin pasarlo por aplicaciones de mensajería ni de redes sociales, que casi siempre lo comprimen para ahorrar espacio. Si necesitan reducir el peso, lo ideal es un formato sin pérdida. Y si solo tienen una versión en JPG, el sitio la acepta, pero lo avisa, porque la medida puede cambiar ligeramente.

[Diapositiva · Aumentos y micras]

> Idea central: Los aumentos del microscopio, 40X o 100X, cambian cuánto mide en la realidad cada píxel. Una micra es la milésima parte de un milímetro.

La unidad natural es la micra, o micrómetro. Una micra es la milésima parte de un milímetro. Un cabello humano mide unas decenas de micras de grosor, y una cabeza de espermatozoide mide unas pocas micras. A esa escala los milímetros resultan demasiado grandes, y por eso se usan micras.

El problema es que una imagen digital no sabe nada de micras. Solo sabe de píxeles. Y cuántas micras representa un píxel depende de cómo se tomó la imagen. Un factor es el aumento del microscopio. Con un aumento de cuarenta X, cada píxel cubre un pedazo de la muestra. Con uno de cien X, ese mismo píxel cubre un pedazo más pequeño, porque el objeto se ve más grande. Otros factores son el tipo de cámara y el tamaño de sus sensores.

Eso significa que dos imágenes que miden lo mismo en píxeles pueden representar tamaños reales muy distintos. Si comparáramos sus medidas en píxeles sin más, estaríamos comparando cosas que no son comparables.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

> Idea central: Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno. El sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, y la declara en cada resultado.

Para cerrar este bloque, la escala. Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno, porque los archivos no guardan ese dato. Y si queremos comparar imágenes entre sí, hay que ponerlas en una misma medida.

Por eso el sitio aplica la misma escala a todas. Es de sesenta píxeles por micra, y cada resultado dice cuál se usó. La imagen marcada trae una regla de trescientos píxeles que equivalen a cinco micras. Cómo se define esa escala no lo voy a explicar hoy; lo vemos en el tercer módulo, cuando revisemos el sistema por dentro.

Veámoslo con números. Si sesenta píxeles son una micra, un largo de sesenta píxeles es una micra de largo, y un largo de trescientos píxeles son cinco micras, que es justo la regla que va dibujada en la imagen. Con las áreas hay un paso más. Un área se mide en unidades cuadradas, así que una micra cuadrada son sesenta por sesenta píxeles, es decir, tres mil seiscientos píxeles. Si una célula ocupa tres mil seiscientos píxeles, su área es de una micra cuadrada. Si ocupa la mitad, media micra cuadrada. Por eso, en el sitio, las áreas en micras cuadradas pueden salir como números pequeños.

Esta decisión importa. Imaginen que el sitio no declarara la escala, y que una persona midiera con él imágenes de cuarenta X y otra de cien X. Las dos obtendrían áreas en micras cuadradas, pero las de una estarían infladas o reducidas respecto de las de la otra, y nadie se enteraría. Los números parecerían precisos y no lo serían.

Con esto cerramos la parte de las imágenes. En el siguiente video vemos dónde vive ya la inteligencia artificial, y empezamos con las redes neuronales.
