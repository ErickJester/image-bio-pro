# Guion del módulo 4, video 2 de 4: El cuaderno de Colab, segunda parte (versión natural)

BioImage-Repro UAM · Módulo 4 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

*4,034 palabras, unos 23.1 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de celda, se ejecuta o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- El mismo cuaderno del video anterior, abierto en Colab y con las celdas hasta la revisión visual de los recortes ya ejecutadas, en `MODO_PRUEBA = True` y `PERFIL = "fluorescencia"`. Si la sesión se cerró, se vuelven a correr desde la primera.
- En este video se ejecuta el entrenamiento, pero solo las dos épocas cortas del modo de prueba. Las cifras que salgan son de una prueba, no de un modelo bueno.
- La carpeta `model/` del proyecto abierta en el explorador de archivos para el último tramo.

[Pantalla 1 · Paso 7: la red]

> Idea central: La red no se construye desde cero: se parte de una Mask R-CNN preentrenada con COCO, que ya sabe ver bordes y formas, y solo se cambia la última capa para que reconozca una clase, la cabeza. Los ajustes del cuaderno (anclas, detalle de la máscara, tamaño de entrada) se cambian en la configuración, y una pieza cuida que el modelo cargado en el servidor calcule lo mismo que el entrenado.

> En pantalla: Colab: el texto del Paso 7 y la celda `construir_modelo`, con su ejecución.

[Acción: abre el cuaderno en la celda del Paso 7, «La red», el texto de arriba]

En el video anterior dejamos los datos listos, con las fotos preparadas, una validación apartada y recortes al azar con su revisión visual. Pero todavía no había una red. Hoy la construimos y la entrenamos, vemos cómo le fue y sacamos el archivo que se lleva al servidor.

Empezamos por el Paso 7, que usa una idea que ya conoces del módulo 2: el aprendizaje por transferencia, el de la guitarra y el ukulele. No se entrena una red desde cero sino que se parte de una Mask R-CNN preentrenada con COCO, una colección de millones de objetos cotidianos. Esa red ya sabe ver bordes y formas y lo único que se le enseña es que existe una clase nueva, la cabeza. Con pocas fotos funciona bien y con cuatro fotos no hay otra opción.

El texto menciona varios ajustes pensados para este problema. Las anclas son los tamaños de caja con los que la red busca objetos y cada perfil pone las suyas, de 16 a 256 píxeles en fluorescencia y de 32 a 512 en campo claro. Las máscaras tienen más detalle para que alcancen a los filamentos delgados. La entrada no se reescala para no perder detalle y se aceptan hasta 300 detecciones por tesela.

Una última frase aclara que se usa la versión con capas de normalización congeladas porque es estable con lotes pequeños, que son los que caben en la tarjeta gratuita de Colab.

[Acción: celda del Paso 7, función construir_modelo: líneas 18 a 27, las opciones]

Veamos la función. Construir modelo tiene dos modos. Con preentrenado en verdadero sirve para entrenar y descarga los pesos de COCO, y con falso sirve para cargar un modelo que ya se entrenó sin necesitar internet. Ese segundo modo es el que usa el servidor y lo veremos al final del video.

Lo primero es armar las opciones. Se crea un generador de anclas con los tamaños de la configuración y tres formas de caja, una mitad de alta que ancha, una cuadrada y una del doble de alta. El lado de entrada tiene el mismo mínimo y máximo para que la red reciba los píxeles tal cual, y también se fija el máximo de detecciones por tesela. El umbral para quitar cajas muy traslapadas vale 0.6 y está alto a propósito, porque los espermatozoides cruzados se traslapan y no hay que descartarlos por eso. Por último se define el tamaño con el que la red dibuja la máscara de cada objeto.

[Acción: líneas 28 a 37: los pesos de COCO y las dos clases]

Aquí se decide con qué pesos empieza la red. Para entrenar se usan los pesos de COCO, pero solo se ajustan los tres últimos bloques de la parte que ve la imagen. Los primeros se quedan congelados porque lo que aprenden son bordes y texturas simples, y eso sirve para cualquier foto.

Después viene el cambio importante. La red de COCO distingue 91 clases y nosotros tenemos dos, que son fondo y espermatozoide. Por eso se reemplazan las dos últimas piezas, la que clasifica la caja y la que dibuja la máscara, por unas nuevas con dos clases. Solo esas empiezan de cero y todo lo demás conserva lo que ya sabía.

[Acción: líneas 38 a 44 y 9 a 15: la normalización congelada]

Queda un parámetro que parece pequeño y no lo es, el de la normalización. Una red tiene capas de normalización que mantienen los números en un rango razonable. Al entrenar con los pesos de COCO torchvision usa versiones congeladas de esas capas, con un valor interno llamado épsilon que puede ser cero. Al cargar un modelo sin esos pesos se arman capas normales con otro épsilon, de 0.00001.

El comentario explica que esa diferencia mínima se acumula a lo largo de toda la red hasta cambiar los resultados. Por eso, cuando se carga un modelo ya entrenado, se cambian las capas por las congeladas con el mismo épsilon que se usó al entrenar, y ese valor viaja guardado dentro del archivo. La función auxiliar de las líneas 9 a 15 recorre la red y hace el cambio capa por capa.

Es una pieza que no se ve desde afuera. Si faltara el servidor no daría ningún error y solo daría resultados un poco distintos a los del entrenamiento.

[Acción: líneas 47 a 50: ejecuta la celda; imprime los parámetros]

Al ejecutarla el cuaderno crea el modelo, lo manda a la tarjeta gráfica y cuenta los parámetros. Un parámetro es un número que la red ajusta al aprender, y la celda imprime cuántos hay en total y cuántos se ajustan al entrenar.

La primera vez la descarga de los pesos de COCO tarda un momento. Con esta configuración son unos 43.9 millones de parámetros y se ajustan casi todos, unos 43.7 millones. Lo que se congela es el primer bloque de la parte que ve la imagen, que es poco en cantidad de números aunque sean los de las formas más simples.

[Pantalla 2 · Paso 8: cómo se mide si funciona]

> Idea central: Para saber si la red funciona hay que medirla igual que en producción: cortar la zona de validación en teselas, juntar resultados, quitar repetidos y comparar cada contorno con las etiquetas. Un contorno acierta si coincide al menos 50 % con una etiqueta. Con eso salen cuatro cifras: precisión, exhaustividad, F1 y AP50.

> En pantalla: Colab: el texto del Paso 8 y la celda de las funciones de medida, de arriba abajo.

[Acción: celda del Paso 8, el texto de las métricas]

Paso ocho, cómo se mide si funciona. La clave está en la primera frase del texto: se analiza cada zona de validación completa, igual que en producción. No tendría sentido medir de una manera y usar la red de otra.

Un espermatozoide detectado cuenta como acierto si su contorno coincide al menos 50 por ciento con el etiquetado, que es el IoU que vimos en el módulo 2. Con eso salen cuatro cifras. La precisión dice qué parte de lo que la red marcó era un espermatozoide de verdad. La exhaustividad, que en inglés se llama recall, dice qué parte de los espermatozoides etiquetados encontró. El F1 es un promedio de las dos y el AP50 mide la calidad global sin escoger un umbral de seguridad.

[Acción: celda de métricas, función detectar: líneas 37 a 85]

La celda que sigue es larga pero casi todo ya lo conoces. Empiezo por la función detectar porque es la misma lógica que vimos en el módulo 3, en modelo punto py.

Recibe una foto o una zona ya preparada y la corta en teselas con traslape. Una función auxiliar calcula las posiciones paso a paso y la última tesela se alinea con el borde. Con una foto de 1,792 por 1,374 píxeles y teselas de 512 salen cinco columnas y cuatro filas, es decir 20 teselas. Las teselas pasan por la red en grupos, de cada objeto se guarda su máscara y su puntaje y se descartan los de puntaje menor a 0.05.

Después vienen tres defensas, las mismas que vimos desde el servidor. Si el objeto toca un borde interno de una tesela se descarta porque lo verá entero la tesela vecina. Los duplicados entre teselas se resuelven con el IoU y se queda el de mayor puntaje. Y al final se quitan los repetidos dentro de un mismo espermatozoide con el filtro de contenido.

[Acción: líneas 1 a 28: interseccion_mascaras, iou_mascaras y quitar_repetidos]

Las funciones del principio de la celda son las piezas. Intersección de máscaras cuenta cuántos píxeles comparten dos contornos: se fija solo en la zona donde se cruzan las cajas y cuenta los píxeles encendidos en las dos máscaras.

El IoU es esa intersección dividida entre la unión. Por ejemplo dos cuadrados de 10 por 10 corridos cinco píxeles comparten 50, la unión es 150 y el IoU es un tercio.

Y quitar repetidos recorre las detecciones de mayor a menor puntaje y descarta una si la mitad o más de su área ya está cubierta por otra que se conservó. Ese valor sale de la configuración y se llama UMBRAL_CONTENIDO.

[Acción: líneas 88 a 118: etiquetas_de_zona y aciertos_de_zona]

Ahora toca comparar con las etiquetas. Etiquetas de zona toma los espermatozoides etiquetados que caen dentro de una zona y para dibujar sus máscaras reutiliza la función del video anterior, máscara local.

Aciertos de zona empareja detecciones con etiquetas. Va de la más segura a la menos segura y a cada detección le busca la etiqueta con la que más se traslapa entre las que todavía no se usaron. Si el IoU llega a 0.5 es un acierto y esa etiqueta queda usada, así que un espermatozoide etiquetado no se puede contar como encontrado dos veces. La función devuelve una lista de pares con el puntaje y si fue acierto o no.

[Acción: líneas 121 a 139: la función metricas]

Y la función que calcula las cifras. Primero ordena los pares por puntaje y con eso arma, para cada puntaje posible, cuántos aciertos y cuántos errores llevaría acumulados. De ahí salen dos curvas, la de precisión y la de exhaustividad. El AP50 es el área bajo esa curva, o sea la calidad que tendría la red si se probaran todos los umbrales posibles.

Después usa el umbral que se le pasa, que por defecto es 0.5, para contar cuántas detecciones tienen puntaje igual o mayor y cuántas de ellas acertaron. Con eso saca la precisión, el recall y el F1.

Un ejemplo. Hay 10 espermatozoides etiquetados y la red marca 8, de los cuales 6 son correctos. La precisión es 6 entre 8, o sea 0.75, y la exhaustividad es 6 entre 10, o sea 0.6. El F1, que es el promedio de las dos, sale 0.667. Cuatro espermatozoides no se encontraron y dos de las marcas sobraron.

[Acción: líneas 142 a 157: pares_de_validacion y validar; ejecuta la celda]

Las dos últimas funciones lo juntan todo. Pares de validación recorre solo las zonas de validación, corta cada una de la foto preparada, la analiza con detectar, saca sus etiquetas y las compara. Después validar le pasa eso a métricas.

Esta celda solo define funciones y por eso al ejecutarla no imprime nada, pero todo lo que sigue las usa.

[Pantalla 3 · Paso 9: preparar el entrenamiento]

> Idea central: Antes de entrenar, el cuaderno prepara tres cosas: guardar sin arriesgar el archivo, la configuración que el servidor necesita y el optimizador con su programa de tasa de aprendizaje. Si ya hay una corrida guardada, la reanuda, siempre que la configuración sea la misma.

> En pantalla: Colab: el texto del Paso 9 y la celda de preparación, de arriba abajo, y su ejecución.

[Acción: celda del Paso 9, el texto de arriba y las líneas 1 a 28: guardar sin riesgo y la configuración]

Paso nueve, entrenar. El texto de arriba resume lo que viene. Cada época toma recortes nuevos al azar y se usa un método de descenso del gradiente con calentamiento y un descenso suave de la tasa de aprendizaje. En la tarjeta gráfica se usa precisión mixta para ir más rápido y con menos memoria. Cada cierto número de épocas se valida y si mejora se guarda el mejor modelo, y si Colab se corta basta con volver a correr todo desde el principio.

Veamos cómo se logra eso. Primero hay una función chiquita llamada escribir atómico que guarda en un archivo temporal y después lo renombra. Así, si la sesión se corta justo en medio de guardar, no queda un archivo roto sino el anterior intacto.

Luego hay dos funciones de configuración. La primera reúne todo lo que el servidor necesita saber para usar el modelo igual que aquí, que es el tamaño de tesela, el traslape, las anclas, si usa grises, el umbral, la versión del cuaderno, el épsilon y las versiones de PyTorch y torchvision. Todo eso viaja dentro del archivo y por eso el sitio puede cambiar un modelo por otro sin tocar el código.

La segunda reúne lo que no se puede cambiar a la mitad de una corrida. Es la primera sin los valores que sí pueden cambiar entre sesiones, más los de entrenamiento, que son las épocas, los recortes por época, el lote, la tasa de aprendizaje, la semilla y la lista de fotos. Más abajo veremos para qué sirve.

[Acción: líneas 31 a 46: el optimizador y el programa de la tasa de aprendizaje]

Ahora el optimizador, que es SGD, descenso del gradiente por lotes, y tiene dos ingredientes. El momento vale 0.9 y hace que cada paso arrastre algo de la dirección del anterior para avanzar más suave. El decaimiento de pesos castiga a los números grandes para que la red no se pase de ajustada. Se aplica solo a los parámetros que se ajustan.

La tasa de aprendizaje no es fija y la función factor de la tasa describe cómo cambia. Durante las primeras 100 iteraciones sube poco a poco desde casi cero, que es el calentamiento, para que los primeros pasos no sean bruscos con una red a medio adaptar. Después baja con una curva suave llamada coseno hasta quedar en el uno por ciento de su valor inicial.

En el entrenamiento real son 100 iteraciones por época y 60 épocas, así que el calentamiento dura una época. En el modo de prueba son 8 iteraciones en total y el calentamiento nunca termina, por eso la tasa se queda baja. Es normal y es otra razón por la que esas cifras no valen como resultado.

Las últimas líneas preparan la precisión mixta, que solo se usa si hay tarjeta gráfica.

[Acción: líneas 48 a 68: reanudar; ejecuta la celda]

Y ahora la parte que protege tu tiempo. Si reanudar está encendido y existe un archivo ultimo punto pt en la carpeta de salida, el cuaderno lo carga, pero antes compara la configuración guardada con la actual. Si algo cambió, por ejemplo la tasa de aprendizaje o las fotos, se detiene con un error que lista cada diferencia y ofrece tres salidas: usar un nombre de corrida nuevo, apagar reanudar y empezar de cero, o devolver la configuración anterior. Es mejor detenerse que mezclar dos entrenamientos distintos sin darse cuenta.

Si todo coincide restaura el modelo, el optimizador, el planificador, el escalador y el historial, y sigue desde la época siguiente. Imprime en qué época reanuda, y si el entrenamiento ya había terminado avisa que lo omite.

En la primera corrida no hay archivo y por eso al ejecutar la celda no imprime nada.

[Pantalla 4 · Paso 9: entrenar]

> Idea central: Cada época arma recortes nuevos, la red calcula su pérdida, el optimizador ajusta los parámetros y, cada cierto número de épocas, se valida y se guarda. El mejor modelo se guarda aparte del último punto de control. En el modo de prueba son dos épocas cortas, y se ve el formato de lo que imprime, no un resultado.

> En pantalla: Colab: la celda de entrenamiento, de arriba abajo, y su ejecución.

[Acción: celda de entrenamiento, líneas 1 a 25: el ciclo de cada época]

Llegamos a donde se aprende. Esta es la celda de entrenamiento y casi todo lo que hemos visto converge aquí.

Hay un ciclo por época. Se pone la red en modo de entrenamiento y se calculan las semillas de la época: cada época usa un tramo distinto de números, desde la época por los recortes por época hasta el tramo siguiente. Recuerda del video anterior que el índice de cada recorte es su semilla. Por eso cada época ve recortes nuevos y si se reanuda en la época cinco esa época vuelve a ver exactamente los mismos recortes. El cargador entrega los recortes en lotes.

Por cada lote las imágenes y los objetivos pasan a la tarjeta gráfica y se llama a la red con precisión mixta pasándole los objetivos. Cuando se le dan objetivos en modo de entrenamiento la red no devuelve detecciones sino pérdidas, un diccionario con las cinco que vimos en el módulo 2. La pérdida total es su suma.

Si la pérdida deja de ser un número normal el cuaderno se detiene, dice en qué época pasó y sugiere bajar la tasa de aprendizaje.

Después vienen los pasos de siempre. Se ponen en cero los gradientes, la retropropagación calcula cuánto contribuyó cada parámetro al error con el escalador de la precisión mixta, y se recorta el gradiente a una norma máxima de 10 para que ningún paso sea demasiado grande. Luego el optimizador da el paso y el planificador ajusta la tasa para la siguiente iteración.

[Acción: líneas 27 a 51: validar, guardar y mostrar]

Al terminar la época se anota un registro con el número de época, la pérdida promedio y la tasa de aprendizaje.

Cada cierto número de épocas, o en la última, se valida con la función validar, que usa todo lo del Paso 8. Y aquí se decide cuál es el mejor modelo. Si el AP50 mejoró se guarda un archivo llamado mejor punto pt con los pesos, la configuración, la época y el AP50, y si la validación no es confiable, como vimos en el video anterior, se queda siempre el último. Todo con escritura atómica.

Cada cierto número de épocas se guarda además ultimo punto pt, el punto de control completo, con el optimizador, el planificador y el historial. Es el que permite reanudar y pesa unos 350 megabytes, por eso no se guarda en cada época. El historial también se escribe cada vez en un archivo de texto.

Por último el cuaderno imprime una línea por época con el número, la pérdida y los minutos transcurridos. Si hubo validación agrega el AP50, la precisión, el recall y el F1, y una marca si ese fue el mejor.

[Acción: ejecuta la celda: las dos épocas del modo de prueba]

En el modo de prueba la celda corre dos épocas de 16 recortes y valida en las dos. Mira el formato de las líneas.

Un aviso importante para leer lo que sale. Con dos épocas cortas y una tasa de aprendizaje que casi no sube la red no aprende nada útil, así que las cifras de pérdida y de validación sirven solo para comprobar que todo corre de principio a fin sin errores. En la corrida real son 60 épocas con 400 recortes cada una, la validación se hace cada cinco épocas y el punto de control se guarda cada diez.

[Pantalla 5 · Paso 10: los resultados]

> Idea central: Se leen primero las gráficas de pérdida y de validación; si la pérdida baja pero la validación no mejora, la red se aprende las fotos de memoria. Después se carga el mejor modelo, se prueban varios umbrales de seguridad, se escoge el de mejor F1 si la validación alcanza, y se dibujan las fotos con lo que encontró la red. Con pocos espermatozoides en la validación, el propio cuaderno avisa que las cifras son inestables.

> En pantalla: Colab: las celdas del Paso 10, con sus salidas y una de las fotos de revisión.

[Acción: celda del Paso 10, el texto «Cómo leer las gráficas» y la gráfica: ejecuta]

Paso diez, los resultados. Primero cómo leer las gráficas. La pérdida debe bajar y si sube o se queda plana desde el principio algo anda mal. Las métricas de validación deben subir. Y si la pérdida baja pero la validación no mejora o empeora, la red se está aprendiendo las fotos de memoria. Es el sobreajuste del módulo 2 y la solución es una sola: más fotos etiquetadas.

La celda dibuja dos gráficas. A la izquierda va la pérdida por época y a la derecha las cuatro métricas de validación en las épocas en las que se validó. También guarda la imagen en la carpeta de salida. Con dos épocas solo hay dos puntos pero la gráfica sale.

[Acción: celda del mejor modelo, líneas 1 a 7: ejecuta]

La siguiente celda carga el mejor modelo, que no es necesariamente el de la última época, y lo mide una última vez. Imprime en qué época fue, su AP50 y las métricas finales con el umbral de 0.5.

[Acción: líneas 9 a 23: el barrido de umbrales y la elección]

Aquí hay una decisión práctica: ¿con qué seguridad mínima conviene contar un objeto? La red da un puntaje a cada contorno. Un umbral alto evita falsos positivos como las fibras y uno bajo encuentra más espermatozoides. No hay uno correcto porque depende del equilibrio que se busque.

El cuaderno lo resuelve con una prueba. Prueba siete umbrales de 0.3 a 0.9, mide precisión, recall y F1 en cada uno e imprime una tabla. Escoge el de mejor F1 y si hay empate el más cercano a 0.5.

Pero con una condición. Si la validación tiene menos de 10 espermatozoides no alcanza para elegir y se usa el umbral por defecto, y si tiene menos de 50 el cuaderno avisa que el umbral es una estimación poco firme. Es el caso de campo claro, que tiene dos espermatozoides en la validación y cuyo modelo se exportó con 0.5.

[Acción: líneas 24 a 38: por tipo de foto; ejecuta la celda]

Lo último de la celda separa los resultados por tipo de foto. Mide fluorescencia y campo claro por separado con el umbral elegido e imprime cuántos espermatozoides había etiquetados, cuántos detectó y las tres cifras. Sirve para ver si entrenar con un tipo empeoró al otro, y si hay menos de 20 espermatozoides avisa que la cifra es muy inestable.

Todo se guarda en un archivo de métricas finales.

[Acción: celda de las fotos con lo que encontró la red: ejecuta y muestra una foto]

Y antes de fiarse de un número hay que mirar las fotos. Esta celda toma cada foto completa, la analiza con el modelo y dibuja en blanco lo que se etiquetó y en verde lo que encontró la red. Un rectángulo amarillo marca la zona de validación.

Recuerda lo que dice el texto: solo dentro del rectángulo cuenta como prueba real. Fuera de él la red ya vio esos espermatozoides al entrenar y que los encuentre no prueba nada.

La celda guarda cada imagen en una carpeta de revisión, imprime por foto cuántos espermatozoides había etiquetados y cuántos detectó, y con eso arma un archivo de conteos. Una diferencia grande entre las dos cifras en una foto es una invitación a mirarla con calma.

[Pantalla 6 · Paso 11: exportar el modelo]

> Idea central: Se exporta un solo archivo, con los pesos y la configuración. Antes de darlo por bueno se carga en CPU desde cero, como lo hará el servidor, y se comprueba que da lo mismo que el modelo en memoria. La misma celda mide cuánto tarda una tesela, para estimar el tiempo de análisis de una foto.

> En pantalla: Colab: el texto del Paso 11 y la celda de exportación, de arriba abajo, y su ejecución.

[Acción: celda del Paso 11, el texto y las líneas 1 a 8: guardar el archivo]

Paso once, exportar. Se guarda un solo archivo llamado modelo cabezas punto pt, con los pesos y con la configuración con la que se entrenó: el tamaño de tesela, el traslape, si usa grises, la versión del cuaderno y el umbral que salió mejor. También guarda la época y el AP50 del mejor modelo.

Al terminar de guardar imprime la ruta y el peso, que son unos 176 megabytes. También recuerda las versiones de PyTorch y de torchvision con las que se entrenó, porque el servidor debe usar versiones compatibles y por eso se guardan dentro del modelo.

[Acción: líneas 11 a 29: cargar_modelo_para_inferencia]

La función que sigue es la que usa el servidor y conviene leerla despacio. Carga el archivo en el procesador, sin tarjeta gráfica y sin descargar nada de internet.

Primero revisa que el archivo traiga el épsilon de la normalización. Si no lo trae es de una versión anterior del cuaderno y daría resultados distintos, así que se detiene. Después construye la red en el modo sin pesos de COCO pasándole ese épsilon y comprueba que no quedó ninguna capa de normalización sin congelar.

Luego carga los pesos y los compara con la red, y si falta algo o sobra algo da un error. La única excepción tolerada es que las capas congeladas no guardan un contador. Por último compara las versiones de PyTorch y torchvision con las instaladas y si difieren avisa, aunque suele funcionar.

[Acción: líneas 32 a 62: comprobar contra el modelo en memoria]

Ahora la comprobación. El cuaderno carga el modelo exportado, toma un trozo de una zona de validación y lo analiza con el modelo exportado y con el que sigue en memoria. Después compara por dentro las características que calcula cada uno y la diferencia máxima debe ser menor que una milésima, y si no es así se detiene con un error.

También cuenta las detecciones de los dos, que deben ser casi iguales. Pueden diferir en una o dos que quedan justo en el borde del umbral por redondeos, pero más que eso es un error.

No es una formalidad. Es lo que garantiza que el archivo que va al servidor hace lo mismo que el modelo que acabas de medir.

[Acción: líneas 64 a 69: ejecuta la celda; el tiempo por tesela]

Al ejecutarla imprime la diferencia máxima y el número de detecciones de cada modelo, y por último una estimación de tiempos. Mide cuánto tardó una tesela en el procesador de Colab y calcula cuántas teselas usan las dos fotos típicas: una de 1,792 por 1,374 píxeles usa 20 y una de 3,584 por 2,748 usa 63. Multiplica y da una referencia en minutos.

La última línea lo dice claro: es solo una referencia, porque el procesador del servidor puede ser más lento o más rápido. Por eso la medición que falta es la del servidor real.

[Pantalla 7 · Mejorar el modelo y de aquí al servidor]

> Idea central: Mejorar el modelo es etiquetar más fotos, variadas, y entrenar una corrida nueva con otro nombre. El archivo exportado se copia a la carpeta del servidor, donde se llama como el tipo de foto y se carga sin tocar el código. Con esto termina el cuaderno; el siguiente video lleva el sitio a un servidor.

> En pantalla: Colab: la última celda de texto, «Mejorar el modelo». Después, el explorador de archivos con la carpeta `model/` del proyecto.

[Acción: celda «Mejorar el modelo»]

La última celda del cuaderno no tiene código y explica cómo mejorar el modelo. Se etiquetan más fotos en CVAT, de preferencia variadas, densas, escasas y con fibras. Se exporta el archivo de etiquetas, se reemplazan el archivo y las fotos de la carpeta de datos y se entrena una corrida nueva con otro nombre.

Y la última frase repite algo que ya sabes: con pocas fotos la validación es inestable, y la gráfica de curvas y las fotos de revisión muestran cuánto.

[Acción: muestra la carpeta model/ del proyecto, con los dos archivos]

El archivo exportado, modelo cabezas punto pt, se copia a la carpeta model del proyecto con el nombre del tipo de foto, fluorescencia punto pt y campo claro punto pt. Esa carpeta no está en Git porque cada archivo pesa unos 176 megabytes, así que se copia a mano. El sitio lee todo de dentro del archivo, la configuración, el umbral y el épsilon, y por eso se puede cambiar un modelo por uno más nuevo sin tocar el código.

Cada archivo dice en su interior de qué corrida y de qué versión del cuaderno salió. El de fluorescencia viene de la corrida 02 con el cuaderno 0.3.1 y el de campo claro de la corrida 04 con el 0.5.0.

Hagamos cuentas del recorrido. Una foto y su archivo de etiquetas se vuelven recortes, una red de COCO se adapta a una clase, se mide como en producción, se entrena y se guarda lo mejor, y se comprueba que el archivo exportado da lo mismo. Y todo queda en un solo archivo.

En el siguiente video ese archivo necesita un lugar donde vivir. Veremos el servidor en la nube, cómo se conecta uno, qué es Docker y cómo se levantan los dos contenedores del sitio.

Gracias por acompañarme.
