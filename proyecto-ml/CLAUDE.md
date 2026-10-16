# Reconocedor de dígitos

Demo de machine learning que se publica en GitHub Pages. Se entrena en Python
y la predicción se hace en el navegador con los pesos exportados a JSON.

## Comandos
- Instalar: `pip install -r requirements.txt`
- Entrenar y exportar: `python train.py` (escribe `model.json`)
- Tests: `python -m pytest -q` (deben pasar antes de dar algo por terminado)
- Probar la web en local: `python -m http.server 8000` y abrir http://localhost:8000

## Reglas del proyecto
- `index.html` es estático: sin frameworks, sin build y sin servidor. Todo debe funcionar en GitHub Pages.
- El JavaScript de `index.html` debe hacer exactamente la misma cuenta que `forward()` en `tests/test_model.py`.
- `model.json` debe pesar menos de 1 MB. Si cambias la arquitectura, actualiza también el JS y los tests.
- Nunca evalúes con datos usados en el entrenamiento. El aumento de datos solo se aplica al conjunto de train.
- Semillas fijas (`--seed`) para que los resultados sean reproducibles.
- Escribe comentarios y textos de la interfaz en español.

## Flujo de trabajo
1. Para cambios grandes, empieza en modo plan y espera mi aprobación.
2. Después de cambiar el entrenamiento: `python train.py` y `python -m pytest -q`.
3. Commits pequeños con mensajes en español que expliquen el porqué.
