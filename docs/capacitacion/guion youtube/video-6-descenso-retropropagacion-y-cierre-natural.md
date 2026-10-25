# Guion del video 6 de 6: Descenso del gradiente, retropropagación y cierre (versión natural)

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Continúa del video 5. Empieza con la frase que lo une con el video anterior.

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos.

[Diapositiva · Ajustar: el descenso del gradiente]

> Idea central: Ajustar los pesos es como bajar una montaña con niebla: en cada paso se avanza hacia donde el suelo baja más. El tamaño del paso es la tasa de aprendizaje.

En el video anterior vimos cómo se mide el error de una red con la función de pérdida. El siguiente paso es ajustar, que es la parte más ingeniosa. Imaginen que están en una montaña con una niebla densa y quieren llegar al valle más bajo. No ven el paisaje. Solo sienten la inclinación del suelo bajo los pies. En cada paso avanzan un poquito hacia donde el suelo baja más. No saben dónde está el valle, pero siguiendo la pendiente llegan, poco a poco, a un lugar bajo.

Esa imagen es literalmente el algoritmo con que se entrena la red: el descenso del gradiente. La altura del terreno es la pérdida. La posición es el conjunto de todos los pesos. La inclinación del suelo es el gradiente, que indica, para cada peso, en qué dirección moverlo para que la pérdida baje. Y el tamaño del paso se llama tasa de aprendizaje. Cómo elegir el tamaño de ese paso lo vemos enseguida.

La palabra gradiente suena complicada, pero la idea es sencilla. El gradiente es, para cada peso, una indicación de hacia dónde moverlo y qué tan sensible es la pérdida a ese movimiento. Si al subir un poquito un peso la pérdida sube, el gradiente dice que hay que bajarlo. Y si al subirlo la pérdida baja, que hay que subirlo.

Volviendo a la montaña con niebla: en una montaña con dos direcciones, norte-sur y este-oeste, la inclinación nos dice cuánto sube o baja el suelo en cada una, y avanzamos en la combinación que más baja. En nuestra red hay decenas de millones de direcciones, una por cada peso, y el gradiente da la inclinación en todas a la vez.

Nada garantiza que el valle al que llegamos sea el más profundo de toda la montaña. Podemos caer en un hueco intermedio. En la práctica, con redes grandes, esos huecos suelen ser suficientemente buenos, y por eso el método funciona.

Este procedimiento no es nuevo ni exclusivo de la inteligencia artificial. Es una técnica clásica de optimización, que se usa en ingeniería y en estadística para encontrar los valores que minimizan una cantidad. Lo que cambió es la escala: ahora se aplica a modelos con decenas de millones de parámetros y con cantidades enormes de datos.

[Diapositiva · Tasa de aprendizaje e hiperparámetros]

> Idea central: La tasa de aprendizaje es el tamaño del paso. Las decisiones que se toman antes de entrenar, como esta, se llaman hiperparámetros y se eligen probando.

Hablemos del tamaño del paso, que se llama tasa de aprendizaje y que es de las decisiones más delicadas del entrenamiento.

Si el paso es demasiado grande, pasa lo que le pasaría a alguien que quiere bajar a un valle dando zancadas enormes: pasa por encima del fondo y llega al otro lado, más arriba de donde estaba. Después vuelve a pasarse. La pérdida, en vez de bajar, sube o rebota sin parar, y el entrenamiento nunca se estabiliza.

Si el paso es demasiado pequeño, la red sí baja, pero tan despacio que el entrenamiento tardaría una eternidad, o se agota el tiempo antes de llegar a un buen lugar. Con una máquina que se paga por tiempo de uso, eso también cuesta dinero.

El paso ideal está entre los dos, y no hay una fórmula que lo dé de antemano. Se prueba. Se entrena un poco con un valor, se ve cómo baja la pérdida y se ajusta. Es común empezar con pasos más grandes al principio y reducirlos conforme la red se acerca al fondo.

La tasa de aprendizaje es un ejemplo de lo que se llama hiperparámetro. Un hiperparámetro es una decisión que se toma antes de entrenar y que no la aprende la red. La diferencia con un peso es esta: los pesos los ajusta el entrenamiento, mientras que los hiperparámetros los elige la persona. Otros ejemplos son cuántas veces se recorren los datos, cuántos ejemplos se usan en cada ajuste o cuántas capas tiene la red.

[Diapositiva · Retropropagación: repartir el error]

> Idea central: La retropropagación calcula cuánto contribuyó cada peso al error, yendo hacia atrás desde la salida, capa por capa. Se parece a revisar los tiros fallados de Batalla naval.

Bueno, también hay que preguntarse cómo se calcula la pendiente con decenas de millones de pesos. Existe una técnica, la retropropagación, que aprovecha que la red es una cadena de operaciones simples para calcular de forma eficiente cuánto contribuyó cada peso al error. Va hacia atrás: parte del error en la salida y retrocede capa por capa.

Una forma de verlo es con el juego de Batalla naval. Al principio la red señala casi al azar, como cuando uno dispara a ciegas. Conforme se avanza por las capas, el peso del error va aumentando, como las piezas blancas que marcan los tiros que no dieron en el blanco. La retropropagación es ir desde el fondo, desde donde el error es más grande, hacia atrás, para ver cuál fue el origen, que era la aleatoriedad del principio.

Veamos la idea con una analogía más cercana. Imaginen una cadena de montaje con varias estaciones, y al final sale un producto defectuoso. Nadie sabe en cuál estación se cometió el error. Una persona revisa el producto y, caminando hacia atrás, va preguntando: ¿esta estación lo hizo bien? ¿La anterior? Así identifica cuánto contribuyó cada una al defecto, y le pide a cada una que corrija lo suyo, un poco, en la dirección correcta.

Con la red pasa lo mismo: el error aparece al final, en la salida, y desde ahí se calcula cuánto se debe a cada neurona de la última capa, luego a las de la capa anterior, y así hasta la entrada. Con eso se sabe, para cada peso, en qué dirección moverlo.

Sin esta técnica, entrenar redes tan grandes sería prácticamente imposible. Con ella, una sola pasada hacia atrás da el gradiente de todos los pesos a la vez.

Un ciclo completo de entrenamiento es: la imagen entra, la red predice con los pesos actuales, se calcula la pérdida, la retropropagación reparte el error hacia atrás, el descenso del gradiente mueve un poco cada peso, y se pasa a la siguiente imagen. Eso, muchas veces, es lo que llamamos entrenar.

Así, ensayo tras ensayo, los pesos van tomando valores útiles, y una red que empezó respondiendo al azar termina marcando los espermatozoides.

[Diapositiva · Lotes, iteraciones y épocas]

> Idea central: En cada ajuste se usa un lote de imágenes. Una iteración es un ajuste; una época es una pasada completa por todos los ejemplos. Se hacen muchas épocas.

Hay tres palabras que aparecen todo el tiempo cuando se habla de entrenar una red, y que conviene distinguir: lote, iteración y época.

Imaginemos que tenemos cien imágenes de entrenamiento. En teoría, podríamos calcular el error de las cien y hacer un solo ajuste de los pesos. Pero eso es lento y gasta mucha memoria. En la práctica se reparte el conjunto en grupos pequeños. Cada grupo es un lote. Por ejemplo, si cada lote tiene cuatro imágenes, las cien imágenes se reparten en veinticinco lotes.

Un ajuste de los pesos, hecho con un lote, es una iteración. Entonces, para pasar por las cien imágenes con lotes de cuatro, se hacen veinticinco iteraciones.

Y una pasada completa por todas las imágenes, en este caso las veinticinco iteraciones, es una época. Una época no suele bastar. La red necesita ver los mismos ejemplos muchas veces para ajustar sus pesos con cuidado, así que el entrenamiento se repite por varias épocas, y en cada una la pérdida baja un poco más.

Una forma de recordarlo es con el estudio para un examen. El lote es el montón de ejercicios que resuelves antes de revisar tus errores. La iteración es cada vez que revisas y corriges. Y la época es cada vez que terminas todos los ejercicios del libro. Se aprende repasando muchas veces.

Ojo con las épocas: si son demasiadas, la red puede aprenderse de memoria los ejemplos, con todo y sus defectos, y luego funcionar mal con imágenes nuevas. Por eso, durante el entrenamiento, se separan algunas imágenes que la red nunca usa para ajustarse, y se miden con ellas los resultados. Cuándo parar y cómo comprobar que la red de verdad generaliza lo veremos en el último módulo.

[Diapositiva · Semillas y repetibilidad]

> Idea central: Como el entrenamiento usa azar, para poder repetirlo se fija una semilla y se documentan las decisiones. Así otra persona puede obtener el mismo modelo.

El azar en el entrenamiento tiene una consecuencia práctica: la repetibilidad.

En un entrenamiento hay varias cosas que dependen del azar. Los pesos iniciales se eligen al azar. El orden en que se presentan las imágenes se baraja en cada época. Y algunas técnicas que se usan para que la red generalice mejor también incluyen azar, como alterar ligeramente las imágenes en cada pasada.

Las computadoras no generan azar de verdad. Generan secuencias de números que lo parecen, a partir de un valor inicial que se llama semilla. Con la misma semilla, la secuencia es siempre la misma. Y eso es útil: si fijamos la semilla, el entrenamiento se vuelve repetible. Con los mismos datos, las mismas decisiones y la misma semilla, otra persona obtiene el mismo resultado.

Esto importa en ciencia. Un resultado que no se puede repetir es difícil de defender. Si alguien afirma que un modelo funciona de cierta manera, otra persona debería poder reproducir el entrenamiento y comprobarlo.

En la práctica, repetir exactamente puede ser más delicado de lo que parece, porque ciertas operaciones en las tarjetas gráficas no son estrictamente deterministas. Aun así, lo que se busca es que los resultados sean comparables y que todo lo demás, los datos, las decisiones y el código, esté documentado.

Por eso, cuando el entrenamiento está en un cuaderno compartido, el cuaderno guarda esas decisiones: los hiperparámetros, la separación de las imágenes, la semilla. Quien lo abre sabe qué se hizo y puede hacerlo otra vez. Es una idea que va a volver en todo el curso: que todo se pueda repetir.

Un entrenamiento repetible no es por eso un entrenamiento correcto: se puede repetir uno malo tantas veces como se quiera. La repetibilidad es la condición para poder revisarlo, y no garantiza que esté bien.

[Diapositiva · Un entrenamiento de ejemplo: la pérdida bajando]

> Idea central: Durante el entrenamiento, la pérdida empieza alta, baja rápido al principio y se estabiliza. Esa curva es la forma de saber si el entrenamiento va bien.

Veamos cómo se ve un entrenamiento desde fuera. Los números que voy a dar son ilustrativos: sirven para entender la forma, y no son los de nuestro modelo.

Imaginemos que, antes de entrenar, la pérdida vale dos. La red responde casi al azar, y por eso el error es grande. Después de la primera época, la pérdida baja a uno punto dos. Después de la segunda, a cero punto ocho. De la tercera, a cero punto seis. De la cuarta, a cero punto cinco. De la quinta, a cero punto cuarenta y cinco.

Al principio, la pérdida baja muchísimo en cada época: de dos a uno punto dos, casi un punto. Después baja cada vez menos: de cero punto cinco a cero punto cuarenta y cinco son solo cinco centésimas. La curva es muy inclinada al principio y se va aplanando.

Esa forma es la esperada, y se entiende bien. Al principio la red está lejos de una buena respuesta, y cualquier ajuste mejora mucho. Cuando ya está cerca, cada ajuste aporta poco. Cuando la curva se aplana, significa que la red ya aprendió casi todo lo que podía aprender de esos datos y con esas decisiones, y no tiene sentido seguir.

Esa gráfica sirve también para detectar problemas. Si la pérdida no baja, hay algo mal: quizá la tasa de aprendizaje es demasiado grande, o los datos tienen un problema. Si baja y luego sube, probablemente el paso fue excesivo. Si baja mucho en los datos de entrenamiento, pero no en las imágenes que la red nunca vio, es señal de que está aprendiendo los ejemplos de memoria.

Quien entrena una red pasa mucho tiempo mirando esta curva. Es como el termómetro del entrenamiento: no dice todo, pero avisa si algo va mal.

[Diapositiva · Repaso: lo que hace una red]

> Idea central: Una red neuronal es una cadena de capas con pesos ajustables, que se ajustan con ejemplos mediante pérdida, gradiente y retropropagación. No hay comprensión: hay números ajustados.

Hagamos un repaso de lo que vimos en esta parte, para que se quede la imagen completa.

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

El cuarto es que el modelo refleja los datos con los que se entrenó. Si había pocos ejemplos de cierta situación, la red la maneja peor. Mejorarlo requiere más ejemplos, más variados y mejor anotados, y un nuevo entrenamiento aparte.

Y el quinto es que un buen resultado en unas imágenes no garantiza uno bueno en todas. Hay que verificar con imágenes propias.

Nada de esto le quita valor al sistema. Un instrumento de laboratorio también tiene su rango de uso, y saber cuál es parte de saber usarlo. Lo que hace diferente a este es que muestra su trabajo: cada resultado trae la imagen marcada, para que cualquiera pueda comprobar si los contornos tienen sentido.

[Diapositiva · Preguntas que suelen surgir]

> Idea central: Respuestas breves a las dudas más comunes: la red no piensa, no necesita millones de imágenes si parte de una ya entrenada, puede equivocarse y se revisa.

Antes de cerrar, aprovecho para contestar algunas dudas que suelen aparecer cuando se explica esto por primera vez.

Una duda frecuente es si la red piensa. No. Calcula. Lo que parece comprensión es una consecuencia de un ajuste muy bien hecho. Es una distinción importante, porque nos recuerda que una red puede equivocarse con total aplomo.

Otra es cuántas imágenes hacen falta. Depende. Entrenando desde cero, muchísimas, decenas de miles o más. Pero cuando cada imagen tiene cientos de células, cada una aporta un ejemplo, y las cantidades necesarias son mucho menores. En el siguiente módulo veremos otra forma de ahorrar ejemplos.

Otra es si la red puede equivocarse. Sí, de las dos maneras que acabamos de ver, y esos errores los revisamos con calma en el siguiente módulo.

Otra es por qué se necesita una tarjeta gráfica para entrenar. Porque entrenar es hacer una cantidad enorme de multiplicaciones y sumas parecidas entre sí, y las tarjetas gráficas están diseñadas para hacer muchas operaciones de ese tipo en paralelo. Un procesador común hace pocas cosas muy rápido. Una tarjeta gráfica hace muchísimas cosas sencillas a la vez.

Y otra, la más honesta, es si el resultado es siempre correcto. No, y nadie debería prometerlo. Es una herramienta de medición, con sus márgenes de error, como cualquier instrumento. Lo que sí podemos prometer es que es consistente y que se puede revisar.

[Diapositiva · Glosario de repaso]

> Idea central: Un repaso rápido de las palabras de este módulo, una por una, para que queden a la mano.

Para terminar esta parte, un glosario rápido, con todas las palabras de este módulo, en una frase cada una. Pueden usarlo como repaso.

Píxel: cada cuadrito de una imagen digital, con un número, o tres si es a color. Canal: cada una de las tablas de números de una imagen a color, la roja, la verde y la azul. Resolución: cuántos píxeles tiene una imagen. Histograma: una gráfica que cuenta cuántos píxeles hay de cada brillo.

Micra: la milésima parte de un milímetro. Escala: la relación entre píxeles y micras; en nuestro sistema es sesenta píxeles por micra, para todas las imágenes.

Inteligencia artificial: el campo amplio. Aprendizaje automático: lo que aprende de ejemplos. Red neuronal: una estructura de operaciones sencillas con pesos ajustables. Aprendizaje profundo: redes con muchas capas.

Neurona: multiplica entradas por pesos, suma, agrega un sesgo y aplica una activación. Capa: un conjunto de neuronas con las mismas entradas. Peso: un número ajustable; los pesos son lo que la red sabe. Sesgo: un número que decide qué tan exigente es una neurona. Activación: la regla que rompe la linealidad.

Pérdida: un número que mide qué tan lejos estuvo la red. Gradiente: la dirección en que hay que mover cada peso. Descenso del gradiente: bajar la pérdida paso a paso. Tasa de aprendizaje: el tamaño del paso. Hiperparámetro: una decisión que toma la persona antes de entrenar. Retropropagación: repartir el error hacia atrás. Lote, iteración y época: grupos de imágenes, un ajuste y una pasada completa.

Anotación: dibujar a mano las respuestas correctas. Aprendizaje supervisado: aprender con ejemplos que traen su respuesta. Semilla: el valor inicial del azar, que se fija para poder repetir un entrenamiento. Modelo: el archivo con los pesos. Entrenamiento: ajustar los pesos con ejemplos. Inferencia: usar el modelo ya entrenado.

Colab: el entorno para entrenar. Python: el lenguaje. Flask: la herramienta para el sitio. Servidor: la computadora donde vive el sitio.

[Diapositiva · Lo que vimos hoy]

> Idea central: El problema era contar y medir a mano; vimos qué es una imagen digital, algunas definiciones y las bases de las redes neuronales: neurona, capas y cómo aprenden.

Para cerrar, un resumen de lo que vimos. El problema de partida era el conteo y la medición manuales, que tardan mucho y dependen de quién los haga. Vimos qué es una imagen digital: una cuadrícula de números, con sus formatos y su escala. Pusimos en orden algunas definiciones y las palabras que vamos a usar. Y vimos las bases de las redes neuronales: la neurona, la capa y la red, y cómo aprende una red ajustando sus pesos a partir de ejemplos.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Idea central: En este módulo vimos qué es una red neuronal y cómo aprende. En el siguiente módulo vemos cómo mira una imagen una red convolucional y cómo se aprovecha una red entrenada para otra cosa; después, el sitio funcionando, y al final, datos, entrenamiento y despliegue.

Y una última idea para llevarse. Si les quedó la impresión de que una red neuronal es una máquina de multiplicar y sumar, tienen razón. Lo que la hace poderosa es la cantidad de operaciones simples y el cuidado con el que se ajustan. Con eso en mente, se entiende por qué el sistema funciona y también por qué conviene revisarlo.

Y termino con una pregunta que seguramente ya se hicieron: ¿cómo sabe el sistema dónde hay un espermatozoide? De eso trata el siguiente módulo: cómo mira una imagen una red como la nuestra, y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides.

Luego viene el sistema funcionando, con el sitio, y por último los datos, el entrenamiento y el despliegue en la nube. Muchas gracias por su atención.
