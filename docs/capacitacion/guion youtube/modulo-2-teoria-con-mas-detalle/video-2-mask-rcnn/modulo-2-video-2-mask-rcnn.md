# Guion del módulo 2, video 2 de 4: Mask R-CNN, la red completa

BioImage-Repro UAM · Módulo 2 · Capacitación en video

Continúa del video anterior. Empieza con la frase que lo une con el video anterior.

*3,412 palabras, unos 19.5 min de habla*

[Diapositiva 1 · Mask R-CNN, la red completa]

> Idea central: El video anterior terminó en mapas de características, que no dicen dónde hay un espermatozoide. Mask R-CNN usa esos mapas para encontrar cada espermatozoide, encuadrarlo y dibujar su contorno, uno por uno. A eso se le llama segmentación por instancias.

El video anterior terminó con una pila de mapas de características: tablas que dicen qué tan presente está cada patrón en cada lugar de la foto. Esos mapas todavía no dicen dónde hay un espermatozoide ni cuántos son. En este video vemos cómo se usan para llegar a eso.

Lo que se le pide a nuestra red son tres cosas por cada espermatozoide: encontrarlo, encuadrarlo en una caja y dibujar su contorno. Y se le pide para cada uno por separado, no para la foto completa. Eso se llama segmentación por instancias. En pantalla hay una foto de fluorescencia con tres espermatozoides, cada uno con su caja y con su contorno de un color distinto.

El nombre de la red tiene dos partes. Mask quiere decir máscara: el contorno relleno de cada objeto. R-CNN quiere decir red convolucional con regiones, y describe la estrategia: proponer regiones de la imagen y revisar cada una con una red convolucional. Las dos partes se entienden mejor viendo cómo se llegó hasta aquí.

[Diapositiva 2 · De dónde viene]

> Idea central: Mask R-CNN es la cuarta de una serie de redes: R-CNN, Fast R-CNN, Faster R-CNN y Mask R-CNN. Cada una resolvió un problema de la anterior.

Mask R-CNN es el resultado de una serie de ideas, y cada una arregló un problema de la anterior. En pantalla están las cuatro en una línea de tiempo, con una frase cada una.

La primera, R-CNN, es de 2014. Proponía unas dos mil regiones por foto con un método clásico, que no aprende, y pasaba cada región por la red convolucional por separado. Funcionaba, pero era muy lenta, porque la misma foto se procesaba miles de veces.

Fast R-CNN, de 2015, calcula los mapas de características una sola vez para toda la foto y de ahí recorta cada región. Faster R-CNN, también de 2015, cambia el método clásico por una red pequeña que aprende a proponer regiones, así que todo el sistema se entrena junto. Y Mask R-CNN, de 2017, agrega una rama que dibuja la máscara de cada objeto y una forma más precisa de recortar las regiones.

Las fechas no hay que memorizarlas. En esta última están las piezas de todas las anteriores, y las vamos a ver una por una, en el orden en que trabajan.

[Diapositiva 3 · Vista general: cinco etapas]

> Idea central: Mask R-CNN trabaja en cinco etapas: base convolucional, pirámide de características, red de propuestas, recorte alineado y cabezas de clasificación y de máscara. De sus 43.9 millones de pesos, más de la mitad están en la base.

Mask R-CNN trabaja en cinco etapas, y en pantalla están en fila, con una flecha entre cada una.

La primera es la base convolucional. Es la ResNet50 del video anterior, que convierte la foto en mapas de características. La segunda es la pirámide de características, que reorganiza esos mapas para que sirvan con objetos de distintos tamaños. La tercera es la red de propuestas, que marca los lugares donde podría haber un objeto. La cuarta es el recorte alineado, que toma cada lugar propuesto y lo lleva a un tamaño fijo. Y la quinta son las cabezas: una decide qué es cada propuesta y afina su caja, y otra dibuja la máscara.

Debajo de cada etapa aparece cuántos pesos tiene. La base tiene unos 23.5 millones. La pirámide, 3.3 millones. La red de propuestas, 0.6 millones. La cabeza de la caja, 13.9 millones. Y la cabeza de la máscara, 2.6 millones. Todo suma 43.9 millones de pesos, la cifra que ya vimos. Es un solo modelo, y las cinco etapas se entrenan juntas.

[Diapositiva 4 · La base y la pirámide]

> Idea central: La base entrega mapas de cuatro tamaños. Los profundos saben qué hay pero con poco detalle del lugar, y los primeros tienen detalle pero patrones simples. La pirámide los combina, y deja cinco mapas de 256 canales cada uno.

Los espermatozoides de nuestras fotos miden entre 10 y 116 píxeles de largo, con una mediana de 63. Hay objetos chicos y grandes, y una sola escala no sirve igual para todos.

Recordemos lo que entrega la base. Cuatro bloques de mapas: de 128 por 128, de 64 por 64, de 32 por 32 y de 16 por 16. Los primeros son grandes y tienen buen detalle del lugar, pero solo reconocen patrones sencillos, como bordes. Los últimos son pequeños, con poco detalle del lugar, pero ya reconocen formas más complejas. Lo ideal sería tener las dos cosas en cada mapa.

Eso hace la pirámide de características. En pantalla se ve como una pirámide al revés. Primero, a cada mapa se le aplica un filtro de uno por uno que lo reduce a 256 canales, para que todos tengan el mismo número. Después se parte del mapa más pequeño y se avanza hacia los grandes. En cada paso se amplía el mapa que viene de abajo al doble de tamaño y se suma con el del nivel que sigue, y un filtro de tres por tres suaviza el resultado. Así los mapas grandes reciben información de los profundos sin perder su detalle.

El resultado son cuatro mapas de 256 canales, de 128, 64, 32 y 16 por lado. Se agrega un quinto, de 8 por 8, que sale de reducir a la mitad el más pequeño. Los mapas grandes sirven para objetos pequeños, y los pequeños, para objetos grandes.

[Diapositiva 5 · Las anclas]

> Idea central: Las anclas son cajas de prueba de tamaño y proporción fijos, puestas en cada punto de cada mapa. Los cinco tamaños, de 16 a 256, se reparten uno por mapa y con tres proporciones suman 65,472 anclas en cada recorte de 512 por 512.

Para proponer dónde hay objetos, la red no empieza de cero. Parte de cajas de prueba, que se llaman anclas. Son cajas de tamaño y proporción fijos, y se colocan en cada punto de cada mapa de la pirámide.

El mapa más grande, de 128 por 128, lleva anclas de 16 píxeles. El de 64 por 64, de 32. El de 32 por 32, de 64. El de 16 por 16, de 128. Y el de 8 por 8, de 256. Cada mapa se encarga de un tamaño. Esos cinco tamaños se eligieron pensando en nuestros espermatozoides, de 10 a 116 píxeles de largo, y con margen para objetos más grandes.

En cada punto hay tres anclas del mismo tamaño pero de distinta proporción: una más ancha que alta, una cuadrada y una más alta que ancha. En pantalla se ven las tres sobre un punto, y las cinco escalas una al lado de otra.

Hagamos la cuenta. Los cinco mapas suman 128 por 128, más 64 por 64, más 32 por 32, más 16 por 16, más 8 por 8, que son 21,824 puntos. Con tres anclas en cada uno, resultan 65,472 anclas para cada recorte de 512 por 512. Las anclas no se aprenden: son fijas. Lo que se aprende es cómo corregirlas.

[Diapositiva 6 · La red de propuestas]

> Idea central: La red de propuestas revisa cada ancla y responde dos cosas: si hay algo ahí, y cómo mover y estirar la caja para que encaje. Se descartan las muy traslapadas y se pasan hasta 1,000 propuestas a la siguiente etapa.

La red de propuestas es una red pequeña, de unos 0.6 millones de pesos, que se aplica sobre cada mapa de la pirámide. Para cada ancla responde dos preguntas.

La primera es si ahí hay algo o solo hay fondo. No dice qué es, solo si hay un objeto. Da un puntaje por ancla. La segunda es cómo debe corregirse la caja: cuánto moverla a un lado y a otro, y cuánto estirarla o encogerla, para que encaje mejor con el objeto. Son cuatro números por ancla. En pantalla se ve una ancla que no coincide con el espermatozoide, y la caja corregida, que sí.

En el entrenamiento aprende con las etiquetas. Las anclas que coinciden bien con un espermatozoide etiquetado cuentan como lugares con algo, y las que caen en fondo oscuro, como lugares sin nada. Con eso, la red aprende a distinguir unas de otras y a corregir las cajas.

De las 65,472 anclas, la mayoría cae en el fondo y recibe puntajes bajos. Se ordenan por puntaje y se quitan las que se traslapan mucho con otra mejor. Más adelante vemos cómo se mide ese traslape. Al final pasan a la siguiente etapa hasta 1,000 propuestas, ya con la caja corregida.

[Diapositiva 7 · El recorte alineado]

> Idea central: Las propuestas tienen tamaños distintos, y las etapas siguientes necesitan un tamaño fijo. El recorte alineado lleva cada propuesta a 7 por 7 para la caja y a 14 por 14 para la máscara, interpolando sin redondear las coordenadas.

Las propuestas tienen tamaños distintos, y las etapas que siguen necesitan siempre un tamaño fijo. Por eso la cuarta etapa toma cada propuesta y la lleva a una cuadrícula fija.

Funciona así. Se elige el mapa de la pirámide que corresponde al tamaño de la propuesta: las chicas, de un mapa grande, y las grandes, de uno pequeño. El de 8 por 8 solo lo usa la red de propuestas. Se recorta esa región, con sus 256 canales, y se muestrea en una cuadrícula de 7 por 7 para la rama que decide qué es y de 14 por 14 para la rama que dibuja la máscara. En pantalla se ve una propuesta sobre un mapa y la cuadrícula pequeña en que se convierte.

Aquí está la palabra que da el nombre a la pieza: alineado. En la versión anterior de la red, las coordenadas de la propuesta se redondeaban a la cuadrícula del mapa. Un desplazamiento de unos pocos píxeles no importa mucho cuando se trata de una caja, pero sí cuando hay que dibujar un contorno. Mask R-CNN calcula cada valor de la cuadrícula interpolando entre los puntos vecinos del mapa, sin redondear, y así la máscara queda alineada con el objeto.

Esta pieza no tiene pesos propios. Solo hace la cuenta de recortar y muestrear.

[Diapositiva 8 · La cabeza de clasificación]

> Idea central: Cada recorte de 7 por 7 por 256 pasa por dos capas de 1,024 neuronas, como las del módulo 1. De ahí salen dos resultados: qué es, espermatozoide o fondo, y cuatro números para afinar la caja.

Ya tenemos un recorte de tamaño fijo por cada propuesta. Ahora hay que decidir qué es. Eso lo hace la cabeza de clasificación.

Tiene una sorpresa para quien vio el primer video. Aquí sí hay neuronas conectadas con todo. El recorte, de 7 por 7 por 256, tiene 12,544 números. Se estiran en una fila y pasan por dos capas de 1,024 neuronas, justo las del módulo 1, cada una con un peso por entrada. La primera capa, solo ella, tiene más de 12.8 millones de pesos. Es la parte de la red con más pesos después de la base, 13.9 millones en total.

La diferencia con lo que descartamos en el video anterior es el tamaño. Allí se trataba de una foto completa. Aquí es un recorte pequeño, que ya viene resumido por los filtros. Conectar todo con todo sobre un resumen pequeño sí es manejable.

La última capa da dos resultados. Primero, un puntaje por cada clase: fondo y espermatozoide. Segundo, cuatro números para afinar la caja, que ya venía corregida de la red de propuestas y aquí se corrige otra vez, con más información. Esa última capa tiene solo 10,250 pesos. En pantalla se ven las dos salidas: un puntaje de 0.97 para espermatozoide y una caja que se ajusta un poco.

[Diapositiva 9 · La cabeza de máscara]

> Idea central: Sobre el recorte de 14 por 14, cuatro capas de filtros y una ampliación dan una máscara de 28 por 28: la probabilidad de que cada punto sea parte del espermatozoide. Con un umbral de 0.5 se convierte en el contorno.

La cabeza de máscara es la pieza que Mask R-CNN agrega a las redes anteriores. Trabaja con el recorte de 14 por 14, con sus 256 canales.

Primero aplica cuatro capas de filtros de tres por tres, como los del video anterior. Después, una capa que duplica el tamaño, y queda en 28 por 28. Y una última que da, para cada clase, una máscara de 28 por 28 con valores de 0 a 1. Cada valor es la probabilidad de que ese punto sea parte del espermatozoide. En pantalla se ve la máscara como un mapa de calor, con los puntos más probables en naranja.

Para obtener una forma definida se aplica un umbral de 0.5: lo que está por encima cuenta como espermatozoide, y lo que está por debajo, como fondo. Es un umbral distinto del de seguridad, que veremos enseguida. Este decide cada punto de la máscara, y aquel decide si la detección completa se queda.

Esa máscara de 28 por 28 se estira al tamaño de la caja y se pega en su lugar de la foto. De ahí el sitio saca el contorno. Para un espermatozoide de unos 60 píxeles de largo, cada punto de la máscara cubre alrededor de dos píxeles. Es el nivel de detalle del contorno que dibuja la red. Entre la cabeza de la caja y la de la máscara se reparten 16.5 millones de pesos.

[Diapositiva 10 · El puntaje de seguridad]

> Idea central: Cada detección sale con un puntaje de 0 a 1. Se conservan las que pasan un umbral de seguridad, que el modelo del sitio guarda en su archivo: 0.9. Un umbral más alto da menos falsos y más omisiones, y uno más bajo, al revés.

Cada detección que sale de la red trae un puntaje, de 0 a 1, que viene de la cabeza de clasificación. Cuanto más alto, más seguro está el modelo. En pantalla hay tres contornos con su puntaje: 0.99, 0.93 y 0.30.

Para decidir qué cuenta como espermatozoide hay que elegir un umbral de seguridad. Si se pone alto, se quedan solo las detecciones muy seguras: hay menos falsos, pero se pierden algunos espermatozoides reales. Si se pone bajo, se encuentran más, pero se cuelan manchas y fibras. No hay un valor perfecto. Hay un equilibrio, y se elige probando con las fotos de validación, algo que vemos en el video cuatro.

En nuestro sistema, la red devuelve todo lo que tenga un puntaje de 0.05 o más. Después, el sitio se queda solo con lo que alcanza el umbral que viene guardado dentro del modelo de fluorescencia, que es 0.9. Ese valor se eligió para este modelo con sus fotos de validación, y puede cambiar si se entrena otro.

Hay que distinguir los dos umbrales. El de 0.5 decide cada punto de una máscara. El de 0.9 decide si una detección completa se queda o se descarta. Los dos números se parecen, pero no hacen lo mismo.

[Diapositiva 11 · IoU: qué tanto coinciden dos contornos]

> Idea central: IoU es el área compartida entre dos contornos dividida entre el área que cubren juntos. Va de 0 a 1. Con 100 y 100 píxeles y 60 en común da 0.43; con 80 en común, 0.67. En la validación, 0.5 o más cuenta como acierto.

Varias veces hemos dicho que dos cajas o dos contornos se traslapan mucho. Hay una medida precisa para eso, que se llama IoU, por intersección sobre unión en inglés.

La idea es sencilla. Se toma el área que comparten los dos contornos y se divide entre el área total que cubren juntos, contando la parte compartida una sola vez. Si no se tocan, el resultado es 0. Si coinciden por completo, es 1.

Un ejemplo con números. En pantalla hay dos contornos de 100 píxeles de área cada uno, y comparten 60. Juntos cubren 100 más 100 menos 60, o sea 140 píxeles. El IoU es 60 entre 140, que es 0.43. Si en cambio comparten 80, el área conjunta es 120 y el IoU es 0.67.

Para decidir si una detección es un acierto se usa un criterio: IoU de 0.5 o más con el contorno etiquetado por una persona. Con 0.43 del primer ejemplo, la detección no cuenta como acierto, aunque se vea cerca. Con 0.67 sí cuenta.

El IoU aparece en tres momentos. Al entrenar, para saber qué anclas coinciden con un espermatozoide etiquetado. Al detectar, para quitar repetidos. Y al validar, para decidir si una detección es un acierto. Vamos con el segundo.

[Diapositiva 12 · Los repetidos]

> Idea central: Un mismo espermatozoide puede aparecer varias veces. Se limpian tres veces: la supresión de cajas (IoU de 0.6) dentro de la red, el descarte de duplicados entre teselas (0.5) y el filtro de contenido del proyecto, que quita un contorno si la mitad ya está dentro de otro.

Un mismo espermatozoide puede aparecer varias veces en la salida de la red. Hay tres filtros que lo corrigen, uno detrás de otro.

El primero está dentro de la red. Se llama supresión de no máximos. Cuando dos cajas se traslapan con un IoU de más de 0.6, se queda la de mayor puntaje y se descarta la otra.

El segundo viene de que la foto se analiza por teselas. La red trabaja con recortes de 512 por 512 píxeles, así que la foto se corta en teselas que se traslapan 128 píxeles con sus vecinas. Un espermatozoide en la zona compartida lo ve dos veces. Si dos detecciones de teselas distintas tienen un IoU de 0.5 o más, se queda la de mayor puntaje. Además, si una detección toca el borde interno de una tesela, se descarta, porque puede estar cortada, y la tesela vecina la verá entera.

El tercero es un filtro propio del proyecto. A veces la red dibuja un espermatozoide entero y, además, un trozo de él. El IoU entre un contorno de 40 píxeles dentro de otro de 100 es solo 0.4, así que los filtros anteriores no lo detectan. Pero el contorno pequeño está contenido por completo en el grande. Por eso se mide otra cosa: qué parte del área de un contorno ya está dentro de uno conservado. Si es la mitad o más, se descarta.

[Diapositiva 13 · Las cinco pérdidas]

> Idea central: Al entrenar, cada decisión tiene su pérdida: si hay algo, dónde está, qué es, cómo se afina la caja y qué forma tiene. Son cinco y se suman en un solo número, que es el que se baja, con el mismo mecanismo del módulo 1.

En el módulo 1 vimos que, para aprender, la red necesita un número que diga qué tan mal lo hizo: la función de pérdida. Mask R-CNN toma varias decisiones, y cada una tiene su propia pérdida. En pantalla están las cinco, ligadas a la etapa a la que corresponden.

En la red de propuestas hay dos. Una mide si acertó en si había algo o no en cada ancla. La otra mide qué tan bien corrigió la caja. En la cabeza de clasificación hay otras dos. Una mide si acertó en qué es: espermatozoide o fondo. La otra mide qué tan bien afinó la caja final. Y en la cabeza de máscara está la quinta, que compara la máscara que dibujó con la que dibujaron las personas, punto por punto.

Las cinco se suman en un solo número, y ese es el que el entrenamiento intenta bajar. El mecanismo es el de siempre. Se calcula la pérdida, se calcula hacia dónde mover cada peso de las cinco etapas a la vez, y se mueve un poco.

Esto explica por qué la calidad de las etiquetas importa tanto. Una sola etiqueta con un contorno descuidado afecta a las cinco pérdidas al mismo tiempo. Cómo baja esa suma durante un entrenamiento real es parte del video cuatro.

[Diapositiva 14 · Un ejemplo con la imagen de muestra]

> Idea central: Con la imagen de muestra del sitio, la red marcó 41 contornos: 37 sobre cabezas y 4 sobre filamentos largos, y unas 9 de las 46 cabezas quedaron sin contorno. La red decide dónde hay un espermatozoide y qué forma tiene, y el sitio mide después, con código.

Veamos todo junto en un ejemplo. El sitio incluye una imagen de muestra, dibujada por computadora: espermatozoides con la cabeza de color y la cola verde sobre fondo negro. No es una foto real, pero sirve para ver el recorrido completo. En pantalla está con los contornos que dibujó la red.

Recorramos lo que pasó. La imagen, de 1200 por 900 píxeles, se preparó con el brillo máximo de rojo, verde y azul, como en el video anterior. Se cortó en teselas de 512 por 512, con 128 píxeles de traslape. Cada tesela pasó por las cinco etapas. Después se quitaron los repetidos, se aplicó el umbral de 0.9 y quedaron 41 contornos.

Al contar las cabezas por su color, hay unas 46 en la imagen. Treinta y siete de los contornos están sobre cabezas. Cuatro están sobre filamentos largos, que la red tomó por espermatozoides. Y unas nueve cabezas quedaron sin contorno. El resultado es bueno, pero no es perfecto, y en la siguiente diapositiva vemos por qué.

Después llega algo que la red no hace. El área, el largo y la distribución de tamaños se calculan a partir de los contornos, con código normal. La red decide dónde hay un espermatozoide y qué forma tiene. Lo demás es medición, y por eso un mismo contorno siempre da las mismas medidas.

[Diapositiva 15 · Límites]

> Idea central: La red marcó filamentos como si fueran espermatozoides y dejó cabezas sin contorno. Además contesta aunque la foto no sea de espermatozoides: con una foto de células dio 0.96 sobre un núcleo y 1.00 sobre un trozo de fibra. Su resultado se revisa.

Antes de cerrar, los límites. El ejemplo anterior ya mostró dos. En la imagen de muestra, la red marcó cuatro filamentos largos como si fueran espermatozoides, con puntajes de 0.9 o más, y dejó unas nueve cabezas sin contorno. Con fotos reales aparecen más casos difíciles. Los espermatozoides empalmados pueden salir como un solo contorno, o como dos con una frontera inventada. Los racimos se confunden más. Las fibras y las manchas brillantes se parecen a una cabeza. Y a veces un espermatozoide sale partido en dos contornos, o dibujado dos veces, y los filtros no siempre lo corrigen.

Hay otro límite, más de fondo. Una red como esta siempre da una respuesta, esté o no ante el tipo de foto para el que se entrenó. Lo comprobé con el modelo de fluorescencia del sitio. Le di un recorte de una foto de células con núcleos fluorescentes, que no tiene ningún espermatozoide. En pantalla está el resultado. Cinco detecciones salieron con puntaje de 0.9 o más: un núcleo celular con 0.96 y un trozo de fibra con 1.00. Un puntaje alto en una foto que el modelo no conoce no garantiza nada.

Lo que sí se puede hacer es revisar. El sitio muestra cada contorno sobre la foto, y quien analiza puede ampliar y corregir. El modelo ayuda a contar y medir, y su resultado se revisa. Entender cómo trabaja sirve para saber cuándo desconfiar.

[Diapositiva 16 · Lo que vimos y lo que sigue]

> Idea central: Vimos qué se le pide a Mask R-CNN, de dónde viene, sus cinco etapas con sus anclas, propuestas, recorte alineado y cabezas, los umbrales, el IoU, los filtros de repetidos, las cinco pérdidas y sus límites. En el siguiente video, cómo aprende con pocas fotos: transferencia.

Para cerrar, un resumen. Vimos que a la red se le pide encontrar, encuadrar y delinear cada espermatozoide por separado. Vimos que Mask R-CNN viene de una serie de redes, y que trabaja en cinco etapas: la base convolucional, la pirámide de características, la red de propuestas, el recorte alineado y las cabezas de clasificación y de máscara.

Vimos las anclas, que son cajas de prueba fijas, y cómo la red de propuestas las corrige. Vimos que cada detección trae un puntaje, que hay un umbral de 0.5 para los puntos de la máscara y uno de 0.9 para quedarse con una detección. Vimos el IoU, que mide cuánto coinciden dos contornos, y los tres filtros que quitan repetidos. Vimos que las cinco decisiones tienen cada una su pérdida, y que se suman en un solo número. Y vimos en un ejemplo que la red marca filamentos de más, deja cabezas sin contorno y contesta aunque no conozca la foto, así que sus resultados se revisan.

En el siguiente video vemos una pregunta que quedó abierta. Esta red tiene casi 44 millones de pesos, y nosotros tenemos muy pocas fotos. Entrenar una red tan grande desde cero suele pedir muchísimos más ejemplos. En el aprendizaje por transferencia se parte de una red que ya aprendió a ver con otras fotos, y se le enseña lo que falta. Gracias por acompañarme.
