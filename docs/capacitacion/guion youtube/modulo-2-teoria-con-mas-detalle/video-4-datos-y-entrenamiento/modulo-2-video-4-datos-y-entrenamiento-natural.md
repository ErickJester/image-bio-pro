# Guion del módulo 2, video 4 de 4: Datos, entrenamiento y validación (versión natural)

BioImage-Repro UAM · Módulo 2 · Capacitación en video

Segunda versión, escrita para decirse en voz alta: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

[Diapositiva 1 · Datos, entrenamiento y validación]

> Idea central: El video anterior mostró que una red preentrenada necesita pocas fotos. Falta ver esas fotos: cómo se anotan, cómo se separan para entrenar y para validar, y cómo se lee un entrenamiento. Este video cierra el módulo 2.

En el video anterior vimos algo importante. Gracias a la transferencia, una red de casi 44 millones de pesos se puede ajustar con muy pocas fotos. Esas pocas fotos son el tema de hoy. De dónde salen. Cómo se anotan. Cómo se separan para entrenar y para comprobar. Y cómo se lee un entrenamiento para saber si salió bien.

Todo gira alrededor de una idea. Un modelo vale lo que valen sus datos. Y lo que vale la forma de medirlo. Si las etiquetas son descuidadas, el modelo aprende el descuido. Si la prueba es débil, una cifra bonita no dice nada.

Vamos por partes. Primero, qué es un dato en nuestro problema y cuántos hacen falta. Después, la anotación y su criterio. Luego, cómo se separan las fotos, cómo se entrena y qué se mide. Y al final, el sobreajuste, la gráfica de curvas y qué tan confiables son nuestros números. Las cifras de este video salen del cuaderno de entrenamiento que veremos en el módulo 4.

[Diapositiva 2 · Qué es un dato]

> Idea central: Cada dato es una foto con el contorno dibujado de cada espermatozoide. En el cuaderno de ejemplo hay 4 fotos de fluorescencia con 258 contornos, y casi todos vienen de dos fotos.

En este problema, un dato es una foto junto con su respuesta. La respuesta es el contorno de cada espermatozoide, dibujado por una persona. Sin el contorno, la foto no le sirve a la red para aprender.

En el cuaderno de ejemplo hay cuatro fotos de fluorescencia. Tres son de 1792 por 1374 píxeles. Una está en vertical, de 1374 por 1792. Entre las cuatro suman 258 espermatozoides etiquetados. En pantalla está el reparto. La primera foto tiene 6. La segunda, 10. La tercera, 120. La cuarta, 122.

Fijémonos en eso. Dos fotos aportan 242 de los 258 contornos. Más del 90 por ciento. Las otras dos casi no cuentan. Cuatro fotos son menos variedad de la que parece. Lo que la red ve es, sobre todo, dos escenas densas. Y los espermatozoides miden entre 10 y 116 píxeles de lado mayor, con una mediana de 63.

Hay una forma útil de contar los datos. La foto es la unidad de variedad: otra iluminación, otra tinción, otro campo del microscopio. El contorno es la unidad de ejemplo: cada uno enseña algo. Con poca variedad y muchos contornos, la red aprende muy bien lo que ya vio. Y no sabemos cuánto sabe de lo que no vio.

[Diapositiva 3 · ¿Cuántas fotos hacen falta?]

> Idea central: No hay un número fijo. Depende de qué tan parecidas sean las fotos nuevas a las de entrenamiento y de qué tan difícil sea la tarea. Con transferencia se necesitan menos. La forma de saberlo es medir, con una validación honesta.

La pregunta que todos hacen es cuántas fotos hacen falta. La respuesta honesta es que no hay un número fijo. Depende de tres cosas.

La primera es qué tan variadas son las fotos con las que se va a usar el modelo. Si siempre son del mismo microscopio, con la misma tinción y la misma luz, hacen falta menos. Si cambian, esa variedad tiene que estar en el entrenamiento. La segunda es qué tan difícil es la tarea. Contornear espermatozoides que se encima o se cruza pide más ejemplos que contar puntos aislados. Y la tercera es si se parte de una red preentrenada, como vimos en el video anterior. Eso baja mucho lo que hace falta.

Hay una forma práctica de averiguarlo sin adivinar. Se entrena con una parte de las fotos, por ejemplo la mitad, y se mide. Luego se entrena con todas y se vuelve a medir. Si la validación mejora bastante, más datos es el camino. Si casi no cambia, el límite está en otro lado. En las etiquetas, en el tipo de foto o en la propia tarea. En pantalla se ve el esquema de esa comparación.

En nuestro caso, el cuaderno con cuatro fotos funciona como un modelo preliminar. Más fotos, y sobre todo más variadas, son la mejora principal. Y como las fotos nuevas hay que etiquetarlas, veamos cómo.

[Diapositiva 4 · Anotar en CVAT]

> Idea central: Las fotos se anotan en CVAT, una herramienta que no publica los datos. Se define la etiqueta, se dibuja un polígono por espermatozoide y se exporta en formato COCO. Un borrador automático ahorra dibujar desde cero, pero hay que corregirlo.

Las fotos son del cliente y no se publican. Por eso se anotan en CVAT. Es una herramienta que se puede usar sin subir los datos a un servicio público. Y las fotos se guardan solo en Google Drive. No están en el repositorio del proyecto.

El flujo es sencillo. Se crea una tarea con las fotos. Se define la etiqueta, que en nuestro caso es una sola. Y para cada espermatozoide se dibuja un polígono, punto por punto, siguiendo su contorno. Al terminar, se exporta el trabajo en formato COCO. Es un archivo de texto con las fotos y los polígonos. El cuaderno lo lee desde ahí.

Dibujar un contorno a mano es lento. Y una foto densa trae más de cien. Por eso el proyecto tiene un pre-anotador. Es un script que propone el contorno de cada cabeza con técnicas clásicas de imagen, sin red neuronal. Su resultado se importa en CVAT como borrador, y la persona lo corrige. Deja casi solo cabezas de verdad, pero se le pasan las más tenues. Esas se agregan a mano. Y en fotos con un solo espermatozoide marca puntos sueltos del fondo, así que ahí no se usa.

El borrador ahorra trabajo, pero tiene un riesgo. Si se acepta sin revisar, la red aprende los errores del borrador. Corregirlo es parte del trabajo.

[Diapositiva 5 · El criterio de anotación]

> Idea central: Cada decisión al anotar es una decisión que la red aprende. Hace falta un criterio escrito y alguien con conocimiento biológico que valide. El cuaderno revisa antes de entrenar que las fotos y las etiquetas cuadren.

En el módulo 1 dijimos que lo más delicado de anotar es el criterio. Ahora lo vemos con los casos concretos de nuestras fotos.

En nuestro cuaderno, un espermatozoide se anota completo. La cabeza y el primer tramo de la cola. Eso fija lo que la red va a contornear. Y también lo que el sitio va a medir. Pero quedan casos que alguien tiene que decidir. Una mancha roja difusa y fuera de foco: ¿cuenta? Una cabeza medio tapada por una cola: ¿se dibuja? Dos cabezas pegadas: ¿un contorno o dos? Un espermatozoide cortado por el borde de la foto: ¿entra? Cada respuesta es una regla que la red aprende. Si dos personas contestan distinto, la red recibe señales que se contradicen.

Por eso se recomiendan dos cosas. Un criterio escrito, de una o dos páginas, con ejemplos de cada caso. Y una persona del grupo con conocimiento biológico que valide las anotaciones. Una forma de medirlo: que dos personas anoten las mismas diez fotos, y comparar con el IoU del video 2 qué tanto coinciden. Si coinciden poco, el criterio no está claro.

Antes de entrenar, el cuaderno hace sus propias revisiones. Se detiene si falta una foto. Si una foto no mide lo que dice el archivo. O si no existe la etiqueta. Y dibuja recortes de entrenamiento con su contorno encima. Si un contorno no coincide con su espermatozoide, el error está en los datos. Conviene corregirlo antes de entrenar.

[Diapositiva 6 · Separar entrenamiento y validación]

> Idea central: Parte de las fotos se aparta para comprobar el modelo con datos que no vio al aprender. Con 10 o más fotos se reservan fotos completas; con menos, una franja de cada foto. Con 4 fotos, la validación sale de las mismas fotos: es una prueba más fácil.

Para saber si un modelo funciona, no se puede probar con las mismas fotos con las que aprendió. Sería como evaluar a un estudiante con las preguntas que ya se sabe de memoria. Por eso se aparta una parte de los datos. La red no la ve al entrenar. Esa parte es la validación.

El cuaderno tiene dos reglas. Con diez fotos o más, reserva fotos completas: una de cada cinco, y como mínimo una. Con menos de diez, de cada foto reserva una franja de una cuarta parte de su lado más largo. Y deja un margen de 100 píxeles entre lo que se entrena y lo que se valida, para que un mismo espermatozoide no quede mitad en cada lado.

Nosotros tenemos cuatro fotos, así que aplica la segunda regla. En pantalla se ven las cuatro con su zona de entrenamiento y su franja de validación. El resultado: 163 espermatozoides para entrenar y 64 para validar. Los 31 restantes quedan en el margen de 100 píxeles y no se usan en ninguna de las dos partes.

Y aquí está la debilidad, que conviene decir en voz alta. La validación sale de las mismas cuatro fotos, de una franja apartada. Es una prueba más fácil que una foto nueva, de otro día o de otro microscopio. Además, casi toda cae en dos fotos. 28 y 31 contornos en la tercera y la cuarta. 5 en la segunda. Ninguno en la primera. Con más fotos, la regla cambia a fotos completas. Y la prueba se vuelve más exigente y más honesta.

[Diapositiva 7 · Aumento de datos]

> Idea central: Durante el entrenamiento se arman recortes al azar con variaciones: volteos, giros, acercar o alejar, brillo, contraste y ruido. Así la red aprende la forma de un espermatozoide y no las fotos de memoria. Es una manera de ver más variedad con las mismas fotos.

Con pocos datos hay una forma de sacarles más provecho. Se llama aumento de datos. En cada paso del entrenamiento, el cuaderno no le da a la red las fotos completas. Le da recortes de 512 por 512 píxeles, tomados al azar. Y a cada uno le hace cambios pequeños.

Los cambios son estos. Se voltea el recorte de izquierda a derecha o de arriba abajo, cada uno con una probabilidad de la mitad. Se gira un múltiplo de 90 grados. Se acerca o se aleja la imagen, entre 0.8 y 1.25 veces. Se cambian el brillo y el contraste, con un factor entre 0.7 y 1.3 y un desplazamiento de hasta 20 niveles. Y se agrega un poco de ruido. En pantalla se ve un mismo recorte con varias de esas variaciones.

Un espermatozoide girado, más oscuro o más grande sigue siendo un espermatozoide. Eso es lo que se le enseña a la red. Así no se aprende la posición ni el brillo exactos de las fotos. Y maneja mejor las fotos con otra iluminación.

Además, el 80 por ciento de los recortes se centran en un espermatozoide, para que la red vea muchos ejemplos. El resto son al azar, con fibras y fondo. Un espermatozoide cortado por el borde del recorte cuenta si se ve al menos el 30 por ciento de él.

Es variedad artificial. Ayuda, pero no sustituye a fotos nuevas de verdad.

[Diapositiva 8 · Entrenar en Colab]

> Idea central: El entrenamiento corre en Google Colab con una GPU gratuita: 60 épocas de 400 recortes, en lotes de 4. Una época tarda unos 0.6 minutos y el total, unos 36. El cuaderno valida cada 5 épocas y guarda el mejor modelo, no el último.

El entrenamiento se hace en Google Colab, con una GPU gratuita, una Tesla T4. Esta es la configuración del perfil de fluorescencia. Sesenta épocas. En cada época, 400 recortes de 512 por 512 píxeles, en lotes de 4. Son 100 pasos por época, los mismos 100 pasos del calentamiento que vimos en el video anterior. El descenso del gradiente usa un momento de 0.9, que suaviza los pasos, y una tasa de aprendizaje de 0.005, la que corresponde a lotes de 4.

Cada época tarda unos 0.6 minutos. Las 60 duran alrededor de 36. Cada cinco épocas el cuaderno se detiene a validar. Si el AP50 mejora, guarda ese modelo como el mejor. Cada diez épocas guarda un archivo más grande, de unos 350 megabytes, que sirve para continuar si Colab se corta. Si pasa, basta volver a correr el cuaderno desde el principio. Retoma en la última época guardada.

También hay un modo de prueba. Entrena dos épocas muy cortas, solo para comprobar que todo funciona. Es el que se muestra en el módulo 4.

Una consecuencia importante. El modelo que se exporta al sitio es el mejor según la validación, no el de la última época. Y se guarda con su configuración: el tamaño de las teselas, las anclas y el umbral de seguridad. Por eso el servidor no necesita saber nada del entrenamiento.

[Diapositiva 9 · Qué se mide]

> Idea central: Un acierto es una detección con IoU de 0.5 o más con un contorno etiquetado. Precisión es qué parte de lo marcado es correcto; exhaustividad, qué parte de lo etiquetado se encontró; F1 las combina. Con umbral 0.5, la validación da 60 aciertos de 75 marcas y 66 etiquetados.

Para medir un modelo hay que decidir qué es un acierto. Usamos el IoU del video 2. Una detección es un acierto si su contorno coincide al menos el 50 por ciento con uno etiquetado. Con eso se cuentan tres cosas: los aciertos, las marcas de más y los espermatozoides que se escaparon.

Veamos los números de la validación del cuaderno, con un umbral de seguridad de 0.5. Hay 66 espermatozoides etiquetados. La red marcó 75. De esas 75 marcas, 60 son aciertos y 15 son falsas. Y se escaparon 6 de los 66.

La precisión es qué parte de lo que marcó la red es correcto. 60 entre 75: 0.80. De cada 100 marcas, 80 son espermatozoides. La exhaustividad, o recall, es qué parte de lo etiquetado encontró. 60 entre 66: 0.91. De cada 100 espermatozoides, encuentra 91. El F1 combina las dos con un promedio que castiga que una sea muy baja. Aquí es 0.85.

Hay una cuarta medida, el AP50. Resume la calidad en todos los umbrales de seguridad a la vez, sin tener que elegir uno, y va de 0 a 1. En esta corrida, el mejor modelo tiene un AP50 de 0.888. Con esa medida se elige cuál guardar.

Las dos primeras medidas tiran en sentidos opuestos. Si se pide más seguridad, la red marca menos. Casi todo lo que marca es correcto, pero se le escapan más espermatozoides. Eso lo vemos ahora.

[Diapositiva 10 · Elegir el umbral]

> Idea central: El umbral de seguridad se elige con la validación: se prueban varios y se toma el de mejor F1. En el cuaderno de ejemplo sale 0.8, pero las diferencias son de uno o dos espermatozoides. El modelo del sitio guarda 0.9 y viene de otra corrida.

Al final del entrenamiento, el cuaderno prueba varios umbrales de seguridad sobre la validación, de 0.3 a 0.9. Y calcula las medidas para cada uno. En pantalla está la tabla.

Con 0.3, la red marca 79. La precisión es 0.76 y la exhaustividad, 0.91. Al subir el umbral, la precisión mejora, y la exhaustividad se mantiene en 0.91 hasta 0.7. Con 0.8 la red marca 70, con una precisión de 0.84 y una exhaustividad de 0.89. Con 0.9 marca 65, con una precisión de 0.86 y una exhaustividad de 0.85. El F1 más alto es el de 0.8, que da 0.868. Por eso el cuaderno elige ese valor.

Miremos qué tan grande es la diferencia. Entre 0.5 y 0.9, la red pasa de 60 aciertos a 56. Son cuatro espermatozoides de 66. Con tan pocos ejemplos, una diferencia así puede venir del azar. El umbral elegido es una estimación. El propio cuaderno lo avisa cuando la validación tiene menos de 50.

Una aclaración para no confundirse. El modelo que está hoy en el sitio guarda un umbral de 0.9 y un AP50 de 0.9148, de la época 25. Viene de otra corrida del cuaderno, no de esta del ejemplo. Por eso los números no coinciden. Es lo normal: cada corrida produce su propio mejor modelo y su propio umbral. Y en los dos casos, la prueba es la misma validación pequeña.

[Diapositiva 11 · Sobreajuste]

> Idea central: El sobreajuste es cuando la red se aprende los datos de entrenamiento en lugar de aprender lo general. La pérdida de entrenamiento sigue bajando, pero la validación deja de mejorar o empeora. Se combate con más datos, aumento, transferencia y guardando el mejor modelo.

Ahora sí, el sobreajuste. Es cuando la red aprende tan bien los datos de entrenamiento que se los sabe de memoria. Y por eso falla con datos nuevos. Es el estudiante que se aprende las respuestas del examen pasado en lugar de entender el tema. Saca diez en ese examen y reprueba el siguiente.

Se reconoce porque las dos medidas se separan. La pérdida de entrenamiento, que mide el error con las fotos que la red ve, sigue bajando. Pero la medida de validación, que mira fotos que no vio, deja de mejorar. O incluso empeora. Mientras las dos mejoran juntas, la red está aprendiendo. Cuando se separan, está memorizando.

Lo arriesgan más las redes con muchos pesos y pocos datos, como la nuestra. Por eso se usan varias defensas, y ya las conocemos. Más datos, y variados. El aumento de datos, que ofrece variaciones. La transferencia, que parte de una red que ya sabe ver y se mueve poco. Y guardar el mejor modelo según la validación, en lugar del último. Esa última atrapa el sobreajuste cuando ya pasó. Aunque el entrenamiento siga después de la época 20, el modelo guardado es el de la época 20.

[Diapositiva 12 · La gráfica de curvas]

> Idea central: La pérdida debe bajar. Si la validación deja de mejorar mientras la pérdida sigue bajando, hay sobreajuste. En el ejemplo la pérdida baja de 1.39 a 0.36 en 46 épocas, y el AP50 llega a su mejor valor en la época 20 y oscila después. Con 66 espermatozoides, no se puede afirmar.

El cuaderno termina con dos gráficas. La pérdida de entrenamiento y las medidas de validación. Se leen con tres reglas. La pérdida debe bajar. Si sube, o si se queda plana desde el principio, algo anda mal. Las medidas de validación deben subir. Y si la pérdida baja pero la validación no mejora, o empeora, la red se está aprendiendo las fotos de memoria.

En pantalla están las dos curvas de la corrida de ejemplo. Son las mismas del video anterior. La pérdida baja de 1.39 en la primera época a 0.46 en la veinte, y a 0.36 en la 46. Siempre hacia abajo, cada vez más despacio.

La validación cuenta otra historia. Sube hasta 0.888 en la época 20. Después oscila entre 0.81 y 0.87, sin superar ese valor. Una lectura posible es que, a partir de la época 20, la red empezó a memorizar. Pero hay que ser prudentes. Con 66 espermatozoides en la validación, un solo acierto más o menos mueve las medidas. Y la curva tiene saltos que son ruido. Lo que sí se puede decir es que seguir entrenando después de la época 20 no mejoró la validación. Y que el cuaderno guardó el modelo de esa época.

Esa es la utilidad práctica de la gráfica. Sirve para decidir cuántas épocas entrenar y si hace falta más datos, más que para presumir una cifra.

[Diapositiva 13 · Qué tan confiables son los números]

> Idea central: Las cifras son preliminares: la validación sale de las mismas fotos, el mejor modelo y el umbral se eligen con ella y, en campo claro, solo hay 2 espermatozoides, así que su 1.00 no prueba nada. Un número solo vale con la prueba que lo respalda.

Pongamos las cifras en su lugar. Tienen tres debilidades. Conviene decirlas siempre que se muestren.

La primera. La validación sale de franjas de las mismas fotos de entrenamiento, no de fotos independientes. La segunda. El mejor modelo y el umbral se eligieron con esa misma validación. Las cifras son algo optimistas. Es como elegir la mejor de varias pruebas y presentar su nota. Y la tercera es el tamaño: 66 espermatozoides. Con eso, una diferencia de unas centésimas no significa nada.

Un ejemplo extremo lo da el modelo de campo claro. Su validación tiene solo 2 espermatozoides. Por eso todas sus medidas dan 1.00. Un 1.00 es un número perfecto, y no prueba nada. El propio cuaderno avisa que con menos de 10 espermatozoides no se puede elegir nada con la validación. Y deja el umbral en 0.5.

También se cuentan fotos completas. En dos fotos con pocas células, la red marcó de más: 11 donde hay 6 etiquetados, y 16 donde hay 10. En las dos fotos densas quedó cerca: 119 contra 120, y 119 contra 122. Pero esas fotos incluyen zonas con las que se entrenó, así que no prueban calidad.

Lo que cambiaría la confianza son fotos nuevas de verdad, de otro día o de otro equipo, etiquetadas por alguien más. Hasta entonces, el sitio dice lo que es: un modelo preliminar. Y sus resultados se revisan.

[Diapositiva 14 · Cómo mejorar el modelo]

> Idea central: Mejorar el modelo es mejorar los datos: más fotos variadas, ejemplos sin espermatozoides para que aprenda a no marcar nada, validación con fotos nuevas y una corrida nueva que se compara con la anterior. El sitio no aprende de lo que suben los usuarios.

¿Cómo se mejora el modelo? Casi siempre mejorando los datos, no la red. Hay cuatro pasos.

Primero, reunir más fotos, y variadas. Densas y escasas. Con fibras. De distinta iluminación y de más de un día. La variedad pesa más que la cantidad. Segundo, agregar fotos sin espermatozoides, como de otros tejidos. El cuaderno tiene una opción para usar fotos sin etiquetas como ejemplos de que aquí no hay nada. Por defecto no las incluye, y hoy el modelo no tiene fotos así. De ahí que pueda marcar manchas o sombras.

Tercero, validar con fotos que la red no haya visto, con la regla de fotos completas cuando haya diez o más. Y cuarto, entrenar una corrida nueva, con otro nombre. Vuelve a partir de los pesos de COCO, con todas las fotos juntas. Se compara con la anterior sobre la misma validación, y se queda la mejor. El archivo del modelo se cambia en el servidor.

Una aclaración sobre algo que se pregunta mucho. El sitio no aprende de las fotos que suben los usuarios. No se vuelve mejor solo ni se reentrena en el servidor. Mejorar exige etiquetar fotos nuevas, reentrenar en Colab y cambiar el archivo.

[Diapositiva 15 · Lo que vimos y lo que sigue]

> Idea central: En el módulo 2 vimos cómo ve una red convolucional, cómo trabaja Mask R-CNN, cómo la transferencia permite entrenar con pocas fotos y cómo se anotan, separan y miden los datos. En el módulo 3, el sitio funcionando y el código.

Cerramos el módulo 2 con un resumen. En este video vimos que un dato es una foto con el contorno de cada espermatozoide. Y que no hay un número fijo de fotos: depende de la variedad y de cómo se mida. Vimos cómo se anota en CVAT, por qué el criterio es lo más delicado y cómo un borrador automático ayuda si se corrige. Vimos cómo se separan los datos y por qué, con cuatro fotos, la validación es débil. Vimos el aumento de datos, el entrenamiento en Colab, y las medidas de precisión, exhaustividad, F1 y AP50 con su ejemplo numérico. Vimos el umbral, el sobreajuste y la gráfica de curvas. Y vimos que las cifras actuales son preliminares, y que mejorar el modelo es, sobre todo, mejorar los datos.

Y de todo el módulo, lo que une los cuatro videos. Un filtro que recorre la imagen. Una red de cinco etapas que encuentra y contornea. Una red preentrenada que ahorra fotos. Y unas fotos bien anotadas y bien medidas.

En el módulo 3 cambiamos de lugar. Abrimos el sitio funcionando, con una cuenta, un análisis y sus resultados. Y después vemos cómo está hecho por dentro, en código. Gracias por acompañarme.
