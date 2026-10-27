# Guion del módulo 2, video 1 de 4: Cómo ve una imagen una red convolucional (versión natural)

BioImage-Repro UAM · Módulo 2 · Capacitación en video

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el módulo anterior.

[Diapositiva 1 · Cómo ve una imagen una red convolucional]

> Idea central: En el módulo 1 vimos que una imagen es una tabla de números y que una red aprende ajustando pesos. Este video junta las dos ideas: cómo mira una imagen una red convolucional. El módulo 2 tiene cuatro videos.

En el módulo 1 vimos dos cosas por separado. Una imagen es una tabla de números. Y una red neuronal es una cadena de capas que aprende ajustando pesos. En este video juntamos las dos: cómo mira una imagen una red.

Este es el módulo 2. Sigue siendo teoría, pero con más detalle que el primero. Son cuatro videos. En este vemos cómo mira una imagen una red convolucional, que es el tipo de red en el que se apoya nuestro sistema. En el segundo veremos Mask R-CNN, la red completa. En el tercero, cómo se aprovecha una red que ya fue entrenada para otra cosa. Y en el cuarto, los datos, el entrenamiento y cómo se sabe si un modelo funciona. Conviene verlos en orden, porque cada uno usa lo del anterior.

En pantalla hay un pedazo de una foto de fluorescencia, de 512 por 512 píxeles. Es el tamaño de recorte con el que trabaja el modelo de fluorescencia. En una esquina hay un cuadro diminuto, marcado en naranja, y a un lado aparece ampliado. Son nueve píxeles: tres por tres. Casi todo lo que sigue consiste en lo que se hace con una ventana así.

[Diapositiva 2 · Conectar todo con todo no funciona]

> Idea central: Conectar cada neurona con todos los píxeles exige una cantidad enorme de pesos y trata a los píxeles como si no tuvieran lugar. En una imagen importa la vecindad, y un mismo patrón puede aparecer en cualquier parte.

En el módulo 1, las neuronas recibían todas las entradas, cada una con su peso. Con dos entradas eso es cómodo. Con una imagen, no.

Pensemos en ese pedazo de 512 por 512. Son más de doscientos sesenta mil píxeles. Una sola neurona conectada a todos necesitaría un peso por cada píxel. Más de doscientos sesenta mil pesos, para una neurona.

Ahora imaginemos una capa que devuelva algo del mismo tamaño que la imagen. Una neurona por cada punto de salida. Harían falta casi setenta mil millones de pesos en una sola capa. En pantalla están las tres cifras, una debajo de otra, con un dibujo de un punto de salida conectado a todos los píxeles de entrada.

Hay un problema más de fondo. Conectar todo con todo no toma en cuenta dónde está cada píxel. Para esa neurona, el píxel de la esquina y su vecino de al lado están tan lejos o tan cerca como el de la esquina opuesta. Y en una imagen lo que cuenta es la vecindad. Un grupo de píxeles brillantes juntos puede ser una cabeza. Un píxel brillante solo, rodeado de oscuridad, es ruido.

Y está la repetición. Una cabeza en una esquina y una cabeza en el centro son lo mismo. Pero con esta forma de conectar, cada lugar tendría que aprender a reconocerla por separado, con sus propios pesos. Hace falta otra idea.

[Diapositiva 3 · La idea: un detector pequeño que recorre la imagen]

> Idea central: En lugar de una neurona que mira toda la imagen, un detector pequeño que mira una ventana y se recorre por toda la imagen. Es el filtro, y recorrerlo es la convolución.

La idea es buscar patrones pequeños y repetirlos por toda la imagen. En lugar de una neurona que mira todo, usamos un detector que mira una ventana de unos pocos píxeles. Y esa misma ventana se recorre por la imagen entera, de izquierda a derecha y luego fila por fila. En pantalla se ve el dibujo: una ventana pequeña, en tres posiciones sucesivas, sobre una imagen.

La ventana es la misma en todas partes. Si sirve para detectar un borde en una esquina, sirve para detectarlo en el centro. Eso trae dos ventajas. Se necesitan muy pocos pesos, porque son los de una sola ventana. Y lo que se aprende en un lugar vale para todos los demás.

A ese detector pequeño se le llama filtro. Y a la operación de recorrerlo por la imagen, convolución. De ahí viene el nombre de las redes convolucionales. La palabra suena complicada, pero lo que ocurre es sencillo. Lo vamos a hacer a mano.

[Diapositiva 4 · El filtro de tres por tres]

> Idea central: Un filtro es una tabla pequeña de pesos, por ejemplo de tres por tres, o sea nueve pesos. Al ponerlo sobre un pedazo de imagen se multiplica y se suma, igual que en una neurona.

Un filtro es una tabla pequeña de pesos. El más común mide tres por tres, así que tiene nueve pesos. El de la pantalla tiene menos uno, cero y uno en cada una de sus tres filas. La columna de la izquierda vale menos uno, la del centro vale cero y la de la derecha vale uno. Los negativos aparecen en azul, el cero en gris y los positivos en naranja.

Para entender qué hace, usamos la cuenta que ya conocemos de las neuronas: multiplicar cada entrada por su peso y sumar. Imaginemos el filtro como una neurona de nueve entradas. Esas entradas son los nueve píxeles que quedan debajo de él.

Con pesos negativos a la izquierda y positivos a la derecha, la cuenta resta lo que hay a la izquierda y suma lo que hay a la derecha. Si los dos lados valen lo mismo, la resta da cero. Si la derecha es más brillante que la izquierda, da un número grande y positivo. Este filtro responde entonces a un cambio de brillo de izquierda a derecha. Es decir, a un borde vertical.

[Diapositiva 5 · La cuenta a mano]

> Idea central: Un parche de tres filas iguales, cero, cero y nueve, por el filtro da veintisiete: hay un cambio de oscuro a claro. Un parche parejo da cero.

Hagamos la cuenta con un pedazo de imagen. Los píxeles tienen valores de cero a nueve. Debajo del filtro hay tres filas iguales: cero, cero, nueve. A la izquierda y al centro está oscuro, y a la derecha hay un píxel brillante. En pantalla el parche aparece junto al filtro, con cada producto escrito en su casilla.

Primera fila. Menos uno por cero, cero. Cero por cero, cero. Uno por nueve, nueve. La fila aporta nueve. Las otras dos filas son iguales y aportan nueve cada una. Sumamos las tres y da veintisiete.

Ese veintisiete es el resultado del filtro en ese lugar. Un número grande dice que aquí hay un cambio de oscuro a claro, de izquierda a derecha.

Y si el parche fuera parejo, con nueve en todas partes, cada fila daría menos nueve, más cero, más nueve. El total sería cero. Cero quiere decir que aquí no hay ningún borde.

[Diapositiva 6 · Deslizar el filtro: el mapa de características]

> Idea central: Al recorrer el filtro por toda la imagen se obtiene una tabla nueva, el mapa de características, que dice en qué lugares aparece el patrón del filtro.

Ahora movemos el filtro. En pantalla hay una imagen de cinco por cinco píxeles. Las dos columnas de la izquierda valen cero y las tres de la derecha valen nueve. Es una imagen sencilla, con un borde vertical.

Ponemos el filtro en la esquina superior izquierda y hacemos la cuenta. Veintisiete, la misma de hace un momento. Lo movemos un píxel a la derecha. Ahora debajo del filtro hay cero, nueve y nueve en cada fila, y la cuenta vuelve a dar veintisiete, porque el borde sigue dentro de la ventana. Un píxel más a la derecha, y el filtro solo ve nueves. El resultado es cero.

Al terminar la fila, bajamos un píxel y repetimos. Como las filas de esta imagen son todas iguales, cada fila del resultado sale igual. Al final tenemos una tabla de tres por tres: veintisiete, veintisiete y cero, repetido tres veces.

Esa tabla se llama mapa de características. Es otra imagen, más pequeña. Y cada número dice cuánto aparece el patrón del filtro en ese lugar. Aquí nos dice dónde hay un borde vertical: valores altos donde lo hay, y cero donde el brillo es parejo.

[Diapositiva 7 · Paso y relleno]

> Idea central: El paso es cuántos píxeles se mueve el filtro cada vez y el relleno es el borde de ceros que se agrega alrededor. Con una imagen de cinco por cinco y un filtro de tres por tres: paso uno da tres por tres, paso dos da dos por dos y relleno de uno da cinco por cinco.

Hay dos ajustes que cambian el tamaño del mapa. El primero es el paso: cuántos píxeles se mueve el filtro cada vez. Con paso uno, como hicimos, una imagen de cinco por cinco con un filtro de tres por tres da un mapa de tres por tres. Con paso dos, el filtro salta de dos en dos y el mapa baja a dos por dos. Un paso más grande da un mapa más pequeño y menos trabajo.

El segundo es el relleno. El filtro necesita nueve píxeles debajo, así que no puede centrarse en los de la orilla. Por eso el mapa siempre sale más chico que la imagen. Para evitarlo, se rodea la imagen con una fila y una columna de ceros. Con ese relleno de uno, la misma imagen de cinco por cinco da un mapa de cinco por cinco. En pantalla están las tres versiones, lado a lado, cada una con su tamaño.

No hace falta memorizar la fórmula. Basta recordar que el paso reduce y el relleno conserva el tamaño. La red de nuestro sistema usa las dos cosas, y lo veremos cuando lleguemos a ella.

[Diapositiva 8 · Qué detecta un filtro en una foto real]

> Idea central: Con filtros de tres por tres se separan las formas del fondo y se ve en qué dirección van sus bordes. También responden las fibras y las manchas, lo que explica algunos errores del sistema.

Veamos qué hace un filtro de verdad. En pantalla hay un pedazo de una foto de fluorescencia. A su lado está el resultado de aplicarle el filtro que acabamos de ver. Y más a la derecha, el de ese mismo filtro girado, que busca bordes horizontales. Los dos resultados se calcularon con la cuenta que hicimos a mano, repetida en cada píxel de la foto.

Con el primero se iluminan los bordes donde el brillo cambia de izquierda a derecha. Con el segundo, los bordes donde cambia de arriba hacia abajo. Las zonas de fondo parejo quedan oscuras. Es el cero de la cuenta anterior. Con dos filtros de nueve pesos cada uno ya se separan las formas del fondo, y se sabe en qué dirección van sus contornos.

También se ve una limitación. El filtro responde a cualquier borde, sea de una cabeza o de otra cosa. Las fibras, el ruido y las manchas de la foto también se iluminan. Por eso un solo filtro no basta. Y por eso, en fluorescencia, a veces una fibra se confunde con un espermatozoide. Es algo que veremos más adelante.

Nada de esto es todavía una detección. Es el primer paso: convertir la foto en tablas que ponen en evidencia ciertos patrones.

[Diapositiva 9 · Otros filtros: suavizar y resaltar manchas]

> Idea central: Cambiando los pesos cambia lo que detecta el filtro. Uno con los nueve pesos iguales promedia y suaviza el ruido, y otro con un centro positivo y alrededor negativo resalta puntos y manchas más brillantes que su entorno.

Cambiando los pesos, cambia lo que el filtro detecta. Veamos dos más, con la misma cuenta.

El primero tiene los nueve pesos iguales: un noveno cada uno. Multiplicar por un noveno y sumar es sacar el promedio de los nueve píxeles. En pantalla hay un parche de tres por tres con ceros en todas partes y un nueve en el centro. Es como un punto de ruido brillante y aislado. El promedio da uno. El nueve se volvió uno: el ruido se atenuó. Este filtro suaviza la imagen.

El segundo tiene un ocho en el centro y menos uno en cada uno de los ocho vecinos. Con un parche parejo, de nueve en todas partes, la cuenta es ocho por nueve, setenta y dos, menos ocho veces nueve, otros setenta y dos. Da cero. Con el parche del punto aislado, el centro aporta setenta y dos y los vecinos no restan nada. Da setenta y dos. Este filtro responde a los puntos y a las manchas más brillantes que lo que las rodea. Y no responde al fondo parejo.

La idea es esa: nueve pesos distintos, un detector distinto. Una cabeza de espermatozoide, en fluorescencia, es una mancha alargada, más brillante que su entorno. Así que filtros de este tipo y de bordes son una buena forma de empezar a verla.

[Diapositiva 10 · Muchos filtros, muchos mapas]

> Idea central: Una capa usa muchos filtros a la vez. Cada uno produce su mapa, y la pila de mapas, cada uno llamado canal, es la entrada de la capa siguiente.

Un solo filtro busca un solo patrón. Una red usa muchos a la vez. Cada filtro produce su propio mapa, y cada mapa responde a algo distinto. Uno a bordes verticales, otro a horizontales, otro a diagonales, otro a manchas brillantes, otro a un cambio suave de brillo. En pantalla hay una imagen a la izquierda, varios filtros en el centro y los mapas que resultan a la derecha.

Los mapas se apilan como hojas transparentes, y esa pila es la salida de la capa. Cada hoja de la pila se llama canal. Ya conocemos esa palabra. Una imagen en color tiene tres: rojo, verde y azul, como vimos en el módulo 1. Cuando la entrada tiene tres canales, cada filtro también tiene tres capas de pesos, una por canal. Y suma las tres cuentas en un solo número.

La capa siguiente recibe esa pila como entrada. Para ella, los mapas ya no son píxeles de una foto. Cada punto de cada mapa dice qué tan presente está un patrón en ese lugar. Y la nueva capa busca combinaciones de esos patrones.

[Diapositiva 11 · La activación después del filtro]

> Idea central: Después de cada filtro se aplica la activación del módulo 1: lo positivo pasa y lo negativo se vuelve cero. Sin esa pequeña no linealidad, apilar capas no aportaría nada.

Después de cada filtro viene una pieza que ya conocemos del módulo 1: la activación. Si el resultado es positivo, pasa. Si es negativo, se pone en cero. En pantalla hay un mapa con números positivos y negativos, y a su derecha, el mismo mapa ya con la activación.

Veamos por qué importa aquí. Pasamos el mismo filtro sobre un borde que va de claro a oscuro. La cuenta da menos veintisiete. Es una respuesta válida, porque hay un borde, pero en el sentido contrario. Con la activación, ese menos veintisiete pasa a cero. Y en el mapa solo quedan los bordes que van de oscuro a claro. Para el otro sentido, la red tiene otros filtros.

Sin esa activación, apilar capas no serviría de mucho. Una cuenta de multiplicar y sumar, seguida de otra cuenta de multiplicar y sumar, equivale a una sola. La pequeña no linealidad de dejar en cero lo negativo es lo que permite que cada capa construya algo nuevo sobre la anterior.

[Diapositiva 12 · Reducir para ver más grande]

> Idea central: Las redes reducen el tamaño de los mapas, por ejemplo tomando el máximo de cada bloque. Así hay menos números y cada punto resume una zona mayor de la imagen.

Las redes convolucionales reducen el tamaño de los mapas cada cierto número de capas. Una forma de hacerlo es tomar el máximo de cada bloque. En pantalla hay un mapa de cuatro por cuatro, dividido en cuatro bloques de dos por dos. De cada bloque se queda el valor más alto: ocho, dos, dos y siete. El mapa de cuatro por cuatro pasa a uno de dos por dos.

Reducir sirve para dos cosas. Primero, hay menos números, así que se hace menos trabajo. Segundo, cada punto del mapa pasa a representar una zona más grande de la imagen original. Los filtros siguientes, con el mismo tamaño de tres por tres, miran entonces un pedazo mucho mayor de la foto. Se pierde precisión sobre el lugar exacto, a cambio de ver el panorama.

Esta reducción por máximo tiene nombre en inglés: max pooling. La misma reducción se consigue también con un paso de dos, como vimos antes. En la red que usamos se combinan las dos maneras.

[Diapositiva 13 · Capas apiladas: de bordes a objetos]

> Idea central: Con capas apiladas, cada una ve una zona mayor de la imagen y combina lo que encontró la anterior: bordes, curvas y esquinas, partes y objetos. Es la escalera de la casa del módulo 1.

Ahora apilamos las capas. La primera mira ventanas de tres por tres y encuentra bordes y manchas. La segunda también usa ventanas de tres por tres, pero sobre los mapas de la primera. Cada punto de esos mapas ya resume una zona de tres por tres píxeles. Así que una ventana de tres por tres sobre ellos abarca, en la imagen original, una zona de cinco por cinco. Con una tercera capa, de siete por siete. En pantalla se ven tres cuadros, cada uno más grande, marcados sobre la misma foto. Con las reducciones que vimos, esa zona crece todavía más rápido.

En una red real esto se organiza en bloques. Filtros, activación y, a veces, una reducción. Y otra vez filtros, activación y reducción. Una red como la nuestra repite ese esquema decenas de veces, y cada vuelta trabaja sobre lo que dejó la anterior.

Por eso lo que detecta cada capa es más complejo que lo de la anterior. La primera encuentra bordes. La siguiente los combina en curvas y esquinas. Las más profundas combinan curvas en formas más grandes. En una red entrenada para este problema, esas formas suelen corresponder a partes de un espermatozoide y a la cabeza completa. Es la misma escalera de la casa del módulo 1, ahora con imágenes: líneas, partes y objeto.

Nadie escribe a mano qué debe detectar cada capa. Cada una termina detectando lo que resulta útil para la tarea, y lo encuentra el entrenamiento.

[Diapositiva 14 · Los filtros se aprenden]

> Idea central: Los pesos de cada filtro son parámetros de la red, como cualquier peso del módulo 1. Empiezan al azar y el entrenamiento los ajusta. Un filtro tiene nueve pesos y se reutiliza en toda la imagen.

Hasta aquí usamos un filtro que escogimos nosotros. En una red convolucional nadie lo escoge. Los nueve pesos de cada filtro son pesos de la red, igual que los de cualquier neurona del módulo 1. Al empezar son valores al azar. Y el entrenamiento los ajusta con el mecanismo de siempre. Se compara la respuesta con la correcta, se calcula la pérdida, se calcula hacia dónde mover cada peso y se mueve un poco.

En pantalla están los 64 filtros de la primera capa de nuestro modelo. Cada cuadrito es un filtro de siete por siete píxeles. Se reconocen muchos detectores de bordes, con distintas orientaciones, y otros de manchas. Los colores aparecen porque la red original se preparó con fotos a color, y cada filtro tiene un juego de pesos por cada canal. Nadie dibujó esos filtros. Salieron del entrenamiento.

Volvamos a la cuenta del principio. Un peso por píxel daba más de doscientos sesenta mil pesos para una sola neurona. Aquí el filtro tiene nueve, y se reutiliza en todos los lugares de la imagen. Esa es la razón por la que estas redes son manejables con imágenes. Pesos compartidos significan muchos menos números que aprender, y un patrón aprendido en un lugar sirve en todos los demás.

Un ejemplo con números. Una capa de 64 filtros de tres por tres, que reciben 64 mapas, tiene 36,864 pesos. Unos treinta y siete mil. Comparémoslos con los casi setenta mil millones de la capa conectada a todo. Esa diferencia es la que permite que una red con decenas de capas quepa en un archivo de 176 megabytes.

[Diapositiva 15 · ResNet50: la base de nuestra red]

> Idea central: La red completa del sistema, Mask R-CNN, empieza con una red convolucional llamada ResNet50. A lo largo de sus cuatro bloques el mapa se reduce de 512 a 16 por lado y los filtros suben de 256 a 2048. Es más de la mitad de los pesos del modelo.

La red que usa el sistema, Mask R-CNN, empieza con una red convolucional que se llama ResNet50. El nombre viene de sus 50 capas. Su primera capa tiene 64 filtros de siete por siete, con tres canales. Son nueve mil cuatrocientos ocho pesos, y avanza con paso dos. Ya desde el primer paso, la imagen se reduce a la mitad por lado. Y una reducción por máximo la baja otra vez a la mitad.

Después vienen cuatro bloques de capas. En pantalla hay una tabla con lo que sale de cada uno. El primero entrega 256 mapas de 128 por 128. El segundo, 512 mapas de 64 por 64. El tercero, 1,024 mapas de 32 por 32. Y el cuarto, 2,048 mapas de 16 por 16. Cada bloque tiene menos píxeles por mapa y más mapas. En el último, cada punto de un mapa resume una zona de unos 32 por 32 píxeles de la foto original.

Esa progresión es la misma escalera de antes. En los primeros bloques hay pocos mapas, grandes y con patrones sencillos. En los últimos hay muchos mapas, pequeños y con patrones más abstractos. Los mapas de cada bloque se conservan, y en el siguiente video veremos cómo se aprovechan.

Esta base es la parte más grande de la red completa. Unos veintitrés millones y medio de pesos, más de la mitad de los casi cuarenta y cuatro millones que tiene el modelo. Las redes muy profundas son difíciles de entrenar. ResNet usa conexiones que dejan pasar la información de una capa a otra, saltándose varias, y eso ayuda a que el entrenamiento funcione. Para nosotros basta con saber que están ahí.

Un detalle de nuestro problema. En fluorescencia el color no importa. Así que antes de entrar a la red, cada píxel se convierte en un solo valor de brillo: el más alto entre rojo, verde y azul. Como la red espera tres canales, ese brillo se repite en los tres. Así la misma red funciona con tinciones de distinto color.

[Diapositiva 16 · Lo que sale y lo que falta]

> Idea central: La parte convolucional entrega mapas de características, no un conteo, ni cajas, ni contornos. Falta otra parte que proponga dónde hay objetos, los clasifique y dibuje su forma, y eso es Mask R-CNN.

Conviene ser precisos sobre lo que sale de esta parte. La red convolucional entrega una pila de mapas de características. No entrega un conteo, ni cajas, ni contornos. Cada punto de cada mapa dice qué tan presente está cierto patrón en cierto lugar, y nada más. En pantalla, a la izquierda está el pedazo de foto de entrada, y a la derecha, algunos de esos mapas.

Para pasar de ahí a decir que en este lugar hay un espermatozoide y que este es su contorno, hace falta otra parte. Esa parte toma los mapas, propone dónde puede haber objetos, decide cuáles lo son y dibuja la forma de cada uno. Es lo que convierte a la red en una Mask R-CNN.

Lo bueno de esta división es que la parte convolucional es general. Sirve para encontrar patrones en cualquier imagen, y de ahí sale la posibilidad de reutilizar una red ya entrenada, que es el tema del tercer video.

[Diapositiva 17 · Lo que vimos y lo que sigue]

> Idea central: Vimos por qué no se conecta todo con todo, cómo un filtro recorre la imagen y produce un mapa, cómo se ajusta su tamaño, por qué hay activación y reducción, y que los filtros son pesos que se aprenden y se comparten. En el siguiente video, Mask R-CNN.

Para cerrar, un resumen. Vimos por qué conectar todos los píxeles con todas las neuronas no es práctico. Vimos cómo un filtro de tres por tres recorre la imagen y produce un mapa de características, y cómo el paso y el relleno cambian el tamaño de ese mapa. Vimos la activación, que deja en cero lo negativo, y la reducción, que hace que cada punto resuma una zona mayor. Vimos cómo, al apilar capas, se pasa de bordes a formas y de formas a objetos. Y vimos que los filtros son pesos que el entrenamiento aprende y que se comparten por toda la imagen.

En el siguiente video vemos Mask R-CNN: cómo se usan esos mapas de características para encontrar cada espermatozoide, encuadrarlo y dibujar su contorno. Gracias por acompañarme.
