# 05 · Limitaciones, riesgos y trabajo futuro

## Limitaciones
- **Pocos datos de una sola fuente.** Cuatro fotos por tipo de imagen. Se desconoce el desempeño con otras muestras, tinciones, microscopios o fotos comprimidas.
- **Validación débil.** Zonas de las mismas fotos; en campo claro solo 2 espermatozoides.
- **Conteos aproximados con células juntas.** La red puede repetir o partir contornos.
- **Sin ejemplos negativos.** Puede marcar sombras o manchas como espermatozoide (falso positivo o "alucinación"). Con una imagen que no es de espermatozoides, no hay garantía de que diga que no encontró nada.
- **Las micras dependen de la escala común** (60 px = 1 µm), que estandariza el tamaño de las imágenes. No es una calibración instrumental.
- **El "largo" no es la longitud de la curva.** Es el lado mayor del rectángulo mínimo del contorno, y el contorno incluye la cabeza y parte de la cola.
- **El histograma está en píxeles** aunque los datos principales se den en micras.
- **Un solo núcleo.** Los análisis simultáneos esperan turno. Tiempos en el VPS sin medir.
- **Sin GPU.** Cada foto tarda decenas de segundos.
- **El modelo no aprende de lo que suben los usuarios.**
- **No interpreta.** El sitio mide; la lectura científica es del grupo de investigación.

## Riesgos
- Un resultado numérico puede parecer más exacto de lo que es: conviene mencionar siempre la validación y la escala.
- Imágenes ajenas al entrenamiento pueden dar conteos sin sentido.

## Trabajo futuro
1. Medir tiempo y memoria en el VPS.
2. Reunir más imágenes, variadas y bien etiquetadas, y reentrenar; incluir ejemplos negativos (hígado, riñón u otras muestras sin espermatozoides).
3. Validar con fotos que la red no haya visto.
4. Medir de cabeza a cola.
5. Avisar si la imagen no parece de espermatozoides.
6. Posible cambio del largo a la longitud de la curva (decisión pendiente).
7. Comparación control contra tratamiento (posible extensión, fuera del alcance actual).

## Qué pasa si algo falla
- Si faltan los modelos: el sitio usa el umbral y avisa en rojo.
- Si no detecta nada: dice que no pudo analizar la imagen.
- Si el análisis tarda: es normal; el sitio lo avisa y no hay que cerrar la página.
