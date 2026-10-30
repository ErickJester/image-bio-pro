# Guion del módulo 3, video 2 de 4: Inferencia con recortes (versión natural)

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

*4,163 palabras, unos 23.8 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- El entorno de Python y el sitio se preparan como en el video 1 (sección Entorno de Python del guion o de su guía de pantalla). Aquí no hace falta el navegador, solo el editor y la terminal.
- Los dos archivos del modelo, `fluorescencia.pt` y `campo_claro.pt`, tienen que estar en la carpeta `model/`. No están en Git. Sin ellos, los comandos de la terminal que cargan el modelo fallan.
- Cuatro comandos para la terminal, ya probados, que están en la guía de pantalla: el tipo de foto, las posiciones de las teselas, el contenido del archivo del modelo y el conteo de detecciones por puntaje. El último tarda unos segundos.

[Pantalla 1 · De la caja negra al código]

> Idea central: La ruta analizar le entrega una imagen a una función y recibe contornos. Esa función está en modelo.py, y hace la inferencia: usar un modelo ya entrenado. Son cuatro pasos: elegir el modelo, preparar la foto, cortarla en teselas y juntar los resultados.

> En pantalla: Editor, `app/analisis/modelo.py`: el comentario inicial (líneas 1 a 15) y la función `detectar` (línea 248).

[Acción: editor, app/analisis/modelo.py, líneas 1 a 15]

En el video anterior vimos el camino de una imagen por el backend. En un punto de ese camino, la ruta analizar le entregaba la imagen a una función y recibía contornos. Dijimos que dentro de esa función estaba el modelo. Hoy abrimos esa función. Vive en el archivo modelo.py.

Antes de entrar, una palabra. Entrenar un modelo es ajustar sus pesos con ejemplos. Eso se hizo en Google Colab, como vimos en el módulo 2. Usar un modelo ya entrenado, con una foto nueva, se llama inferencia. Es lo que hace el servidor. No aprende nada. Solo aplica lo que el modelo ya aprendió. Y es mucho más ligero que entrenar, por eso alcanza con el procesador.

Este comentario inicial resume el trabajo en cuatro pasos. Uno: medir el brillo de la foto para elegir el modelo. Dos: preparar la foto igual que en el entrenamiento. Tres: cortarla en teselas con traslape, y que cada una pase por la red. Y cuatro: juntar los resultados y quitar los repetidos.

[Acción: línea 248: la función detectar]

Fíjate en una frase de ese comentario: el procedimiento tiene que seguir igual al del cuaderno de entrenamiento. Es la regla de oro de este archivo. La red aprendió a ver fotos preparadas de cierta manera. Si el servidor las prepara distinto, la red recibe algo que nunca vio, y responde peor sin avisar. Todo lo que sigue copia lo que hace el cuaderno.

Otro detalle de diseño. Este archivo no depende de Flask. No sabe nada de rutas ni de usuarios. Recibe una foto y devuelve contornos. Por eso se puede probar solo, sin levantar el sitio.

[Pantalla 2 · Dos modelos y cómo se elige]

> Idea central: Hay un modelo por tipo de foto: fluorescencia, de fondo oscuro, y campo claro, de fondo claro. Se elige con una regla de brillo, no con aprendizaje: la mediana del brillo máximo por píxel de la foto reducida, contra 127.

> En pantalla: Editor, `modelo.py`: `ARCHIVOS` y los umbrales (líneas 26 a 29) y `tipo_de_foto` (64 a 68); después terminal, el comando A de la guía, y el editor en `tests/test_modelo.py`, líneas 18 a 24.

[Acción: modelo.py, líneas 26 a 29: ARCHIVOS y los umbrales]

Hay dos modelos, uno por tipo de foto. La línea 26 es un diccionario. En Python es una tabla de pares nombre y valor. Aquí, el tipo de foto y el archivo de su modelo. Fluorescencia es para fotos de fondo oscuro, donde las células brillan. Campo claro es para fotos de fondo claro, con las células oscuras.

La línea 27 tiene la regla para distinguirlos: 127. Es la mitad de la escala del brillo, que va de 0, negro, a 255, blanco. La línea 28 es otro umbral, que veremos más adelante. Y la 29 dice cuántas teselas se procesan a la vez.

[Acción: líneas 64 a 68: tipo_de_foto]

Ahora la función que decide, tipo de foto. Hace tres cosas. Primero, reduce la foto a un octavo de su tamaño, con resize. No hace falta mirar todos los píxeles para saber si el fondo es oscuro o claro. Así es mucho más rápido. Segundo, para cada píxel toma el valor más alto de sus tres canales, rojo, verde y azul. Eso se escribe max con eje 2, y es el brillo máximo del píxel. Y tercero, calcula la mediana de todos esos valores, que es el valor del medio al ordenarlos. Si es mayor que 127, la foto es de campo claro. Si no, de fluorescencia.

¿Por qué la mediana y no el promedio? Porque no se deja engañar por unos pocos píxeles. En una foto de fluorescencia casi todo es negro, y hay unas cuantas células muy brillantes. Con el promedio, esas células subirían un poco el resultado. Con la mediana, que mira el valor del medio, el fondo manda.

[Acción: terminal: comando A de la guía, el tipo de la imagen de ejemplo]

Probémoslo con la imagen de ejemplo del sitio. El comando carga la imagen, la pasa a esta función y muestra el resultado: fluorescencia. Y fíjate que esto es una regla, no un modelo que aprendió. Es una decisión simple, que se puede explicar y verificar.

[Acción: tests/test_modelo.py, líneas 18 a 24]

Así lo comprueba una prueba. Una foto toda negra es fluorescencia. Una foto toda gris clara es campo claro. Y unos cuantos puntos blancos sobre fondo negro siguen siendo fluorescencia, justo por usar la mediana.

[Pantalla 3 · El archivo del modelo]

> Idea central: Cada archivo .pt trae dos cosas: los pesos de la red y la configuración con la que se entrenó. El sitio lee todo de ahí, así que un modelo nuevo se cambia sin tocar el código. Los dos modelos difieren en el tamaño de tesela, el traslape, la reducción y el umbral.

> En pantalla: Terminal, comando C de la guía; después `model/README.md`, y el editor en `modelo.py`, líneas 36 a 39 y 119 a 123.

[Acción: terminal: comando C de la guía, el contenido del archivo del modelo]

Veamos qué hay dentro de un archivo de modelo. Este comando lo abre y muestra sus partes. Son cinco. Una versión. El state dict, que son los pesos: millones de números, los mismos que se ajustaron al entrenar. La época en la que se guardó y la medida de acierto en la validación. Y una que importa mucho para este video: config, la configuración.

La configuración dice con qué reglas se entrenó el modelo, y el servidor las usa tal cual. Estos son los valores del modelo de fluorescencia. Teselas de 512 píxeles, con un traslape de 128. Cinco tamaños de anclas, de 16 a 256. Hasta 300 detecciones por tesela. Un umbral de 0.6 para quitar cajas repetidas dentro de la red. Y un umbral de detección de 0.9: solo se conservan los contornos con un puntaje de 0.9 o más.

[Acción: model/README.md]

El modelo de campo claro tiene otros valores, porque se entrenó con otro tipo de foto. Sus teselas son de 640 píxeles, con un traslape de 384. La foto se reduce a la mitad antes de analizarla. Se invierte, para que lo oscuro quede brillante. Y su umbral de detección es 0.5. Esta es la ventaja de guardar la configuración dentro del archivo. El código no tiene esos números escritos. Los lee. Si mañana hay un modelo mejor, se copia el archivo nuevo a la carpeta y el sitio lo usa. Y por eso estos archivos no están en Git: pesan unos 176 megabytes cada uno y se copian aparte.

[Acción: modelo.py, líneas 36 a 39: carpeta_modelos]

La función carpeta modelos dice dónde buscarlos. En la carpeta que diga la variable de entorno MODELOS_DIR y, si no existe, en la carpeta model del proyecto. En el servidor, la configuración de Docker apunta esa variable a una carpeta de solo lectura.

[Pantalla 4 · Armar y cargar la red]

> Idea central: La red se arma con la misma arquitectura del módulo 2, con los valores de la configuración, y se le cargan los pesos del archivo. Se carga una sola vez y se guarda en memoria, con un candado para que dos peticiones no la carguen a la vez. La carga es segura y comprueba que los pesos coincidan.

> En pantalla: Editor, `modelo.py`: `_construir_red` (líneas 82 a 103), `_hilos` (106 a 108) y `_cargar` (111 a 137).

[Acción: modelo.py, _construir_red, líneas 82 a 103]

Ahora, cómo se arma la red. Esta función, construir red, es la arquitectura Mask R-CNN del módulo 2 escrita en código, con torchvision, la parte de PyTorch para visión. La línea 93 crea la red. Y le dice weights igual a None. No descarga pesos preentrenados, porque los pesos van a venir del archivo.

Los valores que le damos salen de la configuración. El tamaño de entrada, que es el de la tesela, para que la red no la cambie de tamaño. Los tamaños y proporciones de las anclas. El máximo de detecciones. El umbral para quitar cajas repetidas. Y el tamaño del recorte para la máscara, 14 o 28 según el modelo.

La línea 100 cambia la cabeza de clasificación para que distinga dos clases: fondo y espermatozoide. Y la 101 hace lo mismo con la cabeza de máscara. Es la misma idea del video de transferencia. Se reutiliza todo y se reemplaza la última pieza.

[Acción: líneas 73 a 79 y 102: la normalización congelada]

La línea 102 cambia las capas de normalización por una versión congelada, con el valor numérico exacto del entrenamiento. Es un ajuste fino para que el servidor calcule lo mismo que el cuaderno.

[Acción: líneas 106 a 108: _hilos]

Luego, los hilos. La función hilos decide cuántos hilos de procesador usa PyTorch. Los que diga la variable TORCH_HILOS o, si no existe, hasta cuatro, según los núcleos que tenga la computadora.

[Acción: líneas 111 a 118: _cargar, el candado y el diccionario]

Ahora, cargar el modelo. Cargarlo es lento, porque hay que leer 176 megabytes y armar la red. Por eso se hace una sola vez, la primera que se pide, y se guarda en un diccionario que se llama _CARGADOS. Las siguientes peticiones lo toman de ahí, de memoria. Y la línea 113 usa un candado. Recuerda que Gunicorn atiende varias peticiones a la vez, con hilos. Si dos llegan juntas con el modelo sin cargar, sin candado lo cargarían dos veces. Con el candado, la primera entra y carga. La segunda espera, y lo encuentra ya cargado.

[Acción: líneas 119 a 126: la carga segura]

La carga es segura. Un archivo de PyTorch es, por dentro, un paquete de datos de Python. Y un paquete así podría esconder código que se ejecuta al abrirlo. La opción weights only igual a True le dice a PyTorch que solo acepte números y datos simples. El archivo guarda la versión de PyTorch con un tipo propio, y esa pieza se permite aparte. Y si la configuración no trae el valor del entrenamiento, el código se detiene con un mensaje claro. No calcula algo distinto en silencio.

[Acción: líneas 127 a 137: cargar los pesos y comprobar]

Después se arma la red y se le cargan los pesos. Y se comprueba que coincidan. Si faltan pesos o sobran, el código se detiene. Al final, eval deja la red en modo de uso, no de aprendizaje, y se guarda en el diccionario.

[Pantalla 5 · Preparar la foto]

> Idea central: Antes de la red, la foto se prepara exactamente como en el entrenamiento: se reduce si el modelo lo pide, se queda con el brillo máximo de los canales y, en campo claro, se invierte. La red nunca ve la foto original.

> En pantalla: Editor, `modelo.py`, `preparar_imagen` (líneas 142 a 152); después `tests/test_modelo.py`, líneas 32 a 40.

[Acción: modelo.py, preparar_imagen, líneas 142 a 152]

Ahora, la foto. La función preparar imagen convierte la foto en lo que la red va a ver. Y, otra vez, tiene que ser igual a lo que hizo el cuaderno. Lo hace en tres pasos.

[Acción: líneas 144 a 148: reducir]

Primero, reducir. Si la configuración trae una reducción, como la mitad en campo claro, la foto se achica con resize. El método de la línea 148, INTER_AREA, calcula cada píxel nuevo como el promedio del área que reemplaza. Es lo más cuidadoso al achicar. Se reduce porque el modelo de campo claro se entrenó con la foto a la mitad, y la red tiene que ver lo mismo que vio al aprender.

[Acción: línea 149: el brillo máximo]

Segundo, escala de grises por brillo máximo. En lugar de promediar los tres canales, se toma el más alto de cada píxel, con max sobre el eje 2. Así, una cabeza roja, una amarilla y una naranja quedan igual de brillantes, que es lo que importa para encontrarlas. Y la foto pasa de tres canales a uno.

[Acción: líneas 150 a 152: invertir]

Y tercero, en campo claro, invertir. La línea 150 comprueba si el modelo pide invertir y si el fondo es claro. Si es así, la línea 151 hace 255 menos cada valor. Lo claro se vuelve oscuro y lo oscuro, claro. Así las células quedan brillantes sobre fondo oscuro, que es como la red aprendió a verlas, y sirve el mismo tipo de red para los dos casos. La última línea solo acomoda los datos en memoria.

[Acción: tests/test_modelo.py, líneas 32 a 40]

La prueba lo comprueba con una foto inventada. Un fondo rosa claro con un filamento oscuro. Después de preparar, la imagen mide la mitad de ancho y de alto, y el filamento queda más claro que el fondo. Y sin invertir, queda más oscuro.

[Pantalla 6 · Las teselas]

> Idea central: La red trabaja con recortes del tamaño con el que se entrenó. La foto se corta en teselas con traslape: el paso es la tesela menos el traslape, y la última de cada fila y de cada columna se pega al borde. La imagen de ejemplo da 9 teselas.

> En pantalla: Editor, `modelo.py`: `_posiciones` (líneas 155 a 158) y la lista de teselas (192 a 195); terminal, comando B de la guía, y `figuras/teselas.png`; después `tests/test_modelo.py`, líneas 43 a 46.

[Acción: modelo.py, _posiciones, líneas 155 a 158]

Llegamos a lo que da nombre al video. La red se entrenó con recortes de 512 por 512, y una foto puede medir miles de píxeles. Darle la foto entera sería pesado, y la red vería los espermatozoides a otra escala. Así que se corta la foto en teselas. Cada una del tamaño con el que se entrenó, y cada una pasa por la red.

Este es el corte. La función posiciones recibe el largo de la foto, el lado de la tesela y el paso, y devuelve en qué posiciones empieza cada tesela. Si la foto cabe en una tesela, devuelve solo el cero. Si no, empieza en cero y avanza de paso en paso. Y al final agrega una última posición, la del largo menos el lado, para que la última tesela llegue justo al borde.

[Acción: líneas 192 a 195: lado, paso y la lista de teselas]

En la función de inferencia, el paso es el lado menos el traslape: 512 menos 128 da 384. Cada tesela avanza 384 píxeles y comparte 128 con la anterior. La línea 195 arma la lista de todas las teselas con dos ciclos en una sola línea. Una por fila, y dentro, una por columna. Cada tesela es un par: su posición en x y en y.

[Acción: terminal: comando B de la guía, las posiciones de la imagen de ejemplo]

Con la imagen de ejemplo, de 1200 por 900, pasa esto. A lo ancho, las posiciones son 0, 384 y 688. A lo alto, 0, 384 y 388. Tres por tres: nueve teselas.

[Acción: abre figuras/teselas.png]

Así se ven sobre la imagen, cada una con su posición. Y mira lo que pasa en la altura. La segunda fila empieza en 384 y la tercera en 388, casi en el mismo lugar. Es porque la última tesela se pega al borde, y la foto mide 900. Es un efecto pequeño de este método: a veces la última tesela casi repite a la anterior. No daña el resultado. Solo cuesta un poco más de cómputo.

[Acción: tests/test_modelo.py, líneas 43 a 46]

La prueba comprueba las dos reglas. Que la última tesela llegue siempre al borde. Y que una foto más chica que la tesela dé una sola posición.

Con los números del proyecto, una foto de 1792 por 1374 da 20 teselas en fluorescencia. Y una de 3584 por 2748 da 63. En campo claro, como la foto se reduce a la mitad y las teselas son más grandes, son 4 y 24. Más teselas significa más tiempo de análisis.

[Pantalla 7 · Cada tesela por la red]

> Idea central: Cada tesela se convierte en un tensor y pasa por la red, de dos en dos, sin calcular gradientes. Las teselas de las orillas se rellenan con ceros, la imagen en grises se repite en tres canales y los valores se escalan de 0 a 1.

> En pantalla: Editor, `modelo.py`, `_inferir` (líneas 188 a 209): el lote (196 a 199), las teselas de las orillas (202 a 205), la conversión (206 y 207) y la llamada a la red (208).

[Acción: modelo.py, _inferir, líneas 188 a 199: el lote]

Ahora, cada tesela por la red. La línea 197 abre un bloque con inference mode. Cuando se entrena, PyTorch guarda cálculos intermedios para saber cómo ajustar los pesos. Son los gradientes. Al usar el modelo no hacen falta, y este bloque le dice que no los guarde. Ahorra memoria y tiempo.

Las teselas no se procesan una por una, sino en lotes de dos. Un lote es un grupo de entradas que pasan juntas por la red, y es más eficiente que ir de una en una. Y son solo dos, un número pequeño, para no gastar mucha memoria, porque el servidor tiene poca. Las líneas 198 y 199 recorren la lista de teselas de dos en dos.

[Acción: líneas 200 a 205: recortar y rellenar]

Para cada tesela, la línea 202 recorta de la foto el cuadrado que empieza en su posición. Y si la tesela queda más chica que el lado, porque la foto es más chica que 512 o está en una orilla, las líneas 203 a 205 la rellenan con ceros, que es negro, hasta completar el cuadrado. La red siempre recibe cuadrados del mismo tamaño.

[Acción: líneas 206 y 207: convertir a tensor]

Y ahora la conversión. La red de torchvision espera tres canales, así que la imagen en grises se repite tres veces con np.repeat. Luego se convierte en un tensor, que es la forma de tabla de números que usa PyTorch. Y se divide entre 255 para que los valores vayan de 0 a 1, y no de 0 a 255.

[Acción: línea 208: red(entradas)]

La línea 208 llama a la red con el lote. Lo que devuelve es una lista, una entrada por tesela. Y cada entrada trae lo que vimos en el módulo 2: las cajas, los puntajes y las máscaras de cada detección.

[Pantalla 8 · Lo que sale de la red]

> Idea central: De cada detección se usan la máscara y el puntaje. La máscara viene como probabilidades y se convierte en blanco y negro con 0.5. Las detecciones con puntaje menor a 0.05 se tiran. La caja se calcula de la propia máscara.

> En pantalla: Editor, `modelo.py`, `_inferir`, líneas 209 a 217.

[Acción: modelo.py, líneas 209 y 210: las máscaras y los puntajes]

Veamos qué se hace con lo que sale. La línea 209 toma las máscaras. La red las entrega como probabilidades: un número entre 0 y 1 para cada píxel, que dice qué tan probable es que ese píxel sea parte del espermatozoide. Con el signo mayor que 0.5, cada píxel pasa a ser verdadero o falso. Es la máscara en blanco y negro. La línea 210 toma los puntajes, que dicen qué tan segura está la red de cada detección.

[Acción: líneas 211 a 213: el puntaje mínimo]

Después, cada detección. Si su puntaje es menor que 0.05, la constante UMBRAL_MINIMO, se descarta de inmediato. Son detecciones en las que la red casi no confía, y guardarlas solo gastaría memoria. Es distinto del umbral de detección de 0.9, que se aplica al final. El mínimo es un filtro para tirar basura. El de 0.9 es la decisión de cuáles se aceptan.

[Acción: líneas 214 a 217: la caja]

Y las líneas 214 a 217 calculan la caja de la máscara. Buscan qué filas y qué columnas tienen al menos un píxel verdadero, y toman la primera y la última de cada una. Esas cuatro posiciones son los bordes de la caja que encierra la detección.

[Pantalla 9 · Lo que toca el borde interno]

> Idea central: Una detección que toca el borde de una tesela por dentro puede estar cortada. Se descarta, porque la tesela vecina la verá entera. Después se pasan las coordenadas de la tesela a las de la foto.

> En pantalla: Editor, `modelo.py`, `_inferir`, líneas 218 a 226; después `figuras/teselas.png`.

[Acción: modelo.py, líneas 218 a 221: el borde interno]

Aquí viene la parte más ingeniosa. Un espermatozoide que queda justo en el borde entre dos teselas aparece cortado en una de ellas. La red lo vería a medias, y su contorno saldría mal. Pero gracias al traslape, la tesela vecina lo ve entero, porque comparten esa franja.

Entonces la regla es sencilla. Si una detección toca un borde interno de la tesela, se descarta. Las líneas 219 a 221 revisan los cuatro lados. Por ejemplo, si la caja llega al borde izquierdo y la tesela no está en el extremo izquierdo de la foto, esa detección puede estar cortada, y se ignora. Pero en los bordes de la foto sí se conserva, porque ahí no hay vecina que la vea mejor.

[Acción: líneas 222 a 226: coordenadas de la foto]

Hasta ahora, todo está en coordenadas de la tesela: la posición 0, 0 es su esquina. Pero necesitamos las de la foto completa. La línea 222 recorta la máscara a lo que cae dentro de la foto, para quitar el relleno de ceros. Y la 225 suma la posición de la tesela a la caja. Así, una detección que en la tesela empieza en la columna 100, en una tesela que empieza en la columna 384 de la foto, queda en la columna 484. Y se guarda como un diccionario: la caja, la máscara, el área y el puntaje.

[Pantalla 10 · Juntar y quitar repetidos]

> Idea central: Con el traslape, un espermatozoide puede salir en dos teselas. Se ordenan por puntaje y se descarta cada uno que se parezca a uno ya conservado, con IoU de 0.5 o más. Después, un filtro propio quita los contornos que ya están dentro de otro en un 50 por ciento o más.

> En pantalla: Editor, `modelo.py`: `_interseccion` y `_iou` (líneas 161 a 173), la deduplicación (227 a 231) y `_quitar_repetidos` (176 a 183); después `tests/test_modelo.py`, líneas 49 a 56.

[Acción: modelo.py, líneas 227 a 231: la deduplicación]

Ya tenemos las detecciones de todas las teselas, en coordenadas de la foto. Pero, por el traslape, un mismo espermatozoide puede haberse detectado dos veces, una en cada tesela. Las líneas 227 a 231 lo corrigen. Primero ordenan todo por puntaje, de mayor a menor. Luego recorren la lista, y se quedan con una detección solo si no se parece a ninguna de las que ya conservaron.

[Acción: líneas 161 a 173: _interseccion y _iou]

Y se parece se mide con el IoU, que vimos en el módulo 2: la intersección entre las dos máscaras, entre su unión. Sirve para saber qué tanto se encima una detección con otra. La función interseccion alinea las dos cajas y cuenta los píxeles donde las dos máscaras son verdaderas a la vez, con count_nonzero. Y IoU divide eso entre la suma de las dos áreas menos la intersección. Si el IoU es 0.5 o más, son la misma, y se queda la de mayor puntaje.

[Acción: líneas 176 a 183: _quitar_repetidos]

El segundo filtro es propio del proyecto. A veces la red dibuja un espermatozoide entero y, aparte, un trozo del mismo. El IoU entre un contorno pequeño y el grande que lo contiene es bajo, por la diferencia de tamaño, y el primer filtro no los detecta. Así que aquí se mide otra cosa: qué parte del área de un contorno ya está cubierta por uno conservado. Se recorren de mayor a menor puntaje. Y se descarta el contorno si la mitad o más de su área ya está cubierta.

[Acción: tests/test_modelo.py, líneas 49 a 56]

La prueba lo muestra con números. Hay un cuadrado grande de 40 por 40, con puntaje de 0.95. Otro de 10 por 10, que cabe entero dentro del grande, con 0.80. Y un tercero aparte, con 0.90. Al aplicar el filtro quedan dos: el grande y el que está aparte. El que estaba adentro se fue.

[Pantalla 11 · De la máscara al contorno]

> Idea central: Lo último es convertir cada máscara en un contorno, en las coordenadas de la foto original, y quedarse con los de puntaje igual o mayor al umbral guardado en el modelo. En la imagen de ejemplo, la red devuelve 75 detecciones, 57 de 0.5 o más y 41 de 0.9 o más. Salen en orden de lectura.

> En pantalla: Editor, `modelo.py`: `_a_contorno` (líneas 237 a 245) y `detectar` (248 a 267); terminal, comando D de la guía; después `figuras/puntajes.png`.

[Acción: modelo.py, _a_contorno, líneas 237 a 245]

Falta pasar de máscaras a contornos, que es lo que el resto del sitio usa. Esta función toma la máscara de una detección y busca su contorno con findContours, de OpenCV, la biblioteca de imágenes. La opción RETR_EXTERNAL pide solo el borde exterior, sin los huecos. Si hay varios contornos, se queda con el de mayor área. Luego le suma la posición de la caja, para llevarlo a las coordenadas de la foto. Y lo divide entre la reducción, para volver a la foto original, no a la reducida. Un contorno es una lista de puntos.

[Acción: modelo.py, detectar, líneas 248 a 267]

Ahora, la función que une todo, detectar. Primero elige el modelo. Luego lo carga, que ya vimos que es una sola vez. Luego, dentro de un candado que vemos en un momento, prepara la foto y la infiere. Y entonces aplica el umbral de detección, el que guarda el modelo: 0.9 en fluorescencia y 0.5 en campo claro. Solo pasan las detecciones con un puntaje igual o mayor.

Los contornos salen ordenados por su posición. Primero por la fila de la caja y luego por la columna. Es el orden de lectura, de arriba abajo y de izquierda a derecha. Por eso, en la imagen marcada del sitio, los números van en ese orden. Al final, la función devuelve los contornos y un diccionario con información: qué modelo se usó, su versión, el umbral y los puntajes.

[Acción: terminal: comando D de la guía, el conteo por puntaje]

Veamos qué hace cada filtro con la imagen de ejemplo. Este comando analiza la imagen y cuenta las detecciones. La red devolvió 75, ya sin repetidos. De esas, 57 tienen un puntaje de 0.5 o más. Y 41 tienen 0.9 o más. Esas son las que llegan al sitio. Por eso el resultado dice 41 espermatozoides.

[Acción: abre figuras/puntajes.png]

En esta imagen están las 75 por color. En verde, las 41 que pasan el umbral. En naranja, las que tienen entre 0.5 y 0.9. En rojo, las de menos de 0.5. Casi todos los verdes están sobre cabezas, aunque unos pocos caen sobre colas largas, como vimos en el módulo 2. Muchos de los rojos y los naranjas están sobre colas, que la red no debería aceptar. El umbral de 0.9 se eligió, como vimos en el módulo 2, probando varios con la validación, para dejar pasar las cabezas y frenar lo demás. No es perfecto, pero es la decisión que se tomó.

[Pantalla 12 · Un análisis a la vez]

> Idea central: El análisis usa un candado para que solo uno corra a la vez, porque el procesador del servidor no da para dos y cada modelo ocupa unos 176 megabytes. Los hilos de Gunicorn siguen atendiendo el resto del sitio mientras tanto.

> En pantalla: Editor, `modelo.py`: los candados (líneas 31 a 33), `detectar` (255 a 258) y `_hilos` (106 a 108); después `docker-compose.yml`, líneas 8 a 11.

[Acción: modelo.py, líneas 31 a 33: los candados]

Ahora, algo que viene del video anterior. Gunicorn atiende varias peticiones a la vez, con cuatro hilos. Pero el análisis es pesado, y el servidor tiene un solo núcleo y poca memoria. Si dos análisis corrieran juntos, se estorbarían. Y los dos tardarían más que uno detrás del otro.

Por eso hay dos candados. El de la línea 31 es de carga: asegura que el modelo se cargue una sola vez. El de la 32, que se llama de inferencia, es el que nos importa aquí.

[Acción: línea 256: with _BLOQUEO_INFERENCIA]

En la línea 256 está su uso. Un análisis que quiere correr entra en el bloque con with, y toma el candado. Mientras lo tiene, cualquier otro análisis que llegue se queda esperando en esa línea. Cuando el primero termina, suelta el candado, y entra el siguiente. Es una fila de espera.

Eso no bloquea el resto del sitio. Las otras páginas las atienden los otros hilos de Gunicorn, y las personas pueden seguir navegando. Solo los análisis hacen fila. Y, desde el punto de vista de quien espera, es lo que vimos de la cubierta de espera.

[Acción: docker-compose.yml, líneas 8 a 11]

Hay dos variables que ajustan esto desde fuera. MODELOS_DIR, que ya vimos, dice dónde están los archivos. Y TORCH_HILOS fija cuántos hilos de procesador usa PyTorch en cada análisis. Si no se define, el código usa hasta cuatro, según los núcleos que tenga el servidor.

[Pantalla 13 · Si no hay modelo y cómo se comprueba]

> Idea central: Sin PyTorch o sin los archivos de modelo, el sitio no se cae: usa una detección provisional por color y lo avisa en rojo. Las pruebas comprueban cada pieza sin los modelos, y una prueba aparte comprueba que el sitio da los mismos conteos que el cuaderno. Eso prueba la integración, no la calidad científica.

> En pantalla: Editor, `modelo.py`: `disponible` y `motivo_no_disponible` (líneas 46 a 61); después `app/analisis/medicion.py`: `detectar_espermatozoides` (101 a 114); y `tests/test_modelo.py`, líneas 27 a 29 y 59 a 71.

[Acción: modelo.py, líneas 46 a 61: disponible y motivo]

Un sitio no debería caerse porque falte un archivo. La función disponible comprueba dos cosas. Que PyTorch esté instalado, y que estén los dos archivos de modelo. Y motivo no disponible devuelve un texto que explica qué falta, si falta algo.

[Acción: medicion.py, detectar_espermatozoides, líneas 101 a 114]

Y esto se usa en el módulo de medición, que es el siguiente video. Esta función intenta primero el modelo. Si no está disponible, o si falla en pleno análisis, usa una detección provisional. Busca los píxeles rojos brillantes con un umbral de color. Es mucho más tosca, y por eso el sitio lo avisa con un recuadro rojo, que dice que los modelos no se cargaron y que el conteo no es confiable. Es una red de seguridad, no una alternativa.

[Acción: tests/test_modelo.py, líneas 27 a 29]

Y las pruebas. Casi todas corren sin PyTorch ni archivos de modelo, porque prueban piezas pequeñas. Elegir el tipo de foto. Preparar la foto. Calcular las posiciones de las teselas. Quitar repetidos. Y saber si el modelo está disponible. Por eso son rápidas.

[Acción: tests/test_modelo.py, línea 59 y siguientes]

La prueba con los modelos reales es la excepción. Solo corre si están PyTorch y los dos archivos, y si se pide con una variable de entorno, PROBAR_MODELOS. Pone unas manchas rojas sobre un fondo negro, las pasa por el modelo, y comprueba que los contornos que salen tengan forma correcta y estén dentro de la foto.

Además, se comprobó una vez que el sitio da los mismos conteos que el cuaderno en cinco fotos: 114, 9, 2, 1 y 43 contornos. Esa es la verificación de que este archivo copia bien al cuaderno. Y hay que decirlo con cuidado. Eso comprueba que el sitio usa bien el modelo. No comprueba que el modelo cuente bien. La calidad científica se evalúa aparte, con las imágenes anotadas.

[Pantalla 14 · Lo que vimos y lo que sigue]

> Idea central: Vimos cómo el servidor usa el modelo: lo elige por el brillo, lo carga una vez, prepara la foto como en el entrenamiento, la corta en teselas, descarta lo que toca el borde interno, junta los resultados y aplica el umbral. En el siguiente video, la medición: del contorno a las medidas.

> En pantalla: Vuelve al editor, en `modelo.py`, línea 248, mientras das el resumen y te despides.

[Acción: vuelve al editor, modelo.py, línea 248]

Un resumen.

Vimos qué es la inferencia: usar un modelo ya entrenado, como hace el servidor. El archivo modelo.py tiene cuatro pasos. Elegir el modelo con una regla de brillo, la mediana contra 127. Cargarlo una sola vez, con candado, de forma segura, leyendo su configuración del propio archivo. Preparar la foto igual que en el entrenamiento: reducir, tomar el brillo máximo y, en campo claro, invertir. Y cortarla en teselas con traslape.

Cada tesela pasa por la red, en lotes de dos y sin gradientes. De cada detección se usan la máscara y el puntaje. Las que tocan el borde interno de una tesela se descartan, porque la vecina las ve enteras. Las coordenadas se pasan a las de la foto. Se quitan los repetidos con el IoU y con el filtro de contenido. Y se aplica el umbral de detección, el que trae el modelo.

También vimos que solo un análisis corre a la vez, que el sitio sigue funcionando sin modelo, con un aviso, y qué comprueban las pruebas y qué no.

En el siguiente video entramos a la medición. La red ya entregó los contornos. Ahora el código los mide: el área, el largo, la escala y la distribución de tamaños. Y veremos los retos que tuvo el proyecto.

Gracias por acompañarme.
