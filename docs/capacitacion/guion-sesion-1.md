# Guion de la sesión 1: El problema y el sitio

Image Bio Pro · Capacitación · viernes 23 de octubre de 2026, de 6:00 a 8:00 pm

Esta sesión es la primera de cuatro. Presenta el problema como caso de estudio de inteligencia artificial, la idea de imagen digital y el sitio funcionando. Cómo aprende la red se ve en la sesión 2; cómo funciona el sistema por dentro, en la sesión 3; datos, reentrenamiento y despliegue, en la sesión 4.

## Cómo usar este guion

Cada bloque tiene cuatro partes:

- Idea que debe quedar: lo único que el público tiene que llevarse del bloque.
- Ideas, en orden: el hilo del bloque en pocas líneas. Sirve para estudiar y para no perderse; si sabes el hilo, el texto sale solo.
- Texto para decir: el texto completo del bloque. Las frases en recuadro amarillo (en el .md, las que empiezan con `>`) son las frases ancla: aperturas, definiciones y transiciones, que se dicen casi literales. El resto se puede leer, pero conviene decirlo con palabras propias mirando el hilo.
- Indicaciones entre corchetes: en rojo las de pantalla y acciones, en azul las diapositivas. No se dicen en voz alta.

Las muletillas («eh», «este», «bueno», «o sea») y los puntos suspensivos de las frases ancla marcan el tono platicado, con algo de nervio al inicio. Se dicen como salgan; no hay que repetirlos al pie de la letra.

Ritmo medido: el 22 de octubre se cronometró el bloque 1 (108 palabras en 35 segundos), que da 185 palabras por minuto. Los tiempos de este guion usan ese ritmo con el texto completo de cada bloque.

## Resumen de tiempos

| Bloque | Hora | Min | Palabras | Habla (min) | Palabras ancla |
|---|---|---|---|---|---|
| 1. Bienvenida y agenda | 0:00-0:05 | 5 | 659 | 3.6 | 108 |
| 2. El caso de estudio | 0:05-0:19 | 14 | 2,315 | 12.5 | 212 |
| 3. Por qué una plataforma web | 0:19-0:27 | 8 | 1,149 | 6.2 | 120 |
| 4. Qué es una imagen digital | 0:27-0:36 | 9 | 1,292 | 7.0 | 150 |
| 5. El sitio, visto como visitante | 0:36-0:46 | 10 | 871 | 4.7 | 133 |
| 6. Crear una cuenta | 0:46-0:52 | 6 | 503 | 2.7 | 37 |
| 7. Analizar una imagen y esperar | 0:52-1:01 | 9 | 1,015 | 5.5 | 51 |
| 8. Leer los resultados | 1:01-1:15 | 14 | 1,681 | 9.1 | 188 |
| 9. Lo que no es un espermatozoide | 1:15-1:26 | 11 | 1,156 | 6.2 | 85 |
| 10. Descargas, Mis análisis y privacidad | 1:26-1:32 | 6 | 661 | 3.6 | 62 |
| 11. Cierre y adelanto de la sesión 2 | 1:32-1:36 | 4 | 464 | 2.5 | 121 |
| Margen | 1:36-2:00 | 24 | - | - | - |
| Total | | 120 | 11,766 | 63.6 | 1,267 |

Las dos horas son seguidas. De los 120 minutos, unos 64 son de habla, unos 32 son pantalla, demostración y pausas entre diapositivas, y 24 quedan de margen. El margen no se llena: sirve para preguntas, para una demostración que se alargue o para terminar a tiempo. La columna «Habla» es el texto escrito de cada bloque dicho a 185 palabras por minuto; «Min» es el tiempo del bloque con la pantalla incluida.

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
14. Tiempos. La primera versión de este guion calculaba los tiempos con topes de palabras y no con el texto escrito, y prometía mucho más tiempo del que el texto cubría. Esta versión suma el texto real de cada bloque. Si en el ensayo un bloque sale más largo o más corto, ajustar la hora en la tabla de tiempos.

---

## Bloque 1. Bienvenida y agenda

*0:00-0:05 · 5 min · 659 palabras, unos 3.6 min de habla*

Idea que debe quedar: son cuatro sesiones, hoy vemos el problema y el sitio, y pueden preguntar cuando quieran.

Ideas, en orden:

- Saludo y presentación: nombre y qué hace.
- Qué es este curso y cómo se va a contar: un solo proyecto, desde adentro.
- La sesión queda grabada.
- Cómo preguntar: en cualquier momento; lo muy técnico se deja para el final.
- Las cuatro sesiones y sus enfoques.
- La agenda de hoy y el tono: dos horas seguidas, cada término técnico se explica.

Texto para decir:

[Diapositiva · Image Bio Pro]

> Eh... buenas tardes a todos, y gracias por conectarse. Este... soy Angel Frausto Robles, desarrollador de Image Bio Pro.

Les agradezco que estén aquí, sobre todo un viernes por la tarde. Antes de entrar en materia, les cuento rápido de qué se trata esto. Es la primera de cuatro sesiones del curso BIOIMAGE 2026, y todo el curso gira alrededor de un solo proyecto: un sitio web que cuenta y mide espermatozoides en fotografías de microscopio, usando inteligencia artificial.

Yo fui quien desarrolló ese sitio, así que lo que les voy a contar no sale de un libro. Es lo que fui viendo mientras lo construía, con lo que funcionó y con lo que costó trabajo. Por eso van a escucharme explicar tanto el sitio como las decisiones que hay detrás.

> Bueno, primero... esta sesión queda grabada. Si tienen una duda, pregúntenme en cualquier momento, ¿va? Eh, las respuestas muy técnicas las dejamos para el final, para no perder el hilo.

Lo digo desde ahora para que nadie se sorprenda después. La grabación se comparte más adelante y se puede editar si hace falta. Y sobre las preguntas: esto es una charla, no un examen. Yo no les voy a hacer preguntas a ustedes. Quien quiera preguntar, lo hace en el momento que le surja la duda, por el chat o con la voz, como prefiera. Voy a tratar de responder breve y concreto. Si la pregunta es muy técnica, les voy a decir que la vemos al final de la sesión, o en la sesión que corresponda, para no perder el hilo de lo que estamos viendo.

[Diapositiva · Las cuatro sesiones]

> Son cuatro sesiones. Hoy vemos el problema y el sitio... mañana, cómo aprende la computadora; el lunes, cómo funciona el sistema por dentro; y el martes, este, los datos y cómo se reentrena el modelo.

Cada sesión es de dos horas, por Zoom, y cada una se enfoca en una parte distinta de cómo se hace un sistema como este. Hoy, viernes, vemos la parte de adelante: lo que ve y usa una persona cuando entra al sitio. En programación a eso se le llama frontend. Mañana, sábado por la mañana, vemos cómo aprende la computadora, y ahí entran las redes neuronales convolucionales, que son las que saben mirar imágenes.

El lunes vemos la parte de atrás, lo que pasa dentro del sistema cuando alguien sube una imagen. A eso se le llama backend. Y el martes cerramos con los datos, con cómo se vuelve a entrenar el modelo cuando llegan imágenes nuevas, y con cloud computing, que quiere decir usar una computadora en internet, en lugar de la nuestra, para que el sitio esté disponible para todos. Ese día les voy a enseñar cómo subimos este sitio a un servidor de verdad.

[Diapositiva · La agenda de hoy]

> Hoy vamos a empezar por el problema, luego veremos qué es una imagen digital y después el sitio. Al final, un análisis en vivo.

Les detallo un poco más. Primero voy a plantear el problema que vamos a resolver, y por qué conviene hacerlo con una página web en lugar de un programa suelto. Después vamos a ver qué es una imagen digital para una computadora, porque de ahí sale todo lo que se mide. Luego pasamos al sitio funcionando, en el navegador: cómo se crea una cuenta, cómo se sube una imagen, cómo se leen los resultados y cómo se descargan. Y casi al final vemos qué pasa cuando la imagen no es de espermatozoides, porque ahí se entiende bien hasta dónde llega el modelo.

Son dos horas seguidas, así que si alguien necesita pararse un momento, lo puede hacer con toda confianza, que la grabación queda. Y una última cosa sobre el tono: este curso es para una comunidad universitaria con perfiles distintos, algunos con más programación, otros con más biología. Por eso cada término técnico lo voy a explicar en una frase la primera vez que aparezca. Si se me pasa alguno, pregúntenme sin pena.

---

## Bloque 2. El caso de estudio

*0:05-0:19 · 14 min · 2,315 palabras, unos 12.5 min de habla*

Idea que debe quedar: vamos a aprender cómo se usa la inteligencia artificial resolviendo un problema concreto, contar y medir espermatozoides en fotografías, y la clave es repartir el trabajo entre la red y el código.

Ideas, en orden:

- Para qué sirve la inteligencia artificial en la educación y la investigación; una aplicación es analizar imágenes.
- La microscopía como fuente de imágenes y el objetivo del curso.
- Aprender con un caso de estudio; no hace falta venir de la programación ni de la biología.
- La foto de ejemplo y el problema de contar y medir a mano.
- Dos tipos de foto, con un modelo para cada una.
- La red localiza y el código mide; por qué se reparte así.
- Tres principios: no suponer, separar, reproducir.
- Funciona y se puede mejorar; los retos se cuentan al final.

Texto para decir:

[Diapositiva · La inteligencia artificial en la educación y la investigación]

Empiezo con una pregunta, y no hace falta que la contesten en voz alta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Hay muchas respuestas, y una de ellas, que es la que nos interesa hoy, es analizar imágenes. Una persona mira una foto y reconoce lo que hay en ella. Un programa que aprendió de muchos ejemplos puede hacer algo parecido, y puede hacerlo muchas veces seguidas sin cansarse.

Vale la pena detenernos un momento en qué quiere decir aprender de ejemplos, porque es la idea que sostiene todo el curso. Tradicionalmente, cuando uno quiere que una computadora haga algo, le escribe reglas: si pasa esto, haz aquello. Eso funciona muy bien para una calculadora o para una hoja de cálculo, donde las reglas son exactas. Pero para reconocer un espermatozoide en una foto, escribir las reglas es casi imposible. ¿Cómo describirían ustedes, con reglas exactas, la forma de una cabeza, con todas sus variaciones de tamaño, de orientación y de brillo? Cada vez que escribieran una regla, aparecería una foto que la rompe.

En lugar de escribir las reglas, se le muestran a la computadora muchos ejemplos ya resueltos. Es decir, fotos donde una persona marcó a mano dónde están los espermatozoides. El programa ajusta por sí mismo lo que necesita para reproducir esas marcas. A eso se le llama aprender de ejemplos, y a lo que resulta de ese proceso se le llama modelo. Cómo sucede ese ajuste lo vemos mañana con calma; hoy solo necesitamos quedarnos con la idea de que el modelo no recibió reglas, recibió ejemplos.

Las imágenes vienen de muchas fuentes, y una de las más importantes en las ciencias de la vida es la microscopía. Con un microscopio podemos ver células, por ejemplo espermatozoides, y podemos ver cómo cambian de tamaño y de forma bajo ciertas condiciones. Cuando se estudia eso, cada foto trae información, pero alguien tiene que sacarla: contar, medir, comparar.

Para quienes no han trabajado con fluorescencia, una explicación breve. En esta técnica las células se tiñen con un colorante que, al recibir cierta luz, la devuelve en otro color. Por eso en la foto la célula brilla y el fondo queda oscuro: lo único que vemos es lo que está teñido. Esto tiene una consecuencia útil para lo que vamos a hacer, y es que hay mucho contraste entre la célula y el fondo. Más adelante, cuando veamos cómo se ve una imagen para una computadora, esto va a tener mucho sentido.

También conviene decir qué tipo de preguntas se contestan con estas fotos. Quien estudia espermatozoides puede querer saber cuántos hay en una muestra, qué tan grandes son, si ese tamaño cambia cuando cambia una condición, y qué tanto varían unos de otros. Todas esas preguntas se contestan midiendo, y medir a mano, uno por uno, es justo lo que vamos a ver que se vuelve un problema.

El objetivo de esta capacitación es acercar a la comunidad universitaria, de distintas áreas, a lo que es la inteligencia artificial y a cómo se aplica a un problema técnico y científico real. En este caso, un problema de biología de la reproducción. No estamos hablando de teoría en el aire: vamos a seguir un problema concreto de principio a fin.

> Entonces, eh, para entender cómo se aplica la inteligencia artificial, vamos a seguir un caso de estudio, o sea, un ejemplo concreto: contar y medir espermatozoides en fotografías de microscopio.

> Y no se preocupen si algún término no les suena: cada vez que aparezca uno nuevo, lo explico en una frase.

Quiero que quede claro que no hace falta venir de la programación ni de la biología. Si saben programar, van a ver cómo se arma el sistema. Si vienen de biología, van a ver cómo se mide lo que ustedes ya conocen. Y si vienen de otra área, van a ver cómo se aplica la inteligencia artificial a un problema que se puede entender. Aprendemos a través de un ejemplo, y el ejemplo es este.

[Diapositiva · El caso de estudio]

Les muestro cómo se ve el problema. Esta es una foto de fluorescencia, que es una técnica de microscopía donde las células se tiñen y brillan. Lo que ven son manchas de colores brillantes sobre un fondo oscuro. Cada mancha es la cabeza de un espermatozoide, y a veces se alcanza a ver una línea que sale de ella, que es la cola.

Ahora pregunto, sin esperar respuesta: ¿cuántos hay en esta foto? Lo primero que haría cualquiera es contarlos con la vista, uno por uno. Y luego, si además hay que medir cada uno, ya no basta con mirar.

[Diapositiva · Contar y medir a mano]

El problema es este: contar y medir a mano es lento, es repetitivo y cambia según quién lo haga. Una sola foto puede traer decenas o cientos de células. Muchas están encimadas o pegadas unas a otras, y ahí es donde cada persona decide distinto dónde termina una y empieza la otra. No es falta de cuidado. Es que el ojo no tiene una regla fija.

En la diapositiva puse tres conteos distintos de la misma foto, de tres personas distintas. Son números de ejemplo, no de una medición real, pero la idea es esa: tres personas cuidadosas pueden llegar a tres resultados distintos. Y si además hay que comparar muchas imágenes, el trabajo manual se vuelve muy difícil de sostener.

Además de contar, muchas veces lo que importa para la investigación es el tamaño: cuánto mide cada célula, cuánto varía de una a otra y cómo cambia ese tamaño entre una condición y otra. Medir cada célula a mano exige trazar su contorno con cuidado y leer el resultado, una y otra vez. Multipliquen eso por cientos de células en una foto y por muchas fotos. Un sistema que haga ese trabajo siempre de la misma manera deja de ser un lujo y se vuelve algo que de verdad hace falta.

Hay otra consecuencia que a veces se pasa por alto: el cansancio. Una persona que lleva una hora contando no mide igual que cuando empezó. Un programa no se cansa, y esa regularidad, para comparar fotos entre sí, vale mucho.

> Imaginen contar a mano cien células en una foto, y luego repetirlo con muchas fotos... este, cada persona contaría algo distinto, ¿no?

Una cosa más sobre las fotos. En este proyecto trabajamos con dos tipos. Las de fluorescencia, que ya les mostré, con las células brillando sobre un fondo oscuro. Y las de fondo claro, que se ven distinto porque el fondo ya no es oscuro. Para cada tipo tenemos un modelo distinto, y más adelante vamos a ver cómo el sitio elige el que corresponde.

> Trabajamos con dos tipos de foto: las de fluorescencia, donde las células brillan sobre un fondo oscuro, y las de fondo claro. Para cada tipo tenemos un modelo distinto.

[Diapositiva · La red localiza y el código mide]

Aquí está la idea central del proyecto, la que más quiero que se lleven hoy: repartir el trabajo. Una red neuronal, que es un programa que aprende de ejemplos, hace una sola cosa. Decide dónde hay un espermatozoide y traza su contorno. Nada más.

Todo lo demás lo hace código convencional, el que se escribe paso a paso. Cuántos hay, cuánto mide cada uno, cuál es la media y cuál es la desviación estándar. Son procedimientos explícitos y estandarizados, que cualquiera puede revisar y repetir.

Piénsenlo como un asistente que señala y una calculadora que mide. El asistente puede equivocarse al señalar, pero lo que señaló se puede ver. La calculadora siempre hace la misma cuenta con lo que le dan.

> La red localiza y el código mide. Y bueno, esa división se repite en todo el proyecto.

¿Por qué conviene repartirlo así? Porque si la red hiciera todo, cada número saldría de una caja cerrada y no habría cómo comprobarlo. Con el reparto, lo único que no se puede explicar paso a paso es dónde está el contorno, y eso se ve a simple vista. En la práctica, uno abre la imagen marcada, mira el contorno que trazó la red y recalcula la medida. La red propone, y la medición se puede auditar.

Les doy un ejemplo de qué quiere decir que sea verificable. Supongamos que el sitio dice que una célula tiene cierta área. Ustedes abren la imagen marcada, ven el contorno que se trazó alrededor de esa célula y se preguntan: ¿ese contorno está bien? Si está bien, el área que se calculó dentro de él es simplemente un conteo de píxeles, una operación que cualquiera puede repetir con una regla de tres. Si no está bien, el problema está en el contorno, que es lo único que decidió la red, y eso se ve a simple vista en la imagen.

Dividir el trabajo así tiene una ventaja que me parece muy valiosa para la ciencia: acota dónde puede estar un error y lo hace visible. Si el programa completo fuera una caja negra que recibe una foto y devuelve una cifra, un error podría estar en cualquier parte y nadie lo vería. Con el reparto, el único punto que no se explica paso a paso es la ubicación del contorno, y ese punto se puede comprobar con los ojos.

[Diapositiva · Tres principios]

Hay tres principios que explican lo que vamos a ver en estas sesiones, y se los dejo desde ahora para que los vayan reconociendo.

> Hay tres principios que explican lo que vamos a ver. El primero... no suponer. Cuando a un dato le falta información, el sitio no la inventa: la indica en pantalla.

El primero es no suponer. Cuando falta un dato, como la escala de la imagen o lo que marca cada tinción, el sitio no lo inventa: lo indica en pantalla. Por eso cada resultado muestra la escala que se usó. Prefiere un aviso claro a un número que parezca más seguro de lo que es.

Les pongo un ejemplo concreto de este principio. Las imágenes del microscopio no traen escrito cuánto mide cada píxel. El sitio podría simplemente suponer un valor y no decir nada. En lugar de eso, usa una escala que declara abiertamente, la repite en cada resultado y la imprime en el informe. Quien lee un número sabe con qué escala se calculó. Es más incómodo decirlo que callarlo, pero es más honesto, y en ciencia eso pesa.

> El segundo, separar lo que decide la red de lo que se mide. Y el tercero, que todo se pueda repetir: el entrenamiento está en un cuaderno que cualquiera puede abrir y ejecutar.

El segundo es separar lo que decide la red de lo que se mide. Eso ya lo vimos: la red localiza y el código mide, así que cualquier medida se verifica sin abrir la red.

El tercero es la reproducibilidad. El entrenamiento está en un cuaderno de Colab, que es un entorno para programar en la nube, y cualquiera puede abrirlo y ejecutarlo. Además, el modelo guarda dentro de su propio archivo la configuración con la que se entrenó. Si hay que repetir un resultado o reconstruir el entorno, no depende de la memoria de nadie.

Esto importa en ciencia más de lo que parece. Un resultado que no se puede repetir es muy difícil de defender, y lo mismo pasa con un modelo del que nadie recuerda cómo se hizo. Por eso el entrenamiento no es una caja negra que solo yo sé operar: está en un cuaderno abierto, con los pasos escritos en orden, y el modelo carga dentro de sí la configuración con la que se entrenó. Si dentro de un año alguien quiere repetirlo, o mejorarlo, tiene de dónde partir. El martes vamos a abrir ese cuaderno y a verlo por dentro.

Los tres principios se pueden resumir en una sola actitud: decir siempre qué se sabe, qué se supone y cómo se obtuvo cada número. Si en algún momento de estas sesiones algo les parece raro, vuelvan a estos tres principios, porque casi siempre explican por qué el sitio se comporta como lo hace.

[Diapositiva · Funciona y se puede mejorar]

Sobre el estado del modelo, lo digo en general y sin entrar en detalle: funciona, está dando buenos resultados y, como cualquier modelo, se puede mejorar. Tiene pruebas hechas, y mejora con más imágenes.

Algo importante: un modelo así no aprende solo mientras está en línea. Si llegan imágenes nuevas, otras tinciones u otro tipo de célula, se vuelve a entrenar aparte y se cambia el archivo del modelo. Eso lo vemos el martes, con detalle.

También quiero adelantarles que el proyecto tuvo retos, y que los voy a contar como lo que fueron: dificultades que se resolvieron. Les doy un ejemplo. Cuando muchas células se empalman en un mismo punto, contarlas es muy difícil, y se creó una estrategia computacional para contarlas mejor.

Sobre las limitaciones, prefiero ser directo desde ahora, para que no haya sorpresas después. Es un modelo que se entrenó con un conjunto limitado de imágenes. En imágenes que se parecen a las de su entrenamiento, funciona bien. En imágenes muy distintas puede equivocarse, y por eso el sitio tiene avisos y por eso cada resultado se puede revisar. Esa franqueza es parte de cómo se usa bien una herramienta así. Lo que hace el sitio es dar números y mostrar cómo se obtuvieron. La interpretación científica de esos números le corresponde al grupo, y el sitio no la sustituye.

Si me permiten una comparación, es como un instrumento de laboratorio. Una balanza no decide si el resultado de un experimento es bueno o malo, solo da el peso. Este sistema cuenta y mide, y lo hace de forma consistente y revisable. Qué significan esas cuentas y esas medidas es una pregunta de ustedes, que son quienes conocen la biología detrás.

> Al final de las sesiones les cuento los retos que enfrentamos y cómo les dimos la vuelta. Les adelanto uno... cuando muchas células se empalman, pues, contarlas es muy difícil.

---
## Bloque 3. Por qué una plataforma web

*0:19-0:27 · 8 min · 1,149 palabras, unos 6.2 min de habla*

Idea que debe quedar: el modelo entrenado, solo, no hace nada. La plataforma web es lo que permite que cualquier persona de la universidad lo use, con una cuenta propia y sin programar.

Ideas, en orden:

- La pregunta del ensayo: si ya existe la red, ¿por qué una página web y no correrla desde Colab?
- Qué es Colab y qué produce el entrenamiento: un archivo .pt que, solo, no hace nada.
- La plataforma le pone una interfaz; el acceso es con cuenta personal y privada.
- Palabras que van a salir: red neuronal, Colab, Python, Flask, modelo, servidor.
- Dos etapas: entrenamiento en Colab e inferencia en el servidor.
- El sitio como entorno educativo con seis secciones.

Texto para decir:

[Diapositiva · Una parte web y una parte de aprendizaje automático]

Ahora, una pregunta que salió cuando ensayamos esta presentación y que me parece muy buena: si ya tenemos la red neuronal que encuentra los espermatozoides, ¿para qué hacer además una página web? ¿No bastaría con correr la red directamente desde Google Colab?

Les explico qué es Colab, porque lo voy a mencionar varias veces. Google Colab es un cuaderno en la nube, un entorno donde se escribe código y se ejecuta sin instalar nada en la computadora. Ahí es donde se entrena el modelo. Y cuando termina el entrenamiento, lo que sale es un archivo, con extensión punto pt, que guarda lo que la red aprendió.

> El modelo es un archivo que, por sí solo, pues... no puede hacer nada. La plataforma web es lo que permite que cualquier persona de la comunidad universitaria use la inteligencia artificial desde un navegador.

Eso es lo que quiero que se lleven de este bloque. Ese archivo, por sí solo, es como un libro cerrado: tiene todo adentro, pero nadie lo puede leer. Necesitamos un sistema que lo abra, lo cargue y lo use. Eso es lo que hace la plataforma. Le pone una interfaz: botones para subir fotos y pantallas para ver los resultados.

Imaginen el caso contrario. Para usar el modelo desde Colab, cada persona tendría que abrir un cuaderno, entender el código y ejecutarlo celda por celda. Para alguien que investiga con células, eso es una barrera que no tiene por qué existir. Con la plataforma, cualquiera entra desde un navegador, sin instalar nada y sin saber programar. Y el acceso al análisis es con una cuenta personal y privada, algo que vamos a ver cuando lleguemos al sitio.

Hay otra razón práctica para preferir una página web a un programa que cada quien instale. Un programa instalado hay que mantenerlo al día en cada computadora: cada persona con su versión, cada una con sus dependencias, y cuando el modelo mejora hay que repartir el archivo nuevo a todos. En una plataforma web, el modelo vive en un solo lugar, que es el servidor. Cuando mejora, se cambia ahí, y desde ese momento todas las personas que entran usan la versión nueva sin hacer nada. Además, todas usan exactamente el mismo modelo, y eso es lo que permite comparar resultados entre personas.

Para entender cómo funciona una página web, una idea sencilla basta por ahora. Hay dos lados. De su lado está el navegador, que es el programa que usan para ver páginas. Del otro lado está el servidor, una computadora que está siempre encendida, conectada a internet, esperando peticiones. Cuando ustedes hacen clic en un botón, el navegador le manda una petición al servidor, el servidor hace el trabajo que corresponda y devuelve una respuesta, que el navegador dibuja en la pantalla. Así funciona desde la página de un periódico hasta este sitio. La diferencia es que, aquí, el trabajo del servidor incluye correr un modelo de inteligencia artificial sobre una imagen. El lunes vemos con detalle qué hace el servidor, y el martes vemos cómo se pone ese servidor en internet.

[Diapositiva · Palabras que vamos a escuchar]

Antes de seguir, les dejo en pantalla unas palabras que van a escuchar durante las cuatro sesiones. No las voy a leer todas, solo las que salen hoy.

Una red neuronal es un programa que aprende de ejemplos. Google Colab, como ya dije, es un entorno para programar en la nube. 

> Antes de seguir, unas palabras que van a salir. Python es un lenguaje de programación, y Flask es una herramienta para hacer sitios web con Python. El sitio está hecho con las dos.

El modelo es el archivo que guarda lo que la red aprendió. Y el servidor es la computadora donde el sitio está en línea, la que responde cuando alguien entra.

También aparecen dos palabras que explico en la siguiente diapositiva, entrenamiento e inferencia, porque son las que más confunden y las que más importa distinguir.

[Diapositiva · Entrenamiento aparte, inferencia en el servidor]

El desarrollo de la red neuronal ocurre en dos etapas, y están separadas a propósito.

> Entonces, el desarrollo de la red tiene dos etapas. Primero se entrena en Google Colab y, después, cuando queremos analizar fotos nuevas, usamos el modelo en el servidor. A eso se le llama inferencia, ¿va?

La primera etapa es el entrenamiento. Se hace en Colab, con imágenes que las personas ya marcaron a mano, y de ahí sale el archivo del modelo. La segunda etapa es la inferencia, que es usar el modelo ya entrenado para analizar fotos nuevas. Eso se hace en el servidor, en el procesador de la computadora donde está el sitio.

Esto tiene una consecuencia práctica que vale la pena entender. Para mejorar el modelo no se toca el sitio. Se entrena aparte, se obtiene un archivo nuevo y se cambia ese archivo en el servidor. Son dos partes con cuidados distintos: la parte web se mantiene como cualquier sitio, y la parte de aprendizaje automático se mejora con datos.

Una comparación que ayuda: el entrenamiento es como aprender una receta, y la inferencia es como cocinarla las veces que haga falta. Aprender la receta lleva tiempo y esfuerzo, con muchos intentos y correcciones, y se hace una vez, o cada vez que se quiere mejorar. Cocinar con la receta ya aprendida es mucho más rápido y se repite todos los días. Con el sitio pasa igual: entrenar el modelo es lo pesado, y por eso se hace aparte, en Colab, donde hay más capacidad de cálculo. Usarlo para analizar una foto es lo ligero, y por eso puede hacerse en el procesador del servidor del sitio.

Esta separación tiene una ventaja más. El sitio no necesita saber cómo se entrenó el modelo, solo necesita el archivo. Si mañana se entrena una versión mejor, se reemplaza el archivo y el sitio sigue funcionando igual.

[Diapositiva · Un entorno educativo con seis secciones]

Para terminar este bloque, una mirada general al sitio. Lo pensamos como un entorno educativo, con la herramienta de análisis como una de sus partes. Además de la red neuronal, el sitio presenta a las personas que colaboran y temas de biología de la reproducción. Es un sitio informativo que tiene una sección donde se analizan imágenes.

> El sitio tiene seis secciones. Ahorita las nombro, y en unos minutos las vemos una por una.

Las seis secciones son: Inicio, Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto. En la diapositiva las ven con una frase corta cada una. La que nos importa para el análisis es Inteligencia Artificial, y es la que necesita cuenta. Las demás se pueden recorrer sin iniciar sesión. Más adelante entramos al sitio y las vemos funcionando.

Las seis secciones están pensadas para que el sitio sirva también a quien llega sin ninguna intención de analizar una imagen: puede leer una infografía, ver un video o conocer a quienes colaboran. La sección de análisis es el corazón técnico, pero el sitio quiere ser también un lugar donde se aprende.

---

## Bloque 4. Qué es una imagen digital

*0:27-0:36 · 9 min · 1,292 palabras, unos 7.0 min de habla*

Idea que debe quedar: para la computadora una fotografía es una tabla de números, y eso explica todo lo que vamos a medir.

Ideas, en orden:

- ¿Qué es una fotografía para una computadora? Una cuadrícula de píxeles, cada uno con un número.
- Brillo de 0 a 255 en gris; en color, tres números. Una foto grande tiene millones de píxeles.
- Una célula brillante es una zona de números altos; medir el área es contar píxeles.
- Formatos: BMP, PNG y TIFF conservan la imagen; JPG la comprime y mueve los bordes.
- La imagen no sabe cuánto mide un píxel; el sitio usa la misma escala, 60 píxeles por micra.

Texto para decir:

[Diapositiva · Una fotografía es una tabla de números]

Vamos con algo que parece muy básico y de lo que depende todo lo demás. La pregunta es: ¿qué es una fotografía para una computadora?

> Para la computadora, una fotografía es, o sea, una tabla de números. Cada cuadrito, cada píxel, guarda cuánta luz tiene.

Una fotografía digital es una cuadrícula de cuadritos. Cada cuadrito es un píxel, y cada píxel guarda un número. En una imagen en tonos de gris, ese número es el brillo, y va de cero, que es negro, a doscientos cincuenta y cinco, que es blanco. Los números intermedios son los grises. En una imagen a color no es un número sino tres, uno para el rojo, otro para el verde y otro para el azul, y con la mezcla de los tres sale el color de ese cuadrito.

En la diapositiva tengo a la izquierda una foto pequeña con un cuadro azul marcado, y a la derecha lo que hay dentro de ese cuadro, ampliado hasta que se ven los números. Son treinta y cinco cuadritos, siete por cinco. Fíjense en la parte de afuera: números bajos, casi negros. Y en el centro, números altos, hasta un doscientos cincuenta y cinco. Eso es lo que la computadora tiene delante cuando mira una foto.

> Una foto grande tiene, por ejemplo, mil setecientos noventa y dos píxeles de ancho por mil trescientos setenta y cuatro de alto. Son casi dos millones y medio de números.

Hagan la cuenta: casi dos millones y medio de cuadritos, cada uno con su número. La computadora los maneja todos a la vez sin problema, pero a un ojo humano eso no le dice nada. Lo que vemos como células, la computadora lo ve como un mar de números.

Un detalle sobre esos números del cero al doscientos cincuenta y cinco: tienen una razón. Cada píxel guarda su valor en un byte, que son ocho bits, y con ocho bits se pueden representar doscientos cincuenta y seis valores distintos. Por eso el rango empieza en cero y termina en doscientos cincuenta y cinco. Con esos doscientos cincuenta y seis niveles el ojo ve un degradado suave de negro a blanco, sin escalones. En una imagen a color son tres bytes por píxel, uno por cada color.

Y una idea más, la de resolución. Cuantos más píxeles tiene una foto, más detalle puede guardar, porque cada cuadrito representa una zona más pequeña de lo que se fotografió. Una foto con pocos píxeles se ve pixelada cuando se amplía, justamente porque los cuadritos ya no alcanzan a describir la forma. Por eso a las fotos del microscopio les conviene tener muchos píxeles: para que la forma de cada célula quede descrita con detalle.

[Diapositiva · Una célula brillante son números altos]

Ahora pensemos en una foto de fluorescencia. ¿Cómo se ve una célula dentro de esa tabla de números? Como una zona de números altos sobre un fondo de números bajos. La célula brilla, así que sus píxeles tienen valores grandes, y el fondo oscuro tiene valores pequeños.

> La computadora no ve células, solo números. Y nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

Esto cambia la forma de plantear el problema.

Y esto también nos dice cómo se mide el tamaño. En la diapositiva les muestro una célula pequeñita dibujada con números. Los doce cuadritos más brillantes, los que tienen el borde marcado, son la célula.

> En este ejemplo, los números altos forman la célula. Si cuento los cuadritos que ocupa, doce, ya tengo su área: doce píxeles.

Medir el área de una célula es contar cuántos píxeles ocupa. En una foto real serán cientos de píxeles por célula, pero la idea es exactamente la misma. Más adelante, con la escala del sitio, esos píxeles se convierten en micras.

Una pregunta que seguramente se están haciendo: ¿y no bastaría con decir que todo píxel por encima de cierto valor es célula? Es una idea natural y es, de hecho, el primer intento que se suele hacer. Se llama umbralización: se elige un umbral y todo lo que lo supera se considera objeto. Funciona razonablemente cuando las células están separadas y bien iluminadas, pero falla cuando se tocan, cuando hay manchas brillantes que no son células, o cuando el brillo cambia de una foto a otra. Mañana vemos por qué no basta y cómo una red neuronal retoma esa idea y suma otros factores. Hoy les dejo solo la intuición de que la computadora, en el fondo, está comparando números.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

Un tema práctico: los formatos de archivo. No todos guardan la imagen igual.

> BMP, PNG y TIFF guardan la imagen tal cual. JPG la comprime, y al comprimirla puede mover los bordes de las células. Para medir, eso importa.

JPG, en cambio, comprime la imagen para que pese menos. En la diapositiva tengo la misma célula dos veces: a la izquierda con el borde nítido y a la derecha con el borde difuminado y con bloques raros, que es lo que pasa con la compresión.

¿Por qué importa? Porque si el borde se difumina, el contorno cambia, y si el contorno cambia, cambia el área, y entonces cambian los números que nos interesan. El sitio acepta JPG, pero lo avisa. La recomendación es trabajar con los archivos originales del microscopio y evitar que pasen por aplicaciones de mensajería, que suelen comprimirlos sin que nos demos cuenta.

Un dato que ayuda a entender la diferencia: una foto de las que usamos, guardada como BMP, pesa alrededor de siete megabytes, porque guarda todos sus píxeles sin comprimir. El mismo contenido en JPG puede pesar una fracción de eso, y ahí está el atractivo del JPG: ocupa menos. Pero ese ahorro de espacio se paga con fidelidad, y para medir, la fidelidad es justo lo que necesitamos.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

La última idea de este bloque es la escala. Una foto sabe cuántos píxeles mide, pero no sabe cuántas micras es cada píxel, es decir, cuánto mide en la realidad. Los archivos no guardan esa información.

Además, las imágenes pueden venir de distintos aumentos, por ejemplo de cuarenta X y de cien X, y cada aumento cambia lo que representa un píxel. Si queremos comparar fotos entre sí, necesitamos una forma de ponerlas en la misma medida.

> Una foto no sabe cuánto mide un píxel en la realidad. Por eso el sitio usa la misma escala en todas las imágenes, para estandarizar su tamaño, y cada resultado dice cuál.

Por eso el sitio usa la misma escala en todas las imágenes: sesenta píxeles por micra. Es una forma de estandarizar su tamaño y poder compararlas entre sí. Cada resultado dice qué escala se usó, y la imagen marcada trae una regla de trescientos píxeles que equivalen a cinco micras. No voy a entrar hoy en cómo se define esa escala; eso lo vemos el lunes, cuando hablemos de cómo funciona el sistema por dentro.

Les doy dos conversiones concretas, para que la escala no se quede en abstracto. Si sesenta píxeles son una micra, entonces un largo de sesenta píxeles es una micra de largo, y un largo de trescientos píxeles son cinco micras, que es justo la regla que va dibujada en la imagen. Con las áreas hay un paso más. Un área se mide en unidades cuadradas, así que una micra cuadrada son sesenta por sesenta píxeles, es decir, tres mil seiscientos píxeles. Si una célula ocupa tres mil seiscientos píxeles, su área es de una micra cuadrada; si ocupa la mitad, de media micra cuadrada. Por eso, en el sitio, las áreas en micras cuadradas pueden salir como números pequeños.

Y para ubicarnos en la unidad: una micra es la milésima parte de un milímetro. Es la medida natural para hablar de células, porque a esa escala los milímetros resultan demasiado grandes.

---
## Bloque 5. El sitio, visto como visitante

*0:36-0:46 · 10 min · 871 palabras, unos 4.7 min de habla*

Idea que debe quedar: cualquier persona puede recorrer el sitio sin cuenta, y es sencillo, bilingüe y se adapta a la pantalla.

Ideas, en orden:

- Inicio: nombre, lema, botón para analizar y espacio para la imagen principal.
- El menú con las seis secciones, el selector de idioma y el acceso para iniciar sesión.
- Nosotros, Aliados, Infografías y videos, y Contacto.
- Idioma: EN traduce todo el sitio con el servicio de Google.
- Pie de página: privacidad, licencia, enlaces.
- Para analizar imágenes hace falta una cuenta.

Texto para decir:

[Diapositiva · Presentación del sistema]

[Pantalla: cambiar al navegador, con el sitio abierto en la página de inicio, sin sesión iniciada y con el zoom al 125 %. Arriba, centrado, el logotipo (un círculo azul con un punto verde) junto al nombre IMAGE BIO PRO y el lema «Análisis de imágenes de microscopio». Debajo, una barra blanca con el botón «Menú» (tres rayas) a la izquierda y, a la derecha, «ES | EN» e «Iniciar sesión». En el cuerpo, el título «Image Bio Pro», una frase corta, un botón verde «Analizar una imagen» y, a la derecha, un recuadro punteado reservado para la imagen principal. Más abajo, tarjetas numeradas («1 de 3», «2 de 3», «3 de 3») que cuentan el problema, el recorrido y los resultados.]

> Bueno, ahora sí, voy a mostrarles el sitio, empezando como lo vería cualquier visitante, o sea, sin haber iniciado sesión.

Estoy compartiendo el navegador. Lo primero que ven es la página de inicio. Arriba, centrado, está el logotipo con el nombre del proyecto y su lema: «Análisis de imágenes de microscopio». Debajo hay una barra con el botón de menú a la izquierda, y a la derecha el selector de idioma y el acceso para iniciar sesión.

En el cuerpo de la página está el título, una frase que resume lo que hace el sitio y un botón verde que dice «Analizar una imagen». A la derecha hay un recuadro punteado que está reservado para una imagen principal, que se va a poner cuando la tengamos. Más abajo hay tres tarjetas que cuentan el problema, el recorrido y los resultados, en el mismo orden en que lo estamos viendo hoy.

Quiero decir algo sobre el diseño: la interfaz ya es funcional, ya se puede usar completa, pero el diseño se sigue afinando. Lo que ven hoy no es la versión final de cómo se ve.

Algo que cuidamos desde el principio es que la página se lea bien en cualquier pantalla. Si abren este mismo sitio en un teléfono, el menú se acomoda y el contenido se reordena, y no hace falta acercar con los dedos para leer. También es una página sobria a propósito: pocos colores, letra legible, nada que distraiga. Un sitio científico no necesita impresionar, necesita que cualquiera encuentre rápido lo que busca.

[Acción: clic en «Menú». Se despliega una lista a lo ancho con seis opciones, una debajo de otra: Inicio (resaltada en azul), Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto.]

Si abro el menú, aparecen las seis secciones de las que hablamos hace un rato, una debajo de otra: Inicio, Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto. Voy a recorrerlas rápido, una por una.

Nosotros es la sección que cuenta qué es Image Bio Pro. Es texto, y se va a cargar con el contenido real del grupo. Ahí se explica, con palabras sencillas, de qué trata el proyecto y para qué sirve.

[Acción: abrir Aliados. Se ve una cuadrícula de tarjetas, cuatro por fila. Cada tarjeta tiene el nombre arriba, un recuadro cuadrado para la fotografía y un texto breve debajo. Con el contenido real cargado se ven los nombres y las fotos; si todavía no, aparecen los marcadores de ejemplo («Dr. Nombre Apellido», «[foto]» y un texto de relleno).]

> En Aliados hay una tarjeta por persona, con su nombre, su fotografía y lo que estudió. Si alguien quiere aparecer, solo tiene que mandar sus datos.

Es una cuadrícula de tarjetas, cuatro por fila, y todas se ven igual: el nombre arriba, la fotografía en el centro y debajo un texto breve. Me gusta que esta sección ponga caras y nombres. Un sistema de inteligencia artificial puede parecer algo abstracto y sin dueño, y aquí se ve que detrás hay personas, cada una con su formación y sus intereses.

[Acción: abrir Infografías y videos. Arriba, el bloque «Infografías», con tarjetas; al hacer clic en una se abre una ventana grande, centrada, con el título, la imagen y el texto, y se cierra con la X. Más abajo, el bloque «Videos»: reproductores de YouTube de dos en dos, cada uno con su título debajo.]

> Las infografías se abren en una ventana grande, como en un blog, con la imagen y su texto. Abajo hay videos de YouTube, dentro de la misma página.

Cada infografía es una tarjeta, y el título va fuera de la imagen para que se lea bien. Los videos se reproducen sin que tengan que salir del sitio. Las infografías son una forma de explicar ideas difíciles con una imagen y un texto corto, y por eso las pusimos como complemento del análisis: en la propia pantalla de análisis aparecen unas recientes, para que quien está esperando o explorando pueda leer algo útil.

[Acción: abrir Contacto, cuyo título es «Haz contacto». A la izquierda, los datos de contacto (correo, teléfono y dirección, de ejemplo) y un recuadro reservado para un mapa. A la derecha, «Envíanos un mensaje»: campos de nombre, correo y mensaje, y el botón «Enviar».]

Contacto es la sección más sencilla. A la izquierda están los datos de contacto y un espacio para un mapa, y a la derecha un formulario con nombre, correo y mensaje. Lo que se escribe aquí queda guardado para el equipo. Si alguien del curso encuentra un error en el sitio, un texto que no se entiende o tiene una sugerencia, este es el canal.

[Acción: clic en «EN», arriba a la derecha. Menú, títulos, botones y textos cambian a inglés en pantalla, mientras que los nombres propios (como Image Bio Pro) quedan igual. Volver a «ES» al terminar.]

Ahora algo que a veces sorprende. Arriba a la derecha hay un selector de idioma. Si elijo EN, el sitio completo se traduce al inglés.

> Si elijo EN, el sitio completo se traduce con el servicio de Google, así que no hay dos versiones del sitio. La calidad es la de un traductor automático, pero los nombres propios no se traducen.

Eso tiene una ventaja, que es que todo el sitio queda traducido sin trabajo extra, y una desventaja, que es que la calidad es la de un traductor automático. Para cuidar eso, los nombres propios y los nombres de archivo están marcados para que no se traduzcan. Vuelvo a español. La ventaja práctica es que si un colega de otro país quiere usarlo, o si alguien prefiere leer en inglés, puede hacerlo sin que tengamos que mantener dos sitios distintos.

[Acción: bajar hasta el final de la página. Una franja azul oscura con el nombre «Image Bio Pro» y la institución a la izquierda, el contacto y el año a la derecha, los enlaces del menú en una fila y, al final, una línea con el aviso de privacidad 2026 y la licencia Creative Commons.]

Si bajo hasta el final de la página, está el pie. Tiene el nombre del proyecto y la institución, un contacto de ejemplo, los mismos enlaces del menú, y abajo dos cosas que pidió el grupo: el aviso de privacidad 2026 y la mención de la licencia Creative Commons, Atribución y No Comercial. El estilo es sobrio, con pocos colores, y se adapta a distintos tamaños de pantalla, así que también se puede ver desde un teléfono.

> Con esto queda la parte informativa. Lo que justifica el proyecto es el análisis de imágenes y, para usarlo, hace falta una cuenta.

Hasta aquí todo se puede recorrer sin cuenta. Pero la sección que justifica el proyecto es la de Inteligencia Artificial, la que analiza imágenes, y esa sí necesita que alguien inicie sesión. Vamos a crear una cuenta.

---

## Bloque 6. Crear una cuenta

*0:46-0:52 · 6 min · 503 palabras, unos 2.7 min de habla*

Idea que debe quedar: el sitio se recorre sin cuenta, pero para analizar imágenes hay que iniciar sesión, y eso hace que cada análisis sea privado.

Ideas, en orden:

- «Mi cuenta» tiene dos columnas: entrar y crear cuenta.
- Tres datos: nombre, correo y contraseña de al menos ocho caracteres.
- Al registrarse, la sesión inicia en el acto y el sitio lleva a «Analizar imagen».
- Salir y volver a entrar; «Recordarme en este equipo».
- La contraseña se guarda cifrada; el acceso a la red es privado.

Texto para decir:

[Pantalla: hacer clic en «Iniciar sesión», arriba a la derecha. Se abre «Mi cuenta», con dos columnas bajo el título. A la izquierda, «Iniciar sesión»: correo electrónico, contraseña, la casilla «Recordarme en este equipo» y el botón «Entrar». A la derecha, «Crear cuenta»: nombre, correo electrónico, contraseña (con la nota «Al menos 8 caracteres») y el botón «Registrarme».]

Voy a hacer clic en «Iniciar sesión». Se abre una página que se llama «Mi cuenta» y que tiene dos columnas. A la izquierda está quien ya tiene cuenta: pone su correo y su contraseña y entra. A la derecha está quien todavía no: la cuenta nueva.

Para crear una cuenta se piden tres datos. El nombre, que es el que aparece en los informes y arriba en el sitio. El correo, que es con lo que se entra: no tiene que ser de Gmail ni está ligado a ningún servicio externo, sirve cualquier correo. Y una contraseña de al menos ocho caracteres.

[Acción: escribir un nombre, un correo y una contraseña de ejemplo en la columna derecha y hacer clic en «Registrarme».] Si todo está bien, la cuenta se crea y la sesión inicia en el acto, con un mensaje de bienvenida. El sitio lleva directo a «Analizar imagen», y arriba a la derecha, donde decía «Iniciar sesión», ahora se lee el nombre de la persona y «Salir».

> Con la cuenta creada, el sitio me lleva directo a «Analizar imagen». Ya puedo subir mis fotos.

Fíjense: no tuve que confirmar nada por correo ni esperar a que alguien me aprobara. Me registré y ya estoy dentro, y el sitio me llevó a la pantalla donde se suben las imágenes.

[Acción: clic en «Salir», arriba a la derecha. La página vuelve a mostrar «Iniciar sesión». Entrar de nuevo con el correo y la contraseña de ejemplo, en la columna izquierda, y hacer clic en «Entrar».]

Voy a salir y a volver a entrar para que vean las dos cosas. Hay una casilla que dice «Recordarme en este equipo». Es cómoda si es una computadora personal, porque no hay que escribir la contraseña cada vez, pero no la recomiendo en una computadora compartida.

Sobre la contraseña: el sitio no la guarda tal cual. Guarda una versión cifrada que no se puede revertir, así que ni siquiera quien administra el sitio puede ver cuál es. Una recomendación general, que sirve en cualquier sitio: no usen aquí una contraseña que ya usan en otro servicio.

Y una cosa que a veces intriga: ¿cómo sabe el sitio que soy yo mientras navego? Cuando inicio sesión, el sitio le da a mi navegador una especie de pase, que se llama cookie, y mi navegador lo manda en cada petición. Por eso el sitio sabe quién soy mientras me muevo de una pantalla a otra. La casilla de «Recordarme en este equipo» hace que ese pase dure más tiempo, y por eso conviene dejarla marcada solo en una computadora propia.

Si alguien escribe mal su contraseña, el sitio dice que el correo o la contraseña son incorrectos, sin precisar cuál de los dos. Es a propósito: así nadie puede averiguar qué correos están registrados probando uno por uno.

> Para analizar imágenes hay que iniciar sesión. Así cada análisis pertenece a una persona y solo esa persona puede verlo.

Quiero subrayar esto porque lo pidió el equipo que revisó la presentación: el acceso a la red neuronal es privado y se hace con un usuario. Cada análisis es de quien lo hizo, y nadie más puede verlo. Incluso si dos personas analizan exactamente la misma imagen, cada una tiene su propio análisis, con su nombre y su fecha, y ninguna ve el de la otra.

---

## Bloque 7. Analizar una imagen y esperar

*0:52-1:01 · 9 min · 1,015 palabras, unos 5.5 min de habla*

Idea que debe quedar: subir una imagen es sencillo, no hay parámetros que ajustar, y es normal que el análisis tarde.

Ideas, en orden:

- El recuadro tiene solo lo necesario; no hay parámetros, a propósito.
- De una a diez imágenes, hasta 300 MB; formatos y advertencia del JPG.
- La imagen de ejemplo: sintética, para ver el flujo completo.
- La cubierta de espera; es normal que tarde y el aviso al minuto.
- Tiempos y qué pasa del otro lado mientras se espera.

Texto para decir:

[Pantalla: página «Inteligencia Artificial», con el título «Analizar imagen». Una franja con una caja blanca en el centro: la etiqueta «Sube tus imágenes (hasta 10)», el selector de archivos, la nota «Formatos: BMP, PNG o TIFF. JPG se acepta, pero pierde calidad», el aviso de que el análisis puede tardar y no hay que cerrar la página, el botón verde «Analizar» y, justo debajo, el botón «Probar con la imagen de ejemplo». Más abajo, «Infografías recientes» y un enlace para ver todas.]

Esta es la sección de Inteligencia Artificial, la pantalla «Analizar imagen». Quiero que se fijen en lo poco que hay. Una caja con un selector de archivos para subir las imágenes, una nota con los formatos, un botón verde que dice «Analizar» y debajo otro que dice «Probar con la imagen de ejemplo». Eso es todo.

> No hay parámetros ni opciones avanzadas, y es a propósito: así, dos personas que analicen la misma imagen obtienen el mismo resultado.

Es una decisión de diseño. Podríamos haber puesto controles para ajustar el análisis, pero entonces cada persona lo ajustaría distinto y los resultados ya no se podrían comparar. Sin parámetros, la misma imagen da el mismo resultado, la analice quien la analice.

Se pueden subir de una a diez imágenes por vez, hasta trescientos megabytes en total por envío. Los formatos son BMP, PNG o TIFF, y JPG se acepta pero con una advertencia, porque, como vimos, pierde calidad al comprimirse. Un consejo: si van a comparar condiciones, agrupen las fotos por tipo y condición antes de subirlas, porque eso facilita todo lo que viene después. Y pónganles nombres que digan algo, por ejemplo la condición y el número de muestra, porque ese nombre es el que aparece después en los resultados y en el archivo CSV.

Hagamos una cuenta rápida para saber qué esperar. Si una foto grande de fluorescencia tarda unos cuarenta segundos y subo diez, el análisis completo tarda unos siete minutos, porque se hacen una tras otra. Es poco para lo que se está haciendo, pero es mucho para quedarse mirando una pantalla, y por eso conviene saberlo de antemano. Una buena práctica es subir lotes de tamaño razonable y aprovechar la espera para otra cosa, sin cerrar la página.

Si algo sale mal, por ejemplo se sube un archivo que no es una imagen o un formato que el sitio no acepta, el sitio lo avisa con un mensaje claro en la misma pantalla, y no se pierde nada.

Como no tengo aquí una foto propia para subir, voy a usar la imagen de ejemplo.

[Acción: hacer clic en «Probar con la imagen de ejemplo».] Es una imagen sintética, dibujada para la prueba: óvalos de colores, cada uno con una línea verde que hace de cola, sobre un fondo negro. Sirve para ver el flujo completo sin tener una foto propia. No es una foto de microscopio real, y se los aclaro para que no se confundan con los números que van a ver. Que el sitio tenga una imagen de ejemplo es útil en una clase como esta, o cuando alguien quiere comprobar que todo funciona sin gastar una foto propia. Las cifras que salgan no dicen nada biológico, solo muestran cómo se leen.

[Pantalla: la página se difumina y aparece al centro una tarjeta blanca con «Analizando las imágenes…», una barra verde rayada que se mueve sin parar, el texto «Es normal que el análisis tarde… No cierres esta página» y, pasado un minuto, una línea más con letra gruesa: «Tu análisis sigue en curso».]

Apareció una cubierta con una barra verde que se mueve y un mensaje. Esa barra es solo de actividad: no marca cuánto falta, solo confirma que el sistema está trabajando. El mensaje dice que es normal que el análisis tarde y que no cierren la página. Piden no cerrarla porque es justo en esa pantalla donde el sitio va a entregar el resultado cuando termine. La barra no avanza de izquierda a derecha porque el sitio no puede saber de antemano cuánto va a tardar cada imagen; por eso es una barra de actividad y no una barra de progreso.

> Es normal que el análisis tarde, eh. Si pasa un minuto, el sitio avisa que el análisis sigue en curso.

Ese aviso lo agregamos por una sugerencia que salió en el ensayo. Si pasa un minuto y todavía no termina, aparece otra línea que dice «Tu análisis sigue en curso». La idea es que quien espera sepa que no se trabó, y que la tardanza se entienda como algo normal y explicado, no como un fallo. Si la gente no sabe por qué tarda, piensa que el sistema es lento o complicado.

¿Cuánto tarda? En la computadora donde desarrollamos, una foto grande de fluorescencia tarda unos cuarenta segundos, y una de fondo claro entre diez y veinte. Si se suben varias, se analizan una tras otra y los tiempos se suman. Por eso el sitio tiene tiempos de espera amplios.

> Mientras esperamos, les cuento qué pasa del otro lado.

Y mientras esperamos, aprovecho para contarles qué está pasando del otro lado. Primero, la imagen viaja a través de internet hasta el servidor. El servidor revisa el formato del archivo. Después mide el brillo de la imagen para saber si es de fondo oscuro o de fondo claro, y con eso elige cuál de los dos modelos va a usar. Luego analiza la imagen en recortes pequeños. La red devuelve un contorno por cada espermatozoide que encuentra, se juntan los resultados de todos los recortes y el código mide cada contorno. Todo eso ocurre en el procesador del servidor.

Les explico por qué se analiza por recortes. Las fotos son muy grandes y los espermatozoides son pequeños comparados con ellas. Analizar toda la imagen de golpe exigiría mucha memoria al servidor, y el detalle exacto de por qué se hace así lo vemos el lunes. Por eso se corta la imagen en trozos, se analiza cada trozo y después se unen los resultados. Al unirlos puede pasar que una misma célula aparezca en dos trozos vecinos, y entonces hay que quitar el repetido para no contarla dos veces. Todo eso se resuelve dentro del sistema, y es parte de lo que vemos el lunes.

Y el modelo se elige según el tipo de foto. Si la imagen tiene el fondo oscuro, como en fluorescencia, se usa el modelo de fluorescencia. Si el fondo es claro, se usa el de fondo claro. El sitio lo decide solo, midiendo el brillo, y la persona no tiene que elegir nada. Es otra decisión que se quitó de las manos de quien usa el sitio.

No voy a entrar hoy en más detalle de los recortes ni de cómo se juntan los resultados. Eso es del lunes, que es cuando abrimos el sistema por dentro.

[Acción: cuando termine, el sitio abre solo la página de resultados. Si la espera se alarga, abrir el análisis que ya está hecho: clic en el nombre de la persona, arriba a la derecha, y en la primera fila de «Mis análisis».]

Ya terminó, y el sitio me abrió solo la página de resultados. Vamos a verla con calma.

---
## Bloque 8. Leer los resultados

*1:01-1:15 · 14 min · 1,681 palabras, unos 9.1 min de habla*

Idea que debe quedar: cada elemento de la pantalla se puede rastrear hasta un contorno de la imagen, y los números se leen siempre junto con la imagen y la gráfica.

Ideas, en orden:

- Encabezado, aviso de escala, mensaje por imagen y datos del archivo.
- La imagen marcada y los tres datos principales; el largo y las cifras en píxeles.
- El histograma: cómo se construye y cómo se lee.
- El visor con zoom para revisar cada contorno.
- La tabla de detalle y la advertencia de leer los números con la imagen y la gráfica.

Texto para decir:

[Pantalla: página «Resultados del análisis». De arriba hacia abajo: las migas de pan (Inicio › Inteligencia Artificial › Resultados), el título, una línea con el nombre de quien hizo el análisis y la fecha y hora, un recuadro azul con el aviso de escala y, enseguida, el nombre de la imagen con su mensaje en verde y una línea gris con el formato, las dimensiones, el modo de color y el peso. Recorrer sin prisa.]

Estamos en la página de resultados, y la voy a recorrer de arriba hacia abajo, porque cada cosa que aparece está ahí por una razón.

Arriba está el título y, debajo, una línea con el nombre de quien hizo el análisis y la fecha y hora exactas, hasta el segundo. Parece un detalle menor, pero sirve para distinguir muchos análisis entre sí cuando uno acumula varios.

Enseguida hay un recuadro azul con el aviso de escala. Dice que, para estandarizar el tamaño de las imágenes, se usa la misma escala en todas: sesenta píxeles es una micra. Y agrega que la regla de la imagen marcada mide trescientos píxeles, es decir, cinco micras. Más abajo vamos a ver esa regla dibujada en la imagen.

> Arriba aparece quién hizo el análisis, con fecha y hora, y un aviso de escala: el sitio usa la misma en todas las imágenes, sesenta píxeles por micra, para estandarizar su tamaño.

Después viene el nombre del archivo, y debajo un mensaje. Este mensaje, en verde, dice que todo salió bien: «La imagen fue analizada con éxito».

> Cada imagen trae su propio mensaje. Si todo salió bien, es verde. Si hay algo que cuidar, como compresión o muy pocos espermatozoides, el sitio lo avisa. Prefiere decir «no se pudo» a darles un número dudoso.

Ese mensaje puede cambiar. Si la imagen estaba en un formato con compresión, avisa que los bordes pueden haberse alterado. Si se contaron muy pocos espermatozoides, menos de tres, avisa que la distribución de tamaños no es confiable. Y si no se encontró nada, dice en rojo que no se analizó. Entre un «no se pudo» honesto y un número dudoso, el sitio prefiere el primero.

Por ejemplo, si hoy subieran una foto en JPG, verían un aviso amarillo que dice que la imagen está en un formato con compresión y que los bordes pueden alterarse, y que recomienda usar BMP, PNG o TIFF. Es un aviso para que lo sepan, no un error: el análisis se hace igual.

Cuando se suben varias imágenes, cada una trae su propio bloque, con su nombre, su mensaje, su imagen marcada, sus datos y su histograma, y al final de la página aparece una gráfica con el promedio de todas. Esa gráfica de promedios usa un rango común de tamaños para todas las imágenes, de modo que las barras se pueden comparar entre sí.

Debajo hay una línea gris pequeña con los datos del archivo: el formato, las dimensiones en píxeles, el modo de color y el peso.

[Pantalla: bajar un poco. Debajo se ven dos columnas. A la izquierda, la fotografía sobre fondo negro con cada espermatozoide rodeado por un contorno blanco y numerado, y en la esquina inferior izquierda una regla blanca con la leyenda «300 px = 5 micras». A la derecha, tres recuadros con números grandes y, debajo, dos párrafos pequeños con el largo y las cifras en píxeles.]

Ahora sí, lo importante. A la izquierda está la fotografía, con cada espermatozoide rodeado por un contorno blanco y marcado con un número. Ahí, en la esquina de abajo, está la regla de trescientos píxeles, igual a cinco micras. Esa regla va dibujada en la misma imagen para que nadie tenga que adivinar la escala.

A la derecha hay tres recuadros con números grandes. El primero es el conteo: cuántos espermatozoides se marcaron. El segundo es el área media, en micras cuadradas, y el tercero es la desviación estándar de esas áreas. Si la desviación estándar es un término nuevo, es una forma de medir cuánto se alejan, en promedio, las áreas de la media: si es chica, los tamaños son parecidos; si es grande, hay mucha variación.

Les pongo un ejemplo con números inventados y muy sencillos para que se vea la diferencia. Imaginen cinco células con áreas de diez, doce, once, trece y catorce unidades. La media es doce, y las áreas se alejan muy poco de ella: la desviación estándar sale en alrededor de uno y medio. Ahora imaginen otras cinco con áreas de dos, seis, doce, dieciocho y veintidós. La media también es doce, pero ahora las áreas se alejan mucho de ella, y la desviación estándar sale entre siete y ocho. Las dos poblaciones tienen la misma media y son muy distintas. Por eso el sitio da siempre la media y la desviación estándar juntas, y por eso la gráfica importa tanto: la media sola no cuenta esa diferencia.

Debajo hay dos párrafos pequeños. El primero habla del largo del espermatozoide, con su media y su desviación estándar y el mínimo y el máximo. El segundo repite las cifras en píxeles, como apoyo, y da el largo en micras. Digo simplemente «largo» sin entrar en cómo se calcula; eso lo vemos el lunes.

Una pregunta natural es por qué el sitio muestra las dos unidades. Las micras son lo que se reporta, porque son una medida real, la que importa para el trabajo científico. Los píxeles se dejan como apoyo, porque son lo que la computadora mide directamente y permiten comprobar la conversión. Si dividen el área en píxeles entre tres mil seiscientos, deben obtener el área en micras cuadradas, y si dividen el largo en píxeles entre sesenta, el largo en micras. Pueden hacer la prueba con cualquier fila de la tabla, y es una buena manera de convencerse de que todo es consistente.

> Cada número tiene un contorno detrás. Si dice ciento catorce, hay ciento catorce contornos que se pueden revisar uno por uno.

Esto es lo que más quiero que se lleven de la pantalla: cada número tiene un contorno detrás. Si el conteo dice un número, hay exactamente esa cantidad de contornos en la imagen que se pueden revisar uno por uno. Nada sale de una caja cerrada.

[Pantalla: a la derecha, bajo el título «Distribución de tamaños», una gráfica de barras de color azul claro con borde azul. En el eje horizontal, diez intervalos de área en píxeles; en el vertical, «Células», el número de células de cada intervalo. Señalar con el cursor la barra más alta.]

Debajo está una gráfica que se llama «Distribución de tamaños». Es un histograma. Les explico cómo se construye. Se toma la célula más pequeña y la más grande de la imagen, y el rango entre las dos se divide en diez intervalos iguales. En el eje horizontal están esos intervalos, con el área en píxeles. En el eje vertical está cuántas células cayeron en cada uno.

> El histograma divide el rango de áreas en diez intervalos iguales y cuenta cuántas células caen en cada uno. No supone ninguna forma: dibuja lo que se midió.

Una barra alta significa que hay muchas células con ese tamaño. Si las barras están repartidas parejo, los tamaños son muy variados. Algo importante: el histograma no supone ninguna forma. No asume que los tamaños se repartan de cierta manera. Dibuja lo que se midió y ya. Y si se suben varias imágenes, se usa un rango común para todas y aparece, además, una gráfica con los promedios.

Les cuento cómo leerlo, con dos formas típicas. Si las barras forman una sola montaña, con un centro claro y colas hacia los lados, los tamaños se concentran alrededor de un valor. Si aparecen dos montañas separadas, podría ser que haya dos grupos de tamaños distintos, pero también podría ser un problema de las marcas, así que antes de concluir nada hay que mirar la imagen. Y una barra aislada en el extremo derecho suele ser una célula muy grande, o varias células pegadas que se contaron como una. Cualquiera de esas lecturas se comprueba en la imagen marcada, y ahí es donde el visor nos va a servir.

Una aclaración: el sitio no interpreta los resultados ni los compara con valores de referencia. Eso lo hace el grupo. El sitio da los números y la gráfica; la lectura científica les corresponde a ustedes.

[Acción: hacer clic sobre la imagen (en la esquina se lee «Clic para ampliar»). Se abre una ventana a pantalla completa con fondo oscuro. Arriba, los botones «−», «+», «Ajustar» y «100%», y la guía «Rueda para acercar · arrastra para mover». Acercar con la rueda, arrastrar para mover y pasar el cursor sobre un espermatozoide: aparece su número, su área y su largo. Cerrar con la X de arriba a la derecha.]

Y para comprobar que los contornos son los correctos, tenemos el visor. Si hago clic sobre la imagen, se abre una ventana a pantalla completa. Arriba hay botones para acercar y alejar, para ajustar la imagen a la pantalla y para verla a tamaño real. También puedo acercar con la rueda del mouse y arrastrar para moverme.

> El visor sirve para comprobar con sus propios ojos que cada contorno sea de verdad un espermatozoide.

Si paso el cursor por encima de un espermatozoide, aparece su número, su área y su largo, en píxeles y en micras. Si encuentran uno que no encierra una cabeza completa, ese es justo el tipo de cosa que conviene saber. Cierro el visor con la equis.

Les propongo una forma práctica de auditar un resultado. Elijan cinco números al azar de la tabla, ubiquen cada uno en la imagen con el visor y comprueben que el contorno encierra una cabeza completa. Si en esos cinco todo está bien, tienen una buena señal de que el análisis es confiable. Si en esos cinco encuentran varios problemas, desconfíen del conteo y de las medidas y revisen con más cuidado, porque el modelo puede estar teniendo dificultades con ese tipo de imagen. Es una revisión de pocos minutos y vale la pena hacerla antes de usar los números.

[Pantalla: bajar hasta «Detalle por espermatozoide»: una tabla con una fila por célula y las columnas «#», «Área (px)», «Largo (px)», «Área (µm²)» y «Largo (µm)». La tabla tiene su propio desplazamiento dentro del recuadro.]

Más abajo está el detalle por espermatozoide: una tabla con una fila por célula. Las columnas son el número, el área y el largo en píxeles, y el área y el largo en micras. El número es el mismo que aparece en la imagen, así que pueden ir de una fila de la tabla a su contorno en la fotografía. Es la misma información que trae el archivo CSV que vamos a descargar en un momento.

Antes de pasar al siguiente bloque, una advertencia sobre cómo leer todo esto.

> La media sin la gráfica puede engañar. Antes de confiar en un número, miren la imagen marcada y el histograma.

> Un ejemplo con números inventados: una foto con ciento veinte células y otra con ochenta. Eso no quiere decir que una muestra tenga más. Cada foto cuenta lo que había en esa zona.

Les pongo un ejemplo, y es con números inventados, para que no se confundan. Imaginen que una foto tiene ciento veinte células y otra tiene ochenta. Eso no significa que una muestra tenga más células que la otra, porque cada foto cuenta lo que había en esa zona del campo del microscopio, y esa zona puede ser distinta. Y si lo que se quiere es decir que el tamaño medio de dos grupos es distinto, eso solo se puede afirmar con una prueba estadística, y esa decisión la toma el grupo a partir de los datos del CSV. Los números del sitio son un punto de partida para ese análisis. No lo reemplazan.

---
## Bloque 9. Lo que no es un espermatozoide

*1:15-1:26 · 11 min · 1,156 palabras, unos 6.2 min de habla*

Idea que debe quedar: el modelo no es perfecto: puede equivocarse, el sitio avisa cuando no puede analizar, y la forma de mejorar es con más datos, más variados y mejor etiquetados.

Ideas, en orden:

- ¿Qué pasa si subo una imagen que no es de espermatozoides?
- El sitio prefiere no analizar a dar un número dudoso; aun así, no hay garantía.
- Falso positivo, en biología; alucinación, en programación.
- Por qué pasa: la red solo aprende de lo que vio.
- Cómo se mejora: más datos, más variados y mejor etiquetados; qué puede hacer cada persona.

Texto para decir:

[Diapositiva · ¿Y si la imagen no es de espermatozoides?]

Hasta ahora todo salió bien, porque usamos una imagen pensada para que saliera bien. Ahora la pregunta incómoda: ¿qué pasa si subo una imagen que no es de espermatozoides? Preparé tres imágenes de libre uso, por ejemplo de células de hígado y de riñón, para probarlo en vivo.

[Acción: en «Analizar imagen», elegir con el selector de archivos las tres imágenes preparadas (por ejemplo, células de hígado y de riñón) y hacer clic en «Analizar». Esperar el resultado.] Mostrar lo que el sitio realmente responda: un mensaje en rojo sobre la imagen o, si marca algo, la imagen con sus contornos.

Voy a seleccionar las tres imágenes y a hacer clic en «Analizar». Les voy a mostrar lo que el sitio responda de verdad, sea lo que sea. No preparé el resultado de antemano, y no sé exactamente qué va a decir con cada una, así que lo vemos juntos. Mientras corre, recuerden lo que dijimos hace un rato: el modelo se entrenó con fotos de espermatozoides, y estas son de otro tipo de célula, así que se trata de una prueba justa de qué hace el sistema ante algo que no conoce. Lo que espero es que, en el mejor caso, el sitio me diga que no es factible analizarlas.

> Si subo una imagen que no es de espermatozoides, lo que espero es que el sitio me diga que no es factible analizarla. Entre un aviso claro y un número dudoso, prefiere el aviso.

Esa respuesta, que dice que no se encontraron espermatozoides o que la imagen es de mala calidad y que no es factible analizarla, es parte del diseño. El sitio prefiere no analizar a inventar un resultado. Y esto conecta con el primer principio de hace rato, el de no suponer.

Si el sitio marcó algo en alguna de las tres imágenes, ese es un buen ejemplo de falso positivo, y no hay que esconderlo. Lo abrimos en el visor y vemos qué encerró el contorno: una zona más oscura, un borde, un trozo de algo que se parece a lo que el modelo aprendió. Un caso así enseña más que diez casos que salieron bien, porque muestra exactamente dónde está el límite de lo que el modelo sabe.

Pero tengo que ser honesto con ustedes. Que el sitio avise en estos casos no es una garantía. La red aprendió de un conjunto limitado de imágenes, y puede marcar manchas que se le parezcan a lo que aprendió a reconocer. Nadie debería darle un resultado por bueno sin mirarlo.

Para entender por qué pasa esto, hay una idea previa que condiciona cómo se escucha el resto del curso. Una red neuronal no entiende qué es un espermatozoide. No tiene el concepto, no sabe de biología, no sabe qué es una célula ni para qué sirve contarla. Lo que tiene es una enorme colección de números ajustados, de modo que ante ciertos patrones de píxeles produce una salida que coincide con lo que las personas marcaron en los ejemplos. Es un reconocedor de patrones muy sofisticado, y nada más. Eso no le quita mérito, y sirve para razonar sobre cuándo va a funcionar y cuándo no.

Si le muestro una imagen parecida a las de su entrenamiento, va a funcionar. Si le muestro algo muy distinto, no tiene cómo saber que se equivoca, y va a producir una salida con la misma seguridad aparente. Esa es la parte que más cuidado exige: el modelo no duda. Puede marcar algo con el mismo aspecto de firmeza con el que marca un espermatozoide perfecto. Por eso la revisión de las personas no es opcional.

[Diapositiva · Falso positivo: en programación, alucinación]

[Acción: mostrar un caso con un falso positivo, si existe: abrir el visor sobre un contorno que encierre una mancha, una sombra o un trozo de cola y no una cabeza completa.] A veces el modelo marca como espermatozoide algo que no lo es: una sombra, una mancha o un trozo de cola. En la diapositiva lo ven dibujado: tres espermatozoides bien marcados y una mancha con un contorno naranja que dice «¿mancha o célula?».

> A veces el modelo marca algo que parece un espermatozoide y no lo es. En biología se le llama falso positivo; en programación, pues, alucinación.

Un falso positivo es eso: el modelo dice que hay algo donde no lo hay. En programación y en inteligencia artificial a esto también se le llama alucinación. Es un fenómeno conocido, y se presenta en modelos de muchos tipos. Les pasa en general cuando se topan con algo que se parece a lo que aprendieron.

¿Por qué pasa? Porque la red solo aprende de los ejemplos que vio. Si vio pocos ejemplos de un caso, o ninguno, no aprendió a resolverlo. Es como alguien que aprendió a reconocer un tipo de ave viendo cien fotos: si le muestran algo que se parece pero no es, puede equivocarse.

Existe también el error contrario, que es menos visible. Un falso negativo es no marcar un espermatozoide que sí está. Cuando el modelo se salta una célula, no hay contorno que revisar, y por eso es más difícil de notar que un falso positivo. Es otra razón para mirar la imagen entera y no solo los contornos que sí aparecen. Si ven en la foto una cabeza brillante que no tiene número, ese es un falso negativo, y también es útil saberlo.

Entre los dos tipos de error hay un equilibrio. Un modelo muy cuidadoso, que solo marca cuando está seguro, comete menos falsos positivos pero se salta más células. Uno muy generoso marca casi todo, pero se equivoca más seguido al marcar. Cómo se ajusta ese equilibrio es una decisión de diseño.

Y si un resultado les parece raro, hay una pequeña lista de cosas que pueden revisar. Primero, el tipo de imagen: ¿se parece a las que el modelo conoce? Segundo, el formato: ¿es un archivo original o uno que pasó por compresión? Tercero, el aviso que muestra el sitio: ¿dice algo sobre la imagen? Cuarto, el visor: ¿los contornos encierran lo que deberían? Y quinto, un conteo manual de una zona pequeña, para comparar con lo que marcó el modelo. Con esas cinco comprobaciones se sabe, casi siempre, si el resultado se puede usar.

¿Y cómo se mejora? Con más datos, más variados y mejor etiquetados. Es decir, con más imágenes, de más condiciones, y con las marcas hechas con cuidado. Si aun así no alcanzara, habría que cambiar de arquitectura, que es la forma en la que está construida la red, y eso es una decisión mayor.

> Un modelo mejora con ejemplos de sus propios errores. Por eso el grupo es quien puede hacerlo mejor: tiene las imágenes y el criterio para etiquetarlas.

Y de ahí sale lo que me parece más importante de este bloque. Un hábito muy útil es revisar la imagen marcada y guardar las imágenes que el modelo analiza con dificultad. Esas son las más valiosas para volver a entrenar.

Si alguien se pregunta si el modelo mejora solo con el uso, la respuesta es que no. Un modelo en línea no aprende de las imágenes que analiza. Para mejorarlo hay que reunir imágenes nuevas, etiquetarlas, entrenar otra vez en Colab y cambiar el archivo del modelo en el servidor. Eso es lo que vemos el martes.

---

## Bloque 10. Descargas, Mis análisis y privacidad

*1:26-1:32 · 6 min · 661 palabras, unos 3.6 min de habla*

Idea que debe quedar: el CSV es el dato para trabajar, el PDF es el informe para compartir, y cada análisis es privado y queda guardado.

Ideas, en orden:

- Al final de la página: Imprimir, Descargar PDF y Descargar CSV.
- CSV: una fila por espermatozoide, seis columnas, para seguir trabajando.
- PDF: informe con portada, una página por imagen y gráfica de promedios.
- «Mis análisis»: qué se guarda y qué no.
- Privacidad: cada análisis es de quien lo hizo; guardar los originales.

Texto para decir:

[Pantalla: bajar al final de la página de resultados. Debajo de la tabla hay una fila de botones: «Imprimir» (verde), «Descargar PDF» y «Descargar CSV» (con borde) y el enlace «Analizar otras imágenes».]

Volvamos a la página de resultados de la imagen de ejemplo, y bajo hasta el final. Debajo de la tabla hay una fila de botones: Imprimir, Descargar PDF, Descargar CSV, y un enlace para analizar otras imágenes.

El CSV es un archivo de texto con una fila por espermatozoide y seis columnas: la imagen de la que viene, el número del espermatozoide, el área y el largo en píxeles, y el área y el largo en micras. Se abre en una hoja de cálculo o con código, y sirve para seguir trabajando con los datos: hacer comparaciones, estadística, gráficas propias. Como la primera columna trae el nombre de la imagen, si subieron varias pueden separar los datos por imagen o por condición, ordenarlos, filtrarlos, calcular promedios por grupo y hacer sus propias gráficas con las herramientas que ya usan.

Esta es la razón por la que dije que el sitio no interpreta los resultados. El sitio llega hasta los datos; lo que sigue, la comparación entre condiciones y las pruebas estadísticas, es trabajo del grupo, y el CSV es el punto de partida.

El PDF es un solo informe con todas las imágenes del análisis. La primera página trae el encabezado, el usuario, la fecha y el número de imágenes. Luego hay una página por imagen, con la imagen marcada, sus datos y su gráfica. Y al final, si se subieron varias imágenes, la gráfica de promedios. Las medidas van primero en micras y después en píxeles. El PDF se genera una sola vez y no cambia después, así que sirve como constancia de ese análisis. Es el formato adecuado para adjuntar a un reporte, para compartir con alguien que no tiene cuenta, o para guardar como registro de lo que se midió y con qué escala.

> El CSV es el dato para trabajar. El PDF es el informe para compartir. Conviene guardar los dos.

Y el botón de Imprimir oculta el menú y los botones, y deja solo el análisis, para imprimir limpio.

[Acción: clic en el nombre de la persona, arriba a la derecha. Se abre el perfil: el nombre como título, el correo debajo y, bajo «Mis análisis», una tabla de tres columnas (fecha y hora, imágenes y descargas) con una fila por análisis. La fecha es un enlace al análisis, y en la última columna están los enlaces «PDF» y «CSV».]

Si hago clic en mi nombre, arriba a la derecha, llego a mi perfil. Ahí está «Mis análisis»: una tabla con una fila por cada análisis que he hecho. Muestra la fecha y la hora, los nombres de las imágenes y los enlaces para descargar el PDF y el CSV. Si hago clic en la fecha, abro ese análisis, y se ve igual que cuando terminó. No se recalcula, solo se consulta.

> En «Mis análisis» queda una fila por cada análisis, con sus enlaces al PDF y al CSV. Al abrirlo, se ve igual que cuando terminó.

Hablemos de qué se guarda y qué no, porque es importante para la privacidad. El sitio guarda los resultados, una copia reducida de la imagen marcada y el PDF. Lo que no guarda son las imágenes originales: se borran del servidor en cuanto termina el análisis.

> Las imágenes que suben se borran del servidor cuando termina el análisis. Guarden sus originales en su propia computadora.

Eso significa que si quieren volver a ver o volver a analizar una imagen, tienen que conservar su original en su propia computadora. El sitio no se las puede devolver.

Esto tiene una consecuencia a favor de la privacidad: mientras menos material de las personas guarde el servidor, menos hay que proteger. Lo que sí se guarda es lo necesario para consultar el análisis después: los resultados, una copia reducida de la imagen marcada y el informe en PDF.

Y una buena práctica de orden: guarden en una misma carpeta los originales, el CSV y el PDF de cada análisis, con el mismo nombre de condición. Dentro de unos meses, cuando alguien pregunte de dónde salió un número, esa carpeta va a contestar la pregunta.

Y sobre la privacidad: cada análisis es de quien lo hizo, y solo esa persona puede verlo. Nadie más puede abrirlo.

[Acción: hacer clic en «Salir», arriba a la derecha; el sitio vuelve a mostrar «Iniciar sesión».] Hago clic en «Salir», y el sitio vuelve a mostrar «Iniciar sesión». Con esto cerramos el recorrido del sistema.

---

## Bloque 11. Cierre y adelanto de la sesión 2

*1:32-1:36 · 4 min · 464 palabras, unos 2.5 min de habla*

Idea que debe quedar: el sitio convierte una fotografía en datos confiables y descargables, y la siguiente pregunta es cómo sabe la red dónde hay un espermatozoide.

Ideas, en orden:

- Resumen en cuatro frases: el problema, la idea, el sitio y la privacidad.
- Cinco hábitos para usar el sitio.
- La pregunta de mañana y el adelanto del lunes.

Texto para decir:

[Diapositiva · Lo que vimos hoy]

Para cerrar, un resumen de lo que vimos en dos horas, en cuatro frases.

> Para cerrar: el problema era contar y medir a mano; la idea, que la red localiza y el código mide; el sitio, que convierte una foto en datos que se pueden revisar y descargar; y cada análisis es de quien lo hizo.

Si tuvieran que quedarse con una sola idea de hoy, que sea la segunda: la red localiza y el código mide. De ahí salen casi todas las decisiones que vieron en el sitio, desde los avisos hasta la escala declarada en cada resultado.

[Diapositiva · Cinco hábitos para usar el sitio]

Y les dejo cinco hábitos para usar el sitio de la mejor manera.

> Cinco hábitos para llevarse: usar los archivos originales, agrupar las imágenes por tipo, revisar la imagen marcada antes de confiar en un número, guardar el CSV y guardar las imágenes difíciles.

Los cinco tienen una razón de fondo parecida: cuidar lo que entra al sistema y lo que sale de él. Con originales y fotos agrupadas, los resultados se pueden comparar. Revisando la imagen marcada, no se confía a ciegas. El CSV es lo que permite seguir trabajando después. Y las imágenes difíciles son las que más enseñan al modelo cuando llegue el momento de volver a entrenarlo.

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

Y termino con una pregunta que seguramente ya se hicieron varios.

> Seguramente muchos se preguntan cómo sabe el sistema dónde hay un espermatozoide... bueno, esa es la pregunta de mañana: cómo aprende una computadora.

Hoy vimos que la red localiza, pero no vimos cómo aprendió a hacerlo. Eso es lo que vamos a ver mañana, sábado a las nueve de la mañana: qué es una neurona, qué es una red, cómo mira una imagen una red convolucional y cómo aprende a partir de ejemplos. Es la sesión más pesada, así que los espero con ganas.

Para ir calentando motores, un adelanto de cómo empieza. Vamos a retomar la idea que mencioné hoy de decir que todo lo que supere cierto brillo es célula, que se llama umbralización, y vamos a ver por qué no alcanza. De ahí partimos para entender qué hace distinto una red neuronal: cómo se construye desde su pieza más pequeña, la neurona, cómo se organiza en capas y cómo, a base de ejemplos, ajusta lo que necesita hasta acertar. No necesitan preparar nada. Si les quedó alguna duda de hoy, pueden traerla mañana.

> El lunes vemos cómo funciona por dentro, y ahí les cuento los retos: las células empalmadas, los falsos positivos y la escala. Gracias por conectarse.

Y el lunes abrimos el sistema por dentro: la parte de atrás, qué pasa cuando suben una imagen, y los retos que mencioné, como las células empalmadas, los falsos positivos y la escala. Gracias por conectarse, y quedo atento a las preguntas.

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
