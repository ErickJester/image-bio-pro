# Preguntas para el cliente

Lo que falta por confirmar, agrupado por tema. Las marcadas con ⭐ son las que más urgen porque bloquean la construcción del sitio. Las demás se pueden responder después, pero conviene tener respuesta antes del entrenamiento real.

Al final hay una sección con lo que ya está decidido y no se pregunta.

## 1. Cuentas y privacidad (RF-13, RF-14)

1. ⭐ ¿Se guarda un historial de análisis por usuario, o basta con analizar, descargar y ya?
2. ⭐ ¿Cualquier persona con correo puede registrarse, o solo las personas que el grupo autorice (por ejemplo, una lista de correos permitidos)?
3. ¿Se necesita un administrador que vea o dé de baja usuarios?
4. ¿Hay que verificar el correo (enlace de confirmación) o basta con escribirlo? ¿Y qué pasa si alguien olvida su contraseña?

## 2. Imágenes y análisis (RF-10, RF-15 a RF-19)

5. ⭐ ¿Cómo viene la imagen cuando sale del microscopio y cuál es su escala?
   - **Formato:** las de entrenamiento vienen en BMP. ¿Las que subirán los usuarios del sitio también serán BMP, o TIFF, o a veces JPEG? ¿Cuánto pesa una imagen típica?
   - **Escala:** ¿el archivo la trae guardada, hay una barra de escala dibujada en la imagen, o solo se sabe por el aumento del objetivo (por ejemplo, 40x)? ¿Cuál es?
   - ¿Pueden mandarme una imagen original directo del microscopio, sin pasar por WhatsApp?
6. ¿Se analiza una imagen a la vez o varias juntas en un mismo análisis?
7. ¿Las imágenes que suben los usuarios se guardan en el servidor o se borran después del análisis?
8. "Medir cuánto mide cada célula": ¿se refiere al área de la cabeza, al largo de la cabeza, al largo total con la cola, o a varias? ¿En qué unidad lo quieren (µm)?
9. ¿Qué tamaño de imagen y qué número de células por imagen esperan, más o menos?
10. ¿Quieren poder ajustar qué tan estricto es el conteo, o prefieren que siempre funcione igual?
    - **Qué es un parámetro ajustable:** al detectar células, el sistema decide cuáles cuenta. Hay dos controles posibles:
      - *Seguridad mínima:* qué tan seguro debe estar el sistema de que algo es una célula. Más bajo, cuenta más cosas, incluidos puntos de ruido. Más alto, se pierden las células tenues.
      - *Tamaño mínimo:* ignorar objetos más chicos que cierto tamaño, que sirve para descartar el ruido del fondo (RF-16).
    - **La disyuntiva:** con controles, cada persona puede afinar el conteo, pero dos usuarios pueden obtener resultados distintos de la misma imagen. Sin controles, todos los análisis son comparables.
    - Ellos dijeron "iríamos viendo si es necesario o si no". Propuesta: sin controles al inicio, para que los resultados sean comparables, y agregarlos solo si lo piden.

## 3. Tinciones y color (RF-19)

11. ⭐ ¿Qué estructura marca el rojo y cuál marca el verde (o el amarillo)? ¿Cuántas tinciones se usan?
12. ⭐ ¿Qué significa biológicamente una cabeza anaranjada y una roja? ¿Hay un criterio para decidir cuándo es una y cuándo la otra?
13. En la imagen de ejemplo las anaranjadas se concentran donde hay colas encimadas: ¿el naranja puede ser mezcla de colores por superposición? ¿Cómo lo toman ellos?
14. ¿Pueden pasar un par de ejemplos que ellos ya hayan clasificado a mano, para comparar mi resultado con el suyo?
15. Si una célula no es ni roja ni anaranjada (verde, amarilla, dudosa), ¿cómo se reporta?

## 4. Resultados y descargas (RF-18, RF-20, RNF-02)

16. ¿Qué columnas quieren en el CSV?
    - **Una fila por célula.** Ejemplo, con valores inventados:

      ```
      imagen,celula,area_um2,largo_um,color
      muestra1.jpg,1,18.4,6.2,rojo
      muestra1.jpg,2,21.0,6.8,anaranjado
      muestra1.jpg,3,17.9,6.0,rojo
      ```

    - **Un resumen por imagen.** Ejemplo, con valores inventados:

      ```
      imagen,total,rojas,anaranjadas,area_media_um2,desviacion_um2
      muestra1.jpg,152,118,34,18.7,2.3
      ```

    - Pregunta: ¿quieren las dos, solo una, o columnas distintas (por ejemplo, sin el largo o con otra medida)?
17. ¿Qué debe llevar el PDF: conteo, tabla de células, gráfica de distribución? ¿Algo más?
18. ¿Cómo quieren la gráfica de distribución de tamaños?
    - **Qué es:** un histograma, que son barras que cuentan cuántas células caen en cada rango de tamaño. Eje horizontal: tamaño (µm). Eje vertical: número de células. Encima va la curva de campana (tipo Gauss) que pidieron.

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

    - **Preguntas:** ¿una sola gráfica con todas las células, o una por color (rojas contra anaranjadas)? ¿Quieren que se marque la media y la desviación?

## 5. Contenido del sitio (RF-04 a RF-09)

19. ⭐ ¿Cuándo nos pasan los textos, fotos y nombres del grupo (Aliados), las infografías y los videos? Necesito tenerlos antes del 16 de octubre.
20. ¿Dónde van los videos: debajo de las infografías o en otra sección?
21. Contacto: ¿solo el formulario o también los datos del área (dirección, teléfono)?
22. ⭐ ¿A qué correo deben llegar los mensajes del formulario?
23. ¿Tienen logotipo, colores o tipografía que quieran usar?

## 6. Servicios y entrega

24. ⭐ ¿Quién contrata el VPS y el dominio, y cuándo? Necesito acceso antes del 15 de octubre para desplegar.
25. ⭐ ¿Qué dominio quieren?
26. ¿Cuántas personas usarán el sitio al mismo tiempo, más o menos?
27. Capacitación: ¿confirman las fechas (17 al 27 de octubre, 18:00), la plataforma de videollamada y de cuántas personas es el grupo?

## 7. Reentrenamiento y siguientes etapas (RF-21)

28. ¿Cuándo tendrán el siguiente lote de unas 50 imágenes, y quién las va a anotar (marcar las células) o necesitan que yo lo haga?
29. ¿Hay alguien en el grupo con conocimiento biológico que pueda revisar las anotaciones?
30. Red neuronal B (control contra tratamiento): sería otro sistema, no una extensión de este, y se haría después del 28 de octubre. Hay que definir con calma qué debe hacer exactamente, con qué datos y en qué plazo. ¿Es la clasificación que mencionaron como perspectiva?

## Ya decidido (no se pregunta)

| Tema | Decisión | Quién |
|---|---|---|
| Privacidad de los análisis | Cada usuario ve solo sus propios análisis. | Desarrollador |
| Traducción | Se usa la API de Google Traductor, como pidió el cliente (RF-03). | Cliente |
| Licencia del modelo | Mask R-CNN de torchvision (BSD). No se usa Ultralytics por su licencia AGPL. | Desarrollador |
| Capacitación y modelo | El desarrollador entrega el modelo y el material de las sesiones antes de las fechas. No se mueven sesiones a noviembre. | Desarrollador |
| Contornos sobre la imagen original | Fuera de alcance. | Desarrollador |
