# Guion de la sesión 1: El problema y el sitio

Image Bio Pro · Capacitación · viernes 23 de octubre de 2026, de 6:00 a 8:00 pm

Esta sesión es la primera de cuatro. Presenta el problema como caso de estudio de inteligencia artificial, la idea de imagen digital y el sitio funcionando. Cómo aprende la red se ve en la sesión 2; cómo funciona el sistema por dentro, en la sesión 3; datos, reentrenamiento y despliegue, en la sesión 4.

## Cómo usar este guion

No es un texto para leer. Cada bloque tiene tres partes:

- **Idea que debe quedar:** lo único que el público tiene que llevarse del bloque.
- **Ideas, en orden:** lo que hay que tocar, contado con palabras propias.
- **Frases ancla:** aparecen en cita (con `>`). Son aperturas, definiciones y transiciones, y se dicen casi literales. Lo demás se cuenta hablando.

Ritmo considerado: **170 palabras por minuto**. El tope de cada bloque es lo máximo que cabe en los minutos que se hablan (los minutos de pantalla y demostración no cuentan). Es un límite, no una meta que haya que llenar. Las indicaciones entre corchetes (pantalla, acciones y diapositivas) no se cuentan.

## Resumen de tiempos

| Bloque | Hora | Min | Min hablados | Tope (palabras) | Palabras ancla |
|---|---|---|---|---|---|
| 1. Bienvenida y agenda | 0:00–0:05 | 5 | 5 | 850 | 77 |
| 2. El caso de estudio | 0:05–0:20 | 15 | 15 | 2,550 | 89 |
| 3. Por qué una plataforma web | 0:20–0:28 | 8 | 8 | 1,360 | 83 |
| 4. Qué es una imagen digital | 0:28–0:38 | 10 | 9 | 1,530 | 69 |
| 5. El sitio, visto como visitante | 0:38–0:48 | 10 | 6 | 1,020 | 38 |
| Pausa | 0:48–0:55 | 7 | - | - | - |
| 6. Crear una cuenta | 0:55–1:00 | 5 | 3 | 510 | 20 |
| 7. Analizar una imagen y esperar | 1:00–1:12 | 12 | 7 | 1,190 | 44 |
| 8. Leer los resultados | 1:12–1:27 | 15 | 12 | 2,040 | 41 |
| 9. Lo que no es un espermatozoide | 1:27–1:35 | 8 | 6 | 1,020 | 57 |
| 10. Descargas, Mis análisis y privacidad | 1:35–1:43 | 8 | 5 | 850 | 37 |
| 11. Cierre y adelanto de la sesión 2 | 1:43–1:50 | 7 | 7 | 1,190 | 47 |
| Margen | 1:50–2:00 | 10 | - | - | - |
| **Total** | | **120** | **83** | **14,110** | **602** |

De los 120 minutos, unos 83 se hablan, unos 20 son pantalla y demostración, 7 son pausa y 10 quedan de margen. El margen no se llena: sirve para preguntas, para una demostración que se alargue o para terminar a tiempo.

## Notas para quien presenta

Estas notas no se leen en voz alta. Son puntos que conviene resolver o comprobar antes de la sesión.

1. **Ensayo del 20 de octubre.** El revisor notó que casi toda la presentación se leía, que había conceptos que aparecían tarde respecto a su explicación y que lo más importante era el orden y el tono platicado. Este guion sigue su orden: primero el contexto y el caso de estudio, después por qué una plataforma web, la imagen digital, y entonces el sitio funcionando. El revisor también pidió numerar las diapositivas.
2. **Preguntas del público.** El público puede preguntar en cualquier momento; quien presenta no hace preguntas al público. Responder breve y concreto. Si la pregunta es muy técnica: «Buena pregunta, la vemos al final de la sesión» (o en la sesión que corresponda). Como respaldo, las preguntas que no alcancen a contestarse se pueden mandar por escrito (por ejemplo, por el chat de la videollamada); falta definir cuándo se responden.
3. **Grabación.** Decirlo al inicio. Según el revisor, la grabación se sube a redes y se puede editar, incluida la voz, si no se quiere aparecer. Sin cámara, usar una foto de perfil. Confirmar con el revisor qué se dice sobre dónde se publica.
4. **Antes de empezar (15 minutos antes).** Probar la videollamada y compartir pantalla. Abrir el sitio con el zoom del navegador al 125 %. Tener un análisis ya hecho en «Mis análisis». Las capturas de respaldo están en `docs/capacitacion/capturas/`, por si falla la conexión.
5. **Tiempo de análisis.** En la computadora de desarrollo, una foto grande de fluorescencia tarda unos 40 segundos y una de fondo claro entre 10 y 20. En el VPS no se ha medido. Si el análisis en vivo se alarga, abrir el que ya está hecho en «Mis análisis».
6. **Estado del sitio** (revisado el 21 de octubre, después de los commits `fd13cba` y `6c2d5d7`). Ya está hecho, y el guion lo describe así:
   - El aviso de espera: la cubierta dice que es normal que el análisis tarde y, pasado un minuto, avisa que sigue en curso (sugerencia de Isaac).
   - El texto de la escala: «Para estandarizar el tamaño de las imágenes se usa la misma escala en todas: 60 px = 1 µm», en pantalla, en el PDF y en la regla de la imagen marcada.
   - Los recuadros de «modelo preliminar» y de «escala provisional» ya no aparecen, ni en pantalla ni en el PDF.
   - Los datos principales (área media y desviación estándar) salen en µm², con los píxeles como apoyo, y el PDF también pone primero las micras.

   Por revisar antes del viernes:
   - Contenido real de Nosotros, Aliados e infografías. El texto y las fotos se envían a más tardar el jueves temprano.
   - El histograma todavía rotula el eje horizontal en píxeles («Área del espermatozoide (px)»), aunque los datos principales están en micras. Decidir si se cambia o si se explica al leerlo.
   - Que el PDF salga completo (en el ensayo se veía incompleto) y que la imagen de ejemplo no muestre ningún aviso extra (en el ensayo salía uno y se acordó quitarlo).
   - Que el sitio esté en línea, con el VPS, antes del viernes por la tarde.
7. **Tres imágenes que no son espermatozoides (bloque 9).** Prepararlas con anticipación, de libre uso (el revisor sugirió células de hígado y de riñón). Probarlas antes: presentar solo lo que el sitio haga de verdad. Si el sitio marca algo en alguna, sirve para explicar el falso positivo.
8. **Escala.** La escala se presenta como la presenta el sitio: se usa la misma en todas las imágenes para estandarizar su tamaño (60 px = 1 µm; la regla de la imagen marcada mide 300 px = 5 µm). No decir «imaginaria» ni entrar en el detalle de las medidas. Si preguntan cómo se sabe que es correcta: es una escala común para estandarizar el tamaño de las imágenes y poder compararlas entre sí, y cada resultado la declara.
9. **Largo.** En el código, el largo es el lado mayor del rectángulo mínimo que encierra el contorno (`app/analisis/medicion.py`), no la longitud a lo largo de la curva. Este guion solo dice «largo». El README y el guion anterior decían que se mide a lo largo de la forma; conviene corregirlos para que todo diga lo mismo. El detalle del método se ve en la sesión 3.
10. **Conocimiento general.** Lo que se dice de píxeles, brillo de 0 a 255 y compresión del JPG es de conocimiento general, no del repositorio. Las cifras del sitio (hasta 10 imágenes, 300 MB por envío, 10 intervalos del histograma, contraseña de 8 caracteres) salen del código.
11. **Lo que ya no va en esta sesión.** La red neuronal, el entrenamiento y las cifras de los modelos pasan a las sesiones 2 a 4. La versión anterior de este guion, con ese material completo, está en el historial de git: `git show faf9599:docs/capacitacion/guion-sesion-1.md`.
12. **Tono.** Lenguaje profesional pero platicado. Sin comentarios que sugieran que el grupo no sabe. Cada término técnico se explica en una frase la primera vez que aparece.

---

## Bloque 1. Bienvenida y agenda

*0:00–0:05 · 5 min · tope 850 palabras*

**Idea que debe quedar:** son cuatro sesiones, hoy vemos el problema y el sitio, y pueden preguntar cuando quieran.

[Diapositiva · Image Bio Pro]

Ideas, en orden:

- Saludo y presentación: nombre y qué hace.
- La sesión queda grabada.
- Cómo preguntar: en cualquier momento; lo muy técnico se deja para el final.
- El mapa de las cuatro sesiones.
- La agenda de hoy: el problema, la imagen digital, el sitio y un análisis en vivo.

> Buenas tardes a todos, y gracias por conectarse. Soy Angel Frausto Robles, desarrollador de Image Bio Pro.

> Esta sesión queda grabada. Si tienen una duda, pregúntenme en cualquier momento. Las respuestas muy técnicas las dejamos para el final, para no perder el hilo.

[Diapositiva · Las cuatro sesiones]

> Son cuatro sesiones. Hoy vemos el problema y el sitio. Mañana, cómo aprende la computadora. El lunes, cómo funciona el sistema por dentro. Y el martes, los datos y cómo se reentrena el modelo.

---

## Bloque 2. El caso de estudio

*0:05–0:20 · 15 min · tope 2,550 palabras*

**Idea que debe quedar:** vamos a aprender cómo se usa la inteligencia artificial resolviendo un problema concreto, contar y medir espermatozoides en fotografías, y la clave es repartir el trabajo entre la red y el código.

[Diapositiva · La inteligencia artificial en la educación y la investigación]

Ideas, en orden:

- Abrir con una pregunta: ¿para qué sirve la inteligencia artificial en la educación y en la investigación? Una de sus aplicaciones es analizar imágenes.
- Las imágenes vienen de muchas fuentes. Una es la microscopía: permite ver células, por ejemplo los espermatozoides, y ver cómo cambian de tamaño y de forma bajo ciertas condiciones.
- El objetivo de esta capacitación: acercar a la comunidad universitaria, de distintas áreas, a lo que es la inteligencia artificial y a cómo se aplica a un problema técnico-científico real, en este caso de biología de la reproducción.
- Cómo lo hacemos: con un caso de estudio. Aprendemos a través de un ejemplo.

> Para entender cómo se aplica la inteligencia artificial, vamos a seguir un caso de estudio: contar y medir espermatozoides en fotografías de microscopio.

[Diapositiva · Contar y medir a mano]

- El problema: contar y medir a mano es lento, repetitivo y cambia según quién lo haga. Una foto tiene decenas o cientos de células, muchas encimadas o pegadas. Si hay que comparar muchas imágenes, el trabajo manual se vuelve difícil de sostener.
- Decir qué se ve en una foto de fluorescencia: las células salen brillantes sobre fondo oscuro.

> Imaginen contar a mano cien células en una foto, y luego repetirlo con muchas fotos. Cada persona contaría algo distinto.

[Diapositiva · La red localiza y el código mide]

- La idea central es repartir el trabajo. Una red neuronal, que es un programa que aprende de ejemplos, hace una sola cosa: decidir dónde hay un espermatozoide y trazar su contorno.
- Todo lo demás lo hace código convencional: cuántos son, cuánto mide cada uno, la media y la desviación estándar. Son procedimientos explícitos y estandarizados que cualquiera puede verificar.
- En la práctica: se abre la imagen marcada, se mira el contorno que trazó la red y se recalcula la medida. La red propone y la medición se puede auditar.

> La red localiza y el código mide. Esa división es la idea que atraviesa todo el proyecto.

- Un modelo así no aprende solo cuando ya está en línea. Si llegan imágenes nuevas, otras tinciones u otro tipo de célula, se reentrena aparte y se cambia el archivo del modelo. Eso lo vemos el martes.
- Estado del modelo, en general: funciona, está dando buenos resultados y, como cualquier modelo, se puede mejorar. Sin entrar en detalle.
- Anticipar los retos: más adelante les cuento qué dificultades tuvo el proyecto y cómo las resolvimos, por ejemplo cuando las células se empalman.

> Al final de las sesiones les cuento los retos que enfrentamos y cómo les dimos la vuelta. Les adelanto uno: cuando muchas células se empalman, contarlas es muy difícil.

---

## Bloque 3. Por qué una plataforma web

*0:20–0:28 · 8 min · tope 1,360 palabras*

**Idea que debe quedar:** el modelo entrenado, solo, no hace nada. La plataforma web es lo que permite que cualquier persona de la universidad lo use, con una cuenta propia y sin programar.

[Diapositiva · Una parte web y una parte de aprendizaje automático]

Ideas, en orden:

- Plantear la pregunta que se hizo en el ensayo: si ya existe la red, ¿por qué una página web y no correrla desde Google Colab?
- Colab es un cuaderno en la nube, un entorno donde se escribe código y se entrena el modelo. Entrenar produce un archivo (con extensión `.pt`) que guarda lo que la red aprendió. Ese archivo, por sí solo, no hace nada.
- La plataforma lo carga y le pone una interfaz: botones para subir fotos y pantallas para ver resultados. Así cualquiera puede usarlo, sin instalar nada ni saber programar.
- El acceso al análisis es con una cuenta personal y privada.

> El modelo es un archivo que, por sí solo, no puede hacer nada. La plataforma web es lo que permite que cualquier persona de la comunidad universitaria use la inteligencia artificial desde un navegador.

[Diapositiva · Entrenamiento aparte, inferencia en el servidor]

- Definir las dos etapas del desarrollo de la red: el entrenamiento, que se hace en Colab, y la inferencia, que se hace en el servidor. Inferencia es usar el modelo ya entrenado para analizar fotos nuevas; se hace en el procesador del servidor.
- Dos partes con cuidados distintos: la parte web, que se mantiene como cualquier sitio, y la parte de aprendizaje automático, que se mejora con datos.

> El desarrollo de la red tiene dos etapas. Primero se entrena en Google Colab. Después, cuando queremos analizar fotos nuevas, usamos el modelo en el servidor. A eso se le llama inferencia.

[Diapositiva · Un menú con seis secciones]

- Presentar el sitio en general como un entorno educativo con seis secciones: Inicio, Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto. Más adelante se recorre cada una.

> El sitio tiene seis secciones. Ahorita las nombro y en unos minutos las vemos una por una.

---

## Bloque 4. Qué es una imagen digital

*0:28–0:38 · 10 min (9 hablados) · tope 1,530 palabras*

**Idea que debe quedar:** para la computadora una fotografía es una tabla de números, y eso explica todo lo que vamos a medir.

[Diapositiva · Una fotografía es una tabla de números]

Ideas, en orden:

- Pregunta: ¿qué es una fotografía para una computadora?
- Una cuadrícula de cuadritos. Cada cuadrito es un píxel y guarda un número. En una imagen en tonos de gris, el número es el brillo, de 0 (negro) a 255 (blanco). En color son tres números, uno por rojo, verde y azul.
- Mostrar una zona de la foto muy ampliada hasta que se vean los cuadritos.

> Para la computadora, una fotografía es una tabla de números. Cada cuadrito, cada píxel, guarda cuánta luz tiene.

[Diapositiva · Una célula brillante son números altos]

- En una foto de fluorescencia, una célula es una zona de números altos sobre un fondo de números bajos. La computadora no ve una célula; ve números.
- Medir el área de una célula es contar cuántos píxeles ocupa. Una foto grande tiene unos 1,800 píxeles de ancho, o más.

> La computadora no ve células. Ve números. Nuestro trabajo es enseñarle qué patrón de números corresponde a un espermatozoide.

[Diapositiva · Formatos: unos conservan los bordes, otros no]

- Formatos: BMP, PNG y TIFF conservan la imagen tal cual. JPG la comprime y puede alterar los bordes de las células, y con ellos los contornos y las medidas.
- Recomendación: trabajar con los archivos originales del microscopio y evitar que pasen por aplicaciones de mensajería, que los comprimen.

[Diapositiva · La imagen no sabe cuánto mide un píxel]

- Una foto sabe cuántos píxeles mide, pero no cuántas micras es cada uno. Los archivos no guardan esa información.
- Por eso el sitio usa la misma escala en todas las imágenes, 60 píxeles por micra, para estandarizar su tamaño y poder compararlas entre sí. Cada resultado dice qué escala se usó. No entrar en más detalle; el método se ve en la sesión 3.

> Una foto no sabe cuánto mide un píxel en la realidad. Por eso el sitio usa la misma escala en todas las imágenes, para estandarizar su tamaño, y cada resultado dice cuál.

---

## Bloque 5. El sitio, visto como visitante

*0:38–0:48 · 10 min (6 hablados) · tope 1,020 palabras*

**Idea que debe quedar:** cualquier persona puede recorrer el sitio sin cuenta, y es sencillo, bilingüe y se adapta a la pantalla.

[Pantalla: navegador con el sitio abierto en la página de inicio, sin sesión iniciada. Zoom al 125 %.]

![Página de inicio, sin sesión iniciada](capturas/01-inicio.png)

![Menú desplegado con las seis secciones](capturas/02-menu.png)

[Diapositiva · El sitio en funcionamiento]

> Voy a mostrarles el sitio, empezando como lo vería cualquier visitante, sin haber iniciado sesión.

Ideas, en orden:

- Inicio: el nombre del proyecto con su lema, «Análisis de imágenes de microscopio», un espacio para una imagen principal y un botón para analizar una imagen.
- El menú de hamburguesa despliega las seis secciones. A la derecha, el selector de idioma (ES y EN) y el acceso para iniciar sesión.
- Recorrer rápido: Nosotros (qué es Image Bio Pro), Aliados (una tarjeta por persona, con nombre y fotografía), Infografías y videos (las infografías se abren en una ventana grande, como un blog, y abajo hay videos de YouTube dentro de la misma página) y Contacto (formulario con nombre, correo y mensaje).

![Infografías y videos](capturas/04-infografias.png)

- Idioma: al elegir EN, el sitio se traduce completo con el servicio de Google integrado, sin dos versiones del sitio. A cambio, la calidad es la de un traductor automático; los nombres propios están marcados para que no se traduzcan.

![Sitio traducido al inglés con el selector EN](capturas/07-ingles.png)

- Pie de página: nombre del proyecto, institución, contacto de ejemplo, enlaces del menú, aviso de privacidad 2026 y mención de la licencia Creative Commons Atribución-No Comercial (verificar la versión).
- Estilo sobrio, con pocos colores, que se adapta a distintos tamaños de pantalla.

> Con esto queda la parte informativa. Lo que justifica el proyecto es el análisis de imágenes, y para usarlo hace falta una cuenta.

---

## Pausa

*0:48–0:55 · 7 min*

---

## Bloque 6. Crear una cuenta

*0:55–1:00 · 5 min (3 hablados) · tope 510 palabras*

**Idea que debe quedar:** el sitio se recorre sin cuenta, pero para analizar imágenes hay que iniciar sesión, y eso hace que cada análisis sea privado.

[Pantalla: hacer clic en «Iniciar sesión». Se abre la página «Mi cuenta», con dos columnas.]

![Página «Mi cuenta», con los dos formularios](capturas/09-mi-cuenta.png)

[Diapositiva · «Mi cuenta»: entrar o crear una cuenta]

Ideas, en orden:

- La página «Mi cuenta» tiene dos columnas: a la izquierda, quien ya tiene cuenta; a la derecha, la cuenta nueva.
- Tres datos: el nombre (aparece en los informes y en la parte superior del sitio), el correo (es el identificador para entrar; no tiene que ser de Gmail ni está ligado a ningún servicio externo) y una contraseña de al menos ocho caracteres.
- [Acción: llenar el formulario con datos de ejemplo y hacer clic en «Registrarme».] Si todo está bien, la cuenta se crea y la sesión inicia en el acto, con el mensaje de bienvenida.

![Cuenta creada: mensaje de bienvenida](capturas/11-bienvenida.png)

- Mostrar «Salir» y volver a entrar. Hay una casilla «Recordarme en este equipo»: cómoda en un equipo personal, poco recomendable en uno compartido.
- La contraseña no se guarda tal cual: se guarda una versión cifrada que no se puede invertir.

> Para analizar imágenes hay que iniciar sesión. Así cada análisis pertenece a una persona y solo esa persona puede verlo.

*Si preguntan por qué el error de contraseña es vago:* para que nadie pueda averiguar qué correos están registrados.

---

## Bloque 7. Analizar una imagen y esperar

*1:00–1:12 · 12 min (7 hablados) · tope 1,190 palabras*

**Idea que debe quedar:** subir una imagen es sencillo, no hay parámetros que ajustar, y es normal que el análisis tarde.

[Pantalla: página «Inteligencia Artificial», con el título «Analizar imagen».]

![Página «Analizar imagen»](capturas/12-analizar-imagen.png)

[Diapositiva · Un recuadro con lo necesario]

Ideas, en orden:

- El recuadro tiene solo lo necesario: elegir archivos, «Analizar» y «Probar con la imagen de ejemplo». No hay parámetros ajustables ni opciones avanzadas, a propósito.
- Subir de una a diez imágenes. Formatos: BMP, PNG o TIFF; JPG con una advertencia, porque pierde calidad al comprimirse.

> No hay parámetros ni opciones avanzadas, a propósito. Así, dos personas que analicen la misma imagen obtienen el mismo resultado.

- [Acción: hacer clic en «Probar con la imagen de ejemplo».] Decirlo con franqueza: es una imagen sintética, círculos sobre un fondo oscuro, que sirve para ver el flujo completo sin tener una foto propia.

![Cubierta con la barra de progreso mientras se analiza](capturas/14-analizando.png)

[Diapositiva · La cubierta de espera]

- Aparece una cubierta con una barra de progreso, el aviso «No cierres esta página» y un mensaje que dice que es normal que el análisis tarde. Es una barra de actividad: confirma que el sistema está trabajando. Si pasa un minuto, aparece otro aviso: «Tu análisis sigue en curso».
- Tiempos: una foto grande de fluorescencia tarda unos 40 segundos y una de fondo claro entre 10 y 20. Si se suben varias, se analizan una tras otra y los tiempos se suman. Por eso el sitio tiene tiempos de espera amplios.
- Mientras esperamos, contar lo que pasa del otro lado: la imagen viaja al servidor, que revisa el formato, mide el brillo para saber si es de fondo oscuro o claro y elige uno de los dos modelos. Analiza la imagen por recortes pequeños, la red devuelve un contorno por cada espermatozoide, se juntan y se miden. Todo en el procesador del servidor.

> Es normal que el análisis tarde. Si pasa un minuto, el sitio avisa que el análisis sigue en curso. Se puede esperar con confianza.

[Acción: cuando termine, el sitio muestra la página de resultados. Si la espera es larga, abrir el análisis ya hecho en «Mis análisis».]

---

## Bloque 8. Leer los resultados

*1:12–1:27 · 15 min (12 hablados) · tope 2,040 palabras*

**Idea que debe quedar:** cada elemento de la pantalla se puede rastrear hasta un contorno de la imagen, y los números se leen siempre junto con la imagen y la gráfica.

[Pantalla: página «Resultados del análisis». Recorrer de arriba hacia abajo.]

![Resultados: encabezado, avisos, imagen marcada y datos principales](capturas/17-resultados-arriba.png)

[Diapositiva · La página de resultados, de arriba hacia abajo]

Ideas, en orden:

- Encabezado: el nombre de quien hizo el análisis, con fecha y hora exactas. Sirve para distinguir muchos análisis.
- Aviso de escala: el sitio usa la misma escala en todas las imágenes para estandarizar su tamaño, 60 píxeles por micra. La imagen marcada trae una regla de 300 píxeles que equivalen a 5 micras.
- Mensajes por imagen: uno verde si se analizó con éxito. También puede avisar que hay compresión que altera los bordes, que se contaron muy pocos espermatozoides (menos de tres) y la distribución no es confiable, o que no se encontró nada y no se analizó. Prefiere un «no se pudo» honesto a un número dudoso.
- Datos de la imagen: formato, dimensiones en píxeles, modo de color y peso.

![Imagen marcada con los contornos numerados](capturas/18-imagen-marcada.png)

[Diapositiva · Imagen marcada y datos principales]

- A la izquierda, la fotografía con cada espermatozoide marcado y numerado. A la derecha, tres recuadros: el conteo, el área media y la desviación estándar, en micras cuadradas. Debajo, el largo (media y desviación estándar en píxeles, con mínimo y máximo) y, aparte, las mismas cifras en píxeles y el largo en micras.

> Cada número tiene un contorno detrás. Si dice ciento catorce, hay ciento catorce contornos que se pueden revisar uno por uno.

![Gráfica «Distribución de tamaños»](capturas/19-distribucion.png)

[Diapositiva · «Distribución de tamaños»: un histograma]

- El histograma: en el eje horizontal el área en píxeles, dividida en diez intervalos iguales entre el mínimo y el máximo de la imagen; en el vertical, cuántas células caen en cada uno. No supone ninguna forma: dibuja lo que se midió. Con varias imágenes se usa un rango común y aparece una gráfica de promedios.
- Importante: no interpretamos los resultados ni comparamos con valores de referencia; esa lectura corresponde al grupo.

![Visor con zoom](capturas/23-visor-zoom.png)

[Diapositiva · Un visor con zoom para revisar cada contorno]

- [Acción: hacer clic sobre la imagen; usar zoom, mover, y pasar el cursor sobre un espermatozoide.] El visor sirve para revisar si un contorno corresponde de verdad a un espermatozoide. Al pasar el cursor sale su número, su área y su largo, en píxeles y en micras.

![Tabla «Detalle por espermatozoide»](capturas/20-tabla-detalle.png)

- Más abajo, la tabla con una fila por espermatozoide, con el área y el largo en píxeles y en micras. Es la misma información que el CSV.

> La media sin la gráfica puede engañar. Antes de confiar en un número, miren la imagen marcada y el histograma.

*Si hay tiempo:* ejemplo con números inventados, dicho como tal. Dos fotos con 120 y 80 células no significan que una muestra tenga más: cada foto cuenta lo que estaba en esa zona. Una diferencia de medias solo se puede afirmar con una prueba estadística, y eso lo decide el grupo con el CSV.

---

## Bloque 9. Lo que no es un espermatozoide

*1:27–1:35 · 8 min (6 hablados) · tope 1,020 palabras*

**Idea que debe quedar:** el modelo no es perfecto: puede equivocarse, el sitio avisa cuando no puede analizar, y la forma de mejorar es con más datos, más variados y mejor etiquetados.

[Diapositiva · ¿Y si la imagen no es de espermatozoides?]

Ideas, en orden:

- Plantear la pregunta: ¿qué pasa si subo una imagen que no es de espermatozoides?
- [Acción: subir las tres imágenes preparadas, por ejemplo células de hígado y de riñón.] Mostrar lo que el sitio realmente responda. Si responde «no se encontraron espermatozoides o la imagen es de mala calidad; no es factible analizarla», decirlo así: el sitio no entrega números dudosos.
- Aclarar que esto no es una garantía: la red aprendió de pocas imágenes y puede marcar manchas que se le parezcan.
- [Acción: mostrar un caso con un falso positivo, si existe.] Un falso positivo es marcar como espermatozoide algo que no lo es, por ejemplo una sombra o una mancha. En programación a esto se le llama también alucinación.

> A veces el modelo marca algo que parece un espermatozoide y no lo es. En biología se le llama falso positivo; en programación, alucinación. Es la misma idea con dos nombres.

- Por qué pasa: la red solo aprende de los ejemplos que vio. Con pocos ejemplos, hay casos que no aprendió a resolver.
- Cómo se mejora: más datos, más variados y mejor etiquetados. Si aun así no alcanza, habría que cambiar de arquitectura.

> Un modelo mejora con ejemplos de sus propios errores. Por eso el grupo es quien puede hacerlo mejor: tiene las imágenes y el criterio para etiquetarlas.

*Si preguntan si el modelo mejora solo con el uso:* no. Un modelo en línea no aprende de las imágenes que analiza. Para mejorarlo hay que reunir imágenes nuevas, etiquetarlas, reentrenar en Colab y cambiar el archivo del modelo en el servidor. Eso se ve en la sesión 4.

---

## Bloque 10. Descargas, Mis análisis y privacidad

*1:35–1:43 · 8 min (5 hablados) · tope 850 palabras*

**Idea que debe quedar:** el CSV es el dato para trabajar, el PDF es el informe para compartir, y cada análisis es privado y queda guardado.

[Pantalla: bajar al final de la página de resultados, donde están los botones.]

![Botones de salida al final de la página](capturas/21-botones.png)

[Diapositiva · El CSV y el PDF]

Ideas, en orden:

- CSV: un archivo de texto, con una fila por espermatozoide y seis columnas (imagen, número, área y largo en píxeles, área y largo en micras). Se abre en una hoja de cálculo o con código. Sirve para seguir trabajando con los datos.
- PDF: un solo informe con todas las imágenes. Primera página con el encabezado, el usuario, la fecha y el número de imágenes; luego una página por imagen, con su marca, sus datos y su gráfica; y al final la gráfica de promedios. Las medidas van primero en micras y después en píxeles. Se genera una sola vez y no cambia después.
- Imprimir: oculta el menú y los botones; se imprime solo el análisis.

> El CSV es el dato para trabajar. El PDF es el informe para compartir. Conviene guardar los dos.

![Perfil con la sección «Mis análisis»](capturas/28-mis-analisis.png)

[Diapositiva · «Mis análisis» y privacidad]

- «Mis análisis»: una tabla con una fila por análisis, con la fecha, las imágenes y los enlaces al PDF y al CSV. Al abrir uno se ve igual que cuando terminó; no se recalcula.
- Qué se guarda y qué no: se guardan los resultados, una copia reducida de la imagen marcada y el PDF. Las imágenes originales se borran del servidor al terminar el análisis. Hay que guardar los originales por cuenta propia.
- Privacidad: cada análisis es de quien lo hizo y solo esa persona puede verlo.
- [Acción: hacer clic en «Salir».]

> Las imágenes que suben se borran del servidor cuando termina el análisis. Guarden sus originales en su propia computadora.

---

## Bloque 11. Cierre y adelanto de la sesión 2

*1:43–1:50 · 7 min · tope 1,190 palabras*

**Idea que debe quedar:** el sitio convierte una fotografía en datos confiables y descargables, y la siguiente pregunta es cómo sabe la red dónde hay un espermatozoide.

[Diapositiva · Lo que vimos hoy]

Ideas, en orden:

- Resumir en cuatro frases: el problema (contar y medir a mano), la idea (la red localiza, el código mide), el sitio (cuenta, análisis, resultados, descargas) y la privacidad (cada análisis es de quien lo hizo).
- Cinco hábitos para usar el sitio: trabajar con los archivos originales; agrupar las imágenes por tipo y condición; revisar la imagen marcada antes de confiar en los números; guardar el CSV; y guardar las imágenes que el modelo analiza con dificultad, porque son las más útiles para reentrenar.

[Diapositiva · Preguntas frecuentes]

- Respuestas cortas a las dudas más probables. Si olvidan su contraseña: crear una cuenta con otro correo o avisar al desarrollador. Más de diez imágenes: se hacen varios envíos. Mismo archivo, mismo resultado: sí, porque el modelo no cambia entre análisis. Recuperar el original: no, se borra. Otras tinciones u otro tipo de célula: se puede subir, pero el resultado no es confiable.
- Cómo mandar preguntas por escrito, y cuándo se responden (por definir).

[Diapositiva · ¿Cómo sabe el sistema dónde hay un espermatozoide?]

> Seguramente muchos se preguntan cómo sabe el sistema dónde hay un espermatozoide. Esa es la pregunta de mañana: cómo aprende una computadora.

> El lunes vemos cómo funciona por dentro, y ahí les cuento los retos: las células empalmadas, los falsos positivos y la escala. Gracias por conectarse.

---

## Diapositivas que necesita esta sesión

La presentación actual tiene 129 diapositivas y está pensada para el orden anterior. Para esta sesión se necesitan estas, en este orden. Numerarlas al armar la presentación.

| Bloque | Diapositiva |
|---|---|
| 1 | Image Bio Pro · Las cuatro sesiones |
| 2 | La inteligencia artificial en la educación y la investigación · Contar y medir a mano · La red localiza y el código mide |
| 3 | Una parte web y una parte de aprendizaje automático · Entrenamiento aparte, inferencia en el servidor · Un menú con seis secciones |
| 4 | Una fotografía es una tabla de números · Una célula brillante son números altos · Formatos: unos conservan los bordes, otros no · La imagen no sabe cuánto mide un píxel |
| 5 | El sitio en funcionamiento |
| 6 | «Mi cuenta»: entrar o crear una cuenta |
| 7 | Un recuadro con lo necesario · La cubierta de espera |
| 8 | La página de resultados, de arriba hacia abajo · Imagen marcada y datos principales · «Distribución de tamaños»: un histograma · Un visor con zoom para revisar cada contorno |
| 9 | ¿Y si la imagen no es de espermatozoides? |
| 10 | El CSV y el PDF · «Mis análisis» y privacidad |
| 11 | Lo que vimos hoy · Preguntas frecuentes · ¿Cómo sabe el sistema dónde hay un espermatozoide? |

Letra más grande que en la versión anterior, con pocas ideas por diapositiva, y dibujos sencillos donde ayuden (la tabla de píxeles del bloque 4, por ejemplo). Capturas disponibles: `docs/capacitacion/capturas/`.
