# Guion del módulo 3, video 3 de 4: Medición, escala y retos (versión natural)

BioImage-Repro UAM · Módulo 3 · Capacitación en video

Segunda versión, escrita para decirse en voz alta mientras se muestra la pantalla, sin mazo: frases cortas, ritmo de conversación, sin guiones largos. Empieza con la frase que lo une con el video anterior.

*4,785 palabras, unos 27.3 min de habla*

Las líneas que empiezan con [Acción: …] no se leen en voz alta: marcan en qué frase se cambia de pantalla, se hace clic o se baja. El bloque En pantalla de cada tramo resume lo que se abre en él.

## Antes de grabar

- El entorno de Python se prepara como en el video 1 (sección Entorno de Python del guion o de su guía de pantalla). Aquí no hace falta el navegador, solo el editor, la terminal y una imagen.
- Los dos archivos del modelo, `fluorescencia.pt` y `campo_claro.pt`, tienen que estar en la carpeta `model/`. No están en Git. Sin ellos, los comandos B, F y G dan otro resultado, porque el sitio usa la detección provisional.
- Siete comandos para la terminal, ya probados, que están en la guía de pantalla. Dos de ellos, el B y el G, tardan unos segundos.

[Pantalla 1 · La red localiza, el código mide]

> Idea central: La red solo traza el contorno de cada espermatozoide. Todo lo demás lo calcula el código en medicion.py: el área, el largo, la escala, el resumen y el histograma. Como es código común, se puede comprobar sin abrir la red.

> En pantalla: Editor, `app/analisis/medicion.py`: el comentario inicial (líneas 1 a 9) y la función `analizar_imagen` (237 a 297), recorrida sin entrar al detalle.

[Acción: editor, app/analisis/medicion.py, líneas 1 a 9: el comentario inicial]

En el video anterior, el servidor usó el modelo. Le dio una foto y recibió contornos. Un contorno es la línea que rodea a un espermatozoide en la foto: una lista de puntos. Hasta ahí llega la red. Hoy abrimos el archivo que sigue en el camino, medicion.py, donde esos contornos se convierten en números.

Este comentario inicial lo dice en pocas frases. La detección la hacen los modelos. Si no están disponibles, se usa una detección provisional que vive en este mismo archivo. Pero la medición del tamaño y la estadística son las mismas en los dos casos.

Es una decisión de diseño: la red localiza, el código mide. La red solo dibuja el contorno. El área, el largo y todo lo demás lo calcula código común, que con los mismos datos da siempre el mismo resultado. A eso se le llama determinista. Y tiene una ventaja: cualquier medida se puede comprobar a mano, sin abrir la red.

Mira también la nota de las líneas 8 y 9. Dice que, en los datos guardados, la lista de espermatozoides se llama cabezas. Así se llamaba al principio, y se conserva el nombre para que los análisis ya guardados se sigan abriendo. Ten cuidado con eso: en el código vas a ver la palabra cabeza en varios lugares, pero lo que se mide es el espermatozoide visible, con parte de la cola. En pantalla, en el CSV y en el PDF ya dice espermatozoide.

[Acción: baja a la función analizar_imagen, líneas 237 a 297, sin entrar al detalle]

Esta es la función principal del archivo. La ruta analizar, la del primer video, la llama una vez por cada imagen. Y hace siempre lo mismo, en este orden. Abre la imagen. Revisa su formato. Busca los espermatozoides. Mide cada contorno. Calcula el resumen, el histograma y los grados de color. Dibuja la imagen marcada. Y decide el estado del resultado: bien, con aviso, o no analizada.

Vamos por partes. Primero las medidas: área, largo y escala. Después la estadística. Después el estado y la imagen marcada. Y al final, los retos del proyecto, que es lo que más costó resolver.

[Pantalla 2 · Área y largo]

> Idea central: La función medir_cabeza cuenta los píxeles que hay dentro del contorno, y eso es el área. Y toma el lado mayor del rectángulo mínimo que lo encierra, y eso es el largo. Los dos salen en píxeles.

> En pantalla: Editor, `medicion.py`: `medir_cabeza`, líneas 117 a 121 y 128 a 137. Después terminal, comando A de la guía.

[Acción: líneas 117 a 121: medir_cabeza, hasta la máscara]

Empecemos por la medida más sencilla. La función medir cabeza recibe la foto y un contorno. Primero crea una máscara. Una máscara es una imagen del mismo tamaño que la foto, toda en cero, es decir, negra, donde se pintan de blanco solo los píxeles que están dentro del contorno. Un píxel es cada puntito de la imagen.

La línea 119 crea la imagen en ceros. La 120 pinta el contorno por dentro, con relleno. Y la 121 toma de la foto solo los píxeles donde la máscara es mayor que cero. Son los del espermatozoide. Con ellos se puede medir lo que haga falta.

[Acción: líneas 128 a 137: el rectángulo mínimo y el diccionario que devuelve]

El área es el número de píxeles de la máscara. La línea 129 los cuenta, con count_nonzero. Así de simple: el área de un espermatozoide es cuántos píxeles ocupa.

El largo se saca distinto. La línea 128 llama a minAreaRect, una función de OpenCV. Devuelve el rectángulo de área mínima que encierra el contorno. Ese rectángulo puede ir girado, inclinado igual que el espermatozoide. La función entrega su centro, sus dos lados y su ángulo. Aquí solo importan los dos lados. Y la línea 130 se queda con el mayor. Ese es el largo: el lado más largo del rectángulo que encierra al espermatozoide.

Fíjate en lo que no es. No es la longitud de la curva, como si siguieras la cola con un hilo. Es el lado de un rectángulo. Volvemos a esto en el tercer reto.

Al final, la función devuelve un diccionario. Un diccionario es una tabla de pares nombre y valor. Este trae el área en píxeles, el largo en píxeles, el área y el largo en micras, y el índice de color.

[Acción: terminal: comando A, un rectángulo de 60 por 20]

Probémoslo con algo que se puede comprobar a ojo. Este comando dibuja un rectángulo de 60 píxeles de largo por 20 de alto y lo mide. El largo sale 60.0. Justo el lado mayor. El área sale 1,281 píxeles. Es más que 60 por 20, que serían 1,200. ¿Por qué? Porque la máscara pinta también la línea del borde, y entonces el rectángulo ocupa 61 por 21 píxeles. Y 61 por 21 son 1,281.

Un detalle pequeño, pero muestra algo importante: el área cuenta píxeles, no hace geometría exacta. Y en un espermatozoide de unos trescientos píxeles, el borde pesa más que en este rectángulo.

[Pantalla 3 · La escala]

> Idea central: Las medidas salen en píxeles. Para pasarlas a micras, el código usa una sola constante, PX_POR_MICRA, que vale 60: el largo se divide entre 60, y el área, entre 60 al cuadrado. La imagen marcada trae una regla de 300 píxeles, que son 5 micras.

> En pantalla: Editor, `medicion.py`: líneas 37 a 40 y 134 y 135. Después, otra vez la salida del comando A, para hacer la cuenta.

[Acción: líneas 37 a 40: la constante PX_POR_MICRA]

Un píxel no mide nada por sí solo. Cuánto mide en la realidad depende de cómo se tomó la foto. Para pasar de píxeles a micras hace falta una escala. Una micra, o micrómetro, es la milésima parte de un milímetro. Es la unidad natural para algo tan pequeño como una célula. Se escribe µm.

La línea 40 dice PX por micra igual a 60. Son 60 píxeles por cada micra. Los comentarios de arriba cuentan de dónde sale: de una indicación del cliente, por chat, el 16 de octubre de 2026. Una raya de 300 píxeles equivale a 5 micras. Y 300 entre 5 son 60.

El comentario también dice que, por ahora, es una sola constante para todas las imágenes, y que más adelante la escala se leería de la raya de cada imagen. Y trae una palabra clave: provisional, sin calibrar. Calibrar es comprobar contra algo cuya medida se conoce. Aquí todavía no se hizo.

[Acción: líneas 134 y 135: las dos divisiones]

Y así se usa. El largo en micras es el largo en píxeles entre 60. Si 60 píxeles son una micra, 120 son dos. El área en micras cuadradas se divide entre 60 al cuadrado, es decir, entre 3,600. ¿Por qué al cuadrado? Porque el área tiene dos dimensiones. Una micra cuadrada es un cuadrito de una micra por una micra, y en píxeles ese cuadrito es de 60 por 60.

[Acción: vuelve a la salida del comando A en la terminal: la cuenta con el rectángulo de ejemplo]

Con el rectángulo del comando A. Sesenta píxeles de largo, entre 60, es una micra. La salida dice 1.0. El área, 1,281 píxeles entre 3,600, da 0.356 micras cuadradas. Ahí están las dos divisiones, con números que se pueden comprobar con una calculadora.

[Pantalla 4 · Una escala provisional]

> Idea central: La escala no se puede sacar de las fotos, porque no traen barra de escala ni regla impresa. Por eso es una constante provisional. Con ella, la imagen de ejemplo da cabezas de menos de una micra, que no es creíble. Las micras del sitio son aproximadas, y el sitio lo dice.

> En pantalla: Terminal, comando B (el análisis de la imagen de ejemplo). Después `docs/integracion-modelos.md`, sección «Escala en micras», líneas 36 a 51.

[Acción: terminal: comando B, el análisis de la imagen de ejemplo]

Veamos qué sale con la imagen de ejemplo del sitio. Este comando la analiza y muestra el resumen. Tarda unos segundos. Primero el estado: ok, fluorescencia, 41 espermatozoides. Son los mismos 41 del video anterior.

Luego el área en píxeles: media de 301.8, mínimo de 179 y máximo de 455. Y el largo en píxeles: media de 28.62. En micras, el largo medio es de 0.48. Menos de media micra.

Aquí hay que detenerse. Una cabeza de espermatozoide mide varias micras de largo. Y el contorno, además, incluye un pedazo de cola, así que debería salir más largo, no más corto. Un resultado de media micra no es creíble. Dicho de otra forma: con esta escala, esta imagen no sale en micras reales. No sabemos con qué ajuste se tomó la imagen de ejemplo, ni si tiene la misma escala que las fotos del cliente. Lo que sí sabemos es que la escala del código es provisional. Por eso el sitio no la presenta como una calibración.

[Acción: abre docs/integracion-modelos.md, sección «Escala en micras», líneas 36 a 51]

La documentación explica por qué no se puede sacar la escala de las fotos. Las fotos del cliente no traen barra de escala ni regla impresa, y los archivos BMP tampoco guardan una medida. De la imagen sola no se puede deducir cuánto mide un píxel, salvo que supongas el tamaño de algo. Y aquí no se debe suponer nada del espermatozoide.

De qué depende de verdad la escala: del aumento del objetivo del microscopio, que es de 40 veces; del tamaño del sensor de la cámara y de cualquier adaptador; y de la resolución a la que se guarda la foto. Las fotos del cliente vienen en dos tamaños, de 1,792 y de 3,584 píxeles de ancho. Si son del mismo campo con distinta resolución, cada una necesita su propio valor, y el de la grande sería el doble. Esa es una pregunta abierta.

La solución propuesta es una tabla de escalas en un archivo de configuración, con los píxeles por micra de cada resolución, que se edita sin tocar el código. Y obtener cada valor de lo más confiable a lo menos. Una foto de una regla de calibración, que se llama micrómetro de platina, tomada con ese microscopio y esa cámara. O la calibración del programa de la cámara. O un cálculo con la ficha técnica de la cámara. Eso está planteado. No está hecho.

Mientras tanto, la página de resultados muestra arriba un aviso azul. Dice que se usa la misma escala en todas las imágenes para estandarizar su tamaño, y que la regla de la imagen marcada mide 300 píxeles, es decir, 5 micras. Es una escala común. No es una calibración.

[Pantalla 5 · Media y desviación estándar]

> Idea central: La función resumen calcula cuatro números: la media, la desviación estándar, el mínimo y el máximo. La media es el valor típico. La desviación estándar dice cuánto se separan los valores de esa media.

> En pantalla: Editor, `medicion.py`, líneas 171 a 178. Después terminal, comando C de la guía.

[Acción: líneas 171 a 178: resumen]

Pasamos a la estadística. La función resumen recibe una lista de números, por ejemplo las áreas de todos los espermatozoides, y devuelve cuatro cosas. La media, el mínimo y el máximo son fáciles. La desviación estándar merece una explicación.

La media es la suma de todos los valores entre cuántos son. Es el valor típico. La desviación estándar dice cuánto se separan los valores de esa media. Si todos los espermatozoides midieran casi lo mismo, sería chica. Si hay unos muy chicos y otros muy grandes, sería grande.

Se calcula así. A cada valor le restas la media. Esas diferencias se elevan al cuadrado, para que las positivas no cancelen a las negativas. Se suman. Se divide entre uno menos que el número de datos. Y al final se saca la raíz cuadrada, para volver a la unidad de origen.

Eso de dividir entre uno menos es lo que significa ddof igual a 1, en la línea 175. Es la desviación de una muestra, y una muestra es lo que tenemos: unas cuantas células de entre todas las posibles. Fíjate también en el if: si solo hay un valor, la desviación se deja en cero, porque con un solo dato no hay separación que medir. Y todo se redondea a dos decimales.

[Acción: terminal: comando C, el resumen de 10, 20 y 30]

Con tres números que se pueden hacer a mano: 10, 20 y 30. La media es 20. Las diferencias son menos 10, cero y más 10. Al cuadrado, 100, 0 y 100. La suma es 200. Entre 3 menos 1, es decir, entre 2, da 100. Y la raíz de 100 es 10. El comando devuelve media 20, desviación 10, mínimo 10 y máximo 30. Es lo mismo que sale a mano.

En la imagen de ejemplo, el área tiene una media de 301.8 píxeles y una desviación de 55.88. Y el largo, una media de 28.62 y una desviación de 16.72. Guarda ese último número. La desviación del largo es muy grande comparada con su media. Más adelante veremos de dónde sale.

[Pantalla 6 · El histograma]

> Idea central: Un histograma reparte los valores en 10 intervalos iguales entre el mínimo y el máximo y cuenta cuántos caen en cada uno. Para promediar varias imágenes se usa un rango común. El histograma del sitio está en píxeles.

> En pantalla: Editor, `medicion.py`, líneas 181 a 185 y 300 a 313. Terminal, la última línea de la salida del comando B.

[Acción: líneas 181 a 185: histograma]

Un histograma es una forma de ver cómo se reparten los tamaños. En lugar de un solo número, muestra cuántas células hay de cada tamaño. Funciona así. El rango de valores, del mínimo al máximo, se parte en intervalos iguales. Aquí son 10, la constante de la línea 46. Y se cuenta cuántos valores caen en cada intervalo.

La función usa histogram, de NumPy, que devuelve dos listas. Los bordes de los intervalos, que son 11, porque 10 intervalos tienen 11 bordes. Y las frecuencias, que son 10: cuántos hay en cada intervalo. El código las redondea y las guarda.

[Acción: vuelve a la terminal, la última línea de la salida del comando B: el histograma]

En la imagen de ejemplo, el área va de 179 a 455 píxeles. Eso se parte en diez intervalos de 27.6 píxeles de ancho: de 179 a 206.6, de 206.6 a 234.2, y así. Las frecuencias son 3, 1, 7, 7, 7, 8, 4, 2, 1 y 1. Si las sumas, da 41: uno por cada espermatozoide. La mayoría está en el centro. Veintinueve de los 41 caen entre 234 y 345 píxeles. Y hay muy pocos grandes.

Un detalle. Este histograma está en píxeles, no en micras, aunque lo demás se dé en micras. Es una limitación conocida.

[Acción: líneas 300 a 313: promedios_entre_imagenes]

Cuando se suben varias imágenes, el sitio muestra también el promedio entre imágenes. Esta función lo calcula. Necesita al menos dos imágenes analizadas. Si hay menos, no devuelve nada.

Toma el área mínima y la máxima entre todas las imágenes juntas. Con ese rango común calcula el histograma de cada una. Es importante que sea el mismo rango. Si cada imagen usara el suyo, los intervalos no coincidirían y no se podrían promediar. Después promedia, intervalo por intervalo, cuántas células hubo. Con dos copias de la imagen de ejemplo, el promedio sale igual al de una sola. Como debe ser.

[Pantalla 7 · El resultado de una imagen y sus estados]

> Idea central: Analizar una imagen no siempre termina bien. Hay tres estados: ok, aviso y no analizada. Si la imagen no se abre o no tiene espermatozoides, el sitio dice que no se analizó y no inventa números. Si hay menos de tres, cuenta, pero avisa que la distribución de tamaños no es confiable.

> En pantalla: Editor, `medicion.py`, líneas 239 a 265 y 288 a 296. Terminal, comando D de la guía. Editor, `tests/test_sistema.py`, líneas 111 a 124.

[Acción: líneas 239 a 265: abrir, revisar el formato y buscar]

Volvamos a analizar imagen, ahora con lo que puede salir mal. Primero abre la imagen. Si no se puede abrir como imagen, por ejemplo un archivo de texto con extensión png, lo anota y devuelve el estado no analizada, con un mensaje en rojo. No sigue.

Después revisa el formato, con la constante de la línea 47. BMP, PNG y TIFF son formatos sin pérdida. Si es otro, como JPG, agrega un aviso amarillo: el color y los bordes pueden alterarse. Pero sigue adelante. El JPG se analiza igual. Qué pasa con eso lo vemos en el último reto.

Luego busca los espermatozoides con la función de detección. Y si no encuentra ninguno, devuelve no analizada con un mensaje claro: no se encontraron espermatozoides o la imagen es de mala calidad, no es factible analizar la imagen. Esa frase es importante. El código prefiere decir que no pudo, antes que dar un resultado dudoso.

[Acción: líneas 288 a 296: los tres estados]

Al final, el estado. Si se contaron menos de tres espermatozoides, el estado es aviso, con un mensaje amarillo: se contaron muy pocos y la distribución de tamaños no es confiable. Tiene sentido. Con uno o dos valores, un histograma no dice nada. Fíjate que la imagen marcada ya se dibujó antes, en la línea 284. El aviso no la quita.

En cualquier otro caso, el estado es ok y el mensaje es verde: la imagen fue analizada con éxito. Son tres estados. Ok, aviso y no analizada.

[Acción: terminal: comando D, una imagen toda negra]

Veámoslo. Este comando crea una imagen negra de 200 por 200 y la analiza. El estado sale no analizada, y el mensaje es el de que no se encontraron espermatozoides. Cada mensaje es una pareja: el nivel, que da el color, y el texto. Aquí danger, que es rojo.

[Acción: tests/test_sistema.py, líneas 111 a 124: las pruebas del JPG y de la imagen negra]

Dos pruebas lo comprueban. Una sube un JPG y espera ver el aviso de formato con compresión. La otra sube una imagen negra y espera la frase de que no es factible analizarla. Estas pruebas corren sin los modelos, con la detección provisional, para que sean rápidas.

[Pantalla 8 · La imagen marcada]

> Idea central: La función dibujar_marcas dibuja cada contorno con un borde oscuro y un trazo blanco, le pone su número y agrega una regla de 300 píxeles. Guarda dos copias: una reducida, para la página y el PDF, y una ampliada para el zoom. Es la prueba visual de lo que el código contó.

> En pantalla: Editor, `medicion.py`: líneas 217 a 234, 188 a 205 y 140 a 144. Visor de imágenes, `figuras/marcada.png`. Editor, `tests/test_sistema.py`, líneas 164 a 176 y 214 a 220.

[Acción: líneas 217 a 234: dibujar_marcas]

Después de medir, el código dibuja. La imagen marcada es la prueba visual: con ella, quien analiza puede revisar qué contó el sistema. Esta función recibe la foto y los contornos, y para cada uno hace tres cosas.

Dibuja el contorno dos veces. Primero un trazo negro, más grueso. Encima, uno blanco, más delgado. Es un truco: con el borde negro, el trazo blanco se ve igual sobre fondo oscuro, como en fluorescencia, que sobre fondo claro. Luego calcula la esquina del rectángulo que lo encierra, con boundingRect. Y ahí escribe el número del espermatozoide, también dos veces, en negro y en blanco, por la misma razón. Ese número es el de la tabla de resultados. Al final llama a la regla y guarda las copias.

[Acción: imagen figuras/marcada.png: la imagen marcada de la foto de ejemplo]

Esta es la imagen marcada de la foto de ejemplo, la copia grande. Cada contorno blanco lleva su número. Abajo a la izquierda está la regla, con su texto: 300 px igual a 5 micras. Compárala con las cabezas. Una cabeza mide alrededor de una décima parte de la regla. Es lo que vimos con la escala.

Fíjate bien en esta imagen, porque nos va a servir para los retos. Se ven dos cosas. Una: hay cabezas de color sin contorno ni número. Dos: hay contornos largos y delgados, como el 5, el 9, el 18 y el 39, que siguen una cola y no una cabeza. Las dos cosas las vamos a explicar.

[Acción: líneas 188 a 205: dibujar_regla]

La regla se dibuja en dibujar regla. Mide 300 píxeles, el valor de la constante de la línea 43. Y el texto lo calcula con la escala: 300 entre 60, 5 micras. Lleva el mismo truco del borde negro y el trazo blanco. Y se salta si la imagen es muy chica: en las líneas 192 y 193, si no cabe, no se dibuja. Así la imagen siempre muestra con qué escala se calcularon las micras.

[Acción: tests/test_sistema.py, líneas 164 a 176 y 214 a 220: las pruebas de la regla y de las dos copias]

Hablemos de las dos copias. La reducida, de hasta 1,400 píxeles en su lado mayor, es la que usan la página y el PDF. La ampliada, de hasta 2,800, es la del zoom. La función que guarda nunca agranda. Si la foto ya es más chica que el límite, se guarda del mismo tamaño. Por eso la imagen de ejemplo, de 1,200 por 900, sale igual en las dos.

Dos pruebas lo comprueban. Una dibuja la regla sobre una imagen negra y revisa píxeles concretos: blanco a la mitad de la regla, y negro justo después de los 300 píxeles. La otra usa una foto de 3,000 por 2,000 y comprueba que la copia de la página queda en 1,400 y la ampliada en 2,800.

[Acción: líneas 140 a 144: contorno_simple]

Una última cosa de esta parte. Para el detalle que sale al pasar el mouse sobre cada espermatozoide, hace falta guardar la forma de su contorno. Un contorno real tiene cientos de puntos. Esta función los simplifica con approxPolyDP, un algoritmo que quita los puntos que casi están en línea recta, con una tolerancia de un píxel y medio. Guarda la lista de puntos, en las coordenadas de la foto original. Así el análisis guardado pesa menos y sigue dibujando bien cada zona.

[Pantalla 9 · Reto 1: espermatozoides juntos]

> Idea central: Los espermatozoides juntos o encimados son el primer reto. Un umbral de color los funde en una sola mancha, y por eso quedó solo como respaldo. Con la red el problema cambia, pero no desaparece: en zonas amontonadas repite, parte o se salta contornos. Los conteos son aproximados.

> En pantalla: `docs/base-conocimiento/03-decisiones.md`, líneas 12 y 13. Editor, `medicion.py`, líneas 67 a 98. Terminal, comando E. `docs/base-conocimiento/05-limitaciones.md`, línea 6.

[Acción: docs/base-conocimiento/03-decisiones.md, líneas 12 y 13: «Un umbral simple no bastaba»]

Llegamos a los retos. Son cuatro, y son lo que más costó resolver. El primero: separar y contar bien.

Lo primero que se intentó fue lo más simple, un umbral de color. Un umbral es un valor de corte: todo píxel más brillante que ese valor es parte de una célula, y el resto es fondo. Esta nota de las decisiones explica por qué no bastó. Tres razones. Las colas y las manchas también brillan. Las células encimadas se funden en una sola mancha. Y el brillo cambia con la iluminación de cada foto.

[Acción: medicion.py, líneas 67 a 98: detectar_cabezas]

Ese umbral no se tiró. Quedó como respaldo: la detección provisional. Vale la pena ver qué hace, porque muestra la dificultad. Toma el canal rojo y calcula el umbral con el método de Otsu, que lo elige según cada imagen. Pide que el rojo domine o empate con el verde, para dejar fuera las colas, que son verdes. Limpia con una apertura, que quita los puntitos sueltos. Y busca los contornos.

Luego aplica tres filtros. Descarta lo que mida menos de 20 píxeles, que es ruido. Descarta lo que sea más de seis veces la mediana, que son manchas grandes, quizá varias células fundidas. Y descarta lo muy alargado, con una relación de más de 5 a 1, que serían colas. Tres filtros hechos a mano, cada uno con un número escogido.

[Acción: terminal: comando E, el conteo de la detección provisional]

Con la imagen de ejemplo da 45. El modelo dio 41. Esa diferencia no dice cuál tiene la razón. Dice que dos métodos distintos, mirando la misma foto, no cuentan igual. En esta foto las cabezas están bastante separadas. El problema serio aparece cuando se juntan.

[Acción: docs/base-conocimiento/05-limitaciones.md, línea 6: conteos aproximados con células juntas]

Con los modelos el problema cambia, pero no se va. La documentación lo dice sin rodeos: en zonas con muchos espermatozoides juntos, el modelo puede repetir un contorno, partir uno en dos o no encontrar algunos. Contra los repetidos hay tres defensas, que vimos en el video anterior: descartar lo que toca el borde interno de una tesela, quitar repetidos con el IoU y el filtro de contenido. Ayudan. No son perfectas. Por eso los conteos del sitio son aproximados.

[Pantalla 10 · Reto 2: falsos positivos]

> Idea central: La red siempre contesta, aunque no haya un espermatozoide: marca fibras, manchas y núcleos con puntajes altos. No se le enseñó con ejemplos negativos qué no marcar. El código tiene un solo freno: si no encuentra nada, dice que no pudo analizar.

> En pantalla: `docs/base-conocimiento/05-limitaciones.md`, línea 7. Editor, `medicion.py`, líneas 259 a 265.

[Acción: docs/base-conocimiento/05-limitaciones.md, línea 7: sin ejemplos negativos]

El segundo reto son los falsos positivos. Un falso positivo es algo que el sistema marca como espermatozoide y no lo es. Ya hablamos de esto en el módulo 2, en el video de Mask R-CNN. Recuerda el ejemplo. Con un recorte de una foto de células con núcleos fluorescentes, sin ningún espermatozoide, el modelo marcó un núcleo con 0.96 y un trozo de fibra con 1.00. Un puntaje alto no garantiza que sea un espermatozoide.

¿Por qué pasa? La documentación lo resume en una frase: sin ejemplos negativos. Un ejemplo negativo es una foto, o un pedazo de foto, donde la respuesta correcta es que no hay nada que marcar. Los modelos se entrenaron con cuatro fotos por tipo, todas con espermatozoides. Nunca vieron una fibra o un núcleo con la etiqueta de que eso no es. Y por eso, ante algo brillante y compacto, tienden a marcarlo.

[Acción: medicion.py, líneas 259 a 265: el único freno del código]

¿Qué hace el código contra esto? Muy poco, y hay que decirlo. Su único freno está aquí: si no encuentra nada, dice no analizada. Pero si encuentra algo, aunque no sea un espermatozoide, lo mide y lo cuenta. No hay un aviso que diga que la imagen no parece de espermatozoides.

Está en la lista de trabajo futuro: agregar ejemplos negativos al entrenamiento, con hígado, riñón u otras muestras sin espermatozoides, y avisar cuando una imagen no parezca de espermatozoides. Mientras tanto, el resultado se revisa a ojo con la imagen marcada. Para eso está.

[Pantalla 11 · Reto 3: el largo]

> Idea central: El largo es el lado mayor del rectángulo mínimo, no la longitud de la curva, y el contorno incluye la cabeza y parte de la cola. Además, en la imagen de ejemplo cuatro contornos son colas marcadas como si fueran espermatozoides, y ellas solas multiplican por casi cuatro la desviación del largo.

> En pantalla: `docs/base-conocimiento/05-limitaciones.md`, línea 9. Terminal, comando F de la guía y, otra vez, la salida del comando B.

[Acción: docs/base-conocimiento/05-limitaciones.md, línea 9: el largo no es la longitud de la curva]

El tercer reto es qué significa largo. La documentación lo aclara. El largo no es la longitud de la curva. Es el lado mayor del rectángulo mínimo del contorno. Y el contorno incluye la cabeza y parte de la cola, no solo la cabeza. Por eso en pantalla, CSV y PDF se cambió cabeza por espermatozoide.

Hay una decisión pendiente: cambiar el largo a la longitud de la curva. Mientras no se decida, el largo sirve para comparar un espermatozoide con otro, pero no es la medida de la cola ni del espermatozoide completo.

[Acción: terminal: comando F, los contornos más alargados de la imagen de ejemplo]

Ahora, algo que aparece al mirar los datos. Este comando calcula, para cada contorno, qué tan alargado es: el lado mayor entre el lado menor del rectángulo. Y muestra los seis más alargados. Los cuatro primeros son los números 39, 18, 5 y 9, con relaciones de casi 15, 13, 12 y 12 a 1. El quinto ya baja a 3.2, y el resto está en 2.2 o menos.

Son los contornos largos y delgados de la imagen marcada. Colas, no cabezas. La red las marcó como si fueran espermatozoides. Y eso contamina el largo.

Recuerda el largo de la imagen de ejemplo: media de 28.62 y desviación de 16.72. Si quito esos cuatro contornos, quedan 37, con media de 23.41 y desviación de 4.33. Cuatro contornos de 41 multiplican la desviación por casi cuatro. Y el largo máximo, de 87.5 píxeles, que son 1.46 micras, es una cola. No es un espermatozoide.

[Acción: vuelve a la salida del comando B: la línea del largo en micras]

Con la escala, ese máximo es 1.46 micras y el mínimo, 0.25. Dos números en micras que parecen medidas, y que dependen de una escala provisional y de si el contorno es una cabeza o una cola. Es el cuidado que pide la documentación en sus riesgos: un resultado numérico puede parecer más exacto de lo que es.

Una observación. El filtro de alargamiento, el de más de 5 a 1, existe en la detección provisional, pero no en el camino del modelo. Lo que vemos aquí sugiere que algo parecido ayudaría. Es una mejora posible. No está hecha.

[Pantalla 12 · Reto 4: las fotos]

> Idea central: Las fotos traen sus propias dificultades: dos tipos con dos modelos, formatos con compresión que cambian el resultado, y fotos grandes que tardan. Con la misma foto, el conteo pasó de 41 en PNG a 45, 49 y 45 en JPG de distinta calidad.

> En pantalla: Editor, `medicion.py`, líneas 47 y 249 a 252. Terminal, comando G de la guía. `docs/integracion-modelos.md`, líneas 29 y 30, y línea 68.

[Acción: medicion.py, líneas 47 y 249 a 252: los formatos]

El cuarto reto son las fotos mismas. Ya vimos que hay dos tipos, fluorescencia y campo claro, y por eso dos modelos. Falta ver el formato.

BMP, PNG y TIFF guardan la foto tal cual, sin pérdida. JPG guarda una versión comprimida: para pesar menos, descarta información que casi no se nota. Esa compresión se llama con pérdida. Altera un poco el color y los bordes, justo lo que el código usa para localizar y medir. El código lo sabe, y por eso el aviso.

[Acción: terminal: comando G, la misma foto en PNG y en JPG de tres calidades]

¿Cuánto cambia? Hagamos el experimento con la imagen de ejemplo. Este comando analiza la foto original en PNG y después tres copias en JPG, con calidad 95, 75 y 50. La calidad en JPG va de 0 a 100: más baja, más compresión.

El PNG da 41 espermatozoides. El JPG de calidad 95 da 45. El de 75 da 49. Y el de 50, 45. La misma foto, cuatro conteos. No hay una tendencia limpia: no es que menos calidad dé siempre más o siempre menos. Simplemente cambia. Un experimento con una sola imagen no es un estudio. Pero alcanza para ver por qué existe el aviso, y por qué conviene subir BMP, PNG o TIFF.

[Acción: docs/integracion-modelos.md, líneas 29 y 30, y la decisión 2 de la línea 68]

Y están las fotos grandes. En fluorescencia, una foto de 1,792 píxeles de ancho se corta en 20 teselas, como vimos, y una de 3,584, en 63. Cada tesela pasa por la red, en procesador y sin tarjeta gráfica, así que cada foto tarda decenas de segundos. Del servidor real todavía no hay una medición.

¿Cómo se resolvió? El cliente pidió poder subir 10 imágenes a la vez y ver una barra de progreso. Se mantuvieron las dos cosas, con tiempos de espera altos, de 1,800 segundos en Gunicorn y en Nginx, y con análisis de uno en uno. Si en el servidor real diez imágenes tardan demasiado, el plan es limitar cuántas se suben, o pasar el análisis a segundo plano. Eso falta medirlo.

[Pantalla 13 · Lo que no se mide y lo que falta]

> Idea central: Hay cosas que el código calcula y no muestra, como el color. Hay cosas que no mide, como el espermatozoide de cabeza a cola. Y hay cosas que faltan: calibrar la escala, avisar de imágenes ajenas, medir en el servidor y validar con fotos nuevas. El sitio mide. La lectura científica es del grupo de investigación.

> En pantalla: Editor, `medicion.py`, líneas 31 a 35 y 125 y 126. `docs/base-conocimiento/05-limitaciones.md`, líneas 20 a 27.

[Acción: medicion.py, líneas 31 a 35 y 125 y 126: el color]

Antes de cerrar, lo que no se ve. El código calcula el color de cada espermatozoide. En la línea 126, el índice de color es el verde entre la suma de rojo y verde, promediado sobre todos los píxeles del contorno. Cero es rojo puro y 0.5 es amarillo. Y las líneas 31 a 35 reparten ese índice en diez grados, del más rojo al más amarillo.

Pero el color ya no se muestra. En el plan de integración se decidió seguir guardándolo y dejar de mostrarlo en resultados, CSV y PDF. Está declarado, sin usar, por si hace falta más adelante.

[Acción: docs/base-conocimiento/05-limitaciones.md, líneas 20 a 27: trabajo futuro]

Y lo que falta, según el propio proyecto. Medir el tiempo y la memoria en el servidor real. Reunir más imágenes, variadas y bien etiquetadas, con ejemplos negativos, y volver a entrenar. Validar con fotos que la red nunca haya visto. Medir de cabeza a cola. Avisar si la imagen no parece de espermatozoides. Quizá cambiar el largo a la longitud de la curva. Y, como extensión fuera del alcance actual, comparar control contra tratamiento.

A esa lista se suma la calibración de la escala, que vimos antes. Y yo agregaría una cosa, por lo que vimos hoy: descartar los contornos muy alargados que da el modelo. Pero ojo con la última línea de la documentación sobre los límites. El sitio mide. La lectura científica es del grupo de investigación.

[Pantalla 14 · Lo que vimos y lo que sigue]

> Idea central: Vimos cómo el código convierte contornos en medidas, de qué depende la escala, cómo se resumen y se dibujan los resultados, y los cuatro retos del proyecto. En el siguiente video, el último del módulo, se ve todo junto en el sitio funcionando.

> En pantalla: Vuelve al editor, en `medicion.py`, línea 237, mientras das el resumen y te despides.

[Acción: vuelve al editor, medicion.py, línea 237]

Un resumen.

La red localiza y el código mide. Del contorno salen dos medidas: el área, que son los píxeles de la máscara, y el largo, que es el lado mayor del rectángulo mínimo. Las dos salen en píxeles, y se pasan a micras con una escala provisional de 60 píxeles por micra. Esa escala no sale de las fotos. Viene de una indicación del cliente, y con ella la imagen de ejemplo da cabezas de menos de una micra. Por eso las micras son aproximadas.

Después, el resumen: media, desviación estándar, mínimo y máximo. El histograma de 10 intervalos, en píxeles. Los tres estados: ok, aviso y no analizada. Y la imagen marcada, con sus contornos numerados y su regla de 300 píxeles.

Vimos cuatro retos. Espermatozoides juntos, que vuelven aproximados los conteos. Falsos positivos, porque la red no vio ejemplos negativos. El largo, que no es la longitud de la curva y que se contamina con colas marcadas. Y las fotos: el JPG cambió el conteo de 41 a 45, 49 y 45.

En el siguiente video, el último del módulo, vemos todo esto junto en el sitio funcionando, como lo usa una persona.

Gracias por acompañarme.
