"""Comprueba el sitio antes de publicarlo en GitHub Pages.

- La demo de la portada (index.html) usa exactamente el mismo modelo que proyecto-ml/model.json.
- Todos los enlaces y recursos relativos apuntan a archivos que existen.
- Todos los enlaces internos (#seccion) apuntan a un id que existe en la página.

Uso: python scripts/check_site.py   (sale con código 1 si encuentra algún problema)
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "404.html", "proyecto-ml/index.html"]
# En 404.html los enlaces son absolutos porque GitHub Pages la sirve desde cualquier ruta.
SITE_PREFIX = "/Claude_Code/"


def check_model(errors: list[str]) -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r'<script type="application/json" id="model-data">(.*?)</script>', html, re.S)
    if not match:
        errors.append("index.html: no se encuentra el bloque model-data")
        return
    inline = json.loads(match.group(1))
    saved = json.loads((ROOT / "proyecto-ml/model.json").read_text(encoding="utf-8"))
    if inline != saved:
        errors.append("index.html: el modelo de la portada no coincide con proyecto-ml/model.json")


def check_links(page: str, errors: list[str]) -> int:
    path = ROOT / page
    html = path.read_text(encoding="utf-8")
    ids = set(re.findall(r'\bid="([^"]+)"', html))
    scripts = "".join(re.findall(r"<script[^>]*>(.*?)</script>", html, re.S))
    targets = re.findall(r'\b(?:href|src)="([^"]+)"', html) + re.findall(r'fetch\("([^"]+)"\)', scripts)
    checked = 0
    for target in targets:
        url = urlparse(target)
        if url.scheme or target.startswith("//"):
            continue  # enlace externo o data:
        if target.startswith("#"):
            checked += 1
            if target[1:] and target[1:] not in ids:
                errors.append(f"{page}: el enlace {target} no apunta a ningún id")
            continue
        local = unquote(url.path)
        if local.startswith(SITE_PREFIX):
            resolved = ROOT / local[len(SITE_PREFIX):]
        else:
            resolved = (path.parent / local).resolve()
        if local.endswith("/") or resolved.is_dir():
            resolved = resolved / "index.html"
        checked += 1
        if not resolved.exists():
            errors.append(f"{page}: {target} no existe ({resolved.relative_to(ROOT)})")
    return checked


def main() -> None:
    errors: list[str] = []
    check_model(errors)
    total = sum(check_links(page, errors) for page in PAGES)
    if errors:
        print("Problemas encontrados:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    print(f"Sitio correcto: modelo sincronizado y {total} enlaces internos comprobados.")


if __name__ == "__main__":
    main()
