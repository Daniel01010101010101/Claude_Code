---
name: convenciones-ml
description: Buenas prácticas de machine learning para este proyecto (fuga de datos, métricas honestas, semillas, exportar modelos al navegador). Úsala al escribir o revisar código de entrenamiento, evaluación o exportación de modelos.
---

# Convenciones de ML

## Datos
- Separa train/test **antes** de cualquier transformación que aprenda de los datos (escalado, aumento, selección de variables).
- Usa `stratify=y` en clasificación para que todas las clases estén representadas en test.
- Documenta de dónde salen los datos y su licencia en el README.

## Evaluación
- Informa siempre de la métrica en el conjunto de test, nunca en el de entrenamiento.
- Además de la precisión, muestra la matriz de confusión: dice *qué* falla.
- Compara contra una referencia sencilla (por ejemplo, regresión logística) antes de complicar el modelo.

## Reproducibilidad
- Fija `random_state` en todo lo que tenga azar y guárdalo junto al modelo.
- Fija las versiones mínimas en `requirements.txt`.

## Exportar para la web
- Exporta solo los números necesarios (pesos y sesgos) en JSON, redondeados a 4 decimales.
- Mantén el JSON por debajo de 1 MB para que la página cargue rápido en GitHub Pages.
- La función de predicción en JavaScript debe reproducir exactamente la del test de Python.
