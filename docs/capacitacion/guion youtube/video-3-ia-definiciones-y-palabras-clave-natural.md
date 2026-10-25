# Guion del video 3 de 6: La inteligencia artificial a nuestro alrededor, definiciones y palabras clave (versión natural)

BioImage-Repro UAM · Módulo 1 · Capacitación en video

Continúa del video 2. Empieza con la frase que lo une con el video anterior.

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos.

[Diapositiva · La inteligencia artificial a nuestro alrededor]

> Idea central: Sin darnos cuenta, usamos inteligencia artificial todos los días: al escribir, al buscar, al ver recomendaciones. Casi todo se basa en aprender de ejemplos.

En el video anterior vimos qué es una imagen digital: una tabla de números, con sus formatos y su escala. Ahora vamos con la inteligencia artificial. Pero antes de ponernos con las definiciones, miremos dónde ya vive. Seguramente ustedes usan todos los días, sin pensarlo, varias herramientas que funcionan con aprendizaje automático.

Escriben un mensaje en el teléfono y les sugiere la siguiente palabra. ¿Qué está pasando ahí? Un modelo aprendió, de millones de textos, qué palabras suelen seguir a cuáles. El correo manda un mensaje a la carpeta de no deseados: otro modelo se formó con muchísimos correos que otras personas marcaron como basura, y así reconoce los rasgos de ese tipo de mensaje. Y la plataforma de video propone qué ver después porque se apoya en lo que miraron personas parecidas a ustedes.

Lo mismo pasa con la voz. Al dictarle algo al teléfono, el modelo que lo transcribe aprendió a relacionar sonidos con palabras escuchando grandes cantidades de grabaciones transcritas, y un traductor que pasa una frase de un idioma a otro se formó con enormes colecciones de textos traducidos.

Y con las imágenes también. El teléfono agrupa las fotos por personas, o la cámara enfoca sola la cara. Son modelos que aprendieron a reconocer rostros a partir de muchísimos ejemplos.

¿Qué tienen en común todos? En ningún caso alguien escribió una lista de reglas para reconocer una cara, una frase o un mensaje basura. Habría sido imposible, por la cantidad de casos y de excepciones. Lo que se hizo fue reunir muchos ejemplos y dejar que el sistema encontrara por sí mismo qué los distingue.

Esa es la idea que sostiene el resto de lo que vamos a ver. También nos recuerda que estas herramientas no son mágicas ni inteligentes en el sentido humano. Son muy buenas para lo que vieron en sus ejemplos, y se equivocan de maneras que a veces sorprenden. En este curso vemos cómo funciona esa idea con un caso que nos queda muy cerca: contar y medir células.

[Diapositiva · La inteligencia artificial con imágenes de células]

> Idea central: En biología, la inteligencia artificial ayuda a contar, medir y localizar estructuras en imágenes de microscopio. Su valor está en la rapidez y en la consistencia.

Bueno, pasemos de la vida diaria a las ciencias de la vida, que es donde nos interesa. ¿Para qué se usa la inteligencia artificial con imágenes de microscopio?

Lo más directo: contar. Contar células, núcleos, bacterias o colonias en una imagen es algo que se hace todo el tiempo en un laboratorio, y es tedioso. Un modelo que cuenta con un criterio fijo ahorra tiempo y evita la variación entre personas.

Segundo: localizar. Saber dónde está cada estructura dentro de la imagen permite medirla, seguirla en el tiempo si se toman varias imágenes, o estudiar cómo se distribuyen unas respecto de otras. Esta es la tarea que nos ocupa: encontrar cada cabeza de espermatozoide.

Tercero: medir. Una vez localizada una estructura, se puede obtener su tamaño, su forma o su intensidad. Con las mediciones de cientos de estructuras se pueden comparar condiciones y tratamientos.

Cuarto: clasificar. Decidir de qué tipo es una célula, o si una región se ve normal o alterada, a partir de su apariencia. Es una tarea muy estudiada, y los resultados dependen mucho de la calidad de los ejemplos con que se entrena el modelo.

Y una quinta: filtrar. Antes de que una persona revise cientos de imágenes, un modelo puede señalar cuáles merecen atención, y así se aprovecha mejor el tiempo de quien conoce el tema.

En todos los casos pasa lo mismo: la inteligencia artificial no sustituye el criterio de quien investiga. Hace de forma rápida y consistente la parte repetitiva del trabajo, y le deja a la persona lo que requiere conocimiento: decidir qué preguntas hacer, interpretar los resultados y detectar cuándo algo no tiene sentido.

Un resultado producido por un modelo es una medición, con sus márgenes de error, y no una verdad. Por eso, en un buen sistema, el resultado siempre se puede revisar. Esa idea nos va a acompañar en todos los módulos.

[Diapositiva · Algunas definiciones de inteligencia artificial]

> Idea central: Inteligencia artificial, aprendizaje automático, redes neuronales y aprendizaje profundo son capas de un mismo campo, de lo más amplio a lo más específico.

Antes de entrar con las redes neuronales, conviene poner en orden algunas palabras, porque se mezclan muy seguido.

La inteligencia artificial es el campo más amplio: cualquier técnica que haga que una máquina realice tareas que se asocian con la inteligencia. El aprendizaje automático es la parte que aprende de ejemplos. Las redes neuronales son una técnica dentro del aprendizaje automático. Y el aprendizaje profundo se refiere a redes con muchas capas, que les explico en un momento.

La idea de fondo del aprendizaje automático cabe en una frase: el sistema encuentra las reglas a partir de ejemplos, en vez de que alguien las escriba. En la programación tradicional se entregan reglas y datos y salen las respuestas. En el aprendizaje automático se entregan datos y respuestas y salen las reglas. El flujo se invierte, y de eso depende todo lo que sigue.

Muchas familias de técnicas siguen esa idea, desde modelos estadísticos sencillos hasta arquitecturas muy complejas. Las redes neuronales son una de ellas, y rinden especialmente bien con imágenes, sonido o texto: datos crudos, con mucha estructura, que no se describen fácilmente con unas pocas variables. Aquí vamos a usar una red de aprendizaje profundo, que es la técnica que mejor funciona con imágenes.

Para que no se mezclen, conviene verlas como círculos que se contienen unos a otros. El más grande es la inteligencia artificial. Dentro está el aprendizaje automático. Dentro de este, las redes neuronales. Y dentro de las redes neuronales, el aprendizaje profundo, que son las que tienen muchas capas.

Algo que sale de ahí: no toda la inteligencia artificial aprende de ejemplos. Un programa que sigue reglas escritas por una persona, como un sistema que recomienda qué hacer si la temperatura sube de cierto valor, también es inteligencia artificial en el sentido amplio. Lo que distingue al aprendizaje automático es que las reglas se obtienen de los datos, en lugar de escribirlas una persona.

Y otra cosa: cuando se habla de inteligencia artificial en los medios, casi siempre se está hablando de aprendizaje profundo, que es la rama que más ha avanzado en los últimos años con imágenes, sonido y texto. Es la que usamos aquí.

[Diapositiva · Palabras que vamos a escuchar]

> Idea central: Seis palabras para los cuatro módulos: red neuronal, Google Colab, Python, Flask, modelo y servidor. Entrenamiento e inferencia se explican en el siguiente video.

Les dejo en pantalla unas palabras que van a escuchar durante los cuatro módulos. No las voy a leer todas, solo las que salen hoy.

Una red neuronal es un programa que aprende de ejemplos. Google Colab es un entorno para programar en la nube. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python: el sitio está hecho con las dos. El modelo es el archivo que guarda lo que la red aprendió. Y el servidor es la computadora donde el sitio está en línea, la que responde cuando alguien entra. También aparecen dos palabras que explico en el siguiente video, entrenamiento e inferencia, porque son las que más confunden y las que más importa distinguir.

[Diapositiva · Red neuronal]

> Idea central: Una red neuronal es un programa formado por muchas operaciones pequeñas conectadas, cuyos valores se ajustan a partir de ejemplos en lugar de escribirse a mano.

Empecemos por la palabra que más vamos a usar: red neuronal. Dicho de forma sencilla, es un programa que se va afinando con ejemplos.

Un programa tradicional es una lista de instrucciones: si pasa esto, haz aquello. Una red neuronal, en cambio, es una estructura de muchísimas operaciones muy pequeñas, conectadas entre sí, y cada operación tiene unos números que se pueden ajustar. Esos números se llaman pesos. Al principio los pesos valen cualquier cosa, y la red no sirve para nada. Después, con ejemplos, los pesos se van ajustando hasta que la red da buenas respuestas.

Por eso decimos que la red aprende. No aprende como una persona, no comprende lo que hace. Lo que ocurre es que, ejemplo tras ejemplo, sus pesos se acercan a valores que producen la respuesta correcta.

El nombre viene de una inspiración. Las neuronas del cerebro reciben señales y, según el total, se activan o no. Las neuronas artificiales hacen algo parecido, pero mucho más simple. Hay que tomar esa comparación con cautela: una red neuronal artificial no es un cerebro, y el parecido es más de forma que de funcionamiento.

Una cosa más. Hay redes de muchos tamaños. Algunas tienen unas decenas de pesos y se pueden estudiar a mano. Las que se usan con imágenes tienen millones, y la que usamos nosotros tiene decenas de millones. Pero el principio es siempre el mismo: operaciones pequeñas, con pesos ajustables, que se ajustan con ejemplos.

En los siguientes videos vamos a construir una desde cero, empezando por su pieza más pequeña, para que se vea que no hay nada misterioso.

[Diapositiva · Google Colab]

> Idea central: Google Colab es un cuaderno de programación en la nube, con computadoras potentes disponibles desde el navegador. Ahí se entrenó el modelo.

La segunda palabra es Google Colab. Colab es un entorno para programar que funciona dentro del navegador. No hay que instalar nada en la computadora. Uno abre una página, escribe código en celdas, y ese código se ejecuta en una computadora de Google, en la nube.

Eso tiene una ventaja enorme para la inteligencia artificial. Entrenar una red neuronal exige muchísimo cálculo, y una computadora común puede tardar horas o días en algo que una máquina especializada hace en minutos. Colab permite usar esas máquinas potentes, con mucha memoria y con tarjetas gráficas, que son especialmente buenas para este tipo de cálculo, sin comprarlas. Y es accesible: se puede empezar a usar sin costo, y hay planes de pago si hace falta más capacidad.

Se trabaja en cuadernos. Un cuaderno es un documento que mezcla texto explicativo y celdas de código, y se ejecuta celda por celda. Eso lo hace muy bueno para enseñar y para documentar, porque quien lo lee ve qué se hizo, en qué orden y con qué resultado.

En este proyecto, Colab es donde se entrena el modelo. El entrenamiento está escrito en un cuaderno que cualquier persona con el enlace puede abrir y ejecutar, y así cualquiera puede repetir el entrenamiento.

También hay que decir qué no es Colab: no es donde vive el sitio. Cuando el entrenamiento termina, lo que sale es un archivo, y ese archivo se lleva al servidor donde está la página. Colab sirve para entrenar, y no para que las personas usen el modelo todos los días. Esa diferencia es justo la que veremos con entrenamiento e inferencia.

[Diapositiva · Python]

> Idea central: Python es el lenguaje de programación que se usa en casi toda la inteligencia artificial, gracias a sus bibliotecas. Aquí se usa para entrenar el modelo y para hacer el sitio.

La tercera palabra es Python. Python es un lenguaje de programación, o sea, la forma en que le escribimos instrucciones a una computadora de manera que una persona pueda leerlas.

Python tiene fama de ser fácil de leer, porque sus instrucciones se parecen a frases en inglés y no obliga a escribir muchos símbolos. Pero también domina la inteligencia artificial porque alrededor de Python se construyó un enorme conjunto de bibliotecas, que son colecciones de programas ya escritos para tareas comunes.

Algunas son las que usamos en este proyecto. PyTorch es la biblioteca con la que se construye y se entrena la red neuronal. NumPy sirve para trabajar con tablas de números, como las imágenes que vimos hace un momento. OpenCV está especializada en imágenes, y con ella se miden los contornos y las áreas. Y Matplotlib se usa para hacer las gráficas.

Un proyecto como este no se escribe desde cero. Se combinan bibliotecas muy buenas, cada una especializada en algo, y el trabajo propio está en unirlas con cuidado y en decidir cómo se usan.

Hay otros lenguajes que también se usan en inteligencia artificial, como C++ para las partes que necesitan máxima velocidad. Pero Python es el que se usa para escribir y probar las ideas.

[Diapositiva · Flask]

> Idea central: Flask es una herramienta de Python para construir sitios web. Recibe lo que pide el navegador, hace el trabajo y devuelve la página.

La cuarta palabra es Flask. Flask es una herramienta, lo que en programación se llama un marco de trabajo, para hacer sitios web con Python.

Para entender qué hace, recordemos cómo funciona una página web. El navegador le manda una petición al servidor: quiero esta página, o quiero analizar esta imagen. El servidor tiene que recibir esa petición, decidir qué hacer con ella, hacer el trabajo y devolver una respuesta, que normalmente es una página que el navegador dibuja.

Flask se encarga de esa parte. Uno le indica, con unas pocas líneas de código, qué dirección de la página corresponde a qué función. Por ejemplo: cuando alguien entra a la página de inicio, se ejecuta esta función y se muestra esta plantilla. Y cuando alguien sube una imagen, se ejecuta esa otra función que analiza la imagen.

Para armar las páginas se usan plantillas. Una plantilla es una página con huecos: el diseño es siempre el mismo, y los huecos se llenan con lo que corresponda en cada caso, como el nombre de la persona o la tabla de resultados. Este sitio usa plantillas y la biblioteca Bootstrap, que ayuda a que se vea bien tanto en una computadora como en un teléfono.

Flask también se encarga de cosas como las cuentas de las personas, para saber quién entró, y de guardar información en una base de datos. En este proyecto la base de datos es SQLite, una base de datos sencilla que vive en un archivo.

¿Por qué se eligió Flask? Porque es pequeño y claro. No obliga a aprender un montón de reglas, y permite que una persona entienda de principio a fin cómo está hecho el sitio. Y como está escrito en Python, puede llamar directamente a la red neuronal, que también está en Python. El sitio y el modelo hablan el mismo idioma.

[Diapositiva · Modelo]

> Idea central: El modelo es el archivo que guarda lo que la red aprendió: sus pesos. Por sí solo no hace nada, hace falta un programa que lo cargue y lo use.

La quinta palabra es modelo. Cuando una red termina de entrenarse, lo que se obtiene es un archivo. Ese archivo es el modelo.

¿Qué hay dentro? Básicamente, la estructura de la red y el valor de todos sus pesos. Los pesos son los números que se ajustaron durante el entrenamiento, y son lo que la red sabe. Si la red fuera una receta, el modelo sería la receta escrita, con todas las cantidades ya afinadas.

En el proyecto, el modelo es un archivo con extensión punto pt, que es el formato en que PyTorch guarda sus modelos. Contiene decenas de millones de números, y por eso ocupa bastante espacio, del orden de cientos de megabytes. Casi todo ese peso son los pesos.

Un modelo por sí solo no hace nada. Es como un libro cerrado: tiene todo adentro, pero nadie lo puede leer. Hace falta un programa que lo abra, lo cargue en la memoria y le dé una imagen para que responda. Eso es lo que hace el sitio, y eso se llama inferencia.

Otra característica: un modelo está fijo. Una vez entrenado, sus pesos no cambian mientras se usa. Si le damos mil imágenes para que las analice, seguirá siendo exactamente el mismo modelo, con exactamente los mismos pesos. No aprende de lo que analiza. Para que cambie hay que entrenarlo otra vez, aparte, y el resultado es un modelo nuevo, un archivo distinto.

De ahí sale algo que a veces sorprende: dos personas que analizan la misma imagen con el mismo modelo obtienen siempre el mismo resultado. Y eso es justo lo que queremos de un instrumento de medición.

[Diapositiva · Servidor]

> Idea central: El servidor es la computadora, siempre encendida y conectada a internet, donde vive el sitio y donde se usa el modelo cada vez que alguien sube una imagen.

La sexta palabra es servidor. Un servidor es una computadora, o un programa que corre en una computadora, cuyo trabajo es responder peticiones de otras computadoras.

No tiene nada de mágico. Es una computadora como cualquier otra, solo que está siempre encendida, conectada a internet y con un programa esperando a que alguien le pida algo. Cuando ustedes escriben la dirección de un sitio o hacen clic en un botón, su navegador manda una petición y el servidor contesta.

En este proyecto, el servidor es una computadora que se contrata en un servicio de alojamiento. Ahí está instalado el sitio, con sus páginas, sus cuentas y su base de datos. Y ahí también está el archivo del modelo. Cuando alguien sube una imagen, el servidor la recibe, la prepara, se la da al modelo, recibe los contornos, mide, arma los resultados y devuelve la página con todo.

Ese servidor no tiene una tarjeta gráfica especializada. Hace la inferencia con su procesador, el que tiene cualquier computadora. Y se puede, porque usar un modelo ya entrenado es mucho más ligero que entrenarlo. Un análisis tarda unas decenas de segundos, y no horas.

También hay programas que ayudan al servidor a trabajar bien. Uno recibe las peticiones de internet y las reparte, y otro corre el sitio en sí, para que pueda atender a varias personas a la vez. No hace falta que conozcamos los detalles ahora. Quédense con esto: el servidor es el lugar donde las cosas realmente suceden, y el navegador de cada persona es solo una ventana para ver y pedir.

Y de cómo se pone un servidor en internet, y qué cuidados requiere, hablaremos en el último módulo.

[Diapositiva · Cómo se ve un cuaderno de Colab]

> Idea central: Un cuaderno de Colab mezcla texto y celdas de código que se ejecutan una por una, y deja a la vista cada paso y su resultado.

Antes de pasar al entrenamiento, imaginemos cómo se ve un cuaderno de Colab, porque es donde ocurre.

Un cuaderno es un documento con dos tipos de bloques. Unos son de texto: explican qué se va a hacer y por qué. Otros son celdas de código: pequeñas porciones de programa que se pueden ejecutar de una en una. Debajo de cada celda aparece su resultado, que puede ser un número, una tabla, una gráfica o una imagen.

Esa forma de trabajo tiene una ventaja enorme: el proceso queda a la vista. Quien abre el cuaderno puede leer la explicación, ver el código, ejecutarlo y ver el resultado, paso a paso. No hay que adivinar qué se hizo.

El cuaderno de este proyecto está dividido en pasos numerados. Primero, el entorno y la configuración. Después se leen las etiquetas, que son las anotaciones, y se revisa que todo cuadre. Luego se separan las imágenes de entrenamiento de las de validación, y se preparan las imágenes y sus recortes. Más adelante se construye la red, partiendo de una ya entrenada, y se define cómo se mide si funciona. Después viene el entrenamiento propiamente dicho, donde se ve cómo baja la pérdida. Y al final se ven los resultados, con las imágenes y lo que encontró la red, y se exporta el modelo a un archivo.

Se puede ejecutar solo una parte, y eso sirve para probar. Por ejemplo, entrenar unos minutos con pocas imágenes solo para verificar que todo funciona antes de lanzar el entrenamiento completo.

Un cuaderno es, además, un registro. Si alguien quiere saber con qué datos y con qué decisiones se obtuvo un modelo, el cuaderno lo dice. Y si alguien quiere repetirlo, lo ejecuta.

El cuaderno lo vamos a abrir y recorrer juntos en el último módulo. En el siguiente video vemos cómo se entrena un modelo y cómo se usa.
