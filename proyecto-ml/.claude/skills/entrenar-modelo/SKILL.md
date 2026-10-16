---
name: entrenar-modelo
description: Reentrena el reconocedor de dígitos, compara la precisión con la versión anterior y deja model.json listo para publicar. Úsala cuando se pida entrenar, reentrenar o probar otros hiperparámetros.
argument-hint: "[cambio a probar, p. ej. 'capa oculta de 128 neuronas']"
disable-model-invocation: true
allowed-tools: Bash(python train.py*) Bash(python -m pytest*) Read Edit
---

# Reentrenar el modelo

Cambio pedido: $ARGUMENTS

Sigue estos pasos en orden y no te saltes ninguno:

1. Lee la precisión actual con `python -c "import json; print(json.load(open('model.json'))['accuracy'])"` y apúntala.
2. Si hay un cambio pedido, aplícalo en `train.py` sin tocar el reparto train/test.
3. Ejecuta `python train.py` y guarda la matriz de confusión que imprime.
4. Ejecuta `python -m pytest -q`. Si falla, arregla la causa (nunca bajes el umbral del test).
5. Si cambió la arquitectura, actualiza `predict()` en `index.html` para que haga la misma cuenta.
6. Termina con una tabla breve:

| | Antes | Después |
|---|---|---|
| Precisión en test | … | … |
| Tamaño de model.json | … | … |
| Dígitos que más se confunden | … | … |

Si la precisión empeora, dilo claramente y propón deshacer el cambio.
