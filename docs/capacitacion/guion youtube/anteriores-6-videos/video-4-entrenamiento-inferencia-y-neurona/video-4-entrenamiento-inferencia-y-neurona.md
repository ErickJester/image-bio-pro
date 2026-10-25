# Guion del video 4 de 6: Entrenamiento, inferencia y la neurona

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Continúa del video 3. Empieza con la frase que lo une con el video anterior.

*3,147 palabras, unos 18.0 min de habla*

[Diapositiva 1 · Entrenamiento aparte, inferencia en el servidor]

> Idea central: Entrenar es aprender la receta y se hace aparte, en Colab; la inferencia es cocinarla, y se hace en el servidor. Para mejorar el modelo no se toca el sitio, solo se cambia el archivo.

En el video anterior vimos las palabras clave de este curso. Hay dos que conviene separar bien, porque el desarrollo de la red tiene dos etapas, entrenamiento e inferencia, y están separadas a propósito.

La primera etapa es el entrenamiento. Se hace en Colab, con imágenes que las personas ya marcaron a mano, y de ahí sale el archivo del modelo. La segunda etapa es la inferencia, que es usar el modelo ya entrenado para analizar imágenes nuevas. Eso se hace en el servidor, en el procesador de la computadora donde está el sitio.

Esto tiene una consecuencia práctica. Para mejorar el modelo no se toca el sitio. Se entrena aparte, se obtiene un archivo nuevo y se cambia ese archivo en el servidor. Son dos partes con cuidados distintos: la parte web se mantiene como cualquier sitio, y la parte de aprendizaje automático se mejora con datos.

Una comparación que ayuda: el entrenamiento es como aprender una receta, y la inferencia es como cocinarla las veces que haga falta. Aprender la receta lleva tiempo y esfuerzo, con muchos intentos y correcciones, y se hace una vez, o cada vez que se quiere mejorar. Cocinar con la receta ya aprendida es mucho más rápido y se repite todos los días.

Las dos etapas están separadas porque son trabajos de naturaleza distinta, y cada una pide una máquina distinta.

El entrenamiento es un trabajo de mucho cálculo y poca frecuencia. Se hace una vez, o unas pocas veces. Necesita ver muchas veces los mismos ejemplos, y cada pasada ajusta millones de números. Para eso conviene una máquina potente, como las que ofrece Colab, con una tarjeta gráfica.

La inferencia es lo opuesto: poco cálculo, pero muchas veces. Cada vez que alguien sube una imagen, hay que hacer una pasada por la red, solo de ida, sin ajustar nada. Es mucho más barato, y se puede hacer en una máquina modesta.

Esa asimetría es lo que permite que el sistema funcione como funciona. El trabajo pesado se hace una vez, en el lugar adecuado, y el trabajo ligero se hace todos los días, en el servidor del sitio.

Una duda que conviene aclarar: ¿el modelo sigue aprendiendo mientras la gente lo usa? No. Durante la inferencia los pesos no cambian, y para mejorarlo hace falta entrenar otra versión con imágenes nuevas.

[Diapositiva 2 · Entrenamiento]

> Idea central: Entrenar es ajustar los pesos con ejemplos anotados. Necesita muchos cálculos, una máquina potente y se hace pocas veces.

Veamos cada etapa por separado, empezando por el entrenamiento.

Entrenar es el proceso de ajustar los pesos de la red con ejemplos. Para hacerlo se necesitan tres ingredientes. El primero son los ejemplos: imágenes con su respuesta correcta, que en nuestro caso son los contornos de cada cabeza dibujados por personas. El segundo es la red, con una estructura elegida y unos pesos iniciales. Y el tercero es una forma de ajustar, que es lo que veremos más adelante con la pérdida, el gradiente y la retropropagación.

No se usan todas las imágenes para entrenar. Se separa una parte que la red no ve durante el entrenamiento, y que sirve después para comprobar si funciona con imágenes que no conoce. Es la diferencia entre estudiar con los ejercicios del libro y presentar un examen con ejercicios nuevos.

Como es un trabajo pesado, se hace en un entorno aparte, que en nuestro caso es Google Colab, con máquinas que tienen tarjeta gráfica. Y como está en un cuaderno, queda documentado: qué datos se usaron, qué decisiones se tomaron y qué resultado se obtuvo.

El producto del entrenamiento es el archivo del modelo. Es lo único que sale de ahí y lo único que necesita el sitio.

[Diapositiva 3 · Inferencia]

> Idea central: Inferencia es usar el modelo ya entrenado para analizar una imagen nueva. Es una sola pasada, sin ajustar nada, y basta con el procesador de una computadora normal.

La segunda etapa es la inferencia. La palabra suena técnica, pero es sencilla: es usar el modelo ya entrenado para obtener una respuesta con una imagen nueva.

En la inferencia no se ajusta nada. La imagen entra, atraviesa las capas hacia adelante, y sale la respuesta. No hay pérdida, ni gradiente, ni retropropagación. Los pesos están fijos, tal como quedaron al terminar el entrenamiento.

Eso la hace mucho más liviana que el entrenamiento: una pasada hacia adelante cuesta una fracción de una pasada completa con ajuste, y por eso alcanza con el procesador del servidor.

También cambia la forma de pensar en el tiempo. En el entrenamiento, una hora más o menos no importa demasiado. En la inferencia, la persona está esperando con la página abierta, y cada segundo cuenta. Por eso se cuida que el modelo se cargue una sola vez, al iniciar el servidor, y que no haya que volver a leer el archivo con cada análisis.

Y no interviene el azar: ante la misma imagen, el mismo modelo responde siempre lo mismo. Para un instrumento de medición, eso es justo lo deseable.

[Diapositiva 4 · Fundamentos de redes neuronales]

> Idea central: Vamos de lo general a lo concreto: un problema, la idea que lo resuelve y al final el nombre técnico. Sin ecuaciones; cuando haya una, se dice con palabras qué hace.

Con esto ya podemos empezar con las redes neuronales. Voy de lo general a lo concreto: primero un problema que podemos imaginar, luego la idea que lo resuelve y al final el nombre técnico. No voy a usar ecuaciones. Cuando una idea tenga expresión matemática, les digo con palabras qué hace.

La meta de esta parte es que quede claro cómo responder tres preguntas: qué es una red neuronal, cómo aprende y por qué una red entrenada para otra cosa nos sirve para contar espermatozoides. Las dos primeras las vemos en este módulo. La tercera, en el siguiente módulo.

Vamos a hablar de números, pesos y capas, y esas palabras pueden sonar intimidantes, pero todo lo que vamos a ver se reduce a multiplicar, sumar y comparar. Si saben sumar y multiplicar, tienen todo lo necesario.

No voy a pedirles que memoricen nada: lo que me interesa es que al terminar esta parte puedan explicar, con sus propias palabras, qué hay dentro de una red neuronal. Con eso, el resto del curso se va a entender mucho mejor.

[Diapositiva 5 · El primer intento: el umbral]

> Idea central: La primera idea para contar es usar el brillo: todo píxel por encima de cierto valor es célula. Sirve como primera aproximación, pero las reglas se multiplican y se enredan.

Partamos del problema. Supongamos que hay que escribir un programa que reciba una imagen y diga cuántos espermatozoides hay. ¿Cómo se haría con un programa tradicional, escribiendo reglas explícitas?

La primera idea es usar el brillo. Los espermatozoides son brillantes sobre fondo oscuro, así que se podría decir que todo píxel con un brillo mayor a cierto valor pertenece a una célula. Luego se agrupan los píxeles vecinos en manchas, y cada mancha es una célula. Esa técnica se llama umbralización, y el sitio la incluye como respaldo.

Como primera aproximación sirve, pero los problemas aparecen pronto. Las colas también brillan y no se quieren contar. Hay manchas rojas difusas, más grandes y fuera de foco, que pasan el umbral sin ser espermatozoides. Hay células encimadas entre sí o sobre las colas de otras, y el umbral las une en una sola mancha. Además, el brillo de una imagen depende de la iluminación, de la exposición y de la tinción. Un umbral que funciona en una imagen puede fallar en la siguiente.

Se pueden seguir agregando reglas. Si la mancha es muy alargada, probablemente es una cola. Si es muy grande, probablemente es una mancha difusa. Si tiene forma de ocho, probablemente son dos células juntas y hay que partirla por el estrechamiento. Cada regla ayuda un poco y trae sus excepciones. La lista crece, se enreda, y cada extensión nueva obliga a modificar el programa, con el riesgo de romper lo que ya funcionaba.

Veamos con números por qué un umbral, que parece tan razonable, tiene tantos problemas. Tomemos una fila de diez píxeles, con estos valores de brillo: ocho, ocho, sesenta, ciento cuarenta, doscientos treinta, doscientos treinta, ciento cuarenta, sesenta, ocho, ocho. Es la forma típica de una célula: sube, llega a un máximo y baja.

Si ponemos el umbral en cien, los píxeles que lo superan son cuatro: los de ciento cuarenta y los dos de doscientos treinta. Entonces la célula mide, en esa fila, cuatro píxeles. Pero si bajamos el umbral a cincuenta, los de sesenta también pasan, y la célula mide seis píxeles. Con un cambio de cincuenta puntos en el umbral, el tamaño de la célula cambió en la mitad. Y no hay una respuesta correcta: ambos valores parecen razonables.

Ese es el primer problema, y es serio, porque lo que queremos es medir. Un método cuyo resultado depende de un número que alguien eligió sin una razón clara no es un buen instrumento de medición.

El segundo problema es que el umbral trata a todos los píxeles por igual. No distingue una cabeza de una cola, ni una cabeza de una mancha, porque lo único que mira es el brillo de cada píxel por separado. Y el tercero es que ignora la forma. Dos células pegadas se convierten en una mancha grande, porque el umbral no sabe que ahí había dos objetos.

Mirado en conjunto, el umbral deja claro el límite de las reglas escritas a mano: cada regla nueva trae sus excepciones, y cuando se multiplican, mantener el programa deja de ser práctico. Hace falta plantear el problema de otra forma, y ahí entra el aprendizaje automático: se le muestran ejemplos al sistema y se deja que él encuentre las reglas. Con imágenes, la técnica que mejor funciona es la red neuronal.

[Diapositiva 6 · Una red neuronal no entiende]

> Idea central: Una red neuronal no entiende qué es un espermatozoide. Es un reconocedor de patrones muy sofisticado, y eso sirve para razonar cuándo va a funcionar y cuándo no.

Antes de construir la red, hay otra idea previa que condiciona cómo se va a escuchar el resto. Una red neuronal no entiende qué es un espermatozoide. No tiene el concepto ni sabe de biología, no sabe qué es una célula ni para qué sirve contarla. Tiene una enorme colección de números ajustados, de modo que ante ciertos patrones de píxeles produce una salida que coincide con lo que las personas marcaron en los ejemplos. Es un reconocedor de patrones muy sofisticado y nada más.

Eso no le quita mérito; sirve para razonar sobre cuándo va a funcionar y cuándo no. Si le muestro una imagen parecida a las de su entrenamiento, va a funcionar. Si le muestro algo muy distinto, no tiene cómo saber que se equivoca y producirá una salida con la misma seguridad aparente.

Tendemos a atribuirle a la red una comprensión que no tiene. Cuando una persona ve un espermatozoide, sabe qué es: tiene el concepto, sabe para qué sirve contarlos, entiende que una cola cortada sigue siendo parte de una célula. La red no sabe nada de eso. Lo único que tiene es una función muy complicada que recibe números y produce números.

Un buen ejemplo de esto es lo que pasa cuando se le muestra algo que nunca vio. Si le damos la imagen de otro tipo de tejido, no responde «esto no es lo que sé hacer». Responde con la misma seguridad, porque no tiene una forma de medir su propia ignorancia. Para ella, todo es una entrada y debe dar una salida.

Entonces, la confianza que podemos tener en una red depende de cuánto se parecen las imágenes nuevas a las imágenes con las que se entrenó. Si se parecen, la respuesta suele ser buena. Si no, no hay garantía. Por eso conviene mirar siempre la imagen marcada antes de confiar en un número.

Pensarlo así nos quita el misterio: una red neuronal es una máquina de reconocer patrones, muy buena, que hay que usar con criterio.

[Diapositiva 7 · Del umbral a la red: qué cambia]

> Idea central: El umbral usa una regla fija sobre un píxel. La red usa millones de reglas ajustadas con ejemplos, que miran vecindarios. Cambia quién escribe las reglas.

Hagamos una comparación directa entre los dos enfoques que vimos, porque resume lo que ganamos con la red.

El umbral es una sola regla, escrita por una persona: un píxel con brillo mayor a tal valor es célula. Mira cada píxel por separado, sin importar sus vecinos. No distingue forma, ni tamaño, ni textura. Y su resultado depende de un número elegido a mano.

La red neuronal es una enorme colección de reglas, millones de pesos, que no escribió nadie: se obtuvieron ajustándolos con ejemplos. Combina muchos píxeles a la vez, no uno por uno. Puede distinguir una cabeza de una cola por su forma, y una cabeza de una mancha por su textura y sus bordes. Y no depende de un solo número elegido a mano, porque lo que se ajustó fueron todos sus pesos, y se ajustaron para que coincidan con lo que las personas marcaron.

Otra diferencia es cómo se corrigen los errores. Con el umbral, si falla en un caso, hay que agregar una regla, con el riesgo de romper otros casos. Con la red, si falla en un tipo de caso, se agregan ejemplos de ese caso y se entrena de nuevo.

Pero la red también tiene un costo. Necesita ejemplos anotados, necesita entrenamiento, y sus decisiones son más difíciles de explicar que una regla simple. No se puede apuntar a un lugar y decir: esta regla lo decidió. Por eso en este proyecto se separa lo que decide la red, que es dónde está cada cabeza, de lo que se calcula con código, que es todo lo demás, y de ahí viene la idea de que la red localiza y el código mide, que veremos con detalle más adelante.

El cambio de fondo es de método: en lugar de decirle a la computadora cómo hacer algo, le mostramos qué queremos y dejamos que descubra cómo.

[Diapositiva 8 · La neurona artificial]

> Idea central: Una neurona artificial es una operación muy pequeña en cuatro pasos: recibe números, los multiplica por pesos, los suma y decide si se activa.

Ahora sí vamos a construir la idea de la red desde su pieza más pequeña, que es la neurona artificial. Es la pieza elemental, y aunque el nombre es más una inspiración histórica que una descripción fiel de la biología, es una operación muy pequeña que se describe en cuatro pasos.

Primero, recibe una lista de números, que son las entradas. Segundo, cada entrada se multiplica por otro número, que es su peso. Tercero, se suman los resultados. Y cuarto, a esa suma se le aplica una pequeña función que decide cuándo se activa la neurona.

Un ejemplo simple para ver qué hace un peso: imaginen una neurona que decide si un punto de la imagen es rojo e intenso. Recibe tres entradas, la cantidad de rojo, de verde y de azul de un píxel. Para que dé una salida alta con un píxel muy rojo, se le asigna un peso grande y positivo a la entrada del rojo, y pesos pequeños o negativos a las otras dos. Un píxel muy rojo produce una suma muy grande y uno azul una suma muy pequeña.

Los pesos expresan qué le importa a la neurona. Un peso grande dice «esto me va a importar mucho», uno cercano a cero dice «me da igual», y uno negativo dice «esto me hace dudar». Falta un elemento, un número que se suma al final, que se llama sesgo. Desplaza el punto desde el cual la neurona empieza a activarse. Pueden imaginarlo como un interruptor sensible: los pesos deciden a qué se fija y el sesgo decide qué tan exigente es antes de encenderse.

El último paso es la función de activación, que es lo que hace posible que las redes sean tan potentes. Por ahora basta saber que es una regla sencilla: si la suma es negativa, la salida es cero, y si es positiva, pasa tal cual.

Hagamos las cuentas de una neurona con números concretos, para que se vea que de verdad es solo multiplicar y sumar.

Retomemos el ejemplo de la neurona que busca píxeles rojos intensos. Para simplificar, expresamos cada canal entre cero y uno, dividiendo entre doscientos cincuenta y cinco. Le asignamos tres pesos: dos para el rojo, menos uno para el verde y menos uno para el azul. Y un sesgo de menos cero punto tres.

Probemos con un píxel naranja intenso, el de doscientos cuarenta, ciento veintidós y cuarenta y dos. En escala de cero a uno, son más o menos cero punto noventa y cuatro, cero punto cuarenta y ocho y cero punto diecisiete. Multiplicamos cada entrada por su peso: cero punto noventa y cuatro por dos da uno punto ochenta y ocho; menos cero punto cuarenta y ocho; y menos cero punto diecisiete. Sumamos: uno punto ochenta y ocho, menos cero punto cuarenta y ocho, menos cero punto diecisiete, da uno punto veintitrés. Y le restamos el sesgo, cero punto tres, y queda cerca de cero punto noventa y cuatro. La neurona responde con un número alto.

Probemos ahora con un píxel azul, de veinte, treinta y doscientos veinte. Las entradas son cero punto cero ocho, cero punto doce y cero punto ochenta y seis. El rojo aporta cero punto dieciséis, el verde resta cero punto doce y el azul resta cero punto ochenta y seis, y con el sesgo el total queda en menos uno punto doce. Es un número negativo, y la neurona, que se activa solo con valores positivos, responde cero.

Sin que nadie le dijera la palabra rojo, esta neurona distingue un píxel rojo de uno azul, solo por cómo están puestos sus pesos. El sesgo también cuenta: si fuera menos uno en lugar de menos cero punto tres, el píxel naranja daría solo cerca de cero punto veinticuatro, una respuesta mucho más tímida.

Esto es todo lo que hace una neurona: multiplicar, sumar y comparar. La potencia de una red viene de que hay millones de ellas, bien ajustadas.

[Diapositiva 9 · El sesgo, con un ejemplo]

> Idea central: El sesgo mueve el punto de activación. Con el mismo píxel y los mismos pesos, un sesgo más exigente apaga la neurona y uno más permisivo la deja encendida.

El sesgo suele ser el elemento menos intuitivo de la neurona, así que veámoslo con un ejemplo.

Pensemos en una neurona sencilla, que mira solo el brillo de un píxel, expresado entre cero y uno, y tiene un peso de uno. Sin sesgo, su cuenta es multiplicar el brillo por uno y aplicar la activación. Entonces, un píxel con brillo cero punto dos produce cero punto dos, uno con brillo cero punto cinco produce cero punto cinco, y uno con brillo cero punto nueve produce cero punto nueve. La neurona responde en proporción al brillo, desde el más tenue.

Ahora agreguemos un sesgo de menos cero punto seis. La cuenta es brillo por uno, menos cero punto seis. El píxel de cero punto dos da menos cero punto cuatro, y la activación lo convierte en cero. El de cero punto cinco da menos cero punto uno, y también queda en cero. Solo el de cero punto nueve da cero punto tres. Con ese sesgo, la neurona se queda callada con todo lo que sea tenue o medio, y solo responde ante lo muy brillante.

No cambiamos el peso, y sin embargo la neurona se comporta de otra manera. El sesgo funciona como una barrera: el estímulo tiene que superarla para que la neurona se encienda. Un sesgo muy negativo hace a la neurona muy exigente. Uno cercano a cero la hace permisiva.

Y el sesgo también es un número que la red aprende. Durante el entrenamiento se ajusta, igual que los pesos, hasta encontrar qué tan exigente debe ser cada neurona para que el conjunto funcione bien.

Esta idea tiene un parecido con el umbral que vimos antes. Un sesgo negativo con una activación que apaga todo lo que no lo supera es, en cierto modo, un umbral. La diferencia es que aquí el umbral no lo elige una persona a ojo: lo encuentra el entrenamiento, y es distinto para cada neurona. En el siguiente video seguimos con la activación, las capas y cómo aprende una red.
