# Guion del módulo 1, video 3 de 3: Capas, cómo aprende una red y cierre

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Continúa del video anterior. Empieza con la frase que lo une con el video anterior.

*3,608 palabras, unos 20.6 min de habla*

[Diapositiva · De la neurona a la capa y a la red]

> Idea central: Una neurona sola hace muy poco. Muchas neuronas forman una capa, las capas se apilan y eso es una red neuronal; con muchas capas se habla de aprendizaje profundo.

En el video anterior construimos una neurona completa, con sus pesos, su sesgo y su activación. Ahora vamos a juntar muchas de ellas.

Una neurona sola hace muy poco: una decisión simple basada en una combinación ponderada. La potencia aparece al juntar muchas.

La siguiente escala es una capa: un conjunto de neuronas que reciben las mismas entradas pero con pesos distintos, de modo que cada una se fija en una combinación diferente. Cien neuronas mirando los mismos números, cada una con su criterio. La salida de la capa es la lista de las cien respuestas, una por neurona.

Luego se apilan las capas: la salida de una se convierte en la entrada de la siguiente. La primera capa son cien preguntas sobre los datos originales. La segunda capa no ve los datos originales, sino las respuestas de la primera, y hace sus propias preguntas sobre ellas. La tercera pregunta sobre las respuestas de la segunda, y así sucesivamente. Cada capa trabaja con un resumen más abstracto de la anterior.

Esa arquitectura es la red neuronal, y cuando tiene muchas capas se habla de aprendizaje profundo. Profundo, literalmente, por las capas apiladas. Si la visualizamos, hay una entrada, los números que describen el dato; una cascada de capas intermedias que los transforman una y otra vez; y una salida, que es la respuesta final. En un clasificador sencillo podría ser un número entre cero y uno que indique qué tan probable es que la imagen contenga un espermatozoide. En un modelo más elaborado, como el nuestro, la salida es más rica, pero el principio es el mismo.

La red que usamos tiene decenas de millones de pesos. Que un modelo esté entrenado significa que cada uno de esos millones de números ya tiene un valor adecuado. Un modelo sin entrenar tiene los mismos pesos con valores arbitrarios y produce respuestas sin sentido. El entrenamiento es el proceso que encuentra los valores correctos.

Una comparación con el cerebro conviene tomarla con cautela. El concepto nació de la idea de que las neuronas biológicas reciben señales, las ponderan y se activan según el total, pero una neurona artificial es mucho más simple, y la red completa no funciona como un cerebro. Lo útil de la analogía son las muchas unidades simples que, en capas, producen comportamientos complejos. Aunque se llame neuronal, la red no piensa ni comprende.

Dicho en corto, una red neuronal es una cadena de capas. Cada capa toma números, los combina con pesos, aplica una pequeña no linealidad y pasa el resultado a la siguiente. Los pesos son lo que la red sabe, y falta ver cómo lograr que tomen valores útiles.

Otra pregunta frecuente es qué hace cada capa. En una red que trabaja con imágenes, las primeras capas tienden a responder a cosas muy sencillas, como bordes y cambios de brillo. Las capas siguientes combinan esas respuestas para detectar formas, como curvas o esquinas. Y las últimas combinan formas para reconocer objetos completos. Nadie le dice a la red que haga eso; es lo que resulta útil, y por eso es lo que el entrenamiento termina encontrando. Es una jerarquía: de lo simple a lo complejo.

[Diapositiva · Una red pequeña, a mano]

> Idea central: Una red pequeña con dos entradas, dos neuronas ocultas y una salida se calcula con cuatro multiplicaciones y unas sumas. Una red grande hace lo mismo, millones de veces.

Para quitarle todo misterio, calculemos a mano una red muy pequeña. Tiene dos entradas, dos neuronas en una capa intermedia y una neurona de salida.

Supongamos que las dos entradas valen uno y dos. La primera neurona de la capa intermedia tiene los pesos uno y uno, y sesgo cero. Multiplica uno por uno, dos por uno, suma, y da tres. Como es positivo, la activación lo deja pasar: la salida de esta neurona es tres.

La segunda neurona tiene los pesos uno y menos uno, y sesgo cero. Multiplica uno por uno, dos por menos uno, suma, y da menos uno. Al ser negativo, la activación lo deja en cero y la neurona queda apagada.

Ahora la neurona de salida. Recibe las respuestas de la capa anterior: tres y cero. Tiene los pesos dos y uno, y un sesgo de menos uno. Multiplica tres por dos, que son seis, y cero por uno, que es cero. Suma seis. Le resta el sesgo, uno, y queda cinco. Esa es la respuesta de la red.

Eso es todo. Cuatro multiplicaciones en la capa intermedia, dos más en la salida, unas sumas y una regla de activación. Ahora imaginen esto con millones de neuronas, en decenas de capas. El tipo de operación es el mismo; solo cambia la cantidad, y esa cantidad permite que la red capture patrones muy sutiles.

[Diapositiva · Profundidad: por qué importan las capas]

> Idea central: Con una sola capa la red solo puede combinar entradas de forma simple. Apilar capas permite construir ideas sobre otras ideas.

Retomemos la pregunta de por qué se apilan capas, con un ejemplo cotidiano.

Imaginen que quieren describir qué es una casa a alguien que nunca ha visto una. Podrían empezar por las piezas más simples: líneas rectas, ángulos, superficies planas. Con esas piezas, describen partes: una puerta es un rectángulo con una manija, una ventana es un rectángulo con un cruce adentro, un techo es un triángulo sobre un rectángulo. Y con las partes describen el objeto: una casa es una puerta, ventanas y un techo, acomodados de cierta manera.

Cada nivel de la descripción se apoya en el anterior: una casa no se describe directamente con líneas rectas, sino pasando por partes. Esa es la idea de las capas apiladas: cada capa toma lo que hizo la anterior y construye algo un poco más elaborado.

Dicho de otro modo, la profundidad permite construir ideas complejas a partir de ideas más simples, y por eso el aprendizaje profundo funciona tan bien con datos que tienen estructura, como las imágenes.

[Diapositiva · Cómo aprende una red]

> Idea central: La red aprende por ensayo y corrección: predice, mide cuánto se equivocó, ajusta los pesos y repite. La respuesta correcta la ponen las personas, al anotar las imágenes.

¿Cómo aprende la red? ¿Cómo se puede lograr que millones de pesos tomen valores útiles? En pocas palabras, es un proceso de ensayo y corrección, bastante parecido a cómo aprendemos las personas.

Primero, la red hace una predicción con los pesos que tiene en ese momento. Segundo, se compara con la respuesta correcta que alguien proporcionó a mano, y se mide cuánto se equivocó. Tercero, se ajustan un poco los pesos en la dirección que habría reducido el error. Y cuarto, se repite con otro ejemplo, y así miles de veces.

Para mejorar, la red necesita saber cuánto se equivocó. Esa medida se llama función de pérdida, un número que resume la distancia entre lo que la red predijo y lo que debió predecir. Si marca justo los espermatozoides que las personas marcaron, la pérdida es pequeña; si marca otras cosas o se le escapa mucho, es grande.

Las respuestas correctas las ponen las personas, que marcan con un contorno cada espermatozoide de las imágenes de entrenamiento. A ese trabajo se le llama anotación, y de ahí aprende el modelo. Más adelante vemos cómo se hace.

Y es mecánico a una escala enorme. Una sola pasada por una imagen ajusta millones de pesos, y el proceso completo repite eso miles y miles de veces. Ningún ser humano podría hacerlo a mano, y esa es una buena razón para que lo haga la computadora. Pero conviene entender el ciclo, porque cuando algo sale mal casi siempre se debe a uno de sus pasos: ejemplos que no representan bien el problema, una medida de error mal elegida, o un ajuste demasiado brusco.

[Diapositiva · Anotar imágenes: de dónde salen las respuestas]

> Idea central: Alguien tiene que dibujar el contorno de cada cabeza en las imágenes de entrenamiento. La red solo puede aprender lo que esas personas marcaron, con sus aciertos y sus errores.

Para entrenar la red hace falta, como dijimos, un conjunto de imágenes con la respuesta correcta. Esa respuesta no existe sola. Alguien la tiene que crear. En nuestro caso, una persona abre cada imagen en una herramienta de anotación, y para cada cabeza dibuja su contorno, punto por punto, con el cursor. Es un trabajo lento y exigente.

Lo más delicado de la anotación es el criterio. ¿Qué cuenta como una cabeza? ¿Una mancha difusa sí o no? ¿Una cabeza parcialmente tapada por una cola? ¿Dos cabezas pegadas se dibujan juntas o por separado? Cada decisión que se toma al anotar es una decisión que la red va a aprender. Si una persona anota de una manera y otra de otra, la red recibe señales contradictorias.

Por eso es recomendable que alguien del grupo valide las anotaciones, y que haya un criterio escrito. Una red entrenada con anotaciones cuidadosas y consistentes funciona bien. Una entrenada con anotaciones descuidadas aprende el descuido.

Un modelo es, en cierto sentido, un espejo comprimido de sus anotaciones: refleja las decisiones de quienes lo enseñaron.

[Diapositiva · Con respuestas y sin respuestas]

> Idea central: Aprender con ejemplos que traen su respuesta se llama aprendizaje supervisado. Es el que usamos, y por eso necesitamos anotar las imágenes.

Hay formas de aprendizaje en las que a la computadora se le dan ejemplos con la respuesta correcta incluida. A esto se le llama aprendizaje supervisado, porque alguien supervisa: ya dijo cuál es la respuesta. Un ejemplo es darle mil imágenes, cada una con la etiqueta perro o gato, para que aprenda a distinguirlos. El nuestro es de este tipo: le damos imágenes con el contorno de cada cabeza ya dibujado.

Hay otras formas en las que no se da la respuesta. A esto se le llama aprendizaje no supervisado. La computadora recibe datos sin etiquetas y tiene que encontrar por sí misma estructura en ellos, por ejemplo, agrupar imágenes parecidas sin que nadie le haya dicho cuáles son las categorías. Es útil cuando se quiere explorar datos, pero no sirve para una tarea tan precisa como trazar el contorno de una célula.

Para nuestro problema, el supervisado es el adecuado, porque sabemos exactamente qué queremos: que la red encuentre cabezas. Y su costo es el que ya vimos: alguien tiene que anotar las imágenes. Cada contorno dibujado a mano es una respuesta correcta que la red usa para ajustarse.

Aquí las respuestas son la fuente de todo lo que la red aprende. Si son buenas, la red puede ser buena, y si no lo son, ningún entrenamiento lo compensa.

[Diapositiva · La función de pérdida]

> Idea central: La pérdida es un número que resume qué tan mal lo hizo la red. Cuanto más cerca de la respuesta correcta, más baja; el entrenamiento consiste en bajarla.

Una pérdida es un número que se calcula comparando lo que la red predijo con lo que las personas marcaron. Para que sirva, necesita cumplir dos condiciones. La primera es que sea más baja mientras mejor sea la predicción. La segunda es que se pueda calcular de forma automática, para cada ejemplo, sin intervención de nadie.

En un problema muy sencillo, como adivinar el tamaño de una célula, la pérdida podría ser la diferencia entre el tamaño que adivinó la red y el real, elevada al cuadrado. Si la red dice cinco y la respuesta era cuatro, la pérdida es uno. Si dice siete, es nueve. Un error grande castiga mucho más que uno pequeño.

En una red como la nuestra, que debe encontrar cabezas y trazar su contorno, la pérdida combina varias medidas: si la red acertó en que ahí había una cabeza, qué tan bien quedó su ubicación y qué tanto coincide el contorno que dibujó la red con el que dibujó la persona. Todas se suman en un solo número, y ese es el que se intenta reducir.

Ojo: la pérdida mide qué tanto se parece lo que hizo la red a las respuestas que le dimos, no qué tanto entiende el problema. Si esas respuestas traen errores, la red los aprende y la pérdida aun así puede salir muy baja.

[Diapositiva · Ajustar: el descenso del gradiente]

> Idea central: Ajustar los pesos es como bajar una montaña con niebla: en cada paso se avanza hacia donde el suelo baja más. El tamaño del paso es la tasa de aprendizaje.

El siguiente paso es ajustar, que es la parte más ingeniosa. Imaginen que están en una montaña con una niebla densa y quieren llegar al valle más bajo, pero no ven el paisaje; solo sienten la inclinación del suelo bajo los pies. En cada paso avanzan un poquito hacia donde el suelo baja más. No saben dónde está el valle, pero siguiendo la pendiente descendente llegan poco a poco a un lugar bajo.

Esa imagen es literalmente el algoritmo con que se entrena la red, el descenso del gradiente. La altura del terreno es la pérdida, la posición es el conjunto de todos los pesos, la inclinación del suelo es el gradiente, que indica, para cada peso, en qué dirección moverlo para que la pérdida baje, y el tamaño del paso se llama tasa de aprendizaje. Cómo elegir el tamaño de ese paso lo vemos enseguida.

La palabra gradiente suena complicada, pero la idea es sencilla. El gradiente es, para cada peso, una indicación de hacia dónde moverlo y qué tan sensible es la pérdida a ese movimiento. Si al subir un poquito un peso la pérdida sube, el gradiente nos dice que hay que bajarlo. Y si al subirlo la pérdida baja, que hay que subirlo.

Volviendo a la montaña con niebla: en una montaña con dos direcciones, norte-sur y este-oeste, la inclinación nos dice cuánto sube o baja el suelo en cada una, y avanzamos en la combinación que más baja. En nuestra red hay decenas de millones de direcciones, una por cada peso, y el gradiente nos da la inclinación en todas a la vez.

Nada garantiza que el valle al que llegamos sea el más profundo de toda la montaña. Podemos caer en un hueco intermedio. En la práctica, con redes grandes, estos huecos suelen ser suficientemente buenos, y por eso el método funciona.

[Diapositiva · Tasa de aprendizaje e hiperparámetros]

> Idea central: La tasa de aprendizaje es el tamaño del paso. Las decisiones que se toman antes de entrenar, como esta, se llaman hiperparámetros y se eligen probando.

Si el paso es demasiado grande, pasa lo que le pasaría a alguien que quiere bajar a un valle dando zancadas enormes: pasa por encima del fondo y llega al otro lado, más arriba de donde estaba. Después vuelve a pasarse. La pérdida, en vez de bajar, sube o rebota sin parar, y el entrenamiento nunca se estabiliza.

Si el paso es demasiado pequeño, la red sí baja, pero tan despacio que el entrenamiento tardaría una eternidad, o se agota el tiempo antes de llegar a un buen lugar. Con una máquina que se paga por tiempo de uso, eso también cuesta dinero.

El paso ideal está entre los dos, y no hay una fórmula que lo dé de antemano. Se prueba. Se entrena un poco con un valor, se ve cómo baja la pérdida, y se ajusta. Es común empezar con pasos más grandes al principio y reducirlos conforme la red se acerca al fondo.

La tasa de aprendizaje es un ejemplo de lo que se llama un hiperparámetro. Un hiperparámetro es una decisión que se toma antes de entrenar y que no la aprende la red. La diferencia con un peso es esta: los pesos los ajusta el entrenamiento, mientras que los hiperparámetros los elige la persona. Otros ejemplos son cuántas veces se recorren los datos, cuántos ejemplos se usan en cada ajuste, o cuántas capas tiene la red.

[Diapositiva · Retropropagación: repartir el error]

> Idea central: La retropropagación calcula cuánto contribuyó cada peso al error, yendo hacia atrás desde la salida, capa por capa. Se parece a revisar los tiros fallados de Batalla naval.

También hay que preguntarse cómo se calcula la pendiente con decenas de millones de pesos. Existe una técnica, la retropropagación, que aprovecha que la red es una cadena de operaciones simples para calcular de forma eficiente cuánto contribuyó cada peso al error. Va hacia atrás: parte del error en la salida y retrocede capa por capa.

Veamos la idea con una analogía más cercana. Imaginen una cadena de montaje con varias estaciones, y al final sale un producto defectuoso. Nadie sabe en cuál estación se cometió el error. Una persona revisa el producto y, caminando hacia atrás, va preguntando: ¿esta estación lo hizo bien? ¿La anterior? Y así identifica cuánto contribuyó cada una al defecto, y le pide a cada una que corrija lo suyo, un poco, en la dirección correcta.

Con la red pasa lo mismo: el error aparece al final, en la salida, y desde ahí se calcula cuánto se debe a cada neurona de la última capa, luego a las de la capa anterior, y así hasta la entrada. Con eso se sabe, para cada peso, en qué dirección moverlo.

Un ciclo completo de entrenamiento es: la imagen entra, la red predice con los pesos actuales, se calcula la pérdida, la retropropagación reparte el error hacia atrás, el descenso del gradiente mueve un poco cada peso, y se pasa a la siguiente imagen. Eso, muchas veces, es lo que llamamos entrenar.

Así, ensayo tras ensayo, los pesos van tomando valores útiles, y una red que empezó respondiendo al azar termina marcando los espermatozoides.

[Diapositiva · Lotes, iteraciones y épocas]

> Idea central: En cada ajuste se usa un lote de imágenes. Una iteración es un ajuste; una época es una pasada completa por todos los ejemplos. Se hacen muchas épocas.

Hay tres palabras que aparecen constantemente cuando se habla de entrenar una red, y que conviene distinguir: lote, iteración y época.

Imaginemos que tenemos cien imágenes de entrenamiento. En teoría, podríamos calcular el error de las cien y hacer un solo ajuste de los pesos. Pero eso es lento y gasta mucha memoria. En la práctica, se reparte el conjunto en pequeños grupos. Cada grupo es un lote. Por ejemplo, si cada lote tiene cuatro imágenes, las cien imágenes se reparten en veinticinco lotes.

Un ajuste de los pesos, hecho con un lote, es una iteración. Entonces, para pasar por las cien imágenes con lotes de cuatro, se hacen veinticinco iteraciones.

Y una pasada completa por todas las imágenes, en este caso las veinticinco iteraciones, es una época. Una época no suele bastar. La red necesita ver los mismos ejemplos muchas veces para ajustar sus pesos con cuidado, así que el entrenamiento se repite por varias épocas, y en cada una la pérdida baja un poco más.

Ojo con las épocas: si son demasiadas, la red puede aprenderse de memoria los ejemplos, con todo y sus defectos, y luego funcionar mal con imágenes nuevas. Por eso, durante el entrenamiento, se separan algunas imágenes que la red nunca usa para ajustarse, y se miden con ellas los resultados. Cuándo parar y cómo comprobar que la red de verdad generaliza lo veremos en el último módulo.

[Diapositiva · Semillas y repetibilidad]

> Idea central: Como el entrenamiento usa azar, para poder repetirlo se fija una semilla y se documentan las decisiones. Así otra persona puede obtener el mismo modelo.

En un entrenamiento hay varias cosas que dependen del azar. Los pesos iniciales se eligen al azar. El orden en que se presentan las imágenes se baraja en cada época. Y algunas técnicas que se usan para que la red generalice mejor también incluyen azar, como alterar ligeramente las imágenes en cada pasada.

Los computadores no generan azar de verdad. Generan secuencias de números que lo parecen, a partir de un valor inicial que se llama semilla. Con la misma semilla, la secuencia es siempre la misma. Y eso es útil: si fijamos la semilla, el entrenamiento se vuelve repetible. Con los mismos datos, las mismas decisiones y la misma semilla, otra persona obtiene el mismo resultado.

Esto es importante en ciencia. Un resultado que no se puede repetir es difícil de defender. Si alguien afirma que un modelo funciona de cierta manera, otra persona debería poder reproducir el entrenamiento y comprobarlo.

Un entrenamiento repetible no es por eso un entrenamiento correcto: se puede repetir uno malo tantas veces como se quiera. La repetibilidad es la condición para poder revisarlo, y no garantiza que esté bien.

[Diapositiva · Repaso: lo que hace una red]

> Idea central: Una red neuronal es una cadena de capas con pesos ajustables, que se ajustan con ejemplos mediante pérdida, gradiente y retropropagación. No hay comprensión: hay números ajustados.

Empezamos con una neurona: recibe números, los multiplica por pesos, los suma, agrega un sesgo y aplica una activación. Con muchas neuronas se forma una capa, y con capas apiladas, una red. Cuando tiene muchas capas, hablamos de aprendizaje profundo.

Una red recién creada no sirve de nada, porque sus pesos son arbitrarios. Para que aprenda, se le muestran ejemplos que alguien anotó, se calcula con una función de pérdida qué tan lejos estuvo, y se reparte el error hacia atrás con la retropropagación. Con el descenso del gradiente se mueve cada peso un poco en la dirección que baja el error, con un paso cuyo tamaño es la tasa de aprendizaje. Y eso se repite durante muchas épocas.

Lo que no hay también importa: no hay comprensión ni reglas escritas a mano para reconocer espermatozoides. Hay números ajustados con paciencia a partir de ejemplos, y por eso la calidad de los ejemplos y la revisión de las personas son tan importantes.

Con estas ideas ya tenemos las bases de qué es una red neuronal y cómo aprende.

[Diapositiva · Límites y cuidados al usar un modelo]

> Idea central: Un modelo funciona bien con imágenes parecidas a las de su entrenamiento. Con otras puede fallar sin avisar, y por eso se revisa siempre la imagen marcada.

Para cerrar esta parte, hablemos de los límites, porque conocerlos es lo que permite usar bien una herramienta.

El primer límite es el dominio. Un modelo funciona bien con imágenes parecidas a las que se usaron para entrenarlo: el mismo tipo de microscopio, la misma tinción, el mismo tipo de célula, un brillo y una nitidez comparables. Cuando las imágenes se alejan de eso, el rendimiento puede bajar, y no hay una alarma que avise.

El segundo es que el modelo no duda. Marca lo que cree que es una cabeza con el mismo aspecto con que marca una perfecta. No hay una luz que se prenda cuando está confundido. La revisión humana es, por eso, parte del proceso.

El tercero son los errores de dos tipos. Puede marcar algo que no es una cabeza, como una mancha o un trozo de cola. Y puede dejar sin marcar una cabeza que sí está. Los segundos son más difíciles de notar, porque no hay contorno que mirar. Por eso conviene mirar la imagen entera y no solo lo marcado.

[Diapositiva · Lo que vimos hoy]

> Idea central: El problema era contar y medir a mano; vimos qué es una imagen digital, algunas definiciones y las bases de las redes neuronales: neurona, capas y cómo aprenden.

Para cerrar, un resumen de lo que vimos. El problema de partida era el conteo y la medición manuales, que tardan mucho y dependen de quién los haga. Vimos qué es una imagen digital: una cuadrícula de números, con sus formatos y su escala. Pusimos en orden algunas definiciones y las palabras que vamos a usar. Y vimos las bases de las redes neuronales: la neurona, la capa y la red, y cómo aprende una red ajustando sus pesos a partir de ejemplos.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Idea central: En este módulo vimos qué es una red neuronal y cómo aprende. En el siguiente módulo vemos cómo mira una imagen una red convolucional y cómo se aprovecha una red entrenada para otra cosa; después, el sitio funcionando, y al final, datos, entrenamiento y despliegue.

Y una última idea para llevarse. Si les quedó la impresión de que una red neuronal es una máquina de multiplicar y sumar, tienen razón. Lo que la hace poderosa es la cantidad de operaciones simples y el cuidado con el que se ajustan. Con eso en mente, se entiende por qué el sistema funciona y también por qué conviene revisarlo.

Y termino con una pregunta que seguramente ya se hicieron: ¿cómo sabe el sistema dónde hay un espermatozoide? De eso trata el siguiente módulo: cómo mira una imagen una red como la nuestra, y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides.

Luego viene el sistema funcionando, con el sitio, y por último los datos, el entrenamiento y el despliegue en la nube. Muchas gracias por su atención.
