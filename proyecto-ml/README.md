# Reconocedor de dígitos · proyecto de ejemplo

Proyecto final de la clase **Claude Code en el Aula**. Dibujas un número del 0 al 9 y una red neuronal
entrenada en Python lo reconoce en el navegador. No hay servidor: todo funciona en GitHub Pages.

| Archivo | Para qué sirve |
|---|---|
| `train.py` | Entrena el modelo (scikit-learn, dataset `digits`) y escribe `model.json` |
| `model.json` | Pesos de la red neuronal (64 → 64 → 10), unos 35 KB |
| `index.html` | La web: lienzo para dibujar + predicción en JavaScript |
| `tests/test_model.py` | Comprueba la forma del modelo y que la precisión en test sea ≥ 93 % |
| `CLAUDE.md` | Memoria del proyecto para Claude Code: comandos y reglas |
| `.claude/skills/entrenar-modelo/` | Skill manual: `/entrenar-modelo <cambio a probar>` |
| `.claude/skills/convenciones-ml/` | Skill automática con buenas prácticas de ML |
| `.claude/agents/revisor-ml.md` | Subagente que revisa fugas de datos y métricas |
| `.claude/settings.json` | Permisos: comandos permitidos sin preguntar y archivos prohibidos |
| `github-actions/deploy-pages.yml` | Plantilla de workflow: entrena, testea y publica en Pages |

## Probarlo en tu ordenador

```bash
pip install -r requirements.txt
python train.py           # entrena y escribe model.json
python -m pytest -q       # 3 tests en verde
python -m http.server 8000
# abre http://localhost:8000
```

## Publicarlo en GitHub Pages (en tu propio repositorio)

1. Copia esta carpeta a un repositorio nuevo (los archivos en la raíz).
2. Mueve `github-actions/deploy-pages.yml` a `.github/workflows/deploy-pages.yml`.
3. En GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Haz push a `main`. En la pestaña **Actions** verás el workflow; al terminar, tu web estará en
   `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`.

Datos: [dataset digits de scikit-learn](https://scikit-learn.org/stable/datasets/toy_dataset.html#optical-recognition-of-handwritten-digits-dataset)
(copia del conjunto UCI *Optical Recognition of Handwritten Digits*).
