# Guion del video 2 de 6: Qué son las imágenes

Image Bio Pro · Sesión 1 · Capacitación en video

Continúa del video 1. Empieza con la frase que lo une con el video anterior.

*3,363 palabras, unos 19.2 min de habla*

[Diapositiva · ¿Qué son las imágenes?]

> Idea central: Antes de hablar de redes hay que entender qué es una imagen para una computadora. Esa pregunta abre esta parte.

En el video anterior vimos el problema: el conteo y la medición hechos a mano consumen mucho tiempo y varían de una persona a otra. Para resolverlo, hay que empezar por lo básico. La primera pregunta que nos vamos a hacer es: ¿qué son las imágenes?

Una imagen es la categoría general. Abarca cualquier tipo de representación visual: un dibujo, una pintura, una captura, lo que sea. Una fotografía es un tipo de imagen: la que se captura con una cámara y registra la luz que llega a un sensor en un momento concreto. Toda fotografía es una imagen, pero no toda imagen es una fotografía. En microscopía todo lo que se genera se llama imagen, y por eso de aquí en adelante voy a hablar de imágenes, y en particular de imágenes digitales.

[Diapositiva · Una imagen digital es una tabla de números]

> Idea central: Para la computadora una imagen es una tabla de números, uno por píxel, de 0 (negro) a 255 (blanco). Una imagen grande son casi dos millones y medio de números.

Vamos con algo que parece muy básico y de lo que depende todo lo demás. La pregunta es: ¿qué es una imagen para una computadora?

Para la computadora, una imagen es, o sea, una tabla de números: una cuadrícula de cuadritos, los píxeles, y cada uno guarda cuánta luz tiene. En una imagen en tonos de gris, ese número es el brillo, y va de cero, que es negro, a doscientos cincuenta y cinco, que es blanco. Los números intermedios son los grises. En una imagen a color no es un número sino tres, uno para el rojo, otro para el verde y otro para el azul, y con la mezcla de los tres sale el color de ese cuadrito.

En la diapositiva tengo a la izquierda una imagen pequeña con un cuadro azul marcado, y a la derecha lo que hay dentro de ese cuadro, ampliado hasta que se ven los números. Son treinta y cinco cuadritos, siete por cinco. Fíjense en la parte de afuera: números bajos, casi negros. Y en el centro, números altos, hasta un doscientos cincuenta y cinco. Eso es lo que la computadora tiene delante cuando mira una imagen.

Una imagen real de las nuestras tiene casi dos millones y medio de cuadritos, cada uno con su número. La computadora los maneja todos a la vez sin problema, pero a un ojo humano eso no le dice nada: lo que nosotros vemos como células, la computadora lo ve como un mar de números.

Un detalle sobre esos números del cero al doscientos cincuenta y cinco: tienen una razón. Cada píxel guarda su valor en un byte, que son ocho bits, y con ocho bits se pueden representar doscientos cincuenta y seis valores distintos. Por eso el rango empieza en cero y termina en doscientos cincuenta y cinco. Con esos doscientos cincuenta y seis niveles el ojo ve un degradado suave de negro a blanco, sin escalones. En una imagen a color son tres bytes por píxel, uno por cada color.

Hagamos el ejercicio de ponernos en el lugar de la computadora. Cuando ustedes miran una imagen, reconocen formas, bordes, colores, y casi sin esfuerzo saben qué es cada cosa. La computadora no recibe nada de eso. Recibe una lista ordenada de números y una indicación de cuántos hay por fila y cuántas filas son. Con esa información reconstruye la cuadrícula.

Por eso se habla de una matriz. Una matriz es simplemente una tabla de números organizada en filas y columnas, como una hoja de cálculo. Cada celda de esa tabla es un píxel, y el valor de la celda es lo que sabemos de ese punto. En la diapositiva ven un fragmento de siete por cinco, con treinta y cinco celdas.

La computadora no tiene ninguna idea previa de lo que hay en la imagen. No sabe dónde empieza una célula ni dónde termina. Cualquier cosa que queramos que haga, contar, medir o reconocer, tiene que construirse a partir de esos números y de las relaciones entre ellos. Un píxel solo no dice nada. Lo que dice algo es cómo se comportan los números vecinos: dónde suben de golpe, dónde bajan, dónde se mantienen parecidos.

Esa idea, que lo importante son las relaciones entre píxeles vecinos, va a volver una y otra vez, y es justamente la base de cómo una red neuronal mira una imagen.

[Diapositiva · El color: tres números por píxel]

> Idea central: Una imagen a color guarda tres números por píxel, uno para el rojo, uno para el verde y uno para el azul. Un naranja intenso es mucho rojo, algo de verde y poco azul.

Hasta ahora hablamos de imágenes en tonos de gris, donde cada píxel tiene un solo número, el brillo. Pero nuestras imágenes tienen color, y el color añade una dimensión.

En una imagen a color, cada píxel guarda tres números en lugar de uno. Un número dice cuánto rojo tiene el píxel, otro cuánto verde y otro cuánto azul. Cada uno va, igual que el brillo, de cero a doscientos cincuenta y cinco. Estos tres números se llaman canales, y por eso se habla de los canales rojo, verde y azul. Mezclándolos en distintas proporciones se obtiene cualquier color que veamos en una pantalla.

Veamos un ejemplo. El naranja de una cabeza brillante podría tener doscientos cuarenta de rojo, ciento veintidós de verde y cuarenta y dos de azul. Mucho rojo, una cantidad media de verde y casi nada de azul. Si el color tuviera menos verde, por ejemplo treinta, se vería más rojo. Si tuviera más verde, por ejemplo doscientos, se vería más amarillo. Con tres números, entonces, queda descrito el color de cada píxel.

Una imagen de tres canales pesa tres veces más que una de un canal, porque guarda tres números por píxel. Y para muchas tareas, como encontrar dónde hay algo brillante, a veces basta con trabajar con el brillo, que es un solo número por píxel y se calcula combinando los tres canales.

Entonces, resumiendo: una imagen en gris es una tabla de números; una imagen a color son tres tablas del mismo tamaño apiladas, una por canal. Todo lo que se haga con una imagen se hace, finalmente, con esas tablas.

[Diapositiva · Resolución y tamaño del archivo]

> Idea central: Más píxeles significan más detalle, pero también más números que guardar. Una imagen de nuestro tamaño pesa unos siete megabytes sin comprimir.

Hablemos de la resolución, que es una palabra que se usa mucho y se entiende a medias. La resolución de una imagen digital es cuántos píxeles tiene, normalmente expresado como ancho por alto.

Una imagen típica de las que usamos mide mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Si multiplicamos, nos da un poco menos de dos millones y medio de píxeles, que algunas personas llaman dos punto cinco megapíxeles.

¿Qué cambia con la resolución? El detalle. Cada píxel representa un pedacito de lo que se fotografió, y mientras más píxeles hay, más pequeño es ese pedacito. Con pocos píxeles, la forma de una célula se describe con pocos cuadritos y su borde se ve escalonado. Con muchos píxeles, el borde se describe con más cuidado y la medida es más precisa. Por eso, cuando lo que importa es medir, conviene que las imágenes tengan buena resolución.

Pero más píxeles también significa más datos. Hagamos la cuenta del peso. Cada píxel de una imagen a color guarda tres números, y cada número ocupa un byte. Entonces, dos millones y medio de píxeles por tres bytes son más o menos siete millones y medio de bytes, que son unos siete megabytes. Eso es lo que pesa una de nuestras imágenes cuando se guarda sin comprimir. Si fuera en gris, pesaría la tercera parte.

Esto explica un fenómeno que seguramente han notado: las imágenes grandes tardan más en subirse, en abrirse y en procesarse. Para la computadora, procesar una imagen es recorrer esos millones de números, y cada operación que se haga por píxel se multiplica por dos millones y medio. Más adelante veremos cómo el sistema se organiza para manejar eso sin que la espera sea excesiva.

[Diapositiva · Una célula brillante son números altos]

> Idea central: En fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. Medir su área es contar cuántos píxeles ocupa.

Ahora pensemos en una imagen de fluorescencia. ¿Cómo se ve una célula dentro de esa tabla de números? Como una zona de números altos sobre un fondo de números bajos. La célula brilla, así que sus píxeles tienen valores grandes, y el fondo oscuro tiene valores pequeños. La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

Esto también nos dice cómo se mide el tamaño. En la diapositiva les muestro una célula pequeñita dibujada con números. Los doce cuadritos más brillantes, los que tienen el borde marcado, son la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles. Medir el área de una célula es contar cuántos píxeles ocupa. En una imagen real serán cientos de píxeles por célula, pero la idea es exactamente la misma. Más adelante, con la escala del sitio, esos píxeles se convierten en micras.

Una pregunta que seguramente se están haciendo: ¿y no bastaría con decir que todo píxel por encima de cierto valor es célula? Es una idea natural y es, de hecho, el primer intento que se suele hacer. Se llama umbralización: se elige un umbral y todo lo que lo supera se considera objeto. Funciona razonablemente cuando las células están separadas y bien iluminadas, pero falla cuando se tocan, cuando hay manchas brillantes que no son células, o cuando el brillo cambia de una imagen a otra. Más adelante, en esta misma sesión, vemos por qué no basta y cómo una red neuronal retoma esa idea y suma otros factores. Hoy les dejo solo la intuición de que la computadora, en el fondo, está comparando números.

Esta idea tiene una consecuencia muy práctica: separar lo que nos interesa del fondo se puede plantear como una pregunta sobre números. ¿Dónde están los números altos? ¿Dónde están los bajos? ¿Dónde hay un cambio brusco de uno a otro? El borde de una célula es, en la tabla, el lugar donde los valores pasan de bajos a altos en muy pocos píxeles.

Y de ahí se entiende por qué el borde importa tanto. Si el borde es nítido, en la tabla se ve un salto claro, y trazar el contorno es sencillo. Si el borde está borroso, los valores suben poco a poco, y es más difícil decir dónde termina exactamente la célula. Esa diferencia se va a notar enseguida en los formatos de archivo y en la medida.

[Diapositiva · El histograma: contar los brillos]

> Idea central: Un histograma cuenta cuántos píxeles hay de cada nivel de brillo. En fluorescencia, casi todos son oscuros y unos pocos son muy brillantes, y esa forma explica por qué un umbral parece funcionar.

Hay una forma muy útil de resumir una imagen, que se llama histograma. Es una gráfica que cuenta cuántos píxeles hay de cada nivel de brillo. En el eje horizontal van los valores, de cero a doscientos cincuenta y cinco, y en el vertical, cuántos píxeles tienen ese valor.

Para construirlo, se recorre la imagen píxel por píxel, y cada vez que se encuentra un valor, se suma uno a la columna correspondiente. Al final, las columnas altas son los valores más comunes y las bajas los poco comunes.

Veamos cómo es el histograma de una imagen de fluorescencia. Recordemos cómo es la imagen: casi todo es fondo oscuro, y unas pocas zonas son células brillantes. Entonces, el histograma tiene una columna altísima en los valores bajos, porque la inmensa mayoría de los píxeles son oscuros, y después una cola larga y baja hacia los valores altos, que corresponden a las células.

Esa forma explica por qué la idea del umbral parece funcionar. Si en el histograma hay una zona de valores bajos con muchísimos píxeles y una zona de valores altos con unos pocos, se podría trazar una línea en medio: de ahí hacia la izquierda es fondo, de ahí hacia la derecha son células.

Pero también explica por qué falla. Las células no son del mismo brillo: unas son más intensas que otras. Hay colas, que brillan menos que las cabezas pero más que el fondo. Hay manchas difusas con valores intermedios. Y los bordes de las células, donde el brillo baja poco a poco, producen valores intermedios que no pertenecen claramente a ningún grupo. En el histograma, todo eso rellena el espacio entre el fondo y las células, y no hay una línea limpia donde cortar.

Además, el histograma de una imagen puede ser distinto del de la siguiente, si cambió la iluminación o la exposición. Un umbral elegido para una puede no servir para la otra.

Esta es una herramienta que usaremos más adelante para entender qué ve la computadora, y es una buena manera de comprobar, antes de cualquier análisis, si una imagen está bien expuesta.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

> Idea central: BMP, PNG y TIFF guardan la imagen tal cual; JPG la comprime y puede mover los bordes, y con ellos el área. Conviene trabajar con los archivos originales del microscopio.

Un tema práctico: los formatos de archivo. No todos guardan la imagen igual. BMP, PNG y TIFF guardan la imagen tal cual. JPG la comprime para que pese menos, y al comprimirla puede mover los bordes de las células. Para medir, eso importa.

En la diapositiva tengo la misma célula dos veces: a la izquierda con el borde nítido y a la derecha con el borde difuminado y con bloques raros, que es lo que pasa con la compresión. ¿Por qué importa? Porque si el borde se difumina, el contorno cambia, y si el contorno cambia, cambia el área, y entonces cambian los números que nos interesan.

Una imagen de las que usamos, guardada como BMP, pesa unos siete megabytes, como vimos hace un momento. El mismo contenido en JPG puede pesar una fracción de eso, y ahí está su atractivo: ocupa menos. Pero ese ahorro se paga con fidelidad, y para medir, la fidelidad es justo lo que necesitamos.

Veámoslo con un poco más de detalle, porque este es uno de los errores más comunes y más fáciles de evitar.

La compresión es una forma de guardar la misma imagen en menos espacio. Hay dos grandes familias. La compresión sin pérdida guarda la imagen de forma más compacta, pero al abrirla se recupera exactamente cada número, sin cambiar ninguno. PNG y TIFF, bien usados, funcionan así. Y BMP, en la práctica, ni siquiera comprime: guarda todos los números tal cual.

La compresión con pérdida, que es la de JPG, hace otra cosa. Parte de la idea de que el ojo humano no nota ciertos cambios pequeños, y aprovecha eso para descartar información. Divide la imagen en bloques y simplifica cada bloque. El resultado ocupa mucho menos espacio, pero los números que se recuperan al abrir la imagen ya no son los originales, solo se parecen.

Para una fotografía de un paisaje, eso casi no importa. Para una imagen donde vamos a medir el borde de una célula, sí importa, porque la simplificación por bloques tiende a mover y a suavizar justo los bordes. Y hay un detalle que conviene recordar: cada vez que una imagen se guarda en JPG, se pierde un poco más. Si pasa por varias aplicaciones, cada una comprimiéndola otra vez, el daño se acumula.

Por eso la recomendación es sencilla. Trabajar con el archivo original que genera el microscopio o la cámara, sin pasarlo por aplicaciones de mensajería ni de redes sociales, que casi siempre lo comprimen para ahorrar espacio. Si necesitan reducir el peso, lo ideal es un formato sin pérdida. Y si solo tienen una versión en JPG, el sitio la acepta, pero lo avisa, porque la medida puede cambiar ligeramente.

[Diapositiva · Aumentos y micras]

> Idea central: Los aumentos del microscopio, 40X o 100X, cambian cuánto mide en la realidad cada píxel. Una micra es la milésima parte de un milímetro.

Pasemos ahora a una pregunta menos trivial de lo que parece: ¿cuánto mide una célula? Para contestarla necesitamos una unidad y una forma de pasar de píxeles a esa unidad.

La unidad natural es la micra, o micrómetro. Una micra es la milésima parte de un milímetro. Un cabello humano mide unas decenas de micras de grosor, y una cabeza de espermatozoide mide unas pocas micras. A esa escala, los milímetros resultan demasiado grandes, y por eso se usan las micras.

El problema es que una imagen digital no sabe nada de micras. Solo sabe de píxeles. Y cuántas micras representa un píxel depende de cómo se tomó la imagen. Un factor es el aumento del microscopio. Si se usa un aumento de cuarenta X, cada píxel cubre un pedazo de la muestra; si se usa uno de cien X, ese mismo píxel cubre un pedazo más pequeño, porque el objeto se ve más grande. Otros factores son el tipo de cámara y el tamaño de sus sensores.

Eso significa que dos imágenes que miden lo mismo en píxeles pueden representar tamaños reales muy distintos. Si comparáramos sus medidas en píxeles sin más, estaríamos comparando cosas que no son comparables.

Y el archivo no guarda este dato. Las imágenes que usamos no traen escrito cuánto mide cada píxel. Entonces hay dos caminos. Uno es suponer un valor y no decir nada, y el otro es declarar una escala y repetirla en todos los resultados. Nuestro sistema toma el segundo camino, y eso es lo que vemos en la siguiente diapositiva.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

> Idea central: Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno. El sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, y la declara en cada resultado.

Para cerrar este bloque, la escala. Una imagen sabe cuántos píxeles mide, pero no cuántas micras es cada uno, porque los archivos no guardan ese dato. Y si queremos comparar imágenes entre sí, hay que ponerlas en una misma medida.

Por eso el sitio aplica la misma escala a todas. Es de sesenta píxeles por micra, y cada resultado dice cuál se usó. La imagen marcada trae una regla de trescientos píxeles que equivalen a cinco micras. Cómo se define esa escala no lo voy a explicar hoy; lo vemos en la tercera sesión, cuando revisemos el sistema por dentro.

Veámoslo con números. Si sesenta píxeles son una micra, entonces un largo de sesenta píxeles es una micra de largo, y un largo de trescientos píxeles son cinco micras, que es justo la regla que va dibujada en la imagen. Con las áreas hay un paso más. Un área se mide en unidades cuadradas, así que una micra cuadrada son sesenta por sesenta píxeles, es decir, tres mil seiscientos píxeles. Si una célula ocupa tres mil seiscientos píxeles, su área es de una micra cuadrada; si ocupa la mitad, de media micra cuadrada. Por eso, en el sitio, las áreas en micras cuadradas pueden salir como números pequeños.

Esta decisión importa. Imaginen que el sitio no declarara la escala y que una persona midiera con él imágenes de cuarenta X y otra de cien X. Las dos obtendrían áreas en micras cuadradas, pero las de una estarían infladas o reducidas respecto de las de la otra, y nadie se enteraría. Los números parecerían precisos y no lo serían.

Con una escala única, cualquier imagen se interpreta con la misma relación entre píxeles y micras, y eso permite comparar entre imágenes y entre personas. Además, como cada resultado la declara, quien lee un número sabe con qué regla se calculó. Si en el futuro se decide usar otra escala, o una por cada aumento, se puede cambiar y todos sabrán que cambió.

Un último ejemplo: si una cabeza ocupa siete mil doscientos píxeles, su área es de dos micras cuadradas, y si ocupa mil ochocientos, media micra cuadrada. Con cuentas así, que cualquiera puede repetir con una calculadora, se pasa de lo que la computadora ve a lo que el investigador necesita.

[Diapositiva · Dos tipos de imagen, dos modelos]

> Idea central: Las imágenes de fluorescencia y las de fondo claro se ven distintas, y por eso hay un modelo entrenado para cada tipo.

Algo que mencionamos de pasada y que merece su propio momento: trabajamos con dos tipos de imágenes, y para cada una hay un modelo.

Las de fluorescencia son las que hemos visto: células brillantes sobre un fondo oscuro. Las de fondo claro son lo contrario: la muestra se ve oscura, o de un color, sobre un fondo iluminado. Las dos son imágenes digitales, tablas de números, pero los números se comportan de forma muy distinta. En una, lo que buscamos son valores altos rodeados de valores bajos. En la otra, la situación es la contraria.

Podría pensarse que basta con una sola red que lo aprenda todo. En principio se puede, pero tiene un costo. Una red que debe resolver dos problemas muy distintos necesita más ejemplos de cada uno y más capacidad, y suele rendir peor en ambos que dos redes especializadas. Por eso se entrenó un modelo para cada caso.

Esto tiene una consecuencia práctica para quien usa el sitio: hay que subir cada imagen al tipo que le corresponde, y el sitio elige el modelo adecuado. Más adelante, cuando veamos el sistema funcionando, lo vamos a ver en acción.

Un modelo sirve para el tipo de imágenes con las que se entrenó. Cuando cambian las condiciones, como otra tinción, otro microscopio o un tipo de célula distinto, hay que preguntarse si el modelo sigue siendo adecuado, y a veces la respuesta es que se necesita otro. En el siguiente video vemos dónde ya vive la inteligencia artificial y qué palabras vamos a usar.
