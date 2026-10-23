# Guion de la sesión 1: El problema y el sitio

Image Bio Pro · Capacitación · viernes 23 de octubre de 2026, de 6:00 a 8:00 pm

Esta sesión es la primera de cuatro. Presenta el problema como caso de estudio de inteligencia artificial, la idea de imagen digital y el sitio funcionando. Cómo aprende la red se ve en la sesión 2; cómo funciona el sistema por dentro, en la sesión 3; datos, reentrenamiento y despliegue, en la sesión 4.

## Cómo usar este guion

No es un texto para leer. Cada bloque tiene tres partes:

- Idea que debe quedar: lo único que el público tiene que llevarse del bloque.
- Ideas, en orden: lo que hay que tocar, contado con palabras propias.
- Frases ancla: aparecen en cita (con `>`). Son aperturas, definiciones y transiciones, y se dicen casi literales. Lo demás se cuenta hablando.
- Las muletillas («eh», «este», «bueno», «o sea») y los puntos suspensivos de las frases ancla marcan el tono platicado, con algo de nervio al inicio. Se dicen como salgan; no hay que repetirlos al pie de la letra.

Ritmo considerado: 170 palabras por minuto. El tope de cada bloque es lo máximo que cabe en los minutos que se hablan (los minutos de pantalla y demostración no cuentan). Es un máximo y no hace falta llenarlo. Las indicaciones entre corchetes (pantalla, acciones y diapositivas) no se cuentan.

## Resumen de tiempos

| Bloque | Hora | Min | Min hablados | Tope (palabras) | Palabras ancla |
|---|---|---|---|---|---|
| 1. Bienvenida y agenda | 0:00-0:05 | 5 | 5 | 850 | 108 |
| 2. El caso de estudio | 0:05-0:22 | 17 | 17 | 2,890 | 212 |
| 3. Por qué una plataforma web | 0:22-0:31 | 9 | 9 | 1,530 | 120 |
| 4. Qué es una imagen digital | 0:31-0:42 | 11 | 10 | 1,700 | 149 |
| 5. El sitio, visto como visitante | 0:42-0:53 | 11 | 8 | 1,360 | 133 |
| 6. Crear una cuenta | 0:53-0:59 | 6 | 4 | 680 | 37 |
| 7. Analizar una imagen y esperar | 0:59-1:12 | 13 | 8 | 1,360 | 90 |
| 8. Leer los resultados | 1:12-1:29 | 17 | 14 | 2,380 | 188 |
| 9. Lo que no es un espermatozoide | 1:29-1:38 | 9 | 7 | 1,190 | 85 |
| 10. Descargas, Mis análisis y privacidad | 1:38-1:46 | 8 | 6 | 1,020 | 88 |
| 11. Cierre y adelanto de la sesión 2 | 1:46-1:51 | 5 | 5 | 850 | 121 |
| Margen | 1:51-2:00 | 9 | - | - | - |
| Total | | 120 | 93 | 15,810 | 1,331 |

Las dos horas son seguidas. De los 120 minutos, unos 93 se hablan, unos 18 son pantalla y demostración y 9 quedan de margen. El margen no se llena: sirve para preguntas, para una demostración que se alargue o para terminar a tiempo.

## Notas para quien presenta

Estas notas no se leen en voz alta. Son puntos que conviene resolver o comprobar antes de la sesión.

1. Ensayo del 20 de octubre. El revisor notó que casi toda la presentación se leía, que había conceptos que aparecían tarde respecto a su explicación y que lo más importante era el orden y el tono platicado. Este guion sigue su orden: primero el contexto y el caso de estudio, después por qué una plataforma web, la imagen digital, y entonces el sitio funcionando. El revisor también pidió numerar las diapositivas.
2. Preguntas del público. El público puede preguntar en cualquier momento; quien presenta no hace preguntas al público. Responder breve y concreto. Si la pregunta es muy técnica: «Buena pregunta, la vemos al final de la sesión» (o en la sesión que corresponda). Como respaldo, las preguntas que no alcancen a contestarse se pueden mandar por escrito (por ejemplo, por el chat de la videollamada); falta definir cuándo se responden.
3. Grabación. Decirlo al inicio. Según el revisor, la grabación se sube a redes y se puede editar, incluida la voz, si no se quiere aparecer. Sin cámara, usar una foto de perfil. Confirmar con el revisor qué se dice sobre dónde se publica.
4. Antes de empezar (15 minutos antes). Probar la videollamada y compartir pantalla. Abrir el sitio con el zoom del navegador al 125 %. Tener un análisis ya hecho en «Mis análisis».
5. Tiempo de análisis. En la computadora de desarrollo, una foto grande de fluorescencia tarda unos 40 segundos y una de fondo claro entre 10 y 20. En el VPS no se ha medido. Si el análisis en vivo se alarga, abrir el que ya está hecho en «Mis análisis».
6. Estado del sitio (revisado el 21 de octubre, después de los commits `fd13cba` y `6c2d5d7`). Ya está hecho, y el guion lo describe así:
   - El aviso de espera: la cubierta dice que es normal que el análisis tarde y, pasado un minuto, avisa que sigue en curso (sugerencia de Isaac).
   - El texto de la escala: «Para estandarizar el tamaño de las imágenes se usa la misma escala en todas: 60 px = 1 µm», en pantalla, en el PDF y en la regla de la imagen marcada.
   - Los recuadros de «modelo preliminar» y de «escala provisional» ya no aparecen, ni en pantalla ni en el PDF.
   - Los datos principales (área media y desviación estándar) salen en µm², con los píxeles como apoyo, y el PDF también pone primero las micras.

   Por revisar antes del viernes:
   - Contenido real de Nosotros, Aliados e infografías. El texto y las fotos se envían a más tardar el jueves temprano.
   - El histograma todavía rotula el eje horizontal en píxeles («Área del espermatozoide (px)»), aunque los datos principales están en micras. Decidir si se cambia o si se explica al leerlo.
   - Que el PDF salga completo (en el ensayo se veía incompleto) y que la imagen de ejemplo no muestre ningún aviso extra (en el ensayo salía uno y se acordó quitarlo).
   - Que el sitio esté en línea, con el VPS, antes del viernes por la tarde.
7. Tres imágenes que no son espermatozoides (bloque 9). Prepararlas con anticipación, de libre uso (el revisor sugirió células de hígado y de riñón). Probarlas antes: presentar solo lo que el sitio haga de verdad. Si el sitio marca algo en alguna, sirve para explicar el falso positivo.
8. Escala. La escala se presenta como la presenta el sitio: se usa la misma en todas las imágenes para estandarizar su tamaño (60 px = 1 µm; la regla de la imagen marcada mide 300 px = 5 µm). No decir «imaginaria» ni entrar en el detalle de las medidas. Si preguntan cómo se sabe que es correcta: es una escala común para estandarizar el tamaño de las imágenes y poder compararlas entre sí, y cada resultado la declara.
9. Largo. En el código, el largo es el lado mayor del rectángulo mínimo que encierra el contorno (`app/analisis/medicion.py`), no la longitud a lo largo de la curva. Este guion solo dice «largo». El README y el guion anterior decían que se mide a lo largo de la forma; conviene corregirlos para que todo diga lo mismo. El detalle del método se ve en la sesión 3.
10. Conocimiento general. Lo que se dice de píxeles, brillo de 0 a 255 y compresión del JPG es de conocimiento general, no del repositorio. Las cifras del sitio (hasta 10 imágenes, 300 MB por envío, 10 intervalos del histograma, contraseña de 8 caracteres) salen del código.
11. Lo que ya no va en esta sesión. La red neuronal, el entrenamiento y las cifras de los modelos pasan a las sesiones 2 a 4. La versión anterior de este guion, con ese material completo, está en el historial de git: `git show faf9599:docs/capacitacion/guion-sesion-1.md`.
12. Tono. Lenguaje profesional pero platicado. Sin comentarios que sugieran que el grupo no sabe. Cada término técnico se explica en una frase la primera vez que aparece. Las muletillas y las pausas son bienvenidas, sobre todo en los primeros minutos; conforme avance la sesión, la voz se asienta sola.
13. Presentación. Tiene 23 diapositivas numeradas. El sistema se presenta en el navegador: una sola diapositiva («Presentación del sistema», la 18) marca el cambio, y no hay diapositivas con capturas. Por eso los bloques 5 a 8 y 10 se cuentan hablando frente a la pantalla del sitio, y las indicaciones entre corchetes describen con detalle lo que se ve y lo que se hace en cada pantalla, sin imágenes.

---

## Bloque 1. Bienvenida y agenda

*0:00-0:05 · 5 min · tope 850 palabras*

Idea que debe quedar: son cuatro sesiones, hoy vemos el problema y el sitio, y pueden preguntar cuando quieran.

[Diapositiva · Image Bio Pro]

Ideas, en orden:

- Saludo y presentación: nombre y qué hace.
- La sesión queda grabada.
- Cómo preguntar: en cualquier momento; lo muy técnico se deja para el final.
- El mapa de las cuatro sesiones.
- La agenda de hoy: el problema, la imagen digital, el sitio y un análisis en vivo.

> Eh... buenas tardes a todos, y gracias por conectarse. Este... soy Angel Frausto Robles, desarrollador de Image Bio Pro.

> Bueno, primero... esta sesión queda grabada. Si tienen una duda, pregúntenme en cualquier momento, ¿va? Eh, las respuestas muy técnicas las dejamos para el final, para no perder el hilo.

[Diapositiva · Las cuatro sesiones]

> Son cuatro sesiones. Hoy vemos el problema y el sitio... mañana, cómo aprende la computadora; el lunes, cómo funciona el sistema por dentro; y el martes, este, los datos y cómo se reentrena el modelo.

[Diapositiva · La agenda de hoy]

> Hoy vamos a empezar por el problema, luego veremos qué es una imagen digital y después el sitio. Al final, un análisis en vivo.

---

## Bloque 2. El caso de estudio

*0:05-0:22 · 17 min · tope 2,890 palabras*

Idea que debe quedar: vamos a aprender cómo se usa la inteligencia artificial resolviendo un problema concreto, contar y medir espermatozoides en fotografías, y la clave es repartir el trabajo entre la red y el código.

[Diapositiva · La inteligencia artificial en la educación y la investigación]

Ideas, en orden:

- Abrir con una pregunta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Una de sus aplicaciones es analizar imágenes.
- Las imágenes vienen de muchas fuentes. Una es la microscopía: permite ver células, por ejemplo los espermatozoides, y ver cómo cambian de tamaño y de forma bajo ciertas condiciones.
- El objetivo de esta capacitación: acercar a la comunidad universitaria, de distintas áreas, a lo que es la inteligencia artificial y a cómo se aplica a un problema técnico-científico real, en este caso de biología de la reproducción.
- Cómo lo hacemos: con un caso de estudio. Aprendemos a través de un ejemplo.
- Aclarar que no hace falta venir de la programación ni de la biología: cada término técnico se explica la primera vez que aparece.

> Entonces, eh, para entender cómo se aplica la inteligencia artificial, vamos a seguir un caso de estudio, o sea, un ejemplo concreto: contar y medir espermatozoides en fotografías de microscopio.

> Y no se preocupen si algún término no les suena: cada vez que aparezca uno nuevo, lo explico en una frase.

[Diapositiva · El caso de estudio]

- Presentar la foto de ejemplo: células brillantes sobre un fondo oscuro. Cada punto brillante es una cabeza de espermatozoide con su cola.
- Preguntar sin esperar respuesta: ¿cuántas hay aquí? Es lo primero que haría cualquier persona: contar.

[Diapositiva · Contar y medir a mano]

- El problema: contar y medir a mano es lento, repetitivo y cambia según quién lo haga. Una foto tiene decenas o cientos de células, muchas encimadas o pegadas. Si hay que comparar muchas imágenes, el trabajo manual se vuelve difícil de sostener.
- Decir qué se ve en una foto de fluorescencia: las células salen brillantes sobre fondo oscuro.
- Cuando las células están pegadas, dos personas pueden decidir distinto cuántas hay. No es falta de cuidado: el ojo no tiene una regla fija.
- El sitio atiende dos tipos de foto: fluorescencia y fondo claro. Hay un modelo para cada una, y más adelante se ve cómo el sitio elige.

> Imaginen contar a mano cien células en una foto, y luego repetirlo con muchas fotos... este, cada persona contaría algo distinto, ¿no?

> Trabajamos con dos tipos de foto: las de fluorescencia, donde las células brillan sobre un fondo oscuro, y las de fondo claro. Para cada tipo tenemos un modelo distinto.

[Diapositiva · La red localiza y el código mide]

- La idea central es repartir el trabajo. Una red neuronal, que es un programa que aprende de ejemplos, hace una sola cosa: decidir dónde hay un espermatozoide y trazar su contorno.
- Todo lo demás lo hace código convencional: cuántos son, cuánto mide cada uno, la media y la desviación estándar. Son procedimientos explícitos y estandarizados que cualquiera puede verificar.
- En la práctica: se abre la imagen marcada, se mira el contorno que trazó la red y se recalcula la medida. La red propone y la medición se puede auditar.
- Por qué importa repartirlo así: si la red hiciera todo, cada número saldría de una caja cerrada. Con el reparto, el único paso que no se puede explicar paso a paso es dónde está el contorno, y ese se ve a simple vista.

> La red localiza y el código mide. Y bueno, esa división se repite en todo el proyecto.

[Diapositiva · Tres principios]

- Hay tres principios que explican lo que vamos a ver. El primero es no suponer: cuando falta un dato, como la escala o lo que marca cada tinción, el sitio no lo inventa y lo indica en pantalla. Por eso cada resultado muestra la escala que se usó. Prefiere un aviso claro a un número que parezca más seguro de lo que es.
- El segundo es separar lo que decide la red de lo que se mide. La red localiza y el código mide, así que cualquier medida se verifica sin abrir la red.
- El tercero es la reproducibilidad. El entrenamiento está en un cuaderno de Colab, que es un entorno para programar en la nube, y cualquiera puede abrirlo y ejecutarlo. Además, el modelo guarda dentro de su archivo la configuración con la que se entrenó. Si hay que repetir un resultado o reconstruir el entorno, no depende de la memoria de nadie.

> Hay tres principios que explican lo que vamos a ver. El primero... no suponer. Cuando a un dato le falta información, el sitio no la inventa: la indica en pantalla.

> El segundo, separar lo que decide la red de lo que se mide. Y el tercero, que todo se pueda repetir: el entrenamiento está en un cuaderno que cualquiera puede abrir y ejecutar.

[Diapositiva · Funciona y se puede mejorar]

- Un modelo así no aprende solo cuando ya está en línea. Si llegan imágenes nuevas, otras tinciones u otro tipo de célula, se reentrena aparte y se cambia el archivo del modelo. Eso lo vemos el martes.
- Estado del modelo, en general: funciona, está dando buenos resultados y, como cualquier modelo, se puede mejorar. Sin entrar en detalle.
- Anticipar los retos: más adelante les cuento qué dificultades tuvo el proyecto y cómo las resolvimos, por ejemplo cuando las células se empalman. Contarlas como cosas que se resolvieron, con una estrategia computacional para contarlas mejor.

> Al final de las sesiones les cuento los retos que enfrentamos y cómo les dimos la vuelta. Les adelanto uno... cuando muchas células se empalman, pues, contarlas es muy difícil.

---

## Bloque 3. Por qué una plataforma web

*0:22-0:31 · 9 min · tope 1,530 palabras*

Idea que debe quedar: el modelo entrenado, solo, no hace nada. La plataforma web es lo que permite que cualquier persona de la universidad lo use, con una cuenta propia y sin programar.

[Diapositiva · Una parte web y una parte de aprendizaje automático]

Ideas, en orden:

- Plantear la pregunta que se hizo en el ensayo: si ya existe la red, ¿por qué una página web y no correrla desde Google Colab?
- Colab es un cuaderno en la nube, un entorno donde se escribe código y se entrena el modelo. Entrenar produce un archivo (con extensión `.pt`) que guarda lo que la red aprendió. Ese archivo, por sí solo, no hace nada.
- La plataforma lo carga y le pone una interfaz: botones para subir fotos y pantallas para ver resultados. Así cualquiera puede usarlo, sin instalar nada ni saber programar.
- El acceso al análisis es con una cuenta personal y privada.
- Imaginar el caso contrario: para usar el modelo desde Colab habría que abrir un cuaderno, entender el código y ejecutarlo celda por celda. Para quien investiga con células, eso es una barrera que no tiene por qué existir.

> El modelo es un archivo que, por sí solo, pues... no puede hacer nada. La plataforma web es lo que permite que cualquier persona de la comunidad universitaria use la inteligencia artificial desde un navegador.

[Diapositiva · Palabras que vamos a escuchar]

- Explicar en una frase los términos que van a salir: red neuronal (un programa que aprende de ejemplos), Google Colab (un entorno para programar en la nube), Python (un lenguaje de programación), Flask (una herramienta para hacer sitios web con Python), modelo (el archivo que guarda lo que la red aprendió) y servidor (la computadora donde el sitio está en línea).
- No leer la diapositiva completa: señalar las que aparecen en esta sesión. Entrenamiento e inferencia se definen en la siguiente diapositiva.

> Antes de seguir, unas palabras que van a salir. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python. El sitio está hecho con las dos.

[Diapositiva · Entrenamiento aparte, inferencia en el servidor]

- Definir las dos etapas del desarrollo de la red: el entrenamiento, que se hace en Colab, y la inferencia, que se hace en el servidor. Inferencia es usar el modelo ya entrenado para analizar fotos nuevas; se hace en el procesador del servidor.
- Dos partes con cuidados distintos: la parte web, que se mantiene como cualquier sitio, y la parte de aprendizaje automático, que se mejora con datos.
- Una consecuencia práctica: para mejorar el modelo no se toca el sitio. Se entrena aparte y se cambia el archivo del modelo.

> Entonces, el desarrollo de la red tiene dos etapas. Primero se entrena en Google Colab y, después, cuando queremos analizar fotos nuevas, usamos el modelo en el servidor. A eso se le llama inferencia, ¿va?

[Diapositiva · Un entorno educativo con seis secciones]

- Presentar el sitio en general como un entorno educativo con seis secciones: Inicio, Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto. Más adelante se recorre cada una.
- Además de la red neuronal, el sitio presenta a los colaboradores y temas de biología de la reproducción. Es un sitio informativo con una sección que analiza imágenes.

> El sitio tiene seis secciones. Ahorita las nombro, y en unos minutos las vemos una por una.

---

## Bloque 4. Qué es una imagen digital

*0:31-0:42 · 11 min (10 hablados) · tope 1,700 palabras*

Idea que debe quedar: para la computadora una fotografía es una tabla de números, y eso explica todo lo que vamos a medir.

[Diapositiva · Una fotografía es una tabla de números]

Ideas, en orden:

- Pregunta: ¿qué es una fotografía para una computadora?
- Una cuadrícula de cuadritos. Cada cuadrito es un píxel y guarda un número. En una imagen en tonos de gris, el número es el brillo, de 0 (negro) a 255 (blanco). En color son tres números, uno por rojo, verde y azul.
- Mostrar una zona de la foto muy ampliada hasta que se vean los cuadritos. En la diapositiva, una zona pequeña con números bajos casi en todos lados y altos en el centro.
- Una foto grande puede tener 1,792 por 1,374 píxeles: casi dos millones y medio de cuadritos, cada uno con su número.

> Para la computadora, una fotografía es, o sea, una tabla de números. Cada cuadrito, cada píxel, guarda cuánta luz tiene.

> Una foto grande tiene, por ejemplo, mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Son más de dos millones de números.

[Diapositiva · Una célula brillante son números altos]

- En una foto de fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. La computadora no ve una célula; ve números.
- Medir el área de una célula es contar cuántos píxeles ocupa. En el ejemplo de la diapositiva, la célula ocupa doce cuadritos: su área es de doce píxeles.
- Con la escala del sitio, esos píxeles se convierten en micras. Eso se ve en un momento.

> La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

> En este ejemplo, los números altos forman la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

- Formatos: BMP, PNG y TIFF conservan la imagen tal cual. JPG la comprime y puede alterar los bordes de las células, y con ellos los contornos y las medidas.
- Recomendación: trabajar con los archivos originales del microscopio y evitar que pasen por aplicaciones de mensajería, que los comprimen.
- Por qué importa: si el borde se difumina, el contorno cambia, y si el contorno cambia, cambia el área. El sitio acepta JPG, pero avisa.

> BMP, PNG y TIFF guardan la imagen tal cual. JPG la comprime, y al comprimirla puede mover los bordes de las células. Para medir, eso importa.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

- Una foto sabe cuántos píxeles mide, pero no cuántas micras es cada uno. Los archivos no guardan esa información.
- Las imágenes vienen de distintos aumentos, por ejemplo 40X y 100X. Por eso el sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, para estandarizar su tamaño y poder compararlas entre sí. Cada resultado dice qué escala se usó. No entrar en más detalle; el método se ve en la sesión 3.

> Una foto no sabe cuánto mide un píxel en la realidad. Por eso el sitio usa la misma escala en todas las imágenes, para estandarizar su tamaño, y cada resultado dice cuál.

---

## Bloque 5. El sitio, visto como visitante

*0:42-0:53 · 11 min (8 hablados) · tope 1,360 palabras*

Idea que debe quedar: cualquier persona puede recorrer el sitio sin cuenta, y es sencillo, bilingüe y se adapta a la pantalla.

[Diapositiva · Presentación del sistema]

[Pantalla: cambiar al navegador, con el sitio abierto en la página de inicio, sin sesión iniciada y con el zoom al 125 %. Arriba, centrado, el logotipo (un círculo azul con un punto verde) junto al nombre IMAGE BIO PRO y el lema «Análisis de imágenes de microscopio». Debajo, una barra blanca con el botón «Menú» (tres rayas) a la izquierda y, a la derecha, «ES | EN» e «Iniciar sesión». En el cuerpo, el título «Image Bio Pro», una frase corta, un botón verde «Analizar una imagen» y, a la derecha, un recuadro punteado reservado para la imagen principal. Más abajo, tarjetas numeradas («1 de 3», «2 de 3», «3 de 3») que cuentan el problema, el recorrido y los resultados.]

> Bueno, ahora sí, voy a mostrarles el sitio, empezando como lo vería cualquier visitante, o sea, sin haber iniciado sesión.

Ideas, en orden:

- Inicio: el nombre del proyecto con su lema, «Análisis de imágenes de microscopio», un espacio para una imagen principal y un botón para analizar una imagen.
- El menú de hamburguesa despliega las seis secciones. A la derecha, el selector de idioma (ES y EN) y el acceso para iniciar sesión.

[Acción: clic en «Menú». Se despliega una lista a lo ancho con seis opciones, una debajo de otra: Inicio (resaltada en azul), Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto.]

- Decir que la interfaz ya es funcional y que el diseño se sigue mejorando.
- Nosotros: qué es Image Bio Pro.
- Aliados: una tarjeta por persona, con nombre, fotografía y lo que estudió. Quien quiera aparecer solo tiene que mandar sus datos.

[Acción: abrir Aliados. Se ve una cuadrícula de tarjetas, cuatro por fila. Cada tarjeta tiene el nombre arriba, un recuadro cuadrado para la fotografía y un texto breve debajo. Con el contenido real cargado se ven los nombres y las fotos; si todavía no, aparecen los marcadores de ejemplo («Dr. Nombre Apellido», «[foto]» y un texto de relleno).]

- Infografías y videos: las infografías se abren en una ventana grande, con la imagen y su texto, como un blog. El título va fuera de la imagen. Abajo hay videos de YouTube dentro de la misma página.

[Acción: abrir Infografías y videos. Arriba, el bloque «Infografías», con tarjetas; al hacer clic en una se abre una ventana grande, centrada, con el título, la imagen y el texto, y se cierra con la X. Más abajo, el bloque «Videos»: reproductores de YouTube de dos en dos, cada uno con su título debajo.]

- Contacto: formulario con nombre, correo y mensaje, y los datos de contacto.

[Acción: abrir Contacto, cuyo título es «Haz contacto». A la izquierda, los datos de contacto (correo, teléfono y dirección, de ejemplo) y un recuadro reservado para un mapa. A la derecha, «Envíanos un mensaje»: campos de nombre, correo y mensaje, y el botón «Enviar».]

> En Aliados hay una tarjeta por persona, con su nombre, su fotografía y lo que estudió. Si alguien quiere aparecer, solo tiene que mandar sus datos.

> Las infografías se abren en una ventana grande, como en un blog, con la imagen y su texto. Abajo hay videos de YouTube, dentro de la misma página.

- Idioma: al elegir EN, el sitio se traduce completo con el servicio de Google integrado, sin dos versiones del sitio. A cambio, la calidad es la de un traductor automático; los nombres propios y los nombres de archivo están marcados para que no se traduzcan.

[Acción: clic en «EN», arriba a la derecha. Menú, títulos, botones y textos cambian a inglés en pantalla, mientras que los nombres propios (como Image Bio Pro) quedan igual. Volver a «ES» al terminar.]

> Si elijo EN, el sitio completo se traduce con el servicio de Google, así que no hay dos versiones del sitio. La calidad es la de un traductor automático, pero los nombres propios no se traducen.

- Pie de página: nombre del proyecto, institución, contacto de ejemplo, enlaces del menú, aviso de privacidad 2026 y mención de la licencia Creative Commons Atribución-No Comercial (verificar la versión).
- Estilo sobrio, con pocos colores, que se adapta a distintos tamaños de pantalla.

[Acción: bajar hasta el final de la página. Una franja azul oscura con el nombre «Image Bio Pro» y la institución a la izquierda, el contacto y el año a la derecha, los enlaces del menú en una fila y, al final, una línea con el aviso de privacidad 2026 y la licencia Creative Commons.]

> Con esto queda la parte informativa. Lo que justifica el proyecto es el análisis de imágenes y, para usarlo, hace falta una cuenta.

---

## Bloque 6. Crear una cuenta

*0:53-0:59 · 6 min (4 hablados) · tope 680 palabras*

Idea que debe quedar: el sitio se recorre sin cuenta, pero para analizar imágenes hay que iniciar sesión, y eso hace que cada análisis sea privado.

[Pantalla: hacer clic en «Iniciar sesión», arriba a la derecha. Se abre «Mi cuenta», con dos columnas bajo el título. A la izquierda, «Iniciar sesión»: correo electrónico, contraseña, la casilla «Recordarme en este equipo» y el botón «Entrar». A la derecha, «Crear cuenta»: nombre, correo electrónico, contraseña (con la nota «Al menos 8 caracteres») y el botón «Registrarme».]

Ideas, en orden:

- La página «Mi cuenta» tiene dos columnas: a la izquierda, quien ya tiene cuenta; a la derecha, la cuenta nueva.
- Tres datos: el nombre (aparece en los informes y en la parte superior del sitio), el correo (es el identificador para entrar; no tiene que ser de Gmail ni está ligado a ningún servicio externo) y una contraseña de al menos ocho caracteres.
- [Acción: escribir un nombre, un correo y una contraseña de ejemplo en la columna derecha y hacer clic en «Registrarme».] Si todo está bien, la cuenta se crea y la sesión inicia en el acto, con un mensaje de bienvenida. El sitio lleva directo a «Analizar imagen», y arriba a la derecha, donde decía «Iniciar sesión», ahora se lee el nombre de la persona y «Salir».

> Con la cuenta creada, el sitio me lleva directo a «Analizar imagen». Ya puedo subir mis fotos.

- Mostrar «Salir» y volver a entrar. Hay una casilla «Recordarme en este equipo»: cómoda en un equipo personal, poco recomendable en uno compartido.

[Acción: clic en «Salir», arriba a la derecha. La página vuelve a mostrar «Iniciar sesión». Entrar de nuevo con el correo y la contraseña de ejemplo, en la columna izquierda, y hacer clic en «Entrar».]
- La contraseña no se guarda tal cual: se guarda una versión cifrada que no se puede invertir.
- Subrayar que el acceso a la red neuronal es privado y se hace con un usuario. Es una de las cosas que el revisor pidió destacar.

> Para analizar imágenes hay que iniciar sesión. Así cada análisis pertenece a una persona y solo esa persona puede verlo.

*Si preguntan por qué el error de contraseña es vago:* para que nadie pueda averiguar qué correos están registrados.

---

## Bloque 7. Analizar una imagen y esperar

*0:59-1:12 · 13 min (8 hablados) · tope 1,360 palabras*

Idea que debe quedar: subir una imagen es sencillo, no hay parámetros que ajustar, y es normal que el análisis tarde.

[Pantalla: página «Inteligencia Artificial», con el título «Analizar imagen». Una franja con una caja blanca en el centro: la etiqueta «Sube tus imágenes (hasta 10)», el selector de archivos, la nota «Formatos: BMP, PNG o TIFF. JPG se acepta, pero pierde calidad», el aviso de que el análisis puede tardar y no hay que cerrar la página, el botón verde «Analizar» y, justo debajo, el botón «Probar con la imagen de ejemplo». Más abajo, «Infografías recientes» y un enlace para ver todas.]

Ideas, en orden:

- El recuadro tiene solo lo necesario: elegir archivos, «Analizar» y «Probar con la imagen de ejemplo». No hay parámetros ajustables ni opciones avanzadas, a propósito.
- Subir de una a diez imágenes, hasta 300 MB por envío. Formatos: BMP, PNG o TIFF; JPG con una advertencia, porque pierde calidad al comprimirse.
- Agrupar las fotos por tipo y condición antes de subirlas facilita comparar después.

> No hay parámetros ni opciones avanzadas, y es a propósito: así, dos personas que analicen la misma imagen obtienen el mismo resultado.

- [Acción: hacer clic en «Probar con la imagen de ejemplo».] Decir que es una imagen sintética, dibujada para la prueba: óvalos de colores, cada uno con una línea verde que hace de cola, sobre un fondo negro. Sirve para ver el flujo completo sin tener una foto propia.

[Pantalla: la página se difumina y aparece al centro una tarjeta blanca con «Analizando las imágenes…», una barra verde rayada que se mueve sin parar, el texto «Es normal que el análisis tarde… No cierres esta página» y, pasado un minuto, una línea más con letra gruesa: «Tu análisis sigue en curso».]

- Aparece una cubierta con una barra de progreso, el aviso «No cierres esta página» y un mensaje que dice que es normal que el análisis tarde. Es una barra de actividad: confirma que el sistema está trabajando. Si pasa un minuto, aparece otro aviso: «Tu análisis sigue en curso».
- Tiempos: una foto grande de fluorescencia tarda unos 40 segundos y una de fondo claro entre 10 y 20. Si se suben varias, se analizan una tras otra y los tiempos se suman. Por eso el sitio tiene tiempos de espera amplios.
- Presentar la espera como algo normal y explicado, no como un fallo. Si la gente no sabe por qué tarda, pensará que el sistema es lento o complicado.

> Es normal que el análisis tarde, eh. Si pasa un minuto, el sitio avisa que el análisis sigue en curso.

- Mientras esperamos, contar lo que pasa del otro lado: la imagen viaja al servidor, que revisa el formato, mide el brillo para saber si es de fondo oscuro o claro y elige uno de los dos modelos. Analiza la imagen por recortes pequeños, la red devuelve un contorno por cada espermatozoide, se juntan y se miden. Todo en el procesador del servidor.
- No entrar en el detalle de los recortes ni de cómo se juntan los resultados: eso es del lunes.

> Mientras esperamos, les cuento qué pasa del otro lado. La imagen viaja al servidor, que revisa el formato y mide el brillo para saber si es de fondo oscuro o de fondo claro. Con eso elige uno de los dos modelos y analiza la imagen por recortes pequeños.

[Acción: cuando termine, el sitio abre solo la página de resultados. Si la espera se alarga, abrir el análisis que ya está hecho: clic en el nombre de la persona, arriba a la derecha, y en la primera fila de «Mis análisis».]

---

## Bloque 8. Leer los resultados

*1:12-1:29 · 17 min (14 hablados) · tope 2,380 palabras*

Idea que debe quedar: cada elemento de la pantalla se puede rastrear hasta un contorno de la imagen, y los números se leen siempre junto con la imagen y la gráfica.

[Pantalla: página «Resultados del análisis». De arriba hacia abajo: las migas de pan (Inicio › Inteligencia Artificial › Resultados), el título, una línea con el nombre de quien hizo el análisis y la fecha y hora, un recuadro azul con el aviso de escala y, enseguida, el nombre de la imagen con su mensaje en verde y una línea gris con el formato, las dimensiones, el modo de color y el peso. Recorrer sin prisa.]

Ideas, en orden:

- Encabezado: el nombre de quien hizo el análisis, con fecha y hora exactas. Sirve para distinguir muchos análisis.
- Aviso de escala: el sitio usa la misma escala en todas las imágenes para estandarizar su tamaño, 60 píxeles por micra. La imagen marcada trae una regla de 300 píxeles que equivalen a 5 micras.
- Mensajes por imagen: uno verde si se analizó con éxito. También puede avisar que hay compresión que altera los bordes, que se contaron muy pocos espermatozoides (menos de tres) y la distribución no es confiable, o que no se encontró nada y no se analizó. Entre un «no se pudo» honesto y un número dudoso, el sitio prefiere el primero.
- Datos de la imagen: formato, dimensiones en píxeles, modo de color y peso.

> Arriba aparece quién hizo el análisis, con fecha y hora, y un aviso de escala: el sitio usa la misma en todas las imágenes, sesenta píxeles por micra, para estandarizar su tamaño.

> Cada imagen trae su propio mensaje. Si todo salió bien, es verde. Si hay algo que cuidar, como compresión o muy pocos espermatozoides, el sitio lo avisa. Prefiere decir «no se pudo» a darles un número dudoso.

[Pantalla: bajar un poco. Debajo se ven dos columnas. A la izquierda, la fotografía sobre fondo negro con cada espermatozoide rodeado por un contorno blanco y numerado, y en la esquina inferior izquierda una regla blanca con la leyenda «300 px = 5 micras». A la derecha, tres recuadros con números grandes y, debajo, dos párrafos pequeños con el largo y las cifras en píxeles.]

- A la izquierda, la fotografía con cada espermatozoide marcado y numerado. A la derecha, tres recuadros: el conteo, el área media y la desviación estándar, en micras cuadradas. Debajo, el largo (media y desviación estándar en píxeles, con mínimo y máximo) y, aparte, las mismas cifras en píxeles y el largo en micras.
- Explicar la desviación estándar en una frase: cuánto se alejan, en promedio, las áreas de la media.
- Decir «largo» sin entrar al método; el detalle es de la sesión 3.

> Cada número tiene un contorno detrás. Si dice ciento catorce, hay ciento catorce contornos que se pueden revisar uno por uno.

[Pantalla: a la derecha, bajo el título «Distribución de tamaños», una gráfica de barras de color azul claro con borde azul. En el eje horizontal, diez intervalos de área en píxeles; en el vertical, «Células», el número de células de cada intervalo. Señalar con el cursor la barra más alta.]

- El histograma: en el eje horizontal el área en píxeles, dividida en diez intervalos iguales entre el mínimo y el máximo de la imagen; en el vertical, cuántas células caen en cada uno. No supone ninguna forma: dibuja lo que se midió. Con varias imágenes se usa un rango común y aparece una gráfica de promedios.
- El sitio no interpreta los resultados ni los compara con valores de referencia; esa lectura corresponde al grupo.
- Explicar cómo se lee: una barra alta es un tamaño que se repite mucho; barras repartidas, tamaños muy distintos.

> El histograma divide el rango de áreas en diez intervalos iguales y cuenta cuántas células caen en cada uno. No supone ninguna forma: dibuja lo que se midió.

[Acción: hacer clic sobre la imagen (en la esquina se lee «Clic para ampliar»). Se abre una ventana a pantalla completa con fondo oscuro. Arriba, los botones «−», «+», «Ajustar» y «100%», y la guía «Rueda para acercar · arrastra para mover». Acercar con la rueda, arrastrar para mover y pasar el cursor sobre un espermatozoide: aparece su número, su área y su largo. Cerrar con la X de arriba a la derecha.]

- El visor sirve para revisar si un contorno corresponde de verdad a un espermatozoide. Al pasar el cursor sale su número, su área y su largo, en píxeles y en micras.
- Si en la imagen de ejemplo hay un contorno que no encierra una cabeza completa, usarlo como ejemplo de por qué conviene revisar.

> El visor sirve para comprobar con sus propios ojos que cada contorno sea de verdad un espermatozoide.

[Pantalla: bajar hasta «Detalle por espermatozoide»: una tabla con una fila por célula y las columnas «#», «Área (px)», «Largo (px)», «Área (µm²)» y «Largo (µm)». La tabla tiene su propio desplazamiento dentro del recuadro.]

- Más abajo, la tabla con una fila por espermatozoide, con el área y el largo en píxeles y en micras. Es la misma información que el CSV.
- Leer los números siempre junto con la imagen y la gráfica. Un ejemplo con números inventados, dicho como tal: dos fotos con 120 y 80 células no significan que una muestra tenga más, porque cada foto cuenta lo que estaba en esa zona. Una diferencia de medias solo se puede afirmar con una prueba estadística, y eso lo decide el grupo con el CSV.

> La media sin la gráfica puede engañar. Antes de confiar en un número, miren la imagen marcada y el histograma.

> Un ejemplo con números inventados: una foto con ciento veinte células y otra con ochenta. Eso no quiere decir que una muestra tenga más. Cada foto cuenta lo que había en esa zona.

---

## Bloque 9. Lo que no es un espermatozoide

*1:29-1:38 · 9 min (7 hablados) · tope 1,190 palabras*

Idea que debe quedar: el modelo no es perfecto: puede equivocarse, el sitio avisa cuando no puede analizar, y la forma de mejorar es con más datos, más variados y mejor etiquetados.

[Diapositiva · ¿Y si la imagen no es de espermatozoides?]

Ideas, en orden:

- Plantear la pregunta: ¿qué pasa si subo una imagen que no es de espermatozoides?
- [Acción: en «Analizar imagen», elegir con el selector de archivos las tres imágenes preparadas (por ejemplo, células de hígado y de riñón) y hacer clic en «Analizar». Esperar el resultado.] Mostrar lo que el sitio realmente responda: un mensaje en rojo sobre la imagen o, si marca algo, la imagen con sus contornos. Si responde «no se encontraron espermatozoides o la imagen es de mala calidad; no es factible analizarla», decirlo así: el sitio no entrega números dudosos.
- Aclarar que no hay garantía: la red aprendió de pocas imágenes y puede marcar manchas que se le parezcan.
- Insistir en que el aviso es parte del diseño: el sitio prefiere no analizar a inventar un resultado.

> Si subo una imagen que no es de espermatozoides, lo que espero es que el sitio me diga que no es factible analizarla. Entre un aviso claro y un número dudoso, prefiere el aviso.

[Diapositiva · Falso positivo: en programación, alucinación]

- [Acción: mostrar un caso con un falso positivo, si existe: abrir el visor sobre un contorno que encierre una mancha, una sombra o un trozo de cola y no una cabeza completa.] Un falso positivo es marcar como espermatozoide algo que no lo es, por ejemplo una sombra, una mancha o un trozo de cola. En programación a esto se le llama también alucinación.
- Por qué pasa: la red solo aprende de los ejemplos que vio. Con pocos ejemplos, hay casos que no aprendió a resolver.
- Cómo se mejora: más datos, más variados y mejor etiquetados. Si aun así no alcanza, habría que cambiar de arquitectura.
- Qué puede hacer cada persona: revisar la imagen marcada y guardar las imágenes que el modelo analiza con dificultad, porque son las más útiles para reentrenar.

> A veces el modelo marca algo que parece un espermatozoide y no lo es. En biología se le llama falso positivo; en programación, pues, alucinación.

> Un modelo mejora con ejemplos de sus propios errores. Por eso el grupo es quien puede hacerlo mejor: tiene las imágenes y el criterio para etiquetarlas.

*Si preguntan si el modelo mejora solo con el uso:* no. Un modelo en línea no aprende de las imágenes que analiza. Para mejorarlo hay que reunir imágenes nuevas, etiquetarlas, reentrenar en Colab y cambiar el archivo del modelo en el servidor. Eso se ve en la sesión 4.

---

## Bloque 10. Descargas, Mis análisis y privacidad

*1:38-1:46 · 8 min (6 hablados) · tope 1,020 palabras*

Idea que debe quedar: el CSV es el dato para trabajar, el PDF es el informe para compartir, y cada análisis es privado y queda guardado.

[Pantalla: bajar al final de la página de resultados. Debajo de la tabla hay una fila de botones: «Imprimir» (verde), «Descargar PDF» y «Descargar CSV» (con borde) y el enlace «Analizar otras imágenes».]

Ideas, en orden:

- CSV: un archivo de texto, con una fila por espermatozoide y seis columnas (imagen, número, área y largo en píxeles, área y largo en micras). Se abre en una hoja de cálculo o con código. Sirve para seguir trabajando con los datos.
- PDF: un solo informe con todas las imágenes. Primera página con el encabezado, el usuario, la fecha y el número de imágenes; luego una página por imagen, con su marca, sus datos y su gráfica; y al final la gráfica de promedios. Las medidas van primero en micras y después en píxeles. Se genera una sola vez y no cambia después.
- Imprimir: oculta el menú y los botones; se imprime solo el análisis.

> El CSV es el dato para trabajar. El PDF es el informe para compartir. Conviene guardar los dos.

> El PDF trae una página por imagen, con la imagen marcada, sus datos y su gráfica. Las medidas van primero en micras y después en píxeles.

[Acción: clic en el nombre de la persona, arriba a la derecha. Se abre el perfil: el nombre como título, el correo debajo y, bajo «Mis análisis», una tabla de tres columnas (fecha y hora, imágenes y descargas) con una fila por análisis. La fecha es un enlace al análisis, y en la última columna están los enlaces «PDF» y «CSV».]

- «Mis análisis»: una tabla con una fila por análisis, con la fecha, las imágenes y los enlaces al PDF y al CSV. Al abrir uno se ve igual que cuando terminó; no se recalcula.
- Qué se guarda y qué no: se guardan los resultados, una copia reducida de la imagen marcada y el PDF. Las imágenes originales se borran del servidor al terminar el análisis. Hay que guardar los originales por cuenta propia.
- Privacidad: cada análisis es de quien lo hizo y solo esa persona puede verlo.
- [Acción: hacer clic en «Salir», arriba a la derecha; el sitio vuelve a mostrar «Iniciar sesión».]

> En «Mis análisis» queda una fila por cada análisis, con sus enlaces al PDF y al CSV. Al abrirlo, se ve igual que cuando terminó.

> Las imágenes que suben se borran del servidor cuando termina el análisis. Guarden sus originales en su propia computadora.

---

## Bloque 11. Cierre y adelanto de la sesión 2

*1:46-1:51 · 5 min · tope 850 palabras*

Idea que debe quedar: el sitio convierte una fotografía en datos confiables y descargables, y la siguiente pregunta es cómo sabe la red dónde hay un espermatozoide.

[Diapositiva · Lo que vimos hoy]

Ideas, en orden:

- Resumir en cuatro frases: el problema (contar y medir a mano), la idea (la red localiza, el código mide), el sitio (cuenta, análisis, resultados, descargas) y la privacidad (cada análisis es de quien lo hizo).

> Para cerrar: el problema era contar y medir a mano; la idea, que la red localiza y el código mide; el sitio, que convierte una foto en datos que se pueden revisar y descargar; y cada análisis es de quien lo hizo.

[Diapositiva · Cinco hábitos para usar el sitio]

- Cinco hábitos: trabajar con los archivos originales; agrupar las imágenes por tipo y condición; revisar la imagen marcada antes de confiar en los números; guardar el CSV; y guardar las imágenes que el modelo analiza con dificultad, porque son las más útiles para reentrenar.

> Cinco hábitos para llevarse: usar los archivos originales, agrupar las imágenes por tipo, revisar la imagen marcada antes de confiar en un número, guardar el CSV y guardar las imágenes difíciles.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Seguramente muchos se preguntan cómo sabe el sistema dónde hay un espermatozoide... bueno, esa es la pregunta de mañana: cómo aprende una computadora.

> El lunes vemos cómo funciona por dentro, y ahí les cuento los retos: las células empalmadas, los falsos positivos y la escala. Gracias por conectarse.

---

## Diapositivas que necesita esta sesión

La presentación tiene 23 diapositivas, numeradas. El sistema no lleva diapositivas con capturas: se presenta en el navegador. Las diapositivas, en este orden:

| Bloque | Diapositiva |
|---|---|
| 1 | Image Bio Pro · Las cuatro sesiones · La agenda de hoy |
| 2 | La inteligencia artificial en la educación y la investigación · El caso de estudio · Contar y medir a mano · La red localiza y el código mide · Tres principios · Funciona y se puede mejorar |
| 3 | Una parte web y una parte de aprendizaje automático · Palabras que vamos a escuchar · Entrenamiento aparte, inferencia en el servidor · Un entorno educativo con seis secciones |
| 4 | Una fotografía es una tabla de números · Una célula brillante son números altos · Formatos: unos conservan los bordes, otros no · La imagen no sabe cuánto mide un píxel |
| 5 a 8 y 10 | Presentación del sistema (una sola diapositiva; se pasa al navegador) |
| 9 | ¿Y si la imagen no es de espermatozoides? · Falso positivo: en programación, alucinación |
| 11 | Lo que vimos hoy · Cinco hábitos para usar el sitio · ¿Cómo sabe el sistema dónde hay un espermatozoide? |

Letra grande, con pocas ideas por diapositiva y dibujos sencillos donde ayuden (la tabla de píxeles del bloque 4, por ejemplo).
