# Guion del módulo 4, video 1 de 4: El cuaderno de Colab, primera parte

BioImage-Repro UAM · Módulo 4 · Capacitación en video

Se graba con la pantalla: el cuaderno de Colab se muestra mientras hablas, sin mazo. Continúa del módulo anterior. Empieza con la frase que lo une con el módulo 3.

*3,999 palabras, unos 22.9 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- El cuaderno `entrenamiento/entrenar_mask_rcnn.ipynb` abierto en Colab, con el entorno de ejecución en GPU y las fotos y el archivo de etiquetas en la carpeta de Drive que pide el cuaderno. Las celdas se corren en orden, desde la primera.
- En la configuración, `MODO_PRUEBA = True` y `PERFIL = "fluorescencia"`. Así no se mezcla con una corrida real y el cuaderno no entrena más de dos épocas cortas.
- Este video llega hasta la revisión visual de los recortes. El entrenamiento se corre en el video siguiente.

[Pantalla 1 · Un cuaderno de Colab y de dónde sale el modelo]

> Idea central: El sitio solo carga un archivo de modelo ya entrenado. Ese archivo sale de un cuaderno de Colab, que corre en una computadora de Google con tarjeta gráfica. El cuaderno hace diez cosas en orden; este video cubre las seis primeras, que llevan de las fotos y las etiquetas a los recortes con los que se entrena.

> En pantalla: Colab, el cuaderno `entrenar_mask_rcnn.ipynb`: la celda de introducción, la lista «Qué hace, paso a paso» y los requisitos.

[Acción: abre el cuaderno en Colab, celda de introducción, arriba del todo]

En el módulo anterior vimos el sitio funcionando. Subes una foto y el servidor carga un modelo. Los contornos se miden y salen los números. Pero dimos algo por hecho y es ese modelo. Son dos archivos con extensión pt. Uno es para fluorescencia y otro para campo claro. El servidor los lee sin más. ¿De dónde salen?

Salen de este cuaderno y de eso trata el módulo que empieza hoy. También trata de lo que viene después. Cómo llega el sitio a internet. Son cuatro videos. Este y el siguiente recorren el cuaderno. Los dos últimos llevan el sitio a un servidor en la nube con su dominio y su candado de seguridad.

Empecemos por lo básico que es qué es un cuaderno de Colab. Es un documento hecho de celdas. Unas llevan texto como esta de arriba y otras llevan código que se ejecuta celda por celda en orden. Lo que se ejecuta no corre en tu computadora. Corre en una de Google que te presta durante un rato y que puede traer tarjeta gráfica. Entrenar una red necesita esa tarjeta y por eso se entrena aquí y no en el servidor del sitio. Ese servidor solo analiza fotos y lo hace con el procesador.

Esa es la división de trabajo de todo el proyecto. El entrenamiento ocurre una vez en Colab y produce un archivo. El sitio solo usa ese archivo.

Esta celda inicial dice qué se entrena. Es una red de segmentación por instancias llamada Mask R-CNN que dada una foto dibuja el contorno de cada espermatozoide. Y fíjate en una frase. La red aprende solo la forma y el color no interviene en la detección.

[Acción: baja a «Qué hace, paso a paso»]

Aquí está la lista de lo que hace el cuaderno en diez pasos. Prepara el entorno y configura. Lee las etiquetas y separa entrenamiento y validación. Prepara las fotos y arma los recortes. Esos seis son los de hoy. Después viene construir la red y entrenar. Luego mostrar resultados y exportar el modelo. Eso y una última sección sobre cómo mejorarlo ocupan el video siguiente.

Ya en esta introducción aparece algo que conviene retener. El cuaderno entrena un modelo por tipo de foto. Un valor llamado perfil decide qué fotos se usan y con qué tamaños. Fluorescencia tiene fondo oscuro. Campo claro tiene fondo claro y las fotos reducidas a la mitad. Y mixto junta los dos tipos en un solo modelo y es más lento. Ya lo vimos desde el otro lado en el servidor. Dos tipos de foto y dos modelos. Aquí es donde se hacen.

[Acción: baja a «Requisitos» y muestra la estructura de carpetas de Drive]

Los requisitos son un entorno de ejecución con tarjeta gráfica y una carpeta en Google Drive con dos cosas. Las fotos etiquetadas en una carpeta y un archivo de etiquetas exportado de CVAT. Es la herramienta de anotación del módulo 2. Las fotos son del laboratorio. Se quedan en Drive y no se suben al repositorio.

Hay otros dos requisitos que importan hoy. El primero es un modo de prueba. Entrena dos épocas muy cortas solo para comprobar que todo corre y guarda su salida en una carpeta aparte. Es el que usaremos en pantalla porque un entrenamiento completo tardaría demasiado para un video. El segundo es que si Colab se interrumpe basta con ejecutar otra vez desde el principio. El entrenamiento continúa donde se quedó. Eso lo veremos en el siguiente video.

[Pantalla 2 · Paso 1: el entorno]

> Idea central: Colab ya trae PyTorch, torchvision, OpenCV y matplotlib, así que no hay que instalar nada. Las dos primeras celdas comprueban que hay tarjeta gráfica y conectan Google Drive.

> En pantalla: Colab: las celdas del Paso 1. Primero la que revisa la GPU, después la que conecta Drive.

[Acción: celda del Paso 1, comprobar GPU: ejecútala]

El primer paso es el entorno y no hay nada que instalar. Colab ya trae PyTorch que es la biblioteca con la que se programan las redes neuronales. Trae también torchvision que incluye redes ya hechas y herramientas para imágenes. Y trae OpenCV y matplotlib.

Esta celda se limita a imprimir las versiones y a decir si hay tarjeta gráfica y cuál es. La que pide este cuaderno es una T4 de las que Colab ofrece en su plan gratuito. Si dice que no hay ninguna tienes que cambiar el tipo de entorno de ejecución antes de seguir.

[Acción: celda siguiente, conectar Google Drive: ejecútala y acepta el permiso]

La segunda celda conecta Google Drive. La primera vez Google pide un permiso y ese permiso lo concedes tú desde tu cuenta. Fíjate en la estructura try y except. Si el código no corre en Colab esa importación falla. En lugar de detenerse el cuaderno imprime un aviso y sigue con las rutas tal como están. Así el mismo cuaderno se puede abrir en otra computadora.

[Pantalla 3 · Paso 2: la configuración]

> Idea central: Todo lo que se puede ajustar está en una sola celda, con una explicación junto a cada valor. Lo más importante es el perfil, que cambia varios valores a la vez para entrenar un modelo por tipo de foto, y el modo de prueba.

> En pantalla: Colab: la celda de configuración, de arriba abajo; después la celda de imports y dispositivo.

[Acción: celda de configuración, rutas y modo: líneas 1 a 25]

El segundo paso es la configuración. Es una celda larga de unas 120 líneas y probablemente la más útil del cuaderno porque ahí vive todo lo que se puede cambiar con un comentario junto a cada valor. No la vamos a leer entera. Veremos lo necesario para entender los pasos de hoy.

Arriba están el perfil y las rutas. La carpeta base en Drive y la de las fotos y el archivo de etiquetas. Hay un nombre que importa y es el de la corrida. Es único por corrida para que una nueva no sobrescriba a una anterior. Los modelos que tenemos salieron de corridas con nombre propio.

Sigue el modo. Está el modo de prueba que ya mencionamos. Está permitir CPU que viene apagado. Si no hay tarjeta gráfica el cuaderno se detiene para que no entrenes por error en un procesador donde tardaría muchísimo. Está reanudar que viene encendido. Y está una opción más. Incluir fotos sin etiquetas viene apagada. Una foto sin etiquetas casi siempre es una foto que todavía no se etiquetó. Usarla le enseñaría a la red que ahí no hay espermatozoides y la validación contaría como error todo lo que encuentre. Encendida sirve para otra cosa. Sirve para usar fotos que de verdad no tienen espermatozoides como ejemplos negativos. Es justo lo que le falta al proyecto como vimos en el módulo anterior.

[Acción: baja a «Clase» y «Preparación de la imagen»: líneas 26 a 37]

La clase se llama cabeza y es la etiqueta que se puso en CVAT. Por ahora significa espermatozoide visible completo con su primer tramo de cola.

Después viene la preparación de la imagen. Usar grises está encendido. Eso quiere decir que la red no ve el color sino solo el brillo. Se calcula como el valor más alto de los tres canales de color de cada píxel. Así funciona igual con tinciones de distinto color.

Invertir si el fondo es claro atiende al campo claro donde los espermatozoides son oscuros sobre un fondo claro. Con la opción activa se invierte el brillo y quedan claros sobre fondo oscuro como en fluorescencia. La idea es que la red aproveche lo que aprende de un tipo de foto en el otro. El propio comentario advierte que esto no está comprobado. Se comprobaría entrenando otra corrida con la opción apagada y comparando.

[Acción: baja a «Recortes y tamaño de la red»: líneas 38 a 53]

Ahora el tamaño de los recortes. Lado es lo que miden por lado los recortes de entrenamiento y las teselas del servidor. Las teselas ya las conoces del módulo 3 y son las mismas piezas en las que el servidor corta una foto grande.

Solape es el traslape entre teselas y su comentario dice algo que ya vimos desde el otro lado. Tiene que ser mayor que el objeto más grande. En campo claro el mayor mide 677 píxeles y en fluorescencia mide 116.

Más abajo hay valores sobre la red como las anclas y las máscaras y el máximo de detecciones. Pertenecen al video siguiente. Por ahora basta saber que existen y que están en la configuración y no escondidos en el código.

[Acción: baja a «Perfiles: un modelo por tipo de foto»: líneas 95 a 111]

Aquí está la pieza central de la celda. Los perfiles. Es un diccionario con tres entradas. Mixto va vacío y por eso conserva los valores de arriba con teselas de 1024. Fluorescencia cambia varias cosas. Usa teselas de 512 píxeles y traslape de 128 y no invierte. Campo claro cambia más. Las fotos se reducen a la mitad antes de todo porque sus espermatozoides son grandes. Además usa teselas de 640 y traslape de 384 e inversión del brillo.

Fíjate en cómo se aplica. Si el perfil no existe hay un error claro. Si existe una sola línea llamada globals update reemplaza los valores de arriba por los del perfil. Lo que el perfil no menciona se queda como estaba. Cambiar de un modelo a otro es cambiar una palabra.

[Acción: líneas 113 a 119, el modo de prueba y el mensaje final]

Y el modo de prueba en acción. Si está encendido fija las épocas en dos y los recortes por época en 16. Valida y guarda en cada época. Además agrega «_prueba» al nombre de la corrida para no mezclarla con una real. Al final se calcula la carpeta de salida formada por la base más la carpeta entrenamiento más el nombre de la corrida. Ahí se guardan los modelos y las gráficas y las revisiones.

[Acción: ejecuta la celda; aparece «MODO_PRUEBA activo» y la versión del cuaderno]

Al ejecutarla el cuaderno avisa que el modo de prueba está activo y muestra su versión y el perfil y el nombre de la corrida. Conviene mirar esa línea antes de seguir porque confirma qué es lo que vas a entrenar.

Una curiosidad. Los archivos de modelo que tenemos aquí guardan en su interior con qué versión del cuaderno se hicieron. El de fluorescencia dice 0.3.1 y el de campo claro dice 0.5.0 mientras que este cuaderno es el 0.5.1. Los pasos son los mismos. Lo que cambia son detalles de configuración.

[Acción: siguiente celda, imports y dispositivo: ejecútala]

La celda siguiente importa lo que falta y escoge el dispositivo. Usa la tarjeta gráfica si la hay y el procesador si no. Aquí está la protección de la que hablamos. Si resulta ser procesador y no se permitió el cuaderno se detiene con un mensaje.

También fija las semillas con el valor 42. Recuerda las semillas del módulo 1. Sirven para que lo que se hace al azar pueda repetirse y por eso con la misma semilla salen los mismos recortes al azar. Y crea la carpeta de salida.

[Pantalla 4 · Paso 3: leer las etiquetas]

> Idea central: El cuaderno lee el archivo de etiquetas de CVAT y revisa que todo cuadre con las fotos antes de gastar tiempo de tarjeta gráfica: que no falte ninguna foto, que mida lo que dice el archivo y que exista la etiqueta. Después imprime una tabla de fotos y de espermatozoides etiquetados.

> En pantalla: Colab: la celda del Paso 3, función `leer_anotaciones` y su salida.

[Acción: celda del Paso 3, función leer_anotaciones: líneas 17 a 47]

El tercer paso es leer las etiquetas y aquí el cuaderno hace algo que ahorra mucho tiempo. Revisa antes de entrenar. Si algo no cuadra se detiene con un mensaje claro antes de gastar tarjeta gráfica.

El archivo que sale de CVAT usa un formato llamado COCO. Es un archivo de texto con tres listas. Una de categorías y otra de imágenes y otra de anotaciones. Cada anotación dice a qué imagen pertenece y trae un polígono. Es la lista de puntos que rodea al espermatozoide.

La función empieza por la categoría. Si la etiqueta buscada no existe da un error y te dice cuáles hay. Luego busca las fotos en la carpeta. Para comparar nombres usa una función auxiliar que quita la carpeta y pone los acentos en una sola forma y no distingue mayúsculas. Parece un detalle pero no lo es. Un mismo nombre con acento puede guardarse de dos maneras según el sistema. Sin esta función una foto que sí existe aparecería como faltante.

Por cada imagen del archivo hace tres revisiones. Si la foto no está la anota para avisar. Si mide algo distinto de lo que dice el archivo da un error cuyo mensaje sugiere que puede ser otra versión de la foto. Y decide si es de fondo claro o de fondo oscuro. Para eso la reduce y mira la mediana del brillo. Si pasa de 127 es de fondo claro. Con eso el perfil descarta las fotos que no son de su tipo porque un perfil de fluorescencia no entrena con campo claro.

[Acción: líneas 49 a 84: las anotaciones y los avisos]

Después recorre las anotaciones. Se queda solo con las de la clase correcta y omite las que no tienen un polígono válido. Eso incluye las que vienen en formato de máscara comprimida y para esas muestra un aviso. Ese formato no es el que genera CVAT con polígonos.

De cada espermatozoide guarda cuatro cosas. Sus polígonos y la caja que lo rodea y el centro de esa caja y su área. El centro lo vamos a usar muchas veces. Y las coordenadas se multiplican por el factor de reducción. Si la foto se achica a la mitad las etiquetas también.

Al final se omiten las fotos que no tienen ninguna etiqueta con un aviso que explica cómo usarlas como ejemplos negativos.

[Acción: ejecuta la celda y muestra la tabla de fotos]

Al ejecutarla sale un resumen. Cuántas fotos y cuántos espermatozoides etiquetados. Una tabla con cada foto y su tamaño y su cantidad de etiquetas. Y el lado mayor de los espermatozoides con su mínimo y su mediana y su máximo. Si el más grande no cabe en el traslape aparece un aviso.

Con nuestras fotos de fluorescencia son cuatro fotos y 258 espermatozoides etiquetados. De campo claro también son cuatro fotos pero solo 45 espermatozoides. Conviene tener presentes estos dos números porque son pocos. Es una de las razones por las que no se entrena una red desde cero. Y es la razón por la que hay que cuidar tanto la validación. Eso es lo que sigue.

[Pantalla 5 · Paso 4: entrenamiento y validación]

> Idea central: La validación son zonas de las fotos que la red no ve al aprender, y sirven para medir si el modelo funciona de verdad. Con diez fotos o más se reservan fotos completas; con menos, de cada foto se reserva una franja, con un margen para que un mismo espermatozoide no quede en las dos zonas.

> En pantalla: Colab: la celda del Paso 4, función `crear_zonas` y su salida.

[Acción: celda del Paso 4, función crear_zonas, líneas 1 a 22]

El cuarto paso separa entrenamiento de validación. Ya lo vimos en teoría en el módulo 2. Una parte de los datos la red la ve para aprender y otra no la ve. Con esa segunda se mide si de verdad funciona. Aquí vemos cómo se hace en código.

La función crear zonas devuelve una lista de zonas. Cada una es un rectángulo de una foto marcado como entrenamiento o como validación. Hay dos casos.

Si hay diez fotos o más se reservan fotos completas. Una quinta parte y por lo menos una. Se escogen al azar con la semilla y por eso siempre salen las mismas.

Si hay menos de diez no se pueden apartar fotos enteras. Ese es nuestro caso. Entonces de cada foto se reserva una franja del lado más largo. La fracción de franja es un cuarto y por eso el corte cae a las tres cuartas partes. Lo que queda antes del corte es entrenamiento y lo que queda después es validación. Pero hay un margen llamado separación. La zona de entrenamiento termina cien píxeles antes del corte para que un mismo espermatozoide no quede mitad en cada zona.

Un ejemplo con una foto de 1,792 píxeles de ancho. Las tres cuartas partes son 1,344. Entrenamiento va de cero a 1,244 y validación va de 1,344 a 1,792. En medio queda una franja de cien píxeles que no se usa.

[Acción: ejecuta la celda: la tabla de zonas y los avisos]

Al ejecutarla sale una tabla con una fila por zona. Muestra su uso y sus coordenadas y cuántos espermatozoides contiene contados por su centro. Abajo salen los totales de entrenamiento y de validación.

Después vienen tres avisos que merecen atención. Si hay menos de 20 espermatozoides para validar avisa que las métricas serán poco confiables. Y si hay menos de 10 esa validación no sirve para elegir nada. El modelo que se guarda como el mejor será el de la última época y el umbral de seguridad se queda en el valor fijo 0.5.

Esto no es teórico. En campo claro con cuatro fotos la validación tiene apenas dos espermatozoides. El cuaderno lo avisa y por eso un resultado perfecto ahí no prueba nada. En la corrida de fluorescencia hay 66 en la validación y ahí sí se pueden elegir cosas. Aun así conviene decirlo con honestidad. Con cuatro fotos la validación sale de las mismas fotos con las que se entrena pero en franjas distintas. No equivale a probar con fotos que la red nunca vio.

La última línea calcula cuántos recortes se toman en cada época cuando no se fijó un número. Es el mayor entre un mínimo y una cantidad por foto. Con el perfil de fluorescencia son 400 y en modo de prueba son 16.

[Pantalla 6 · Paso 5: preparar las fotos]

> Idea central: Cada foto se lee una sola vez, se convierte en lo que va a ver la red y se guarda en disco local como arreglo de números. Así los recortes se sacan sin volver a decodificar el BMP. La función de preparación es la misma que usa el servidor, porque la red tiene que ver lo mismo al entrenar y al analizar.

> En pantalla: Colab: la celda del Paso 5, funciones `preparar_imagen` y `preparar_cache`, y el panel de archivos con la carpeta de caché.

[Acción: celda del Paso 5, función preparar_imagen, líneas 1 a 12]

El quinto paso prepara las fotos y aquí está la función más importante de todo el cuaderno aunque sea corta. Se llama preparar imagen. Recibe una foto de tres canales de color y devuelve lo que va a ver la red.

Su docstring lo dice sin ambigüedad. Debe ser idéntico en entrenamiento y en el servidor. Si la red aprendió con una versión de la foto y en el servidor ve otra los resultados se deterioran sin que haya ningún error a la vista. Por eso esta preparación está repetida a propósito en modelo punto py que es el archivo del módulo 3.

Veamos qué hace. Primero achica la foto con un método que promedia áreas si hay reducción. Después toma el valor máximo de los tres canales en cada píxel si se usan grises. Ese valor es el brillo. Luego mira la mediana del brillo. Si pasa de 127 el fondo es claro y si además la inversión está activada da vuelta los valores con 255 menos el valor. Termina asegurándose de que los datos queden contiguos en memoria.

[Acción: función preparar_cache, líneas 15 a 24]

La segunda función recorre las fotos y guarda el resultado de cada una en un archivo con extensión npy que es el formato de NumPy para guardar un arreglo. Lo hace en el disco local de Colab. Ese disco es rápido y se borra al cerrar.

El nombre del archivo lleva el identificador de la foto y una etiqueta que resume la preparación. Una g si son grises y una i si se invierte y el porcentaje de reducción. Para fluorescencia queda «g_r100» y para campo claro queda «gi_r50». Así si cambias la preparación no reutilizas por error un archivo preparado de otra manera. Y si el archivo ya existe no se rehace y por eso correr la celda otra vez es casi instantáneo.

¿Por qué guardar así? Una foto BMP pesa unos 30 megabytes y leerla y decodificarla cada vez que se necesita un recorte sería lentísimo. De esta forma se hace una sola vez. Además el arreglo en grises ocupa un tercio de lo que ocuparía con tres canales.

[Acción: ejecuta la celda y muestra la carpeta de caché en el panel de archivos]

Al ejecutarla imprime cuántas fotos preparó y cuánto tardó. Dice también cuántas son de fluorescencia y cuántas de campo claro. En el panel de archivos a la izquierda aparece la carpeta de caché con los archivos npy.

[Pantalla 7 · Paso 6: recortes y aumento de datos]

> Idea central: En cada paso la red recibe un recorte de lado por lado píxeles, no la foto entera. Cada recorte se arma al azar, con variaciones: volteos, giros, acercar o alejar, más o menos brillo y un poco de ruido. Se hace para que la red aprenda la forma y no se aprenda las fotos de memoria. Antes de entrenar se revisa a ojo que los contornos coincidan.

> En pantalla: Colab: la celda del Paso 6, funciones y la clase `RecortesEntrenamiento`; después la celda de revisión visual.

[Acción: celda del Paso 6, función mascara_local, líneas 1 a 16]

El sexto paso son los recortes. La foto entera es demasiado grande para la red y por eso en cada paso del entrenamiento recibe un recorte. Esos recortes no son siempre los mismos. Se arman al azar y cada uno lleva variaciones. Es el aumento de datos y con pocas fotos sirve para que la red vea muchas versiones distintas de lo mismo.

Primero va una función auxiliar llamada máscara local. Dibuja un espermatozoide dentro de una ventana. Toma sus polígonos y los desplaza y escala a la ventana y los rellena en una máscara. La descarta si casi no se ve. La condición es que queden visibles al menos 20 píxeles y al menos el 30 por ciento de su área. Un espermatozoide cortado por el borde del recorte cuenta si se ve lo suficiente.

[Acción: clase RecortesEntrenamiento, líneas 23 a 52: escoger dónde cortar]

Ahora la clase. Es un Dataset de PyTorch que es la pieza que le entrega ejemplos a la red. Tiene dos métodos importantes. Uno dice cuántos ejemplos hay por época y eso es la cantidad de recortes. El otro entrega un ejemplo.

Aquí hay algo ingenioso. El método recibe un índice y lo usa como semilla. Con la semilla fija y ese índice el generador al azar da siempre los mismos números. Así cada recorte puede repetirse exactamente y si uno sale raro lo puedes volver a generar.

Veamos cómo se arma. Lo primero es decidir dónde cortar. En el 80 por ciento de los casos el recorte se centra en un espermatozoide escogido al azar. En el 20 restante se corta en un lugar cualquiera de la foto. Esos recortes traen fondo y fibras y sirven para que la red también los vea.

Luego viene el tamaño. Se escoge un factor entre 0.8 y 1.25 que acerca o aleja la imagen un poco y que sirve para fotos de distinto tamaño. Se calcula cuánta foto original cabe en un recorte sin pasar nunca de la zona de entrenamiento. Eso garantiza que ningún recorte de entrenamiento invada la zona de validación.

[Acción: líneas 54 a 71 y 73 a 85: cortar el recorte y armar las máscaras]

Con eso se corta. Se carga el arreglo desde el caché sin traerlo entero a la memoria y se extrae el trozo. Si no mide lado por lado se reescala. Se usa promedio de áreas cuando hay que achicar e interpolación lineal cuando hay que agrandar.

Después vienen las máscaras. Para cada espermatozoide de la foto cuya caja toque la ventana se dibuja su máscara con la función de antes. Se descartan las que no se ven lo bastante. Las demás se acomodan en una pila con una máscara por espermatozoide.

[Acción: líneas 87 a 101: volteos, giros, brillo y ruido]

Y aquí las variaciones. Con un 50 por ciento de probabilidad hay un volteo horizontal y con otro 50 hay uno vertical. Además se gira un número al azar de veces de cero a tres en pasos de 90 grados. La foto y las máscaras reciben exactamente la misma transformación.

Después se alteran el brillo y el contraste. Se multiplica por un factor entre 0.7 y 1.3 y se suma un desplazamiento de menos 20 a más 20. Se agrega ruido al azar. Y si la imagen tuviera color se mezclan los canales para que no importe cuál es cuál. Al final se pasa a valores entre cero y uno. Como la red espera tres canales el gris se repite tres veces.

Piensa en lo que esto significa con cuatro fotos. Cada época de 400 recortes es una colección distinta con otros centros y otra escala y otro giro y otro brillo. La red nunca ve dos veces lo mismo.

[Acción: líneas 103 a 116: el objetivo que recibe la red]

Lo último que arma el método es lo que la red debe adivinar. Es el objetivo y es un diccionario con tres cosas. Las cajas que se calculan a partir de las máscaras ya giradas. Las etiquetas que son todas uno porque hay una sola clase. Y las máscaras.

La celda termina creando el conjunto y diciendo cuántos espermatozoides hay disponibles para centrar recortes. Son los de las zonas de entrenamiento.

[Acción: celda «Revisión visual de los recortes»: ejecuta y muestra las seis imágenes]

Antes de entrenar hay una revisión que no conviene saltarse. Esta celda toma seis recortes con las semillas de 1000 a 1005 y dibuja en verde el contorno de cada máscara sobre la imagen. El título de cada uno dice cuántos espermatozoides contiene.

Comprueba que el contorno verde coincida con el espermatozoide incluso girado o con otro brillo. Si algún contorno no coincide el error está en los datos y se corrige antes de entrenar. Descubrirlo aquí cuesta mucho menos que hacerlo después de una hora de entrenamiento.

[Pantalla 8 · Lo que ya está listo y lo que sigue]

> Idea central: Hasta aquí no hay red ni aprendizaje: hay datos preparados. Se leyeron las etiquetas, se separó la validación, se prepararon las fotos y se armaron recortes con variaciones. En el siguiente video se construye la red, se entrena, se mide, se mira el resultado y se exporta el modelo.

> En pantalla: Colab: la celda de introducción, con la lista de pasos.

[Acción: vuelve a la celda de introducción, la lista de pasos]

Un resumen de lo que vimos. Los seis primeros pasos del cuaderno. El entorno con tarjeta gráfica y Drive. La configuración concentrada en una sola celda con perfiles para cada tipo de foto. La lectura de las etiquetas con revisiones antes de gastar tiempo. La separación de entrenamiento y validación con un margen. La preparación de las fotos idéntica a la del servidor. Y los recortes al azar con variaciones que se revisan a ojo.

Observa que todavía no hay una red. Ni una sola pérdida ni una época. Buena parte del trabajo de un proyecto como este es esto. Datos limpios y bien separados y bien revisados. Una red excelente con datos mal preparados da resultados malos y a veces ni se nota.

En el siguiente video viene la parte que falta. Construimos la red a partir de una Mask R-CNN preentrenada y vemos cómo se mide si funciona. Entrenamos en modo de prueba. Leemos las gráficas y exportamos el archivo que se copia al servidor.

Gracias por acompañarme.
