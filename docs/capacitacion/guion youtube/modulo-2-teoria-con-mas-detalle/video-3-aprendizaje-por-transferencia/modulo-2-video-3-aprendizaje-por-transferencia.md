# Guion del módulo 2, video 3 de 4: Aprendizaje por transferencia

BioImage-Repro UAM · Módulo 2 · Capacitación en video

Continúa del video anterior. Empieza con la frase que lo une con el video anterior.

*3,377 palabras, unos 19.3 min de habla*

[Diapositiva 1 · Mucha red y pocas fotos]

> Idea central: El video anterior dejó una pregunta: Mask R-CNN tiene 43.9 millones de pesos y nosotros tenemos muy pocas fotos etiquetadas. El aprendizaje por transferencia resuelve eso: en vez de empezar de cero, se parte de una red que ya aprendió a ver con otras fotos.

El video anterior terminó con una pregunta que quedó abierta. Mask R-CNN tiene casi 44 millones de pesos, y nosotros tenemos muy pocas fotos con espermatozoides etiquetados. Entrenar una red de ese tamaño desde cero suele pedir muchísimos más ejemplos de los que tenemos. Y sin embargo, el sitio funciona. En este video vemos por qué.

La respuesta se llama aprendizaje por transferencia, o transfer learning en inglés. La idea cabe en una frase: en lugar de empezar con una red que no sabe nada, se empieza con una que ya aprendió a ver con otras fotos, y se le enseña solo lo que falta.

En pantalla están los números que plantean el problema. Del lado izquierdo, una red con 43.9 millones de pesos. Del derecho, nuestros datos, los del cuaderno de entrenamiento que usamos de ejemplo: cuatro fotos de fluorescencia con 258 espermatozoides etiquetados, de los que 163 se usan para entrenar y 64 para validar. Más adelante revisamos esos números con calma. Por ahora quedémonos con la desproporción: muchísimos pesos y muy pocos ejemplos.

Vamos a ver tres cosas. Primero, por qué empezar de cero es difícil. Segundo, qué se reutiliza de la red que ya aprendió y qué se cambia. Y tercero, qué pasa cuando se entrena así, con números de un entrenamiento real, y dónde se queda corta la idea.

[Diapositiva 2 · Empezar de cero]

> Idea central: Una red recién creada tiene pesos al azar y no sabe ni qué es un borde. Aprender todo desde cero con 163 espermatozoides de entrenamiento daría unos 270,000 pesos por cada ejemplo, y la red tendería a aprenderse las fotos de memoria.

Recordemos cómo nace una red. Se crea con pesos al azar. Una red recién creada no sabe qué es un borde, ni una esquina, ni una mancha brillante sobre fondo oscuro. Todo eso tendría que descubrirlo durante el entrenamiento, ajustando sus pesos poco a poco, como vimos en el módulo 1.

Hagamos una cuenta con el cuaderno de ejemplo. De los 258 espermatozoides etiquetados, 163 quedaron en la parte de las fotos que se usa para entrenar. Con 43,922,395 pesos, eso son unos 270,000 pesos por cada espermatozoide. Para cada ejemplo hay cientos de miles de números que ajustar.

Es verdad que cada época se arman recortes nuevos al azar, con la imagen un poco acercada o alejada, y eso da variedad. Pero las cabezas siguen siendo las mismas 163. Con tantos pesos y tan pocos ejemplos, una red tiene un riesgo claro: en lugar de aprender qué es un espermatozoide, se aprende esas fotos de memoria. Se vería perfecta con lo que ya vio y fallaría con una foto nueva. Eso tiene nombre, sobreajuste, y lo vemos con detalle en el siguiente video.

Hay otra parte del problema. Aunque se logre, aprender desde cero a ver bordes y formas cuesta tiempo de cómputo y muchos ejemplos, y esa es justo la parte que más se parece entre una tarea y otra. Un borde se ve igual en la foto de un perro y en la de un espermatozoide. Sería un desperdicio aprenderlo otra vez.

[Diapositiva 3 · La guitarra y el ukulele]

> Idea central: Quien toca la guitarra aprende el ukulele mucho más rápido que quien nunca ha tocado un instrumento, porque ya trae oído, ritmo y manos entrenadas. Solo falta lo propio del ukulele. Con una red pasa algo parecido.

Una forma de entenderlo es con instrumentos. En pantalla hay una guitarra y un ukulele.

Alguien que nunca ha tocado nada y quiere aprender el ukulele tiene que aprenderlo todo: a sostener el instrumento, a llevar el ritmo, a distinguir una nota de otra, a mover los dedos con soltura. Alguien que ya toca la guitarra no empieza de cero. Ya trae oído, ya lleva el ritmo, ya tiene los dedos entrenados. Lo que le falta es lo propio del ukulele: tiene cuatro cuerdas en lugar de seis, se afina distinto y los acordes tienen otra forma. En unas semanas ya toca canciones.

Con las redes pasa algo parecido. La guitarra es una red que ya aprendió a ver con muchas fotos de otras cosas. El ukulele es nuestra tarea: encontrar y contornear espermatozoides. Lo que la red ya trae, ver bordes, texturas y formas, se aprovecha. Lo que le falta, saber que lo que nos interesa es una cabeza de espermatozoide, es lo que se le enseña con nuestras fotos.

La analogía tiene un límite que conviene decir desde ahora. El guitarrista que aprende ukulele sigue sabiendo tocar la guitarra. Una red que se sigue entrenando cambia sus pesos, y con ellos puede perder parte de lo que traía. Por eso, al afinar, se cuida cuánto se mueven los pesos y cuáles se dejan fijos. Eso lo vemos en la diapositiva 8.

[Diapositiva 4 · Qué aprende cada parte de la red]

> Idea central: Las primeras capas de una red convolucional aprenden patrones muy generales, como bordes y manchas, que sirven en casi cualquier foto. Las últimas aprenden cosas cada vez más específicas de la tarea. Por eso lo general se puede reutilizar y lo específico se cambia.

Para que la analogía funcione, tiene que ser cierto que en una red hay una parte general y una parte específica. Y lo es. En el primer video de este módulo vimos los filtros de la primera capa y los mapas que producen. En pantalla están otra vez, de menor a mayor profundidad.

Las primeras capas detectan cosas muy sencillas: un borde en cierta dirección, un cambio de brillo, una mancha. Esos patrones aparecen en cualquier foto. Los mismos filtros sirven para una calle, para un rostro y para un espermatozoide. A medida que se avanza, las capas combinan lo anterior y reconocen cosas más complejas: una esquina, una curva, una textura, una forma redondeada. Y las últimas ya responden a combinaciones propias de la tarea para la que se entrenó la red.

Esto se ha comprobado en muchas redes. Lo que está al principio de la base se parece mucho de una tarea a otra, y lo que está al final cambia más. De ahí sale la estrategia: lo general se conserva y lo específico se vuelve a entrenar.

Un ejemplo concreto con nuestra red. La primera capa de la base tiene 64 filtros de 7 por 7, con 3 canales de entrada. Son 9,408 pesos. Sirven igual para fotos de cualquier cosa, y no hay razón para volver a aprenderlos. En el otro extremo, la cabeza de clasificación del video anterior decide entre las clases con las que se entrenó. Si las clases cambian, esa pieza tiene que cambiar. Entre una y otra hay una gradación: cuanto más cerca de la salida, más específica es la pieza y más probable es que haya que ajustarla.

[Diapositiva 5 · La idea: partir de lo ya aprendido]

> Idea central: Transferir es partir de los pesos de una red ya entrenada en otra tarea. Se llama preentrenada. La tarea original es la de origen, la nuestra es la de destino, y el entrenamiento nuevo, que ajusta los pesos, se llama afinar.

Pongámosle nombres a las piezas, porque se usan mucho.

Una red preentrenada es una red que ya fue entrenada antes, por alguien más, con otra tarea. Esa tarea es la tarea de origen. La nuestra, contar espermatozoides, es la tarea de destino. Aprendizaje por transferencia es usar lo aprendido en la tarea de origen para resolver la de destino.

El entrenamiento que se hace después, con nuestras fotos, se llama afinar, o fine-tuning en inglés. No se parte de pesos al azar sino de los pesos preentrenados, y se ajustan un poco para que encajen con nuestra tarea.

En pantalla se ve el flujo. A la izquierda, la tarea de origen con sus muchas fotos, de la que sale una red con sus pesos. En el centro, esos pesos que se copian. A la derecha, la tarea de destino con pocas fotos, que ajusta los pesos copiados. El entrenamiento largo y caro lo hizo otro, con equipos que nosotros no tenemos. A nosotros nos toca la parte corta. Para dar una idea de la diferencia: en el cuaderno, descargar los pesos preentrenados tarda un par de segundos, y el entrenamiento completo de ejemplo dura unos 36 minutos en la GPU gratuita de Colab.

[Diapositiva 6 · COCO, la tarea de origen]

> Idea central: La red del sitio parte de una Mask R-CNN que torchvision entrenó con COCO, un conjunto público con más de cien mil fotos de objetos cotidianos en 80 tipos, con contornos dibujados por personas. Ahí no hay microscopía ni espermatozoides.

La red de la que partimos viene de torchvision, la biblioteca de PyTorch que usamos. Sus autores entrenaron una Mask R-CNN con un conjunto de datos llamado COCO y publicaron los pesos, que se descargan en un archivo de unos 170 megabytes.

COCO es un conjunto público de fotos de objetos cotidianos. Tiene más de cien mil fotos de entrenamiento con 80 tipos de objetos: personas, perros, bicicletas, autos, tazas, sillas. En cada foto, personas dibujaron el contorno de cada objeto. Es decir, es el mismo tipo de tarea que nuestra red hace con los espermatozoides: encontrar cada objeto, encuadrarlo y delinearlo. En pantalla hay una foto de ese tipo, con sus contornos.

Aquí aparece una pregunta honesta. En COCO no hay fotos de microscopio, ni fluorescencia, ni un solo espermatozoide. ¿Cómo puede ayudar? Ayuda porque lo que se reutiliza es lo general. Esa red ya sabe ver bordes, manchas y formas. Ya sabe distinguir un objeto de su fondo. Ya sabe proponer regiones, recortarlas y dibujar un contorno. Todo eso se parece mucho entre una taza y una cabeza de espermatozoide.

También hay diferencias, y se notan. Las fotos de COCO son en color, de escenas cotidianas. Las nuestras son de fluorescencia, con fondo negro, y la red las ve en grises. Eso quiere decir que no todo lo que traen los pesos de COCO es útil para nosotros, y por eso conviene afinar en lugar de usar la red tal como viene.

[Diapositiva 7 · Qué se reutiliza y qué se cambia]

> Idea central: De los 43,922,395 pesos del modelo, 43,649,231 (99.4 %) vienen de COCO y 273,164 (0.6 %) se crean nuevos: la última capa de clasificación (10,250) y la cabeza de máscara final (262,914). Las anclas de COCO también se reemplazan por otras más chicas.

Veamos con números qué se reutiliza. En pantalla hay una barra con los pesos del modelo, dividida en dos partes.

La parte grande, de 43,649,231 pesos, que es el 99.4 por ciento, viene de COCO tal como estaba: la base convolucional, la pirámide, la red de propuestas, las dos capas de 1,024 neuronas de la cabeza de clasificación y las cuatro capas de filtros de la cabeza de máscara. La parte pequeña, de 273,164 pesos, el 0.6 por ciento, se crea nueva y empieza al azar.

¿Cuáles son esas piezas nuevas? La red original distingue 80 tipos de objetos, y la nuestra solo necesita dos clases: fondo y espermatozoide. Por eso se cambia la última capa de la cabeza de clasificación, la que da el puntaje por clase y los cuatro números de la caja. Con dos clases tiene 10,250 pesos, la cifra del video anterior. Y se cambia la última parte de la cabeza de máscara: la capa que duplica el tamaño y la que da una máscara por clase. Allí hay 262,914 pesos nuevos.

Hay un tercer cambio que no está en esa cuenta, y es de otro tipo. Las anclas. En la red de COCO miden de 32 a 512 píxeles. En la nuestra, de 16 a 256, porque nuestros espermatozoides son mucho más chicos. Los pesos de la red de propuestas se copian de COCO, pero ahora se aplican a anclas de otro tamaño, así que esa pieza no encaja del todo y se tiene que reajustar. Reutilizar pesos pide revisar si todavía encajan con lo que se cambió alrededor.

[Diapositiva 8 · Congelar o afinar]

> Idea central: Hay dos maneras de usar una red preentrenada: congelar casi todo y entrenar solo las piezas nuevas, o afinar casi todo. En el sitio se congela solo el primer bloque (222,400 pesos) y se afinan 43.7 millones.

Una vez que se tienen los pesos de COCO, hay dos maneras de aprovecharlos. En pantalla están las dos.

La primera es congelar. Se dejan fijos casi todos los pesos de la red y solo se entrenan las piezas nuevas. Es más rápido y hay muy poco riesgo de que la red se aprenda las fotos de memoria, porque casi nada puede moverse. El inconveniente es que la red no se adapta a lo que tengan de particular nuestras fotos. Si son muy distintas de COCO, queda corta.

La segunda es afinar. Se entrenan casi todos los pesos, empezando desde los de COCO. La red se adapta mejor a nuestras fotos, pero tiene más libertad para equivocarse con pocos datos, y hay que tener más cuidado con qué tanto se mueven los pesos en cada paso.

En nuestro caso se hace algo intermedio, pero más cerca de afinar. Se congela solo el principio de la base: la primera capa, con sus 9,408 pesos, y el primer bloque de filtros, con 212,992. Son 222,400 pesos en total, el 0.5 por ciento. Son los más generales, los de bordes y manchas, así que tiene sentido no tocarlos. Los otros 43.7 millones de pesos sí se ajustan. También se dejan fijas las capas de normalización, porque con lotes pequeños, como los que caben en la GPU gratuita de Colab, eso hace el entrenamiento más estable. Este valor, congelar el primer bloque, es el que torchvision trae por omisión. Con otros valores los resultados podrían cambiar, y aquí no los comparamos.

Para no sacudir de golpe lo que traen los pesos, el entrenamiento arranca con un calentamiento: durante los primeros cien pasos la tasa de aprendizaje sube poco a poco. En el cuaderno, cien pasos son exactamente la primera época.

[Diapositiva 9 · Un entrenamiento de ejemplo]

> Idea central: En la corrida de ejemplo del cuaderno, con 163 espermatozoides de entrenamiento, la pérdida baja de 1.39 a 0.70 en cinco épocas, unos 3 minutos, y el AP50 de validación ya es 0.857. El mejor valor, 0.888, llega en la época 20. La validación es pequeña y sale de las mismas fotos, así que son cifras orientativas.

Veamos qué pasa al entrenar así. Los números de esta diapositiva salen de una corrida del cuaderno de entrenamiento, el que vemos en el módulo 4. Se entrenó en la GPU gratuita de Colab, con el perfil de fluorescencia. Eran cuatro fotos con 258 espermatozoides etiquetados. De ellos, 163 quedaron en la zona de entrenamiento y 64 en la de validación. Los 31 restantes quedaron en una franja de 100 píxeles que se deja entre las dos zonas para no cortar un espermatozoide a la mitad.

Cada época toma 400 recortes de 512 por 512 píxeles, en lotes de cuatro. Tarda unos 36 segundos. En pantalla está la curva de la pérdida, que es la suma de las cinco pérdidas del video anterior. En la primera época vale 1.39. En la segunda baja a 0.87. En la quinta, a 0.70. En la época 20, a 0.46. Baja rápido al principio, que es lo esperable de una red que no empieza de cero.

La segunda curva es la de validación, que se mide cada cinco épocas. El AP50 es una medida de calidad que va de 0 a 1, y la vemos con más detalle en el video cuatro. Ya en la quinta época, a los tres minutos de empezar, vale 0.857, con una precisión de 0.77 y una exhaustividad de 0.86. El cuaderno guarda el mejor modelo de toda la corrida, y fue el de la época 20, con un AP50 de 0.888. Ninguna validación posterior lo supera. Entre las épocas 25 y 45 oscilan entre 0.81 y 0.87.

Hay que leer esto con cuidado. La zona de validación tiene alrededor de 65 espermatozoides y sale de una franja de las mismas cuatro fotos, no de fotos nuevas. Es una prueba más fácil que la que presentaría una foto distinta, y con tan pocos ejemplos una diferencia de unas centésimas puede ser casualidad. Los números sirven para ver la forma de la curva, y no hay que tomarlos como la calidad final del sitio. Tampoco podemos decir cuánto peor habría sido empezar desde cero, porque esa comparación no es parte de este curso. Lo que sí se ve es que, con pesos preentrenados, una red de 43.9 millones de pesos ya funciona razonablemente a los tres minutos y con 163 ejemplos.

[Diapositiva 10 · Lo que la transferencia no resuelve]

> Idea central: La transferencia reduce lo que hace falta, pero no lo elimina. No arregla etiquetas descuidadas, no vuelve confiable una validación pequeña, hereda lo que la red de origen no sabe, y la red sigue contestando ante fotos que no conoce.

La transferencia ayuda mucho, y tiene sus límites. Son cuatro.

La primera: no arregla las etiquetas. Si los contornos de entrenamiento están descuidados, la red aprende contornos descuidados. Con pocas fotos pesan todavía más, porque cada etiqueta cuenta mucho. Con las cinco pérdidas sumadas en un solo número, una etiqueta mala afecta a todas.

La segunda: no hace confiable la validación. Con pocas fotos, la medición también es pobre, como acabamos de ver. Tener un modelo que arranca bien no quiere decir que sepamos qué tan bien funciona. Para eso hacen falta fotos de validación que la red no haya visto, y suficientes.

La tercera: la red hereda lo que su tarea de origen le enseñó. Como COCO está hecho de fotos de objetos cotidianos, la red trae una idea de objeto que no siempre coincide con la nuestra. Las fibras y las manchas brillantes pueden parecerle objetos, y ya vimos en el video anterior que el sitio las marca a veces como si fueran espermatozoides.

La cuarta: la red sigue contestando aunque la foto no sea de lo que conoce. En el video anterior, el modelo dio 0.96 sobre un núcleo de célula. Que la red parta de COCO no cambia eso: sigue sin saber qué es un espermatozoide hasta que se le enseña, y aun después contesta en fotos que no conoce.

[Diapositiva 11 · Cuándo conviene y cuándo no]

> Idea central: Como regla práctica, cuanto más se parezcan las dos tareas y menos datos haya, más conviene congelar. Cuanto más distintas sean y más datos haya, más conviene afinar. Con tareas muy distintas y pocos datos, la transferencia ayuda menos.

¿Cuándo conviene usar transferencia y cómo? Aquí no hay una regla exacta, pero sí una regla práctica, que se puede resumir en una tabla de dos por dos. En pantalla está.

Si las dos tareas se parecen y hay pocos datos, lo mejor suele ser congelar casi todo y entrenar poco. Hay poco que cambiar y mucho riesgo de memorizar. Si se parecen y hay más datos, se puede afinar más, con confianza. Si las tareas son muy distintas y hay muchos datos, conviene afinar casi todo, porque hay ejemplos para corregir lo heredado, y a veces incluso entrenar desde cero es razonable. Y si son muy distintas y hay pocos datos, es la situación difícil: la transferencia ayuda menos, y hace falta conseguir más ejemplos.

¿Dónde estamos nosotros? Tenemos pocos datos, y nuestras fotos se parecen poco a las de COCO en lo superficial, porque tienen fondo negro y vienen de un microscopio, pero se parecen bastante en lo que importa: manchas con borde sobre un fondo. Por eso afinar casi todo funciona. Pero no hay garantía. Es una decisión que se confirma midiendo, con fotos de validación que sean de verdad nuevas, y que mejora conforme se etiquetan más fotos.

Eso último tiene una consecuencia práctica. Cuando hay más fotos etiquetadas, el cuaderno no sigue entrenando el modelo anterior. Entrena una corrida nueva, que vuelve a partir de los pesos de COCO, con todas las fotos juntas y con un nombre distinto, para no sobrescribir la anterior. Así se pueden comparar las dos corridas con la misma validación y quedarse con la mejor. Mientras más variadas sean las fotos nuevas, con espermatozoides densos, escasos y con fibras, más aprovecha la red lo que ya trae.

[Diapositiva 12 · Cómo se ve en el código]

> Idea central: En el cuaderno, la transferencia son tres pasos: cargar la red con los pesos de COCO, cambiar las dos piezas finales a dos clases y entrenar. El servidor no descarga nada de COCO: el archivo del modelo entrenado ya trae todos los pesos.

Para terminar con la parte técnica, veamos cómo se ve todo esto en el código. En el módulo 4 recorremos el cuaderno completo. Aquí solo mostramos las líneas que hacen la transferencia, y son pocas.

La primera carga la Mask R-CNN de torchvision indicando que se quieren los pesos de COCO, y le dice que deje fijo el primer bloque. Junto con eso se le dan las opciones propias del proyecto, como el tamaño de las anclas. La segunda línea cambia la última capa de la cabeza de clasificación por una de dos clases. Y la tercera hace lo mismo con la cabeza de máscara. Después viene el entrenamiento, que es un ciclo igual al que vimos en el módulo 1: calcular la pérdida, ver hacia dónde mover los pesos y moverlos.

La función que arma la red tiene dos modos. Uno es para entrenar: descarga los pesos de COCO y los usa como punto de partida. El otro es para servir el sitio: arma la misma estructura sin pesos y espera que se los den después. Que la estructura sea idéntica en los dos casos es lo que permite pasar el modelo entrenado de Colab al servidor.

Un detalle útil. El servidor del sitio nunca descarga los pesos de COCO. Cuando el entrenamiento termina, el modelo se guarda en un archivo, y ese archivo ya trae todos los pesos, los heredados y los ajustados. Para analizar una foto, el servidor arma la misma estructura de red, sin pesos, y carga ese archivo. Los pesos de COCO solo hicieron falta una vez, al entrenar.

[Diapositiva 13 · Lo que vimos y lo que sigue]

> Idea central: Vimos por qué empezar de cero es difícil, la analogía de la guitarra y el ukulele, qué es una red preentrenada, de dónde vienen los pesos de COCO, qué se reutiliza y qué se cambia, congelar o afinar, un entrenamiento de ejemplo y sus límites. En el siguiente video, los datos y el entrenamiento.

Resumamos. Vimos que entrenar una red de 43.9 millones de pesos desde cero, con 163 espermatozoides, es un mal plan: faltan ejemplos y sobra riesgo de memorizar. Vimos que una red que ya aprendió a ver con otras fotos sirve de punto de partida, igual que quien toca la guitarra aprende el ukulele más rápido. Vimos que las primeras capas son generales y las últimas, específicas, y que por eso se reutiliza casi todo y se cambia lo final.

Vimos que el modelo del sitio parte de una Mask R-CNN entrenada con COCO. Que el 99.4 por ciento de sus pesos vienen de ahí, que 273,164 se crean nuevos para las dos clases y que las anclas se cambiaron por unas más chicas. Vimos que se congela solo el primer bloque, con 222,400 pesos, y se afinan los otros 43.7 millones. Vimos una corrida de ejemplo en la que la pérdida baja pronto y la validación llega a 0.857 a los tres minutos. Y vimos sus límites: no arregla etiquetas descuidadas, no hace confiable una validación pequeña y la red sigue contestando ante fotos que no conoce.

En el siguiente video entramos al otro lado de la moneda: los datos. Cuántas fotos hacen falta, cómo se etiquetan, quién valida las etiquetas, y cómo se entrena y se valida un modelo: qué es el sobreajuste y cómo se lee la gráfica de curvas. Gracias por acompañarme.
