# BioImage-Repro UAM: contexto para responder preguntas en vivo

**Cómo responder:** el público son unas 6 o 7 personas (quizá hasta 40) de distintas áreas, y la sesión se graba y se publica. Respuestas breves, concretas y en lenguaje sencillo. Si la pregunta es muy técnica, dar la idea general y ofrecer verla al final o en otra sesión. No afirmar nada que no esté aquí.

## 1. Resumen
BioImage-Repro UAM es un sitio web bilingüe (español/inglés) que analiza fotografías de microscopía de espermatozoides: detecta cada uno, los cuenta, mide área y largo, dibuja la distribución de tamaños y exporta CSV y PDF. Resuelve que contar y medir a mano es lento, repetitivo y cambia según quién lo haga. Se hizo para un grupo de investigación de la UAM Xochimilco y se presenta como caso de estudio de IA para la comunidad universitaria, en cuatro sesiones de dos horas (23, 24, 26 y 27 de octubre de 2026). Desarrollador: Ing. Angel Frausto Robles. Entrega: 28 de octubre.

## 2. Objetivo y alcance
**Logrado:** cuentas privadas; hasta 10 imágenes por análisis; conteo, área y largo con media y desviación estándar; histograma por imagen y de promedios; imagen marcada con zoom; CSV y PDF único; "Mis análisis"; imagen de ejemplo sintética.
**Fuera de alcance o pendiente:** el sitio no interpreta resultados ni es un analizador general de células; el color se calcula pero no se muestra; medidas de cabeza a cola; aviso de imagen ajena; control contra tratamiento.

## 3. Arquitectura y tecnologías
Navegador → Nginx → Gunicorn (un proceso, 4 hilos) → Flask → modelo → medición → resultados. VPS Ubuntu con Docker y HTTPS.
- **Sitio:** Flask, Jinja2, Bootstrap, Flask-Login (contraseñas cifradas), Flask-WTF (CSRF), SQLite. Traducción con el servicio de Google.
- **Modelo:** Mask R-CNN (PyTorch), entrenado en Google Colab; en el servidor solo hay inferencia, en CPU. Dos modelos: fluorescencia (fondo oscuro) y campo claro. El sitio mide el brillo (mediana del máximo RGB mayor a 127 = fondo claro) y elige uno.
- **Inferencia:** corta la foto en teselas con traslape, junta contornos y quita repetidos.
- **Medición:** OpenCV y numpy dentro de cada contorno; la red no decide medidas.
- **Salidas:** Chart.js, y matplotlib con fpdf2 para el PDF.

## 4. Decisiones técnicas
- **La red localiza, el código mide:** cualquier medida se verifica sin abrir la red.
- **Mask R-CNN y no YOLO:** la licencia AGPL-3.0 de YOLO obliga a publicar el código del sitio; Mask R-CNN es BSD.
- **Transfer learning:** hay pocas imágenes; se parte de un modelo preentrenado.
- **Dos modelos:** funcionó mejor uno por tipo de fondo; la elección es una regla de brillo, no aprendizaje.
- **VPS:** el hosting compartido no corre Flask con PyTorch.
- **Un proceso y análisis de uno en uno:** cada modelo pesa unos 176 MB; varios procesos los duplicarían.
- **No suponer:** si falta un dato (la escala), el sitio lo declara.
- **Imágenes subidas se borran al terminar:** pesan mucho y cuestan espacio. Se guardan el PDF y una copia reducida marcada.
- **Flask y SQLite, por ligereza:** Flask es un framework pequeño que corre en el mismo proceso de Python que el modelo. SQLite es un solo archivo, sin servidor de base de datos que instalar, y alcanza para un grupo de investigación.

## 5. Resultados y métricas
- Entrenamiento: fluorescencia, 4 fotos y 258 etiquetas; campo claro, 4 fotos y 45.
- El sitio da los mismos conteos que el cuaderno en cinco fotos (114, 9, 2, 1 y 43): prueba de integración, no de calidad científica.
- En zonas amontonadas, en fluorescencia, encuentra unos 85 de cada 100.
- Escritorio: unos 40 s por foto de fluorescencia (1792 px) y de 10 a 20 s en campo claro. VPS: dato no disponible.
- Validación (IoU 0.5, umbral 0.5), con zonas reservadas de las mismas fotos, no muestras independientes. Fluorescencia: AP50 0.91 (guardado en el modelo). Campo claro: AP50, precisión, recall y F1 de 1.00, pero solo con 2 espermatozoides; no prueba calidad.
- Campo claro, foto con más células: 42 detectados contra 38 etiquetados (sobredetección leve).
- Precisión y recall de fluorescencia: [COMPLETAR].

## 6. Limitaciones y riesgos
- Pocos datos de una sola fuente, y dos tipos de imagen, que no es lo ideal para entrenar; se desconoce el desempeño con otras muestras, tinciones o fotos comprimidas.
- Conteos aproximados con células juntas: la red repite o parte contornos.
- Sin ejemplos negativos: puede marcar sombras o manchas (falsos positivos).
- Las micras dependen de la escala común (60 px = 1 µm) que estandariza el tamaño de las imágenes.
- El "largo" es el lado mayor del rectángulo mínimo del contorno, no la longitud de la curva; los contornos incluyen parte de la cola.
- Plan Hostinger KVM 1 (un núcleo): los análisis simultáneos esperan turno. Tiempos en el VPS sin medir.

## 7. Trabajo futuro
Medir en el VPS; más imágenes y reentrenar; medir de cabeza a cola; avisar si la imagen no es de espermatozoides; control contra tratamiento.

## 8. Glosario
- **Segmentación por instancias:** detectar cada objeto y trazar su contorno.
- **Mask R-CNN:** red que detecta objetos y da una máscara por cada uno.
- **Transfer learning:** reutilizar una red ya entrenada y ajustarla con datos propios.
- **Entrenamiento / inferencia:** ajustar la red con ejemplos / usarla con fotos nuevas.
- **Pesos (.pt):** números aprendidos, guardados en un archivo.
- **Tesela:** recorte de la foto que se analiza por separado.
- **Falso positivo / alucinación:** marcar como espermatozoide algo que no lo es.
- **Función de pérdida:** número que mide cuánto se equivocó la red.
- **Descenso del gradiente:** ajustar los pesos paso a paso hacia donde baja el error, como bajar una pendiente con niebla.
- **Retropropagación:** calcular, de la salida hacia atrás, cuánto contribuyó cada peso al error.

## 9. Preguntas difíciles probables
1. **¿Qué precisión tiene?** En las zonas de validación, que la red no vio al aprender, el AP50 de fluorescencia es 0.91. Son zonas de las mismas fotos y no muestras independientes, y en zonas amontonadas ronda 85 de cada 100. Por eso es un modelo preliminar.
2. **Con 4 fotos, ¿no hay sobreajuste?** Son pocas fotos pero cientos de etiquetas, y partimos de un modelo preentrenado. No sabemos cómo generaliza; más datos es la mejora principal.
3. **¿Por qué no basta un umbral?** Colas y manchas también brillan, las células encimadas se unen y el brillo cambia con la iluminación.
4. **Sin escala en la imagen, ¿cómo saben que es correcta?** Usamos la misma escala en todas las imágenes para estandarizar su tamaño y poder compararlas entre sí, y cada resultado la declara.
5. **¿Por qué una plataforma web y no Colab?** El modelo es un archivo que solo no hace nada. La plataforma permite que cualquiera lo use sin programar.
6. **¿Por qué dos modelos?** Hay fotos de fondo oscuro y de fondo claro; con pocos datos funcionó mejor uno por tipo, elegido por brillo.
7. **¿Y si subo una imagen que no es de espermatozoides?** Si no encuentra nada, avisa que no se pudo analizar. No hay garantía: puede marcar manchas, un falso positivo o alucinación. Más datos variados y bien etiquetados lo reducen.
8. **¿El modelo aprende de lo que subo?** No. Mejorarlo exige etiquetar imágenes nuevas, reentrenar en Colab y cambiar el archivo.
9. **¿Qué pasa con mis imágenes?** Se borran al terminar. Se guardan resultados, PDF y una copia reducida, visibles solo para quien analizó.
10. **¿Cuántos usuarios simultáneos aguanta?** Navegar, muchos; analizar, uno a la vez. Medición en el VPS: dato no disponible.
11. **¿Por qué tarda?** Corre en CPU, sin GPU, para mantener bajo el costo. Es normal y el sitio lo avisa.
12. **¿Qué mide el largo?** El lado mayor del rectángulo mínimo que encierra el contorno, en píxeles y en micras.
13. **¿Por qué 10 intervalos en el histograma?** Siempre son 10 de igual ancho, entre el mínimo y el máximo; con varias imágenes se usa un rango común para poder compararlas.
14. **¿Qué es una capa oculta?** Una capa intermedia que combina los números de la imagen; se explica en la sesión 2.
15. **¿Es reproducible? ¿Tiene validez científica?** Sí es reproducible: el modelo no cambia y las medidas son deterministas. El sitio no interpreta: la lectura científica es del grupo.

## 10. Preguntas sobre la IA
- **¿Cómo funciona?** Mask R-CNN recorre la foto por teselas y devuelve un contorno por espermatozoide; el código mide.
- **¿Por qué esa red?** Traza contornos exactos, sirve con pocas imágenes y su licencia no obliga a publicar el sitio.
- **¿Costos?** Estimaciones del README: VPS de 100 a 250 MXN al mes, dominio de 200 a 400 al año, Colab unos 300. Plan: Hostinger KVM 1; precio real [COMPLETAR].
- **¿Privacidad?** Cuentas privadas, contraseñas cifradas, imágenes borradas, modelos no expuestos.
- **¿Sesgos?** Pocas fotos de un solo grupo: puede fallar con otras tinciones o muestras.
- **¿Y si falla?** Sin modelo, usa el umbral y avisa en rojo; si no detecta nada, dice que no analizó.

## Pendientes [COMPLETAR]
1. Precisión y recall de fluorescencia (salida de su cuaderno de Colab).
2. Tiempo y memoria en el VPS KVM 1; precio real.
