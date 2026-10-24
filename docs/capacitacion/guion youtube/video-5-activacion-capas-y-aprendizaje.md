# Guion del video 5 de 6: Activación, capas y cómo aprende una red

Image Bio Pro · Módulo 1 · Capacitación en video

Continúa del video 4. Empieza con la frase que lo une con el video anterior.

*3,299 palabras, unos 18.9 min de habla*

[Diapositiva · La función de activación]

> Idea central: La activación introduce una torcedura en la suma: si el total es negativo la salida es cero, y si es positivo se deja pasar. Sin ella, apilar capas no serviría de nada.

En el video anterior construimos una neurona con sus pesos y su sesgo, y falta un paso. Dediquemos unos minutos a la función de activación, porque es el paso que más fácil se pasa por alto.

Recordemos lo que hace la neurona hasta antes de este paso. Multiplica las entradas por los pesos y suma, y eso es una operación lineal. Una operación lineal es aquella en que, si duplico la entrada, se duplica la salida, y si sumo dos entradas, la salida es la suma de las salidas. Es una operación muy limitada.

Si se encadenan varias operaciones lineales, el resultado sigue siendo una sola operación lineal. Pueden apilar diez capas, o cien, o mil, y si solo multiplican y suman, todo eso equivale a una única capa. La profundidad no aporta nada.

Aquí entra la función de activación. Después de multiplicar y sumar, se aplica una pequeña regla que rompe la linealidad. La que más se usa hoy es muy sencilla: si el resultado es negativo, la salida es cero; si es positivo, la salida es ese mismo número. Se le llama la rectificadora, porque rectifica los negativos.

En una gráfica, es una línea plana en cero hasta el origen, y luego una línea que sube en diagonal. Esa pequeña esquina es lo que hace posible que las redes sean tan potentes. Con ella, cada neurona tiene un comportamiento de encendido y apagado: no responde nada hasta que el estímulo supera cierto nivel, y a partir de ahí responde de forma proporcional.

Y al combinar muchas de estas esquinas en capas, la red puede dibujar relaciones tan complicadas como queramos: curvas, bordes, formas. Es la diferencia entre trazar con una sola regla recta y trazar con miles de segmentos pequeños que, juntos, siguen cualquier contorno.

En conjunto: los pesos fijan a qué atiende cada neurona, el sesgo cuánta exigencia tiene, y la activación permite que la red represente algo más que simples proporciones. Con esas tres ideas queda completa la neurona.

[Diapositiva · De la neurona a la capa y a la red]

> Idea central: Una neurona sola hace muy poco. Muchas neuronas forman una capa, las capas se apilan y eso es una red neuronal; con muchas capas se habla de aprendizaje profundo.

Una neurona sola hace muy poco: una decisión simple basada en una combinación ponderada. La potencia aparece al juntar muchas.

La siguiente escala es una capa: un conjunto de neuronas que reciben las mismas entradas pero con pesos distintos, de modo que cada una se fija en una combinación diferente. Cien neuronas mirando los mismos números, cada una con su criterio. La salida de la capa es la lista de las cien respuestas, una por neurona.

Luego se apilan las capas: la salida de una se convierte en la entrada de la siguiente. La primera capa son cien preguntas sobre los datos originales. La segunda capa no ve los datos originales, sino las respuestas de la primera, y hace sus propias preguntas sobre ellas. La tercera pregunta sobre las respuestas de la segunda, y así sucesivamente. Cada capa trabaja con un resumen más abstracto de la anterior.

Esa arquitectura es la red neuronal, y cuando tiene muchas capas se habla de aprendizaje profundo. Profundo, literalmente, por las capas apiladas. Si la visualizamos, hay una entrada, los números que describen el dato; una cascada de capas intermedias que los transforman una y otra vez; y una salida, que es la respuesta final. En un clasificador sencillo podría ser un número entre cero y uno que indique qué tan probable es que la imagen contenga un espermatozoide. En un modelo más elaborado, como el nuestro, la salida es más rica, pero el principio es el mismo.

La red que usamos tiene decenas de millones de pesos. Que un modelo esté entrenado significa que cada uno de esos millones de números ya tiene un valor adecuado. Un modelo sin entrenar tiene los mismos pesos con valores arbitrarios y produce respuestas sin sentido. El entrenamiento es el proceso que encuentra los valores correctos.

Una comparación con el cerebro conviene tomarla con cautela. El concepto nació de la idea de que las neuronas biológicas reciben señales, las ponderan y se activan según el total, pero una neurona artificial es mucho más simple, y la red completa no funciona como un cerebro. Lo útil de la analogía son las muchas unidades simples que, en capas, producen comportamientos complejos. Aunque se llame neuronal, la red no piensa ni comprende.

Dicho en corto, una red neuronal es una cadena de capas. Cada capa toma números, los combina con pesos, aplica una pequeña no linealidad y pasa el resultado a la siguiente. Los pesos son lo que la red sabe, y falta ver cómo lograr que tomen valores útiles.

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

La segunda neurona tiene los pesos uno y menos uno, y sesgo cero. Multiplica uno por uno, dos por menos uno, suma, y da menos uno. Al ser negativo, la activación lo deja en cero y la neurona queda apagada.

Ahora la neurona de salida. Recibe las respuestas de la capa anterior: tres y cero. Tiene los pesos dos y uno, y un sesgo de menos uno. Multiplica tres por dos, que son seis, y cero por uno, que es cero. Suma seis. Le resta el sesgo, uno, y queda cinco. Esa es la respuesta de la red.

Eso es todo. Cuatro multiplicaciones en la capa intermedia, dos más en la salida, unas sumas y una regla de activación. Ahora imaginen esto con millones de neuronas, en decenas de capas. El tipo de operación es el mismo; solo cambia la cantidad, y esa cantidad permite que la red capture patrones muy sutiles.

Si cambiamos uno solo de los pesos, la respuesta final cambia. Por ejemplo, si el segundo peso de la primera neurona fuera tres en lugar de uno, esa neurona daría uno más seis, que son siete, y la respuesta final sería trece en lugar de cinco. Entrenar una red es precisamente buscar los valores de todos esos pesos que hacen que la respuesta sea la correcta para los ejemplos que tenemos.

[Diapositiva · Profundidad: por qué importan las capas]

> Idea central: Con una sola capa la red solo puede combinar entradas de forma simple. Apilar capas permite construir ideas sobre otras ideas.

Retomemos la pregunta de por qué se apilan capas, con un ejemplo cotidiano.

Imaginen que quieren describir qué es una casa a alguien que nunca ha visto una. Podrían empezar por las piezas más simples: líneas rectas, ángulos, superficies planas. Con esas piezas, describen partes: una puerta es un rectángulo con una manija, una ventana es un rectángulo con un cruce adentro, un techo es un triángulo sobre un rectángulo. Y con las partes describen el objeto: una casa es una puerta, ventanas y un techo, acomodados de cierta manera.

Cada nivel de la descripción se apoya en el anterior: una casa no se describe directamente con líneas rectas, sino pasando por partes. Esa es la idea de las capas apiladas: cada capa toma lo que hizo la anterior y construye algo un poco más elaborado.

Una red de una sola capa tendría que describir la casa directamente a partir de los píxeles. Es posible en teoría, pero necesitaría un número enorme de neuronas para cubrir todas las combinaciones posibles. Con varias capas, cada una resuelve un pedazo pequeño y el conjunto resuelve el problema completo con muchos menos recursos.

También es verdad que más capas no siempre es mejor. Cada capa agrega pesos que ajustar, y una red muy profunda con pocos ejemplos puede aprender de memoria en lugar de generalizar. Hay un equilibrio, y encontrarlo es parte del diseño.

Dicho de otro modo, la profundidad permite construir ideas complejas a partir de ideas más simples, y por eso el aprendizaje profundo funciona tan bien con datos que tienen estructura, como las imágenes.

[Diapositiva · Cómo aprende una red]

> Idea central: La red aprende por ensayo y corrección: predice, mide cuánto se equivocó, ajusta los pesos y repite. La respuesta correcta la ponen las personas, al anotar las imágenes.

¿Cómo aprende la red? ¿Cómo se puede lograr que millones de pesos tomen valores útiles? En pocas palabras, es un proceso de ensayo y corrección, bastante parecido a cómo aprendemos las personas.

Primero, la red hace una predicción con los pesos que tiene en ese momento. Segundo, se compara con la respuesta correcta que alguien proporcionó a mano, y se mide cuánto se equivocó. Tercero, se ajustan un poco los pesos en la dirección que habría reducido el error. Y cuarto, se repite con otro ejemplo, y así miles de veces.

Para mejorar, la red necesita saber cuánto se equivocó. Esa medida se llama función de pérdida, un número que resume la distancia entre lo que la red predijo y lo que debió predecir. Si marca justo los espermatozoides que las personas marcaron, la pérdida es pequeña; si marca otras cosas o se le escapa mucho, es grande.

Las respuestas correctas las ponen las personas, que marcan con un contorno cada espermatozoide de las imágenes de entrenamiento. A ese trabajo se le llama anotación, y de ahí aprende el modelo. Más adelante vemos cómo se hace.

Ninguno de estos cuatro pasos requiere que alguien le explique a la red qué es un espermatozoide. Lo único que se necesita son ejemplos con su respuesta correcta y una forma de medir qué tan lejos estuvo la red de esa respuesta. Todo lo demás es mecánico: predecir, comparar, ajustar, repetir.

Y es mecánico a una escala enorme. Una sola pasada por una imagen ajusta millones de pesos, y el proceso completo repite eso miles y miles de veces. Ningún ser humano podría hacerlo a mano, y esa es una buena razón para que lo haga la computadora. Pero conviene entender el ciclo, porque cuando algo sale mal casi siempre se debe a uno de sus pasos: ejemplos que no representan bien el problema, una medida de error mal elegida, o un ajuste demasiado brusco.

[Diapositiva · Pesos al azar: el punto de partida]

> Idea central: Antes de entrenar, los pesos tienen valores al azar y la red responde sin sentido. El entrenamiento los mueve poco a poco hasta que dan buenas respuestas.

Hablemos del punto de partida: ¿con qué valores empieza una red?

Cuando se crea una red nueva, sus pesos tienen valores que se eligen al azar, dentro de rangos razonables. No hay otra opción, porque todavía no sabemos cuáles son los buenos. Si todos empezaran con el mismo valor, todas las neuronas de una capa harían lo mismo y se ajustarían igual, y la red no podría especializarse. El azar rompe esa simetría y permite que cada neurona tome su propio camino.

Con esos valores, la red hace predicciones sin sentido. Si le damos una imagen, marcará regiones que no corresponden a nada. La pérdida es alta. Es lo que esperamos, y es el estado desde el cual empieza todo.

A partir de ahí, cada ajuste mueve un poco los pesos en la dirección que reduce el error. Al principio los cambios son grandes, porque cualquier mejora cuenta. Después se vuelven más finos.

Como el punto de partida es al azar, dos entrenamientos de la misma red con los mismos datos no dan exactamente el mismo resultado: son parecidos, pero no idénticos. Más adelante vemos cómo controlar ese azar.

Otro detalle es que no empezar de cero cambia mucho. Si en lugar de pesos al azar se parte de pesos que ya vienen de un entrenamiento anterior, la red ya sabe hacer algunas cosas útiles desde el primer momento. Es una técnica que se usa mucho y de la que hablaremos en el siguiente módulo.

Una red sin entrenar es una red que todavía no aprendió, y todo lo que sepa lo sabrá porque se le mostró.

[Diapositiva · Anotar imágenes: de dónde salen las respuestas]

> Idea central: Alguien tiene que dibujar el contorno de cada cabeza en las imágenes de entrenamiento. La red solo puede aprender lo que esas personas marcaron, con sus aciertos y sus errores.

Hablemos de la parte más humana del proceso, porque es la que menos se ve y la que más pesa: la anotación.

Para entrenar la red hace falta, como dijimos, un conjunto de imágenes con la respuesta correcta. Esa respuesta no existe sola. Alguien la tiene que crear. En nuestro caso, una persona abre cada imagen en una herramienta de anotación, y para cada cabeza dibuja su contorno, punto por punto, con el cursor. Es un trabajo lento y exigente.

La herramienta que se usó se llama CVAT. Es un programa pensado para anotar imágenes, que permite dibujar polígonos sobre los objetos y exportar el resultado en un formato que la red puede leer. Tiene una ventaja importante: no publica los datos, de modo que las imágenes de la investigación se quedan donde deben.

Es útil recordar las cantidades. Cada imagen tiene del orden de ciento cincuenta cabezas, así que anotar una imagen son ciento cincuenta contornos. Con diez imágenes, ya son más de mil quinientos. Parece mucho trabajo, pero es muy poco frente a los millones de ejemplos que necesitaría una red entrenada desde cero. Y hay una forma de ahorrar ejemplos de la que hablaremos en el siguiente módulo.

Lo más delicado de la anotación es el criterio. ¿Qué cuenta como una cabeza? ¿Una mancha difusa sí o no? ¿Una cabeza parcialmente tapada por una cola? ¿Dos cabezas pegadas se dibujan juntas o por separado? Cada decisión que se toma al anotar es una decisión que la red va a aprender. Si una persona anota de una manera y otra de otra, la red recibe señales contradictorias.

Por eso es recomendable que alguien del grupo valide las anotaciones, y que haya un criterio escrito. Una red entrenada con anotaciones cuidadosas y consistentes funciona bien. Una entrenada con anotaciones descuidadas aprende el descuido.

Un modelo es, en cierto sentido, un espejo comprimido de sus anotaciones: refleja las decisiones de quienes lo enseñaron.

[Diapositiva · Con respuestas y sin respuestas]

> Idea central: Aprender con ejemplos que traen su respuesta se llama aprendizaje supervisado. Es el que usamos, y por eso necesitamos anotar las imágenes.

Hay una distinción que ayuda a ubicar lo que hacemos dentro del panorama más amplio del aprendizaje automático.

Hay formas de aprendizaje en las que a la computadora se le dan ejemplos con la respuesta correcta incluida. A esto se le llama aprendizaje supervisado, porque alguien supervisa: ya dijo cuál es la respuesta. Un ejemplo es darle mil imágenes, cada una con la etiqueta perro o gato, para que aprenda a distinguirlos. El nuestro es de este tipo: le damos imágenes con el contorno de cada cabeza ya dibujado.

Hay otras formas en las que no se da la respuesta. A esto se le llama aprendizaje no supervisado. La computadora recibe datos sin etiquetas y tiene que encontrar por sí misma estructura en ellos, por ejemplo, agrupar imágenes parecidas sin que nadie le haya dicho cuáles son las categorías. Es útil cuando se quiere explorar datos, pero no sirve para una tarea tan precisa como trazar el contorno de una célula.

Y hay una tercera, el aprendizaje por refuerzo, donde el sistema aprende probando acciones y recibiendo premios o castigos, como en un juego. Es lo que se usa, por ejemplo, para enseñar a una máquina a jugar ajedrez o a controlar un robot.

Para nuestro problema, el supervisado es el adecuado, porque sabemos exactamente qué queremos: que la red encuentre cabezas. Y su costo es el que ya vimos: alguien tiene que anotar las imágenes. Cada contorno dibujado a mano es una respuesta correcta que la red usa para ajustarse.

Aquí las respuestas son la fuente de todo lo que la red aprende. Si son buenas, la red puede ser buena, y si no lo son, ningún entrenamiento lo compensa.

[Diapositiva · La función de pérdida]

> Idea central: La pérdida es un número que resume qué tan mal lo hizo la red. Cuanto más cerca de la respuesta correcta, más baja; el entrenamiento consiste en bajarla.

Hablemos con más detalle de la medida del error, que se llama función de pérdida. Es la brújula del entrenamiento: sin ella, la red no sabría si va mejorando o empeorando.

Una pérdida es un número que se calcula comparando lo que la red predijo con lo que las personas marcaron. Para que sirva, necesita cumplir dos condiciones. La primera es que sea más baja mientras mejor sea la predicción. La segunda es que se pueda calcular de forma automática, para cada ejemplo, sin intervención de nadie.

En un problema muy sencillo, como adivinar el tamaño de una célula, la pérdida podría ser la diferencia entre el tamaño que adivinó la red y el real, elevada al cuadrado. Si la red dice cinco y la respuesta era cuatro, la pérdida es uno. Si dice siete, es nueve. Un error grande castiga mucho más que uno pequeño.

En una red como la nuestra, que debe encontrar cabezas y trazar su contorno, la pérdida combina varias medidas: si la red acertó en que ahí había una cabeza, qué tan bien quedó su ubicación y qué tanto coincide el contorno que dibujó la red con el que dibujó la persona. Todas se suman en un solo número, y ese es el que se intenta reducir.

Ojo: la pérdida mide qué tanto se parece lo que hizo la red a las respuestas que le dimos, no qué tanto entiende el problema. Si esas respuestas traen errores, la red los aprende y la pérdida aun así puede salir muy baja.

Esa pérdida se vigila durante todo el entrenamiento. En el siguiente video vemos cómo se ajustan los pesos.
