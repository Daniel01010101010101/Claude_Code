# Claude Code en el Aula

**🌐 Ver la clase: https://daniel01010101010101.github.io/Claude_Code/**
· Demo del proyecto: https://daniel01010101010101.github.io/Claude_Code/proyecto-ml/

Material para dar una clase completa de **Claude Code desde cero hasta nivel avanzado**, pensada para
estudiantes que quieren hacer su propio proyecto de machine learning y publicarlo en GitHub Pages.

- **`index.html`**: la clase. Una sola página con 8 bloques (≈ 3 h), toda desde la app de Claude o
  claude.ai/code, sin instalar nada: qué es Claude Code, primera sesión, la interfaz parte por parte, los
  modelos y el nivel de esfuerzo, entornos en la nube conectados a GitHub (red, script de configuración,
  ramas y pull requests), modos de permiso y prompts (con un constructor interactivo), CLAUDE.md, skills,
  funciones avanzadas, el proyecto guiado con los prompts listos para copiar, despliegue en GitHub Pages,
  chuleta y test de autoevaluación. Incluye ilustraciones de cada paso y una demo de ML en el navegador.
- **`proyecto-ml/`**: el proyecto final resuelto (reconocedor de dígitos con scikit-learn), con su
  `CLAUDE.md`, dos skills, un subagente, permisos y una plantilla de workflow de GitHub Actions.
  Ver [proyecto-ml/README.md](proyecto-ml/README.md).

## Cómo usarla en clase

Abre `index.html` en el navegador. El botón **Modo presentación** amplía el texto, oculta las notas para
el docente y permite avanzar por bloques con las flechas ← →. El botón **Cambiar tema** alterna claro y
oscuro.

## Cómo se publica

El workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) publica el sitio en cada push a la
rama principal del repositorio. Antes de publicar pasa los tests del modelo y ejecuta
[`scripts/check_site.py`](scripts/check_site.py), que comprueba que la demo de la portada usa el mismo
modelo que `proyecto-ml/model.json` y que no hay enlaces rotos. Si algo falla, no se publica y la versión
anterior sigue en línea.

Configuración necesaria (una sola vez): **Settings → Pages → Build and deployment → Source: GitHub Actions**.

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La clase |
| `404.html` | Página para enlaces que no existen |
| `og.png` | Imagen de vista previa al compartir el enlace (WhatsApp, Teams, redes) |
| `.nojekyll` | Sirve los archivos tal cual, sin procesarlos con Jekyll |
| `proyecto-ml/` | Proyecto de ejemplo y su demo |

## Regenerar el modelo

```bash
cd proyecto-ml
pip install -r requirements.txt
python train.py && python -m pytest -q
```

Si reentrenas, copia el contenido de `proyecto-ml/model.json` dentro de
`<script type="application/json" id="model-data">` en `index.html` para que la demo de la portada use el
modelo nuevo. `python scripts/check_site.py` te avisa si se te olvida.
