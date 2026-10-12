# Guion para la reunión con el cliente

Solo para mí. Está escrito para decirlo en voz alta, con "usted" porque así hablamos en la reunión anterior. Las preguntas llevan el mismo número que en [`preguntas-cliente.md`](preguntas-cliente.md), para anotar las respuestas con ese número.

Las que dicen (urgente) bloquean el sitio o tienen fecha cerca. Si veo que el tiempo se acaba, hago esas primero y dejo el resto para un correo.

Regla para toda la reunión: si no saben una respuesta, que la consulten con el grupo y me avisen. Anoto quién se compromete y para cuándo.

---

## 1. Saludo y arranque

Buenas tardes, gracias por darme el tiempo. Les cuento rápido cómo vamos y luego tengo unas preguntas, porque hay cosas que solo ustedes pueden decidir y de eso depende que el sitio salga a tiempo.

Lo que ya tengo es un boceto de todas las pantallas: inicio, nosotros, aliados, infografías y videos, la página de inteligencia artificial, los resultados, el contacto y el inicio de sesión. Si quieren, se los comparto en pantalla al final y me dicen si van bien.

Del lado técnico, ya definí tres cosas para que no tengan que preocuparse. El sitio va en español e inglés con la API de Google Traductor, como pidieron. Cada usuario va a ver solo sus propios análisis. Y la red neuronal, el material de la capacitación y el sitio los entrego yo antes de las fechas acordadas.

Son unas 30 preguntas, pero muchas son de sí o no. Voy por temas.

---

## 2. Cuentas

**1. Historial (urgente).** Cuando alguien hace un análisis, ¿quieren que el sistema se lo guarde en su cuenta para volver a verlo después, o basta con que analice, descargue sus resultados y ya?

**2. Registro (urgente).** ¿Cualquier persona con un correo puede crear su cuenta, o solo las personas que ustedes autoricen? Por ejemplo, yo podría tener una lista de correos permitidos.

**3. Administrador.** ¿Hace falta que alguien del grupo pueda ver quién está registrado o dar de baja a un usuario?

**4. Correo y contraseña.** ¿Quieren que el sistema mande un enlace para confirmar el correo? Y si alguien olvida su contraseña, ¿le mandamos un correo para cambiarla?

---

## 3. Las imágenes

**5. Formato y escala (urgente).** Esta es de las más importantes. La imagen que me pasaron vino por WhatsApp, o sea, comprimida y sin escala. Necesito saber cómo viene la imagen cuando sale del microscopio.

- ¿Qué formato tiene el archivo? ¿TIFF u otro sin compresión, o JPEG? ¿Cuánto pesa más o menos?
- Para medir en micrómetros necesito la escala. ¿La imagen la trae guardada en el archivo? ¿O trae una barra de escala dibujada? ¿O solo se sabe por el aumento del objetivo, por ejemplo 40x? ¿Cuál es?
- ¿Me podrían mandar una imagen original directo del microscopio, sin pasar por WhatsApp?

**6. Una o varias.** ¿Se analiza una imagen a la vez, o suben varias juntas en el mismo análisis?

**7. Guardar imágenes.** Las imágenes que suben los usuarios, ¿se guardan en el servidor o se borran cuando termina el análisis?

**8. Qué se mide.** En la reunión pasada dijeron "medir cuánto mide cada célula". ¿Se refieren al área de la cabeza, al largo de la cabeza, al largo total con la cola, o a varias? ¿Y en micrómetros?

**9. Tamaño típico.** Más o menos, ¿de qué tamaño son las imágenes y cuántas células salen en cada una?

**10. Qué tan estricto es el conteo.** Cuando el sistema detecta células, decide cuáles cuenta. Hay dos controles que podría darles:

- Uno es qué tan seguro debe estar el sistema de que algo es una célula. Si lo bajo, cuenta más cosas, incluido el ruido. Si lo subo, se le pierden las células muy tenues.
- El otro es un tamaño mínimo, para ignorar los puntos chiquitos del fondo.

El problema es que con esos controles dos personas pueden sacar resultados distintos de la misma imagen. Sin ellos, todos los análisis son comparables. Mi propuesta es empezar sin controles y agregarlos si ven que los necesitan. ¿Le parece?

---

## 4. Color y tinciones

Aquí me voy a apoyar en la imagen de ejemplo. La pongo en pantalla y señalo células.

**11. Tinciones (urgente).** ¿Qué estructura marca el rojo y cuál marca el verde o el amarillo? ¿Cuántas tinciones usan?

**12. Qué significa el color (urgente).** Una cabeza anaranjada y una roja, ¿qué quieren decir biológicamente? ¿Hay un criterio para decidir cuándo es una y cuándo la otra?

**13. Mezcla de colores.** En esta imagen las anaranjadas aparecen sobre todo donde hay muchas colas encimadas. ¿El naranja puede ser una mezcla por superposición? ¿Cómo lo toman ustedes?

**14. Ejemplos clasificados a mano.** ¿Me podrían pasar unos ejemplos que ya hayan clasificado ustedes? Así comparo mi resultado con el suyo.

**15. Los que no son ni rojas ni anaranjadas.** Si una célula sale verde, amarilla o dudosa, ¿cómo la reporto?

---

## 5. Resultados y descargas

**16. Columnas del CSV.** Les voy a enseñar cómo se vería, para que me digan qué quitar o agregar. Los números son inventados.

Opción A: una fila por célula.

| imagen | celula | area_um2 | largo_um | color |
|---|---|---|---|---|
| muestra1.jpg | 1 | 18.4 | 6.2 | rojo |
| muestra1.jpg | 2 | 21.0 | 6.8 | anaranjado |
| muestra1.jpg | 3 | 17.9 | 6.0 | rojo |
| muestra1.jpg | ... | ... | ... | ... |

Opción B: un resumen por imagen.

| imagen | total | rojas | anaranjadas | area_media_um2 | desviacion_um2 |
|---|---|---|---|---|---|
| muestra1.jpg | 152 | 118 | 34 | 18.7 | 2.3 |

Les pregunto: ¿quieren las dos, solo una, o hay columnas que les sirvan más? Por ejemplo, quitar el largo, o poner otra medida.

**17. PDF.** El PDF, ¿qué debe llevar? Yo pensaba en el conteo, la tabla de células y la gráfica de distribución. ¿Algo más?

**18. Gráfica de distribución.** Es un histograma: barras que cuentan cuántas células caen en cada rango de tamaño, y encima la curva de campana que pidieron. Se vería así:

```
células
  |         ██
  |       ████▄
  |     ▄██████▄
  |   ▄██████████▄
  | ▄██████████████▄
  +--------------------- tamaño (µm)
   14   16   18   20   22
            ↑ media
```

¿Quieren una sola gráfica con todas las células, o una para las rojas y otra para las anaranjadas? ¿Y les sirve que marque la media y la desviación?

---

## 6. El sitio

**19. Contenidos (urgente).** Para armar Aliados, Nosotros, infografías y videos necesito sus textos, las fotos, los nombres y los videos. Lo ideal es tenerlos antes del 16 de octubre. ¿Para cuándo me los pueden pasar, y quién me los manda?

**20. Videos.** ¿Dónde quieren los videos? ¿Debajo de las infografías, o en otra sección?

**21. Contacto.** ¿Solo el formulario, o también los datos del área, como dirección y teléfono?

**22. Correo del formulario (urgente).** ¿A qué correo deben llegar los mensajes que manden por el formulario?

**23. Imagen del sitio.** ¿Tienen logotipo, colores o tipografía que quieran que use?

---

## 7. Servicios y entrega

**24. VPS y dominio (urgente).** El sitio necesita un servidor, el VPS, y un dominio. ¿Quién los contrata y cuándo? Necesito acceso a más tardar el 15 de octubre para dejar todo montado. Recuerden que el plan va por lo justo, unos 100 a 250 pesos al mes el servidor y unos 200 a 400 al año el dominio.

**25. Dominio (urgente).** ¿Qué dominio quieren?

**26. Usuarios al mismo tiempo.** ¿Cuántas personas van a usar el sitio a la vez, más o menos?

**27. Capacitación.** Propuse cinco sesiones de dos horas, a las 18:00, del 17 al 27 de octubre. ¿Confirman las fechas? Y necesito saber por qué plataforma de videollamada y cuántas personas van a ser.

---

## 8. Lo que viene después

**28. Siguiente lote de imágenes.** El modelo de ahora es un esqueleto, entrenado con unas 10 imágenes, y sirve para mostrar el flujo completo pero no tiene validez científica. Para el entrenamiento real hacen falta unas 50. ¿Cuándo las tendrían? Y para entrenar hay que marcar las células en cada imagen: ¿lo hacen ustedes o lo hago yo?

**29. Revisión de las marcas.** ¿Alguien del grupo con conocimiento biológico puede revisar esas marcas? Yo no voy a saber si una célula está bien marcada.

**30. La otra red neuronal.** Ustedes mencionaron una segunda red, la que distingue control contra tratamiento. Eso sería otro sistema, y lo entiendo como algo para después del 28 de octubre. Quiero definirlo con calma: qué debe hacer, con qué datos y en qué plazo. ¿Es esa la clasificación que tenían en mente?

---

## 9. Cierre

Perfecto, con esto tengo lo que necesito para avanzar. Lo que me quede pendiente se los resumo por correo hoy mismo, con quién lo debe mandar y para cuándo.

Antes de irnos, ¿les enseño el boceto? Si algo no les gusta de las pantallas, este es el momento de decirlo, porque después cuesta más cambiarlo.

Gracias.

---

## Para anotar durante la reunión

| # | Respuesta | Quién la da | Para cuándo |
|---|---|---|---|
| | | | |
