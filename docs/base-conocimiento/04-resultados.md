# 04 · Resultados, pruebas y datos reales

## Datos de entrenamiento
- Fluorescencia (fondo oscuro): 4 fotos y 258 espermatozoides etiquetados.
- Campo claro (fondo claro): 4 fotos y 45 espermatozoides etiquetados.
- Las etiquetas se hicieron a mano en CVAT. Los espermatozoides se anotan completos: cabeza y primer tramo de cola.

## Validación
Las métricas se calculan con IoU 0.5, sobre **zonas reservadas de las mismas fotos**, no sobre muestras independientes. En fluorescencia el umbral de detección es 0.8 (el que dio el mejor F1 en esa validación); en campo claro es 0.5.

| Modelo | AP50 | Precisión | Recall | F1 | Espermatozoides en validación |
|---|---|---|---|---|---|
| Fluorescencia | 0.888 | 0.843 | 0.894 | 0.868 | 66 |
| Campo claro | 1.00 | 1.00 | 1.00 | 1.00 | 2 |

- Fluorescencia: con 66 espermatozoides en la validación, la red marcó 70. De cada 100 marcas, unas 84 son correctas (precisión), y de cada 100 espermatozoides, encuentra unos 89 (recall). La mejor versión del modelo (época 20 de 60) y el umbral se eligieron con esa misma validación, así que las cifras son algo optimistas. En las zonas de validación la prueba con el umbral de 0.5 da precisión 0.80, recall 0.91 y 75 detectados.
- En fotos completas de fluorescencia (etiquetados contra detectados): 6 y 11, 10 y 16, 120 y 119, 122 y 119. En las dos fotos con pocas células la red marca de más; en las dos densas queda cerca, pero esas fotos incluyen zonas con las que se entrenó, así que no prueban calidad.
- El 1.00 de campo claro **no prueba calidad**: solo hay 2 espermatozoides en la validación y el propio cuaderno avisa que es poco confiable. Con ese tamaño no se pudo elegir el umbral con la validación; se dejó en 0.5.
- En campo claro, la foto con más células tiene 38 etiquetados y la red detectó 42 (sobredetección leve). En las otras tres fotos los conteos coinciden: 1 y 1, 1 y 1, 5 y 5.

## Prueba de integración
El sitio da los mismos conteos que el cuaderno de Colab en cinco fotos: 114, 9, 2, 1 y 43. Esto comprueba que el sitio usa bien el modelo, no la calidad científica del modelo. Esos conteos se midieron con la versión anterior del modelo de fluorescencia; con la nueva no se han repetido.

## Zonas amontonadas
En fluorescencia, donde las células están muy juntas, la red encuentra unos 89 de cada 100 (recall 0.894). Las zonas de validación de las fotos densas tienen entre 28 y 31 espermatozoides.

## Tiempos
- Computadora de escritorio de desarrollo: unos 40 s por foto de fluorescencia (1792 px) y de 10 a 20 s por foto de campo claro.
- CPU de Colab (referencia del cuaderno): unos 2.6 s por tesela de 512 px; una foto de fluorescencia de 1792 x 1374 usa 20 teselas, unos 0.9 min.
- VPS KVM 1: dato no disponible [COMPLETAR].
- Memoria usada en el VPS: dato no disponible [COMPLETAR].

## Pruebas automáticas
El proyecto tiene pruebas con `python -m pytest`. Última corrida: 33 pruebas, 32 pasaron y 1 se omitió (la que usa los modelos reales, que solo corre si están instalados PyTorch y los dos `.pt`). Tardó unos 29 segundos. Estas pruebas comprueban que el sitio funciona; no miden la calidad científica del modelo.

## Costos (estimaciones, no verificadas)
El costo es un dato secundario y no afecta al proyecto. VPS KVM 1: 2,520 pesos por 2 años (unos 105 pesos al mes). Dominio de 200 a 400 MXN al año y Colab unos 300 MXN (estimaciones, no verificadas).
