# 04 · Resultados, pruebas y datos reales

## Datos de entrenamiento
- Fluorescencia (fondo oscuro): 4 fotos y 258 espermatozoides etiquetados.
- Campo claro (fondo claro): 4 fotos y 45 espermatozoides etiquetados.
- Las etiquetas se hicieron a mano en CVAT. Los espermatozoides se anotan completos: cabeza y primer tramo de cola.

## Validación
Las métricas se calculan con IoU 0.5 y umbral de detección 0.5, sobre **zonas reservadas de las mismas fotos**, no sobre muestras independientes.

| Modelo | AP50 | Precisión | Recall | F1 | Espermatozoides en validación |
|---|---|---|---|---|---|
| Fluorescencia | 0.91 | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] | [COMPLETAR] |
| Campo claro | 1.00 | 1.00 | 1.00 | 1.00 | 2 |

- El 1.00 de campo claro **no prueba calidad**: solo hay 2 espermatozoides en la validación y el propio cuaderno avisa que es poco confiable. Con ese tamaño no se pudo elegir el umbral con la validación; se dejó en 0.5.
- En campo claro, la foto con más células tiene 38 etiquetados y la red detectó 42 (sobredetección leve). En las otras tres fotos los conteos coinciden: 1 y 1, 1 y 1, 5 y 5.

## Prueba de integración
El sitio da los mismos conteos que el cuaderno de Colab en cinco fotos: 114, 9, 2, 1 y 43. Esto comprueba que el sitio usa bien el modelo, no la calidad científica del modelo.

## Zonas amontonadas
En fluorescencia, donde las células están muy juntas, la red encuentra unos 85 de cada 100.

## Tiempos
- Computadora de escritorio de desarrollo: unos 40 s por foto de fluorescencia (1792 px) y de 10 a 20 s por foto de campo claro.
- VPS KVM 1: dato no disponible [COMPLETAR].
- Memoria usada en el VPS: dato no disponible [COMPLETAR].

## Pruebas automáticas
El proyecto tiene pruebas con `python -m pytest`. Resultado de la última corrida: [COMPLETAR].

## Costos (estimaciones, no verificadas)
VPS de 100 a 250 MXN al mes, dominio de 200 a 400 MXN al año, Colab unos 300 MXN. Precio real del KVM 1: [COMPLETAR].
