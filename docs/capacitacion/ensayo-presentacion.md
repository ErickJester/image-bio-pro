# Ensayo de la presentación de la sesión 1

Resumen de la reunión de ensayo, combinando dos transcripciones. Sin marcas de tiempo. Donde las transcripciones no coinciden o se oye mal, se indica con [verificar].

**Participantes**
- **Ángel:** desarrollador de Image Bio Pro, presenta.
- **Evaluador:** quien revisa la presentación y da retroalimentación (rol inferido de la conversación).
- **Isaac:** se une al final para la parte de tiempos de espera.

## 1. Qué le dijo el evaluador al inicio

- La presentación debe dirigirse a la comunidad universitaria de distintas áreas, no solo a clientes.
- Hay que explicar qué es la inteligencia artificial y cómo se aplica a problemas técnico-científicos, con un caso concreto de biología de la reproducción.
- El caso de estudio es el conteo de espermatozoides. Lo educativo se enseña a través de ese ejemplo.
- La introducción debe decirse en español.

## 2. Introducción: cómo empezar

- Ángel iba a leer su introducción tal como la tenía escrita, con "Buenas tardes… mi nombre es Ángel Frausto Robles, desarrollador de Image Bio Pro".
- El objetivo del proyecto se puede repetir; el evaluador dijo que no importa repetir la introducción.
- El párrafo sobre la necesidad ("contar y medir células a mano es lento…") fue cuestionado por la palabra "explícitos". Se acordó decir **explícitos y estandarizados**.
- El evaluador pide no ir demasiado rápido: Ángel dijo que tiene mucho texto para las dos horas.
- Hay que numerar las diapositivas para poder comentar por número. La presentación tiene 129 diapositivas.

## 3. Cómo presentar el sistema

- Se presenta el sitio como si estuviera completo. Los pendientes se mencionan en general ("el modelo funciona, aunque puede mejorarse y estamos a la espera de más información") sin ahondar.
- El objetivo es transmitir que el modelo sí funciona.
- Ángel explica la división en dos partes: una parte web que se mantiene como cualquier sitio, y una parte de aprendizaje automático que mejora con datos. Cada una necesita cuidados distintos.
- El evaluador pregunta por qué se necesita una plataforma web si la red puede correr en Google Colab. Respuesta: Colab sirve para entrenar. El modelo sale como un archivo `.pt`, que por sí solo no hace nada. El sitio es lo que lo carga y permite visualizar resultados.
- Ese punto es importante y debe quedar claro: la plataforma permite que cualquier persona de la comunidad universitaria use la función de inteligencia artificial desde una interfaz.

## 4. Las secciones del sitio

Son seis secciones: Inicio, Nosotros, Aliados, Infografías y videos, Inteligencia Artificial y Contacto.

- **Inicio:** título con el lema "Análisis de imágenes de microscopio". Espacio para una imagen principal que se pondrá después.
- **Nosotros:** qué es Image Bio Pro.
- **Aliados:** una tarjeta por persona, con nombre, fotografía y lo que estudió. Quien quiera aparecer solo tiene que mandar sus datos.
- **Infografías y videos:** las infografías se abren en una ventana grande con imagen y texto, como un blog. El título va fuera de la imagen. Abajo hay unos cuatro videos de YouTube dentro de la misma página.
- **Contacto:** formulario con nombre, correo y mensaje, y datos de contacto.
- **Inteligencia Artificial:** es la sección del análisis.

El evaluador sugiere presentar cómo se organiza el sitio como un entorno educativo con varias secciones, y decirlo en lenguaje sencillo.

**Idioma:** el selector cambia el sitio completo al inglés. La traducción la hace el servicio de Google. Los nombres propios y los nombres de archivo están marcados para que no se traduzcan. A cambio, la calidad es la de un traductor automático.

**Pie de página:** nombre del proyecto, institución, contacto de ejemplo, enlaces del menú, aviso de privacidad 2026 y la licencia Creative Commons Atribución-No Comercial. El evaluador no estaba seguro de cuál versión de Creative Commons es. [verificar]

## 5. Cuentas y acceso

- Es un sitio que se puede recorrer sin cuenta, pero analizar imágenes requiere iniciar sesión. El evaluador pidió destacar este punto: el acceso a la red neuronal es privado y se hace con un usuario.
- Para crear cuenta se piden tres datos: nombre (aparece en los informes y en la parte superior del sitio), correo (no tiene que ser de Gmail) y contraseña de al menos ocho caracteres.
- Al entrar, el sitio lleva directo a "Analizar imagen".

## 6. Analizar una imagen

- El análisis no tiene parámetros ajustables ni opciones avanzadas, a propósito: dos personas que analicen la misma imagen obtienen el mismo resultado.
- Se pueden subir de una a diez imágenes a la vez. Formatos aceptados: BMP, PNG y TIFF. JPG se acepta con advertencia, porque pierde calidad al comprimirse.
- Mientras se analiza, aparece una barra de progreso animada y el aviso de no cerrar la página.
- El tiempo es importante: una fotografía grande de fluorescencia tarda unos 40 segundos en la computadora de desarrollo, y una de fondo claro entre 10 y 20 segundos. Con diez imágenes, el tiempo es la suma. Por eso hay tiempos de espera de hasta media hora.
- **Sugerencia de Isaac:** avisar al usuario desde el inicio que el análisis puede tardar, y que después de uno o dos minutos siga viendo un mensaje de que el análisis sigue corriendo. Ángel dijo que lo revisará.
- **Sugerencia del evaluador:** que la tardanza se presente como algo normal y explicado, no como un fallo. Si la gente no sabe por qué tarda, pensará que el sistema es lento o complicado.
- **Resultados:** conteo, área y largo de cada espermatozoide, media y desviación estándar, y una gráfica de distribución por imagen. Con varias imágenes hay una gráfica adicional con promedios. Se pueden descargar en CSV y en un solo PDF.
- **Mis análisis:** cada usuario ve sus análisis. Son privados. Al abrir uno se ve igual que al terminar, solo para consulta.
- **Imagen de ejemplo:** sirve para probar el flujo completo sin una imagen propia. En realidad es una distribución de círculos sobre fondo oscuro, generada para la prueba. Ángel dijo que el aviso de escala que sale con ella se quitará.

**Imagen de referencia:** la de la demostración muestra un aviso sobre la escala. El evaluador preguntó si ese aviso se quita. Ángel dijo que sí, porque se trata de un aviso de que la imagen no tiene escala, y la imagen de ejemplo no tiene esa información.

## 7. Escala en micras

- Las fotos no traen barra de escala ni regla impresa, y los archivos no guardan esa información.
- El sitio usa 60 píxeles por micra, que sale de una raya de 300 píxeles que equivale a 5 micras. Cada resultado indica la escala usada, y la escala se guarda en una tabla que se edita sin tocar el código.
- El evaluador pidió no presentarlo como una escala imaginaria. La formulación que propuso: el grupo usa una escala para estandarizar el tamaño de las imágenes, con imágenes de distintos aumentos (40X, 100X). [verificar el nombre técnico del aumento]
- Las medidas en micras no deben ahondarse en la introducción; se verán en la parte técnica.
- Al explicar la imagen de ejemplo (sección 6), Ángel dijo que el área mínima, el promedio, la desviación y el área máxima se muestran en píxeles, y que lo corregirá después.

## 8. Los tres principios

Ángel los presenta así:

1. **No suponer.** Cuando falta un dato, como la escala o lo que marca cada tinción, el sitio no lo inventa. Lo indica en pantalla. Por eso cada resultado muestra la escala y el estado del modelo. Prefiere un aviso claro a un número que parezca más seguro de lo que es.
2. **Separar lo que decide la red de lo que se mide.** La red localiza y el código mide, así que cualquier medida se verifica sin abrir la red.
3. **Reproducibilidad.** El entrenamiento está en un cuaderno de Colab que cualquiera puede abrir y ejecutar. El modelo guarda dentro de su archivo la configuración con la que se entrenó. Si hay que repetir un resultado o reconstruir el entorno, no depende de la memoria de nadie.

El evaluador lo consideró muy bueno. Pidió lo siguiente:
- Al mencionar Colab, explicar qué es: un entorno de trabajo para programar en la nube.
- Cuando aparezcan términos como Python o Flask, explicarlos al pasar, en una frase, para no perder a la audiencia. Por ejemplo: "Python, un lenguaje de programación; Flask, una herramienta para hacer sitios web con Python".
- Introducir los conceptos poco a poco.

## 9. Dónde explicar la parte de dos etapas

Ángel dijo que escribió que el entrenamiento ocurre en Colab y la inferencia en el servidor, y que la gente podría no entender por qué "entrenamiento aparte". El evaluador propuso esta redacción:

> El desarrollo de la red neuronal se lleva a cabo en dos etapas: el entrenamiento, en Google Colab, y la inferencia, que se realiza en el servidor.

Después: "Cuando queremos aplicarla a nuevas imágenes, la inferencia se lleva a cabo en el servidor."

## 10. Retos y experiencia del equipo

- El evaluador pidió incluir al final una parte sobre los retos que se presentaron para desarrollar el modelo. Propuso presentarlos como cosas que se resolvieron, no como cosas que no se pudieron resolver.
- Ejemplo de reto: cuando muchas células se empalman en un punto, es difícil contarlas. El equipo generó una estrategia computacional para poder contarlas y dar una mejor predicción.
- El evaluador pidió no presentar el modelo como una versión final sin limitaciones; sí presentarlo como funcional, con pruebas y en espera de más información.

## 11. Alcance

- El servidor solo hace inferencia, en procesador. El entrenamiento ocurre aparte, en Colab.
- El sitio entrega conteos, medidas y gráficas. No interpreta resultados. La lectura científica corresponde al grupo.
- Ángel dijo que, por ser más educativa la presentación, este punto se quedará más breve.

## 12. Demostración en vivo

- Ángel mostrará la página de inicio sin haber iniciado sesión, para que se vea lo que ve cualquier visitante.
- Hay que mencionar que la interfaz todavía es provisional, aunque ya es funcional. El diseño se está mejorando.
- Ángel dijo que el logotipo de la universidad aparece en la barra de navegación, a la izquierda del acceso para iniciar sesión. [verificar: aparece solo en una de las transcripciones]
- Las frases del entrenamiento y de la red se mencionan aquí en general; el detalle es para la parte técnica.

## 13. Ideas de mejora y decisiones de presentación

- El evaluador pidió no ahondar en lo que falta. Basta con decir que hay detalles pendientes y que el modelo está en espera de más información.
- Ángel dijo que, por lo que se acordó, la presentación se enfocará en lo educativo, con un caso de estudio y no con una necesidad real de laboratorio.
- El evaluador notó que la gente pone atención a los primeros 20 minutos. Por eso la introducción debe ser clara y no demasiado técnica.

## 14. Pendientes acordados

- **Sitio web:** Ángel enviará al evaluador el texto de la página web, a más tardar el jueves temprano, para cargarlo al sitio. El evaluador dijo que luego se puede ajustar.
- **Fotos de Aliados:** el evaluador enviará las fotos de las personas del grupo.
- **Sesión de ajuste:** se confirmará el jueves temprano si hay una sesión rápida para revisar la página y la presentación. Isaac está invitado si hay sesión.
- **Mensaje de espera:** Ángel revisará la sugerencia de Isaac de avisar que el análisis puede tardar, y de que siga corriendo después de uno o dos minutos.
- **Numerar diapositivas:** para poder hacer comentarios por número.
- **Corrección de unidades:** cambiar píxeles por micras donde corresponda.
- **Quitar el aviso de escala** de la imagen de ejemplo, como acordaron.
- **Redacción de dos etapas** (entrenamiento en Colab e inferencia en el servidor), según la propuesta del evaluador.

## 15. Cierre

Se acordó que el evaluador dará confirmación de la sesión del jueves. Ángel dijo que lo confirma si es posible. La reunión terminó con agradecimientos.
