# Claude Code en el Aula

Material para dar una clase completa de **Claude Code desde cero hasta nivel avanzado**, pensada para
estudiantes que quieren hacer su propio proyecto de machine learning y publicarlo en GitHub Pages.

- **`index.html`**: la clase. Una sola página con 8 bloques (≈ 3 h): qué es Claude Code y sus ventajas,
  instalación, tres formas de conectarlo a GitHub, atajos y comandos, modos de permiso, cómo escribir
  buenos prompts (con un constructor interactivo), CLAUDE.md, skills (crearlas, buscarlas e instalarlas),
  funciones avanzadas (subagentes, hooks, MCP, plugins, `claude -p`, sesiones en la nube), el proyecto
  guiado paso a paso con los prompts listos para copiar, despliegue en GitHub Pages, chuleta y test de
  autoevaluación. Incluye capturas ilustradas de cada paso y una demo de ML que funciona en el navegador.
- **`proyecto-ml/`**: el proyecto final resuelto (reconocedor de dígitos con scikit-learn), con su
  `CLAUDE.md`, dos skills, un subagente, permisos y una plantilla de workflow de GitHub Actions.
  Ver [proyecto-ml/README.md](proyecto-ml/README.md).

## Cómo usarla en clase

Abre `index.html` en el navegador. El botón **Modo presentación** amplía el texto, oculta las notas para
el docente y permite avanzar por bloques con las flechas ← →. El botón **Cambiar tema** alterna claro y
oscuro.

## Publicar esta clase en GitHub Pages

1. En el repositorio: **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
2. Elige la rama que contiene este `index.html` y la carpeta **/ (root)**, y pulsa **Save**.
3. En uno o dos minutos estará en `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`, con la demo del
   proyecto en `.../proyecto-ml/`.

El archivo `.nojekyll` hace que GitHub Pages sirva los archivos tal cual, sin procesarlos con Jekyll.

## Regenerar el modelo

```bash
cd proyecto-ml
pip install -r requirements.txt
python train.py && python -m pytest -q
```

Si reentrenas, copia el contenido de `proyecto-ml/model.json` dentro de
`<script type="application/json" id="model-data">` en `index.html` para que la demo de la portada use el
modelo nuevo.
