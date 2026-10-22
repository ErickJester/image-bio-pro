# 06 · Preguntas difíciles con respuesta modelo

Respuestas breves, para decirse en voz alta. Los datos [COMPLETAR] se desconocen: decir "dato no disponible".

## Sobre la calidad del modelo

**1. ¿Qué precisión tiene?**
En las zonas de validación, que la red no vio al aprender, el modelo de fluorescencia tiene un AP50 de 0.89, una precisión de 0.84 y un recall de 0.89: de cada 100 marcas unas 84 son correctas, y de cada 100 espermatozoides encuentra unos 89. Son zonas de las mismas fotos y no muestras independientes, con solo 66 espermatozoides, y el mejor punto del modelo se eligió con esa misma validación, así que las cifras son algo optimistas. Por eso lo presento como un modelo preliminar.

**2. Con solo 4 fotos, ¿no hay sobreajuste?**
Son pocas fotos, pero con cientos de etiquetas (258 en fluorescencia), y partimos de un modelo preentrenado. Aun así no sabemos cómo generaliza a otras muestras: más datos variados es la mejora principal.

**3. El 1.00 de campo claro, ¿es real?**
Es real para esa validación, pero no prueba calidad: solo hay 2 espermatozoides ahí. El propio cuaderno avisa que es poco confiable.

**4. ¿Cuántos espermatozoides se le escapan o se le inventan?**
En fluorescencia, en la validación, de 66 espermatozoides la red marcó 70: se le escapan unos 11 de cada 100 (recall 0.89) y unas 16 de cada 100 marcas son falsas (precisión 0.84). En fotos con pocas células tiende a marcar de más, por ejemplo 11 detectados donde hay 6 etiquetados. En campo claro, en la foto con más células, marcó 42 donde hay 38 etiquetados.

**5. ¿Y si subo una imagen que no es de espermatozoides?**
Si no encuentra nada, avisa que no se pudo analizar. No hay garantía: puede marcar manchas o sombras, lo que llamamos falso positivo o alucinación. Más datos variados y bien etiquetados lo reducen.

**6. ¿Por qué no basta con un umbral de brillo?**
Porque las colas y las manchas también brillan, las células encimadas se unen en una sola, y el brillo cambia con la iluminación de cada foto. Quedó solo como respaldo.

## Sobre las medidas

**7. Sin escala en la imagen, ¿cómo saben que las micras son correctas?**
Usamos la misma escala (60 píxeles = 1 micra) en todas las imágenes para estandarizar su tamaño y poder compararlas entre sí, y cada resultado la declara. No es una calibración instrumental.

**8. ¿Qué mide exactamente el "largo"?**
El lado mayor del rectángulo más pequeño que encierra el contorno del espermatozoide. No es la longitud a lo largo de la curva, y el contorno incluye la cabeza y parte de la cola.

**9. ¿Por qué el histograma tiene 10 intervalos?**
Siempre son 10 de igual ancho, entre el valor mínimo y el máximo. Con varias imágenes se usa un rango común para poder compararlas. El eje horizontal está en píxeles.

**10. ¿Se puede ajustar la sensibilidad o el umbral?**
No, a propósito. Así la misma imagen siempre da el mismo resultado y cualquiera puede repetirlo.

## Sobre el diseño

**11. ¿Por qué una plataforma web y no solo el cuaderno de Colab?**
El modelo es un archivo que solo no hace nada. La plataforma permite que cualquier persona lo use sin programar, con su cuenta, su historial y sus reportes.

**12. ¿Por qué Mask R-CNN y no YOLO?**
YOLO tiene licencia AGPL-3.0, que obligaría a publicar el código de todo el sitio. Mask R-CNN tiene licencia BSD y además traza el contorno exacto, que es lo que necesito para medir.

**13. ¿Por qué dos modelos?**
Hay fotos de fondo oscuro (fluorescencia) y de fondo claro. Con pocos datos funcionó mejor un modelo por tipo, y el sitio elige uno midiendo el brillo de la foto.

**14. ¿Por qué Flask y SQLite?**
Por la ligereza del proyecto. Flask es pequeño y corre en el mismo proceso de Python que el modelo. SQLite es un solo archivo, sin servidor de base de datos, y alcanza para un grupo de investigación.

**15. ¿Por qué la red solo localiza y el código mide?**
Porque así cualquier medida se puede verificar sin abrir la red: es código determinista sobre el contorno, y esa es la base de la reproducibilidad.

## Sobre el uso y el servidor

**16. ¿Qué pasa con mis imágenes?**
Se borran al terminar el análisis, porque pesan mucho. Se guardan los resultados, el PDF y una copia reducida de la imagen marcada, visibles solo para quien hizo el análisis.

**17. ¿El modelo aprende de lo que subo?**
No. Mejorarlo exige etiquetar imágenes nuevas, reentrenar en Colab y cambiar el archivo del modelo.

**18. ¿Cuántos usuarios simultáneos aguanta?**
Navegar el sitio, muchos; analizar, uno a la vez, porque el plan tiene un solo núcleo. La medición exacta en el VPS: dato no disponible.

**19. ¿Por qué tarda tanto?**
Corre en CPU, sin GPU, para mantener bajo el costo. En la computadora de desarrollo son unos 40 segundos por foto de fluorescencia y de 10 a 20 en campo claro. Es normal y el sitio lo avisa.

**20. ¿Y si el modelo falla o no está?**
El sitio usa una detección por umbral y avisa en rojo que no es confiable. Si no detecta nada, dice que no pudo analizar la imagen.

**21. ¿Cuánto cuesta?**
Es poco y no es lo importante del proyecto: el VPS costó 2,520 pesos por 2 años, unos 105 al mes. El dominio y Colab son estimaciones: dominio de 200 a 400 al año y Colab unos 300.

## Sobre ciencia e IA

**22. ¿Tiene validez científica? ¿Es reproducible?**
Es reproducible: el modelo no cambia y las medidas son deterministas. El sitio no interpreta: la lectura científica es del grupo de investigación y debe citar la validación y la escala.

**23. ¿Qué entra a la red y qué es una capa oculta?**
Entra la imagen convertida en números. Las capas ocultas son las intermedias, que combinan esos números; se explican en la sesión 2.

**24. ¿Qué sesgos puede tener?**
Pocas fotos de un solo grupo: puede fallar con otras tinciones, microscopios o muestras que no vio al entrenar.

**25. ¿Qué sigue?**
Medir en el VPS, reunir más imágenes (incluidas muestras sin espermatozoides), validar con fotos nuevas y reentrenar; después, medir de cabeza a cola y avisar cuando la imagen no sea de espermatozoides.

## Sobre el contexto, el alcance y el público general

**26. ¿Qué diferencia hay con herramientas como ImageJ o los sistemas de análisis seminal (CASA)?**
No las sustituyo ni las comparé: no tengo una comparación medida. Lo que sí puedo decir es qué hace este sitio: detecta, cuenta y mide espermatozoides en fotos con un modelo ya entrenado, sin que la persona configure nada, y entrega histograma, CSV y PDF. ImageJ es una herramienta general de análisis de imagen, y los sistemas CASA son sistemas especializados de análisis seminal; este sitio no mide movilidad, solo fotos fijas. Comparación formal con ellos: dato no disponible.

**27. ¿Reemplaza al investigador?**
No. El sitio cuenta y mide, pero no interpreta. Decidir qué significan los resultados y si son confiables para una muestra concreta le corresponde al grupo de investigación. Es una ayuda para la parte repetitiva.

**28. ¿Qué pasa con la privacidad de los datos y de las muestras? ¿Tienen consentimiento?**
Sobre el sitio: las cuentas son privadas, las contraseñas se guardan cifradas, las imágenes subidas se borran al terminar el análisis y cada persona ve solo sus resultados. El sitio tiene un aviso de privacidad 2026 en el pie de página. Sobre el origen de las muestras y su consentimiento: dato no disponible [COMPLETAR]; eso lo maneja el grupo de investigación que aportó las fotos.

**29. ¿Se puede usar para diagnóstico clínico?**
No. Es un modelo preliminar, entrenado con pocas fotos y validado en zonas de esas mismas fotos, y el sitio no interpreta resultados. Es un caso de estudio y una herramienta de apoyo a la investigación, no un dispositivo de diagnóstico.

**30. ¿Qué es una red neuronal, explicada sin tecnicismos?**
Es un programa que aprende por ejemplos en lugar de seguir reglas escritas a mano. Se le muestran muchas fotos donde ya se marcó a mano dónde están los espermatozoides; al principio se equivoca, y cada vez que se equivoca se ajusta un poco, como quien practica hasta acertar. Al final se guarda lo aprendido en un archivo y se usa con fotos nuevas.

**31. ¿Es de código abierto? ¿Quién puede usarlo?**
El pie de página del sitio indica la licencia Creative Commons Atribución-NoComercial 4.0: se puede compartir citando la autoría y sin fines comerciales. El repositorio no incluye un archivo de licencia de software, y si es público: dato no disponible [COMPLETAR]. Sobre el uso: cualquier persona puede crear una cuenta gratis con su correo y analizar sus imágenes. Las herramientas que usa, como Flask y Mask R-CNN de PyTorch, son de código abierto; elegí Mask R-CNN, de licencia BSD, justamente para que su licencia no obligara a publicar el código del sitio.

**32. ¿Cuánto tiempo llevó hacerlo?**
La construcción del sitio fue del 8 al 16 de octubre de 2026, y la entrega es el 28 de octubre. El cuaderno de Colab donde se entrenan los modelos empezó antes, a inicios o mediados de septiembre. El primer registro en el repositorio es del 6 de octubre. Horas totales: dato no disponible.

**33. ¿Puede usarse con otras células o con otros temas?**
La técnica sí: el mismo enfoque de detectar, contornear y medir sirve para otros objetos en imágenes. Pero este modelo solo aprendió espermatozoides; para otras células habría que etiquetar fotos nuevas y reentrenar en Colab. Por eso lo presento como caso de estudio y no como un analizador general de células.
