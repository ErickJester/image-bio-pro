# 03 · Decisiones técnicas y alternativas descartadas

## La red localiza, el código mide
La red solo traza el contorno de cada espermatozoide. Área y largo se calculan con código determinista, así que cualquier medida se puede verificar sin abrir la red.

## Mask R-CNN y no YOLO
YOLO se descartó por su licencia AGPL-3.0, que obliga a publicar el código de todo el sitio. Mask R-CNN (torchvision) tiene licencia BSD. Además traza contornos exactos, que es lo que se necesita para medir.

## Transfer learning
Hay pocas imágenes, así que no se entrena desde cero: se parte de una red preentrenada y se ajusta con las fotos propias.

## Un umbral simple no bastaba
Colas y manchas también brillan, las células encimadas se funden en una sola mancha y el brillo cambia con la iluminación de cada foto. Por eso el umbral quedó solo como respaldo.

## Dos modelos en lugar de uno
Con pocos datos funcionó mejor un modelo por tipo de fondo (oscuro y claro). La elección entre ambos la hace una regla de brillo, no una red.

## Plataforma web y no solo el cuaderno de Colab
El archivo `.pt` del modelo no hace nada por sí solo. La plataforma permite que cualquier persona lo use sin programar, con cuenta, historial y reportes.

## VPS y no hosting compartido
Un hosting compartido no corre Flask con PyTorch. Se eligió un VPS de Hostinger, plan KVM 1.

## Inferencia en CPU
Se evita la GPU para mantener bajo el costo. A cambio, cada foto tarda decenas de segundos.

## Un proceso y análisis de uno en uno
Cada modelo pesa unos 176 MB; varios procesos los duplicarían en memoria y el plan tiene un solo núcleo. Si dos personas analizan a la vez, una espera su turno.

## Flask y SQLite, por ligereza
Flask es un framework pequeño y corre en el mismo proceso de Python que el modelo. SQLite es un solo archivo, sin servidor de base de datos que instalar, y alcanza para un grupo de investigación.

## Sin parámetros ajustables
El usuario no mueve umbrales ni sensibilidad: la misma imagen siempre da el mismo resultado.

## Imágenes subidas se borran
Las fotos pesan mucho y cuestan espacio. Se guardan el PDF y una copia reducida marcada.

## Escala común
Para estandarizar el tamaño de las imágenes se usa la misma escala en todas (60 px = 1 µm) y cada resultado la declara. No se presenta como calibración exacta.

## Cuentas privadas
El análisis requiere cuenta (gratis, con correo). Cada persona ve solo sus análisis.
