# Guion del módulo 1, video 2 de 3: Inteligencia artificial, entrenamiento y la neurona (versión natural)

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

[Diapositiva 1 · La inteligencia artificial a nuestro alrededor]

> Idea central: Sin darnos cuenta, usamos inteligencia artificial todos los días: al escribir, al buscar, al ver recomendaciones. Casi todo se basa en aprender de ejemplos.

En el video anterior vimos qué es una imagen digital: una tabla de números, con sus formatos y su escala. Ahora vamos con la inteligencia artificial. Pero antes de ponernos con las definiciones, miremos dónde ya vive. Seguramente ustedes usan todos los días, sin pensarlo, varias herramientas que funcionan con aprendizaje automático.

Escriben un mensaje en el teléfono y les sugiere la siguiente palabra. ¿Qué está pasando ahí? Un modelo aprendió, de millones de textos, qué palabras suelen seguir a cuáles. El correo manda un mensaje a la carpeta de no deseados: otro modelo se formó con muchísimos correos que otras personas marcaron como basura, y así reconoce los rasgos de ese tipo de mensaje. Y la plataforma de video propone qué ver después porque se apoya en lo que miraron personas parecidas a ustedes.

¿Qué tienen en común todos? En ningún caso alguien escribió una lista de reglas para reconocer una cara, una frase o un mensaje basura. Habría sido imposible, por la cantidad de casos y de excepciones. Lo que se hizo fue reunir muchos ejemplos y dejar que el sistema encontrara por sí mismo qué los distingue.

Esa es la idea que sostiene el resto de lo que vamos a ver. También nos recuerda que estas herramientas no son mágicas ni inteligentes en el sentido humano. Son muy buenas para lo que vieron en sus ejemplos, y se equivocan de maneras que a veces sorprenden. En este curso vemos cómo funciona esa idea con un caso que nos queda muy cerca: contar y medir células.

[Diapositiva 2 · La inteligencia artificial con imágenes de células]

> Idea central: En biología, la inteligencia artificial ayuda a contar, medir y localizar estructuras en imágenes de microscopio. Su valor está en la rapidez y en la consistencia.

Bueno, pasemos de la vida diaria a las ciencias de la vida, que es donde nos interesa. ¿Para qué se usa la inteligencia artificial con imágenes de microscopio?

Segundo: localizar. Saber dónde está cada estructura dentro de la imagen permite medirla, seguirla en el tiempo si se toman varias imágenes, o estudiar cómo se distribuyen unas respecto de otras. Esta es la tarea que nos ocupa: encontrar cada cabeza de espermatozoide.

En todos los casos pasa lo mismo: la inteligencia artificial no sustituye el criterio de quien investiga. Hace de forma rápida y consistente la parte repetitiva del trabajo, y le deja a la persona lo que requiere conocimiento: decidir qué preguntas hacer, interpretar los resultados y detectar cuándo algo no tiene sentido.

Un resultado producido por un modelo es una medición, con sus márgenes de error, y no una verdad. Por eso, en un buen sistema, el resultado siempre se puede revisar. Esa idea nos va a acompañar en todos los módulos.

[Diapositiva 3 · Algunas definiciones de inteligencia artificial]

> Idea central: Inteligencia artificial, aprendizaje automático, redes neuronales y aprendizaje profundo son capas de un mismo campo, de lo más amplio a lo más específico.

Antes de entrar con las redes neuronales, conviene poner en orden algunas palabras, porque se mezclan muy seguido.

La inteligencia artificial es el campo más amplio: cualquier técnica que haga que una máquina realice tareas que se asocian con la inteligencia. El aprendizaje automático es la parte que aprende de ejemplos. Las redes neuronales son una técnica dentro del aprendizaje automático. Y el aprendizaje profundo se refiere a redes con muchas capas, que les explico en un momento.

La idea de fondo del aprendizaje automático cabe en una frase: el sistema encuentra las reglas a partir de ejemplos, en vez de que alguien las escriba. En la programación tradicional se entregan reglas y datos y salen las respuestas. En el aprendizaje automático se entregan datos y respuestas y salen las reglas. El flujo se invierte, y de eso depende todo lo que sigue.

Para que no se mezclen, conviene verlas como círculos que se contienen unos a otros. El más grande es la inteligencia artificial. Dentro está el aprendizaje automático. Dentro de este, las redes neuronales. Y dentro de las redes neuronales, el aprendizaje profundo, que son las que tienen muchas capas.

Algo que sale de ahí: no toda la inteligencia artificial aprende de ejemplos. Un programa que sigue reglas escritas por una persona, como un sistema que recomienda qué hacer si la temperatura sube de cierto valor, también es inteligencia artificial en el sentido amplio. Lo que distingue al aprendizaje automático es que las reglas se obtienen de los datos, en lugar de escribirlas una persona.

Y otra cosa: cuando se habla de inteligencia artificial en los medios, casi siempre se está hablando de aprendizaje profundo, que es la rama que más ha avanzado en los últimos años con imágenes, sonido y texto. Es la que usamos aquí.

[Diapositiva 4 · Palabras que vamos a escuchar]

> Idea central: Seis palabras para los cuatro módulos: red neuronal, Google Colab, Python, Flask, modelo y servidor. Entrenamiento e inferencia se explican en el siguiente video.

Les dejo en pantalla unas palabras que van a escuchar durante los cuatro módulos. No las voy a leer todas, solo las que salen hoy.

Una red neuronal es un programa que aprende de ejemplos. Google Colab es un entorno para programar en la nube. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python: el sitio está hecho con las dos. El modelo es el archivo que guarda lo que la red aprendió. Y el servidor es la computadora donde el sitio está en línea, la que responde cuando alguien entra. También aparecen dos palabras que explico un poco más adelante, entrenamiento e inferencia, porque son las que más confunden y las que más importa distinguir.

[Diapositiva 5 · Red neuronal]

> Idea central: Una red neuronal es un programa formado por muchas operaciones pequeñas conectadas, cuyos valores se ajustan a partir de ejemplos en lugar de escribirse a mano.

Empecemos por la palabra que más vamos a usar: red neuronal. Dicho de forma sencilla, es un programa que se va afinando con ejemplos.

Un programa tradicional es una lista de instrucciones: si pasa esto, haz aquello. Una red neuronal, en cambio, es una estructura de muchísimas operaciones muy pequeñas, conectadas entre sí, y cada operación tiene unos números que se pueden ajustar. Esos números se llaman pesos. Al principio los pesos valen cualquier cosa, y la red no sirve para nada. Después, con ejemplos, los pesos se van ajustando hasta que la red da buenas respuestas.

Por eso decimos que la red aprende. No aprende como una persona, no comprende lo que hace. Lo que ocurre es que, ejemplo tras ejemplo, sus pesos se acercan a valores que producen la respuesta correcta.

El nombre viene de una inspiración. Las neuronas del cerebro reciben señales y, según el total, se activan o no. Las neuronas artificiales hacen algo parecido, pero mucho más simple. Hay que tomar esa comparación con cautela: una red neuronal artificial no es un cerebro, y el parecido es más de forma que de funcionamiento.

Una cosa más. Hay redes de muchos tamaños. Algunas tienen unas decenas de pesos y se pueden estudiar a mano. Las que se usan con imágenes tienen millones, y la que usamos nosotros tiene decenas de millones. Pero el principio es siempre el mismo: operaciones pequeñas, con pesos ajustables, que se ajustan con ejemplos.

Más adelante en este video vamos a construir una desde cero, empezando por su pieza más pequeña, para que se vea que no hay nada misterioso.

[Diapositiva 6 · Modelo]

> Idea central: El modelo es el archivo que guarda lo que la red aprendió: sus pesos. Por sí solo no hace nada, hace falta un programa que lo cargue y lo use.

La quinta palabra es modelo. Cuando una red termina de entrenarse, lo que se obtiene es un archivo. Ese archivo es el modelo.

¿Qué hay dentro? Básicamente, la estructura de la red y el valor de todos sus pesos. Los pesos son los números que se ajustaron durante el entrenamiento, y son lo que la red sabe. Si la red fuera una receta, el modelo sería la receta escrita, con todas las cantidades ya afinadas.

Un modelo por sí solo no hace nada. Es como un libro cerrado: tiene todo adentro, pero nadie lo puede leer. Hace falta un programa que lo abra, lo cargue en la memoria y le dé una imagen para que responda. Eso es lo que hace el sitio, y eso se llama inferencia.

Otra característica: un modelo está fijo. Una vez entrenado, sus pesos no cambian mientras se usa. Si le damos mil imágenes para que las analice, seguirá siendo exactamente el mismo modelo, con exactamente los mismos pesos. No aprende de lo que analiza. Para que cambie hay que entrenarlo otra vez, aparte, y el resultado es un modelo nuevo, un archivo distinto.

[Diapositiva 7 · Entrenamiento aparte, inferencia en el servidor]

> Idea central: Entrenar es aprender la receta y se hace aparte, en Colab; la inferencia es cocinarla, y se hace en el servidor. Para mejorar el modelo no se toca el sitio, solo se cambia el archivo.

Ahora, dos palabras que conviene separar bien: entrenamiento e inferencia. El desarrollo de la red tiene dos etapas, y están separadas a propósito.

La primera etapa, el entrenamiento, se hace en Colab, con imágenes que las personas ya marcaron a mano. De ahí sale el archivo del modelo. La segunda, la inferencia, es usar ese modelo ya entrenado para analizar imágenes nuevas. Eso se hace en el servidor, con el procesador de la computadora donde está el sitio.

¿Qué consecuencia tiene? Una muy práctica. Para mejorar el modelo no se toca el sitio. Se entrena aparte, sale un archivo nuevo y se cambia ese archivo en el servidor. Son dos partes con cuidados distintos. La parte web se mantiene como cualquier sitio. La de aprendizaje automático se mejora con datos.

Piénsenlo como una receta. Entrenar es aprender la receta: lleva tiempo, esfuerzo, muchos intentos y correcciones, y se hace una vez, o cada vez que se quiere mejorar. La inferencia es cocinarla las veces que haga falta. Eso es mucho más rápido, y se repite todos los días.

Una pregunta que suele salir: ¿el modelo sigue aprendiendo mientras la gente lo usa? No. Durante la inferencia los pesos no cambian, y para mejorarlo hace falta entrenar otra versión con imágenes nuevas.

[Diapositiva 8 · Entrenamiento]

> Idea central: Entrenar es ajustar los pesos con ejemplos anotados. Necesita muchos cálculos, una máquina potente y se hace pocas veces.

Entrenar es ajustar los pesos de la red con ejemplos. Para hacerlo hacen falta tres ingredientes. Primero, los ejemplos: imágenes con su respuesta correcta, que en nuestro caso son los contornos de cada cabeza, dibujados por personas. Segundo, la red, con una estructura elegida y unos pesos iniciales. Y tercero, una forma de ajustar, que veremos más adelante con la pérdida, el gradiente y la retropropagación.

No se usan todas las imágenes para entrenar. Se separa una parte que la red no ve durante el entrenamiento, y que sirve después para comprobar si funciona con imágenes que no conoce. Es como la diferencia entre estudiar con los ejercicios del libro y presentar un examen con ejercicios nuevos.

[Diapositiva 9 · Inferencia]

> Idea central: Inferencia es usar el modelo ya entrenado para analizar una imagen nueva. Es una sola pasada, sin ajustar nada, y basta con el procesador de una computadora normal.

La segunda etapa es la inferencia. La palabra suena técnica, pero es sencilla: usar el modelo ya entrenado para obtener una respuesta con una imagen nueva.

En la inferencia no se ajusta nada. La imagen entra, atraviesa las capas hacia adelante y sale la respuesta. No hay pérdida, ni gradiente, ni retropropagación. Los pesos están fijos, tal como quedaron al terminar el entrenamiento.

Eso la hace mucho más liviana que el entrenamiento: una pasada hacia adelante cuesta una fracción de una pasada completa con ajuste, y por eso alcanza con el procesador del servidor.

Y no interviene el azar: ante la misma imagen, el mismo modelo responde siempre lo mismo. Para un instrumento de medición, eso es justo lo deseable.

[Diapositiva 10 · El primer intento: el umbral]

> Idea central: La primera idea para contar es usar el brillo: todo píxel por encima de cierto valor es célula. Sirve como primera aproximación, pero las reglas se multiplican y se enredan.

Partamos del problema. Supongamos que hay que escribir un programa que reciba una imagen y diga cuántos espermatozoides hay. ¿Cómo se haría con un programa tradicional, con reglas explícitas?

La primera idea es usar el brillo. Los espermatozoides son brillantes sobre fondo oscuro. Entonces se podría decir: todo píxel con un brillo mayor a cierto valor pertenece a una célula. Luego se agrupan los píxeles vecinos en manchas, y cada mancha es una célula. Esa técnica se llama umbralización, y el sitio la incluye como respaldo.

Como primera aproximación sirve. Pero los problemas aparecen pronto. Las colas también brillan, y no se quieren contar. Hay manchas rojas difusas, más grandes y fuera de foco, que pasan el umbral sin ser espermatozoides. Hay células encimadas entre sí, o sobre las colas de otras, y el umbral las une en una sola mancha. Además, el brillo de una imagen depende de la iluminación, de la exposición y de la tinción. Un umbral que funciona en una imagen puede fallar en la siguiente.

Veamos con números por qué un umbral, que parece tan razonable, tiene tantos problemas. Tomemos una fila de diez píxeles, con estos brillos: ocho, ocho, sesenta, ciento cuarenta, doscientos treinta, doscientos treinta, ciento cuarenta, sesenta, ocho, ocho. Es la forma típica de una célula: sube, llega a un máximo y baja.

Si ponemos el umbral en cien, los píxeles que lo superan son cuatro: los de ciento cuarenta y los dos de doscientos treinta. La célula mide, en esa fila, cuatro píxeles. Pero si bajamos el umbral a cincuenta, los de sesenta también pasan, y la célula mide seis píxeles. Con un cambio de cincuenta puntos en el umbral, el tamaño de la célula cambió en la mitad. Y no hay una respuesta correcta, porque los dos valores parecen razonables.

Ese es el primer problema, y es serio, porque lo que queremos es medir. Un método cuyo resultado depende de un número que alguien eligió sin una razón clara no es un buen instrumento de medición.

Mirado en conjunto, el umbral deja claro el límite de las reglas escritas a mano: cada regla nueva trae sus excepciones, y cuando se multiplican, mantener el programa deja de ser práctico. Hace falta plantear el problema de otra forma, y ahí entra el aprendizaje automático: se le muestran ejemplos al sistema y se deja que él encuentre las reglas. Con imágenes, la técnica que mejor funciona es la red neuronal.

[Diapositiva 11 · Una red neuronal no entiende]

> Idea central: Una red neuronal no entiende qué es un espermatozoide. Es un reconocedor de patrones muy sofisticado, y eso sirve para razonar cuándo va a funcionar y cuándo no.

Antes de construir la red, hay una idea previa que cambia cómo se va a escuchar el resto. Una red neuronal no entiende qué es un espermatozoide. No tiene el concepto, no sabe de biología, no sabe qué es una célula ni para qué sirve contarla. Tiene una enorme colección de números ajustados, y ante ciertos patrones de píxeles produce una salida que coincide con lo que las personas marcaron en los ejemplos. Es un reconocedor de patrones muy sofisticado, y nada más.

Eso no le quita mérito. Sirve para razonar sobre cuándo va a funcionar y cuándo no. Si le muestro una imagen parecida a las de su entrenamiento, va a funcionar. Si le muestro algo muy distinto, no tiene cómo saber que se equivoca, y va a producir una salida con la misma seguridad aparente.

Un buen ejemplo es lo que pasa cuando se le muestra algo que nunca vio. Si le damos la imagen de otro tipo de tejido, no responde «esto no es lo que sé hacer». Responde con la misma seguridad, porque no tiene forma de medir su propia ignorancia. Para ella todo es una entrada, y debe dar una salida.

Entonces, la confianza que podemos tener en una red depende de cuánto se parecen las imágenes nuevas a las imágenes con las que se entrenó. Si se parecen, la respuesta suele ser buena. Si no, no hay garantía. Por eso conviene mirar siempre la imagen marcada antes de confiar en un número.

Pensarlo así nos quita el misterio: una red neuronal es una máquina de reconocer patrones, muy buena, que hay que usar con criterio.

[Diapositiva 12 · Del umbral a la red: qué cambia]

> Idea central: El umbral usa una regla fija sobre un píxel. La red usa millones de reglas ajustadas con ejemplos, que miran vecindarios. Cambia quién escribe las reglas.

El umbral es una sola regla, escrita por una persona: un píxel con brillo mayor a tal valor es célula. Mira cada píxel por separado, sin importar sus vecinos. No distingue forma, ni tamaño, ni textura. Y su resultado depende de un número elegido a mano.

La red neuronal es una enorme colección de reglas, millones de pesos, que no escribió nadie: se obtuvieron ajustándolos con ejemplos. Combina muchos píxeles a la vez, no uno por uno. Puede distinguir una cabeza de una cola por su forma, y una cabeza de una mancha por su textura y sus bordes. Y no depende de un solo número elegido a mano, porque lo que se ajustó fueron todos sus pesos, para que coincidan con lo que las personas marcaron.

El cambio de fondo es de método: en lugar de decirle a la computadora cómo hacer algo, le mostramos qué queremos y dejamos que descubra cómo.

[Diapositiva 13 · La neurona artificial]

> Idea central: Una neurona artificial es una operación muy pequeña en cuatro pasos: recibe números, los multiplica por pesos, los suma y decide si se activa.

Ahora sí vamos a construir la red desde su pieza más pequeña: la neurona artificial. Es la pieza elemental. El nombre es más una inspiración histórica que una descripción fiel de la biología, y lo que hace es una operación muy pequeña que se describe en cuatro pasos.

Uno: recibe una lista de números, que son las entradas. Dos: cada entrada se multiplica por otro número, que es su peso. Tres: se suman los resultados. Cuatro: a esa suma se le aplica una pequeña función que decide cuándo se activa la neurona.

Un ejemplo para ver qué hace un peso. Imaginen una neurona que decide si un punto de la imagen es rojo e intenso. Recibe tres entradas: la cantidad de rojo, de verde y de azul de un píxel. Para que dé una salida alta con un píxel muy rojo, se le asigna un peso grande y positivo a la entrada del rojo, y pesos pequeños o negativos a las otras dos. Un píxel muy rojo produce una suma muy grande, y uno azul, una suma muy pequeña.

Los pesos expresan qué le importa a la neurona. Un peso grande dice «esto me va a importar mucho». Uno cercano a cero dice «me da igual». Uno negativo dice «esto me hace dudar». Falta un elemento: un número que se suma al final, que se llama sesgo. Desplaza el punto desde el cual la neurona empieza a activarse. Pueden imaginarlo como un interruptor sensible: los pesos deciden a qué se fija, y el sesgo decide qué tan exigente es antes de encenderse.

El último paso es la función de activación, que es lo que hace posible que las redes sean tan potentes. Por ahora basta saber que es una regla sencilla: si la suma es negativa, la salida es cero, y si es positiva, pasa tal cual.

Retomemos la neurona que busca píxeles rojos intensos. Para simplificar, expresamos cada canal entre cero y uno, dividiendo entre doscientos cincuenta y cinco. Le asignamos tres pesos: dos para el rojo, menos uno para el verde y menos uno para el azul. Y un sesgo de menos cero punto tres.

Probemos con un píxel naranja intenso, el de doscientos cuarenta, ciento veintidós y cuarenta y dos. En escala de cero a uno, son más o menos cero punto noventa y cuatro, cero punto cuarenta y ocho y cero punto diecisiete. Multiplicamos cada entrada por su peso: cero punto noventa y cuatro por dos da uno punto ochenta y ocho; menos cero punto cuarenta y ocho; y menos cero punto diecisiete. Sumamos: uno punto ochenta y ocho, menos cero punto cuarenta y ocho, menos cero punto diecisiete, da uno punto veintitrés. Le restamos el sesgo, cero punto tres, y queda cerca de cero punto noventa y cuatro. La neurona responde con un número alto.

Sin que nadie le dijera la palabra rojo, esta neurona distingue un píxel rojo de uno azul, solo por cómo están puestos sus pesos. El sesgo también cuenta: si fuera menos uno en lugar de menos cero punto tres, el píxel naranja daría solo cerca de cero punto veinticuatro, una respuesta mucho más tímida.

Esto es todo lo que hace una neurona: multiplicar, sumar y comparar. La potencia de una red viene de que hay millones de ellas, bien ajustadas.

[Diapositiva 14 · El sesgo, con un ejemplo]

> Idea central: El sesgo mueve el punto de activación. Con el mismo píxel y los mismos pesos, un sesgo más exigente apaga la neurona y uno más permisivo la deja encendida.

Pensemos en una neurona sencilla que mira solo el brillo de un píxel, expresado entre cero y uno, y tiene un peso de uno. Sin sesgo, su cuenta es multiplicar el brillo por uno y aplicar la activación. Un píxel con brillo cero punto dos produce cero punto dos. Uno con brillo cero punto cinco produce cero punto cinco. Uno con brillo cero punto nueve produce cero punto nueve. La neurona responde en proporción al brillo, desde el más tenue.

Ahora agreguemos un sesgo de menos cero punto seis. La cuenta es brillo por uno, menos cero punto seis. El píxel de cero punto dos da menos cero punto cuatro, y la activación lo convierte en cero. El de cero punto cinco da menos cero punto uno, y también queda en cero. Solo el de cero punto nueve da cero punto tres. Con ese sesgo, la neurona se queda callada ante todo lo que sea tenue o medio, y solo responde ante lo muy brillante.

No cambiamos el peso, y sin embargo la neurona se comporta de otra manera. El sesgo funciona como una barrera: el estímulo tiene que superarla para que la neurona se encienda. Un sesgo muy negativo hace a la neurona muy exigente. Uno cercano a cero la hace permisiva.

Esta idea se parece al umbral que vimos antes. Un sesgo negativo, con una activación que apaga todo lo que no lo supera, es en cierto modo un umbral. La diferencia es que aquí el umbral no lo elige una persona a ojo: lo encuentra el entrenamiento, y es distinto para cada neurona.

[Diapositiva 15 · La función de activación]

> Idea central: La activación introduce una torcedura en la suma: si el total es negativo la salida es cero, y si es positivo se deja pasar. Sin ella, apilar capas no serviría de nada.

Dediquemos unos minutos más a la función de activación, porque es el paso que más fácil se pasa por alto.

Recordemos lo que hace la neurona hasta antes de este paso. Multiplica las entradas por los pesos y suma. Eso es una operación lineal. ¿Qué quiere decir lineal? Que si duplico la entrada, se duplica la salida, y si sumo dos entradas, la salida es la suma de las salidas. Es una operación muy limitada.

Y aquí viene lo curioso. Si se encadenan varias operaciones lineales, el resultado sigue siendo una sola operación lineal. Pueden apilar diez capas, o cien, o mil, y si solo multiplican y suman, todo eso equivale a una única capa. La profundidad no aporta nada.

Entra la función de activación. Después de multiplicar y sumar, se aplica una pequeña regla que rompe la linealidad. La que más se usa hoy es muy sencilla: si el resultado es negativo, la salida es cero. Si es positivo, la salida es ese mismo número. Se le llama la rectificadora, porque rectifica los negativos.

En una gráfica es una línea plana en cero hasta el origen, y luego una línea que sube en diagonal. Esa pequeña esquina es lo que hace posible que las redes sean tan potentes. Con ella, cada neurona tiene un comportamiento de encendido y apagado: no responde nada hasta que el estímulo supera cierto nivel, y a partir de ahí responde de forma proporcional.

Al combinar muchas de estas esquinas en capas, la red puede dibujar relaciones tan complicadas como queramos: curvas, bordes, formas. Es la diferencia entre trazar con una sola regla recta y trazar con miles de segmentos pequeños que, juntos, siguen cualquier contorno.

En conjunto: los pesos fijan a qué atiende cada neurona, el sesgo cuánta exigencia tiene, y la activación permite que la red represente algo más que simples proporciones. Con esas tres ideas queda completa la neurona.

En el siguiente video juntamos muchas neuronas en capas y vemos cómo aprende una red.
