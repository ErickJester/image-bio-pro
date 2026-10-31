# Guion del módulo 4, video 1 de 4: El cuaderno de Colab, primera parte (versión natural)

BioImage-Repro UAM · Módulo 4 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el módulo anterior.

*3,939 palabras, unos 22.5 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- El cuaderno `entrenamiento/entrenar_mask_rcnn.ipynb` abierto en Colab, con el entorno de ejecución en GPU y las fotos y el archivo de etiquetas en la carpeta de Drive que pide el cuaderno. Las celdas se corren en orden, desde la primera.
- En la configuración, `MODO_PRUEBA = True` y `PERFIL = "fluorescencia"`. Así no se mezcla con una corrida real y el cuaderno no entrena más de dos épocas cortas.
- Este video llega hasta la revisión visual de los recortes. El entrenamiento se corre en el video siguiente.

[Pantalla 1 · Un cuaderno de Colab y de dónde sale el modelo]

> Idea central: El sitio solo carga un archivo de modelo ya entrenado. Ese archivo sale de un cuaderno de Colab, que corre en una computadora de Google con tarjeta gráfica. El cuaderno hace diez cosas en orden; este video cubre las seis primeras, que llevan de las fotos y las etiquetas a los recortes con los que se entrena.

> En pantalla: Colab, el cuaderno `entrenar_mask_rcnn.ipynb`: la celda de introducción, la lista «Qué hace, paso a paso» y los requisitos.

[Acción: abre el cuaderno en Colab, celda de introducción, arriba del todo]

En el módulo anterior vimos el sitio funcionando. Subes una foto. El servidor carga un modelo. Los contornos se miden y salen los números. Pero hay algo que dimos por hecho. Ese modelo. Son dos archivos con extensión pt. Uno para fluorescencia y otro para campo claro. El servidor los lee y ya. ¿De dónde salen?

Salen de este cuaderno. Y este módulo se trata de eso y de lo que viene después. Cómo llega el sitio a internet. Son cuatro videos. Este y el siguiente recorren el cuaderno. Los dos últimos llevan el sitio a un servidor en la nube con su dominio y su candado de seguridad.

Primero qué es un cuaderno de Colab. Es un documento con celdas. Unas celdas llevan texto como esta de arriba. Otras llevan código y se ejecutan una por una en orden. Lo que se ejecuta no corre en tu computadora. Corre en una de Google que te presta durante un rato y que puede traer una tarjeta gráfica. Para entrenar una red hace falta esa tarjeta. Por eso se entrena aquí y no en el servidor del sitio. Ese servidor solo analiza fotos y lo hace con el procesador.

Y esa es la división de trabajo de todo el proyecto. El entrenamiento pasa una vez en Colab y produce un archivo. El sitio solo usa ese archivo.

Esta primera celda dice qué entrena. Una red de segmentación por instancias llamada Mask R-CNN. Dada una foto dibuja el contorno de cada espermatozoide. Y fíjate en una frase. La red aprende solo la forma. El color no interviene en la detección.

[Acción: baja a «Qué hace, paso a paso»]

Aquí está la lista de lo que hace el cuaderno en diez pasos. Prepara el entorno. Configura. Lee las etiquetas. Separa entrenamiento y validación. Prepara las fotos. Arma los recortes. Esos son los seis de hoy. Después construye la red. Entrena. Muestra resultados. Exporta el modelo. Esos cuatro pasos y una última sección sobre cómo mejorarlo van en el siguiente video.

Hay un detalle que sale ya en esta introducción. El cuaderno entrena un modelo por tipo de foto. Hay un valor llamado perfil que decide qué fotos se usan y con qué tamaños. Fluorescencia es de fondo oscuro. Campo claro es de fondo claro y con fotos reducidas a la mitad. Mixto junta los dos tipos en un solo modelo y es más lento. Ya lo vimos del otro lado en el servidor. Dos tipos de foto y dos modelos. Aquí es donde se hacen.

[Acción: baja a «Requisitos» y muestra la estructura de carpetas de Drive]

Los requisitos. Un entorno de ejecución con tarjeta gráfica. Y una carpeta en Google Drive con dos cosas. Las fotos etiquetadas en una carpeta y un archivo de etiquetas. Ese archivo sale de CVAT. Es la herramienta de anotación del módulo 2. Las fotos son del laboratorio. Se quedan en Drive y no se suben al repositorio.

Otros dos requisitos importan para hoy. El cuaderno tiene un modo de prueba. Entrena dos épocas muy cortas solo para comprobar que todo corre y guarda su salida en una carpeta aparte. Es el que vamos a usar en pantalla porque un entrenamiento completo tarda demasiado para un video. Y si Colab se interrumpe basta con ejecutar otra vez desde el principio. El entrenamiento continúa donde se quedó. Eso lo veremos en el siguiente video.

[Pantalla 2 · Paso 1: el entorno]

> Idea central: Colab ya trae PyTorch, torchvision, OpenCV y matplotlib, así que no hay que instalar nada. Las dos primeras celdas comprueban que hay tarjeta gráfica y conectan Google Drive.

> En pantalla: Colab: las celdas del Paso 1. Primero la que revisa la GPU, después la que conecta Drive.

[Acción: celda del Paso 1, comprobar GPU: ejecútala]

Paso uno. El entorno. No hay nada que instalar. Colab ya trae PyTorch. Es la biblioteca con la que se programan redes neuronales. También trae torchvision que tiene las redes ya hechas y las herramientas para imágenes. Y trae OpenCV y matplotlib.

Esta celda solo imprime las versiones y si hay tarjeta gráfica. Si la hay dice cuál es. La tarjeta que pide este cuaderno es una T4 de las que Colab da en su plan gratuito. Si dice que no hay tienes que cambiar el tipo de entorno de ejecución antes de seguir.

[Acción: celda siguiente, conectar Google Drive: ejecútala y acepta el permiso]

La segunda celda conecta Google Drive. La primera vez Google pide permiso y ese permiso lo das tú en tu cuenta. Fíjate en la estructura try y except. Si el código no está corriendo en Colab esa importación falla. En lugar de detenerse imprime un aviso y sigue con las rutas tal como están. Así el mismo cuaderno se puede abrir en otra computadora.

[Pantalla 3 · Paso 2: la configuración]

> Idea central: Todo lo que se puede ajustar está en una sola celda, con una explicación junto a cada valor. Lo más importante es el perfil, que cambia varios valores a la vez para entrenar un modelo por tipo de foto, y el modo de prueba.

> En pantalla: Colab: la celda de configuración, de arriba abajo; después la celda de imports y dispositivo.

[Acción: celda de configuración, rutas y modo: líneas 1 a 25]

Paso dos. La configuración. Es una celda larga de unas 120 líneas y es la más útil del cuaderno porque ahí vive todo lo que se puede cambiar. Cada valor lleva un comentario. No la vamos a leer entera. Vamos a ver lo que hace falta para entender los pasos de hoy.

Arriba están el perfil y las rutas. La carpeta base en Drive. La carpeta de las fotos. Y el archivo de etiquetas. Aquí hay un nombre que importa y es el nombre de la corrida. Es único por corrida para que una corrida nueva no sobrescriba una anterior. Los modelos que tenemos vienen de corridas con nombre propio.

Luego el modo. Modo de prueba que ya mencionamos. Permitir CPU está apagado. Si no hay tarjeta gráfica el cuaderno se detiene. Así no entrenas por error en un procesador que tardaría muchísimo. Reanudar está encendido. Y hay una opción más. Incluir fotos sin etiquetas está apagada. Una foto sin etiquetas casi siempre es una foto que todavía no se etiquetó. Si se usara le enseñaría a la red que ahí no hay espermatozoides y la validación contaría como error todo lo que encuentre. Encendida sirve para otra cosa. Sirve para usar fotos que de verdad no tienen espermatozoides como ejemplos negativos. Es justo lo que le falta al proyecto como vimos en el módulo anterior.

[Acción: baja a «Clase» y «Preparación de la imagen»: líneas 26 a 37]

La clase se llama cabeza. Es la etiqueta que se puso en CVAT. Por ahora significa espermatozoide visible completo con su primer tramo de cola.

Y la preparación de la imagen. Usar grises está encendido. Eso quiere decir que la red no ve el color. Ve solo el brillo. Se calcula como el valor más alto de los tres canales de color de cada píxel. Así funciona igual con tinciones de distinto color.

Invertir si el fondo es claro. En campo claro los espermatozoides son oscuros sobre un fondo claro. Con esta opción se invierte el brillo y quedan claros sobre fondo oscuro como en fluorescencia. La idea es que la red aproveche lo que aprende de un tipo de foto en el otro. El propio comentario avisa que no está comprobado. Se mediría entrenando otra corrida con la opción apagada y comparando.

[Acción: baja a «Recortes y tamaño de la red»: líneas 38 a 53]

Ahora el tamaño de los recortes. Lado. Los recortes de entrenamiento y las teselas del servidor miden lado por lado píxeles. Ya conoces las teselas del módulo 3. Son las mismas piezas en las que el servidor corta una foto grande.

Y solape que es el traslape entre teselas. El comentario dice algo que ya vimos desde el otro lado. Debe ser mayor que el objeto más grande. En campo claro el mayor mide 677 píxeles. En fluorescencia mide 116.

Debajo hay más valores sobre la red. Las anclas. Las máscaras. El máximo de detecciones. Son del video siguiente. Aquí solo quédate con que existen y que están en la configuración y no escondidos en el código.

[Acción: baja a «Perfiles: un modelo por tipo de foto»: líneas 95 a 111]

Aquí está la pieza central de la celda. Los perfiles. Es un diccionario con tres entradas. Mixto va vacío. Se queda con los valores de arriba que son teselas de 1024. Fluorescencia cambia cosas. Usa teselas de 512 píxeles y traslape de 128 y no invierte. Campo claro cambia más. Las fotos se reducen a la mitad antes de todo porque sus espermatozoides son grandes. Usa teselas de 640 y traslape de 384 e invierte el brillo.

Fíjate cómo se aplica. Si el perfil no existe hay un error claro. Y si existe una sola línea llamada globals update reemplaza los valores de arriba por los del perfil. Lo que el perfil no menciona se queda como estaba. Así cambiar de un modelo a otro es cambiar una palabra.

[Acción: líneas 113 a 119, el modo de prueba y el mensaje final]

Y el modo de prueba en acción. Si está encendido reemplaza las épocas por dos y los recortes por época por 16 y valida y guarda en cada época. Además agrega «_prueba» al nombre de la corrida para no mezclar una prueba con una corrida real. Al final se calcula la carpeta de salida. Es la base más la carpeta entrenamiento más el nombre de la corrida. Ahí se guardan los modelos y las gráficas y las revisiones.

[Acción: ejecuta la celda; aparece «MODO_PRUEBA activo» y la versión del cuaderno]

Al ejecutarla el cuaderno avisa que el modo de prueba está activo y dice su versión y el perfil y el nombre de la corrida. Es buena costumbre mirar esa línea antes de seguir. Te confirma qué vas a entrenar.

Una curiosidad. Los archivos de modelo que tenemos aquí guardan en su interior con qué versión del cuaderno se hicieron. El de fluorescencia dice 0.3.1. El de campo claro dice 0.5.0. Este cuaderno es el 0.5.1. Los pasos son los mismos. Cambian detalles de configuración.

[Acción: siguiente celda, imports y dispositivo: ejecútala]

La celda que sigue importa lo que falta y escoge el dispositivo. Usa la tarjeta gráfica si hay y el procesador si no. Y aquí está la protección que mencionamos. Si es procesador y no se permitió el cuaderno se detiene con un mensaje.

También fija las semillas con el valor 42. Recuerda las semillas del módulo 1. Sirven para que lo que se hace al azar se pueda repetir. Con la misma semilla salen los mismos recortes al azar. Y crea la carpeta de salida.

[Pantalla 4 · Paso 3: leer las etiquetas]

> Idea central: El cuaderno lee el archivo de etiquetas de CVAT y revisa que todo cuadre con las fotos antes de gastar tiempo de tarjeta gráfica: que no falte ninguna foto, que mida lo que dice el archivo y que exista la etiqueta. Después imprime una tabla de fotos y de espermatozoides etiquetados.

> En pantalla: Colab: la celda del Paso 3, función `leer_anotaciones` y su salida.

[Acción: celda del Paso 3, función leer_anotaciones: líneas 17 a 47]

Paso tres. Leer las etiquetas. Y aquí el cuaderno hace algo que ahorra mucho tiempo. Revisa antes de entrenar. Si algo no cuadra se detiene con un mensaje claro antes de gastar tarjeta gráfica.

El archivo que viene de CVAT usa un formato llamado COCO. Es un archivo de texto con tres listas. Una de categorías. Una de imágenes. Y una de anotaciones. Cada anotación dice a qué imagen pertenece. Trae también un polígono. Es la lista de puntos que rodea al espermatozoide.

La función empieza con la categoría. Si la etiqueta que buscamos no existe da un error y te dice cuáles hay. Luego busca las fotos en la carpeta. Para comparar nombres usa una función auxiliar. Quita la carpeta y pone los acentos en una sola forma y no distingue mayúsculas. Parece un detalle. No lo es. El mismo nombre con acento se puede guardar de dos maneras distintas según el sistema. Sin esto una foto que sí existe aparecería como faltante.

Por cada imagen del archivo hace tres revisiones. Si la foto no está la anota para avisar. Si mide algo distinto de lo que dice el archivo da un error. El mensaje dice que puede ser otra versión de la foto. Y decide si es de fondo claro o de fondo oscuro. Para eso una función reduce la foto y mira la mediana del brillo. Si la mediana pasa de 127 es de fondo claro. Con eso el perfil descarta las fotos que no son de su tipo. Un perfil de fluorescencia no entrena con campo claro.

[Acción: líneas 49 a 84: las anotaciones y los avisos]

Después recorre las anotaciones. Se queda solo con las de la clase correcta. Y omite las que no tienen un polígono válido. Si vienen en formato de máscara comprimida las omite con un aviso. Ese formato no es el que genera CVAT con polígonos.

Por cada espermatozoide guarda cuatro cosas. Sus polígonos. La caja que lo rodea. El centro de esa caja. Y su área. Ese centro lo vamos a usar muchas veces. Las coordenadas se multiplican por el factor de reducción. Si la foto se achica a la mitad las etiquetas también.

Al final las fotos sin ninguna etiqueta se omiten con un aviso que explica cómo usarlas como ejemplos negativos.

[Acción: ejecuta la celda y muestra la tabla de fotos]

Al ejecutarla sale un resumen. Cuántas fotos y cuántos espermatozoides etiquetados. Una tabla con cada foto y su tamaño y su cantidad de etiquetas. Y el lado mayor de los espermatozoides con su mínimo y su mediana y su máximo. Si el más grande no cabe en el traslape sale un aviso.

Con nuestras fotos de fluorescencia son cuatro fotos y 258 espermatozoides etiquetados. De campo claro también son cuatro fotos pero solo 45. Son dos números que conviene tener en la cabeza. Son pocos. Es una de las razones por las que no se entrena una red desde cero. Y es la razón por la que hace falta cuidar tanto la validación. Eso es lo que sigue.

[Pantalla 5 · Paso 4: entrenamiento y validación]

> Idea central: La validación son zonas de las fotos que la red no ve al aprender, y sirven para medir si el modelo funciona de verdad. Con diez fotos o más se reservan fotos completas; con menos, de cada foto se reserva una franja, con un margen para que un mismo espermatozoide no quede en las dos zonas.

> En pantalla: Colab: la celda del Paso 4, función `crear_zonas` y su salida.

[Acción: celda del Paso 4, función crear_zonas, líneas 1 a 22]

Paso cuatro. Separar entrenamiento de validación. Esto ya lo vimos en teoría en el módulo 2. Una parte de los datos la red la ve para aprender. Otra parte no la ve y con esa se mide si de verdad funciona. Aquí vemos cómo se hace en código.

La función crear zonas devuelve una lista de zonas. Cada zona es un rectángulo de una foto marcado como entrenamiento o como validación. Hay dos casos.

Si hay diez fotos o más se reservan fotos completas. Una quinta parte y por lo menos una. Se escogen al azar con la semilla y por eso siempre salen las mismas.

Si hay menos de diez no se pueden regalar fotos enteras. Ese es nuestro caso. Entonces de cada foto se reserva una franja del lado más largo. La fracción de franja es un cuarto y por eso el corte se hace a las tres cuartas partes. Lo que queda antes del corte es entrenamiento. Lo que queda después es validación. Pero hay un margen. La zona de entrenamiento termina cien píxeles antes del corte. Es la separación. Sirve para que un mismo espermatozoide no quede mitad en cada zona.

Un ejemplo. Una foto de 1,792 píxeles de ancho. Tres cuartas partes son 1,344. Entrenamiento va de cero a 1,244. Validación va de 1,344 a 1,792. Entre las dos queda una franja de cien píxeles que no se usa.

[Acción: ejecuta la celda: la tabla de zonas y los avisos]

Al ejecutarla sale una tabla. Cada fila es una zona con su uso y sus coordenadas. También dice cuántos espermatozoides tiene. Se cuenta por el centro de cada uno. Y abajo salen los totales de entrenamiento y de validación.

Después vienen tres avisos que merecen atención. Si hay menos de 20 espermatozoides para validar avisa que las métricas serán poco confiables. Y si hay menos de 10 no se puede elegir nada con esa validación. El modelo que se guarda como el mejor será el de la última época. Y el umbral de seguridad se queda en el valor fijo 0.5.

Esto no es teórico. En campo claro con cuatro fotos la validación tiene apenas dos espermatozoides. El cuaderno lo avisa y por eso un resultado perfecto ahí no prueba nada. En la corrida de fluorescencia hay 66 en la validación y ahí sí se pueden elegir cosas. Y recuerda algo que conviene decir con honestidad. Con cuatro fotos la validación sale de las mismas fotos con que se entrena pero en franjas distintas. No es lo mismo que probar con fotos que la red nunca vio.

La última línea calcula cuántos recortes se toman en cada época si no se fijó un número. Es lo mayor entre un mínimo y una cantidad por foto. Con el perfil de fluorescencia son 400. En modo de prueba son 16.

[Pantalla 6 · Paso 5: preparar las fotos]

> Idea central: Cada foto se lee una sola vez, se convierte en lo que va a ver la red y se guarda en disco local como arreglo de números. Así los recortes se sacan sin volver a decodificar el BMP. La función de preparación es la misma que usa el servidor, porque la red tiene que ver lo mismo al entrenar y al analizar.

> En pantalla: Colab: la celda del Paso 5, funciones `preparar_imagen` y `preparar_cache`, y el panel de archivos con la carpeta de caché.

[Acción: celda del Paso 5, función preparar_imagen, líneas 1 a 12]

Paso cinco. Preparar las fotos. Y aquí está la función más importante de todo el cuaderno aunque sea corta. Se llama preparar imagen. Recibe una foto de tres canales de color y devuelve lo que va a ver la red.

La docstring lo dice claro. Debe ser idéntico en entrenamiento y en el servidor. Si la red aprendió con una versión de la foto y en el servidor ve otra los resultados se deterioran sin que haya ningún error a la vista. Por eso esta preparación está duplicada a propósito en modelo punto py del módulo 3. Es lo que vimos ahí.

Qué hace. Primero achica la foto si hay reducción. Usa un método que promedia áreas para no perder calidad. Después si se usan grises toma el valor máximo entre los tres canales de cada píxel. Eso es el brillo. Luego mira la mediana del brillo. Si pasa de 127 el fondo es claro. Y si además está activada la inversión da vuelta los valores con 255 menos el valor. Termina asegurándose de que los datos estén contiguos en memoria.

[Acción: función preparar_cache, líneas 15 a 24]

La segunda función recorre las fotos y guarda el resultado de cada una en un archivo con extensión npy. Es el formato de NumPy para guardar un arreglo. Lo guarda en el disco local de Colab. Ese disco es rápido y se borra al cerrar.

El nombre del archivo lleva el identificador de la foto y una etiqueta con la preparación. Una letra g si son grises. Una i si se invierte. Y el porcentaje de reducción. Para fluorescencia queda «g_r100». Para campo claro queda «gi_r50». Así si cambias la preparación no reutilizas por error un archivo preparado de otra manera. Y si el archivo ya existe no se vuelve a hacer. Correr la celda otra vez es casi instantáneo.

¿Por qué guardar así? Una foto BMP pesa unos 30 megabytes y leerla y decodificarla cada vez que se necesita un recorte sería lentísimo. Aquí se hace una vez. Además el arreglo en grises ocupa un tercio de lo que ocuparía en tres canales.

[Acción: ejecuta la celda y muestra la carpeta de caché en el panel de archivos]

Al ejecutarla imprime cuántas fotos preparó y cuánto tardó. También dice cuántas son de fluorescencia y cuántas de campo claro. En el panel de archivos de la izquierda aparece la carpeta de caché con los archivos npy.

[Pantalla 7 · Paso 6: recortes y aumento de datos]

> Idea central: En cada paso la red recibe un recorte de lado por lado píxeles, no la foto entera. Cada recorte se arma al azar, con variaciones: volteos, giros, acercar o alejar, más o menos brillo y un poco de ruido. Se hace para que la red aprenda la forma y no se aprenda las fotos de memoria. Antes de entrenar se revisa a ojo que los contornos coincidan.

> En pantalla: Colab: la celda del Paso 6, funciones y la clase `RecortesEntrenamiento`; después la celda de revisión visual.

[Acción: celda del Paso 6, función mascara_local, líneas 1 a 16]

Paso seis. Los recortes. La foto entera es demasiado grande para la red. Por eso en cada paso del entrenamiento recibe un recorte. Y esos recortes no son siempre los mismos. Se arman al azar y cada uno lleva variaciones. Es el aumento de datos. Con pocas fotos sirve para que la red vea muchas versiones distintas de lo mismo.

Primero una función auxiliar llamada máscara local. Dibuja un espermatozoide dentro de una ventana. Toma sus polígonos. Los mueve y los escala a la ventana. Y los rellena en una máscara. Luego la descarta si casi no se ve. La condición es que tienen que quedar visibles al menos 20 píxeles y al menos el 30 por ciento de su área. Un espermatozoide cortado por el borde del recorte cuenta si se ve lo suficiente.

[Acción: clase RecortesEntrenamiento, líneas 23 a 52: escoger dónde cortar]

Ahora la clase. Es un Dataset de PyTorch. Es la pieza que le entrega ejemplos a la red. Tiene dos métodos importantes. El primero dice cuántos ejemplos hay por época. Eso es la cantidad de recortes. El segundo entrega un ejemplo.

Y aquí hay algo ingenioso. El método recibe un índice y ese índice se usa como semilla. Con la semilla fija y ese índice el generador al azar da siempre los mismos números. Así cada recorte se puede repetir exactamente. Si algo sale raro en un recorte lo puedes volver a generar.

Veamos cómo se arma. Lo primero es decidir dónde cortar. En el 80 por ciento de los casos el recorte se centra en un espermatozoide escogido al azar. En el otro 20 se corta en un lugar cualquiera de la foto. Esos recortes traen fondo y fibras y sirven para que la red también los vea.

Luego el tamaño. Se escoge un factor entre 0.8 y 1.25. Acerca o aleja la imagen un poco y sirve para fotos de distinto tamaño. Se calcula cuánta foto original cabe en un recorte y nunca más que la zona de entrenamiento. Eso garantiza que ningún recorte de entrenamiento se meta a la zona de validación.

[Acción: líneas 54 a 71 y 73 a 85: cortar el recorte y armar las máscaras]

Con eso se corta. Se carga el arreglo desde el caché sin traerlo todo a la memoria y se extrae el trozo. Si no mide lado por lado se reescala. Cuando hay que achicar se usa el promedio de áreas. Cuando hay que agrandar se usa interpolación lineal.

Después las máscaras. Para cada espermatozoide de la foto cuya caja toque la ventana se dibuja su máscara con la función de antes. Las que se descartan se descartan. Las demás se acomodan en una pila. Una máscara por espermatozoide.

[Acción: líneas 87 a 101: volteos, giros, brillo y ruido]

Y aquí las variaciones. Con un 50 por ciento de probabilidad hay un volteo horizontal. Con otro 50 hay uno vertical. Y se gira un número al azar de veces de cero a tres en pasos de 90 grados. La foto y las máscaras reciben exactamente la misma transformación.

Después el brillo y el contraste. Se multiplica por un factor entre 0.7 y 1.3 y se suma un desplazamiento de menos 20 a más 20. Se agrega ruido al azar. Y si la imagen tuviera color se mezclan los canales para que no importe cuál es cuál. Al final se pasa a valores entre cero y uno. Como la red espera tres canales el gris se repite tres veces.

Piensa en lo que esto hace con cuatro fotos. Cada época de 400 recortes es una colección distinta con otros centros y otra escala y otro giro y otro brillo. La red nunca ve dos veces lo mismo.

[Acción: líneas 103 a 116: el objetivo que recibe la red]

Lo último que arma el método es lo que la red debe adivinar. Es el objetivo. Un diccionario con tres cosas. Las cajas que se calculan a partir de las máscaras ya giradas. Las etiquetas que son todas uno porque hay una sola clase. Y las máscaras.

La celda termina creando el conjunto. Y dice cuántos espermatozoides hay disponibles para centrar recortes. Son los de las zonas de entrenamiento.

[Acción: celda «Revisión visual de los recortes»: ejecuta y muestra las seis imágenes]

Antes de entrenar hay una revisión que no hay que saltarse. Esta celda toma seis recortes con las semillas de 1000 a 1005 y dibuja en verde el contorno de cada máscara sobre la imagen. Cada título dice cuántos espermatozoides tiene el recorte.

Mira que el contorno verde coincida con el espermatozoide incluso girado o con otro brillo. Si un contorno no coincide el error está en los datos y se corrige antes de entrenar. Es mucho más barato descubrirlo aquí que después de una hora de entrenamiento.

[Pantalla 8 · Lo que ya está listo y lo que sigue]

> Idea central: Hasta aquí no hay red ni aprendizaje: hay datos preparados. Se leyeron las etiquetas, se separó la validación, se prepararon las fotos y se armaron recortes con variaciones. En el siguiente video se construye la red, se entrena, se mide, se mira el resultado y se exporta el modelo.

> En pantalla: Colab: la celda de introducción, con la lista de pasos.

[Acción: vuelve a la celda de introducción, la lista de pasos]

Un resumen. Vimos los seis primeros pasos del cuaderno. El entorno con tarjeta gráfica y Drive. La configuración en una sola celda con perfiles para cada tipo de foto. La lectura de las etiquetas con revisiones antes de gastar tiempo. La separación de entrenamiento y validación con un margen. La preparación de las fotos idéntica a la del servidor. Y los recortes al azar con variaciones que se revisan a ojo.

Fíjate que todavía no hay una red. Ni una sola pérdida ni una época. Casi todo el trabajo de un proyecto como este es esto. Datos limpios y bien separados y bien revisados. Una red excelente con datos mal preparados da resultados malos y a veces ni se nota.

En el siguiente video viene la parte que falta. Construimos la red a partir de una Mask R-CNN preentrenada. Vemos cómo se mide si funciona. Entrenamos en modo de prueba. Leemos las gráficas. Y exportamos el archivo que se copia al servidor.

Gracias por acompañarme.
