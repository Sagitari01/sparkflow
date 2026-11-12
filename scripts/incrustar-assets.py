#!/usr/bin/env python3
"""Incrusta las imágenes y la fuente del tema de oficina dentro de index.html.

El juego se distribuye como un único archivo (se puede descargar index.html y
abrirlo sin conexión), así que el tema no puede depender de la carpeta assets/.
Este script convierte los recursos en data URIs y reescribe el bloque marcado
entre INICIO y FIN. Ese bloque no se edita a mano: si cambia una imagen, se
vuelve a ejecutar:

    python3 scripts/incrustar-assets.py
"""
import base64
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
INDEX = RAIZ / "index.html"
INICIO = "<!-- sparkflow-assets:inicio (generado por scripts/incrustar-assets.py; no editar a mano) -->"
FIN = "<!-- sparkflow-assets:fin -->"

# nombre de la variable CSS -> archivo
IMAGENES = {
    "--img-oficina": "assets/oficina/fondos/oficina-dia.webp",
    "--img-coordinadora": "assets/oficina/personajes/coordinadora-retrato.png",
    "--img-operador": "assets/oficina/personajes/operador-retrato.png",
    "--img-coordinadora-caminar": "assets/oficina/personajes/animacion/coordinadora-caminar.png",
    "--img-operador-caminar": "assets/oficina/personajes/animacion/operador-caminar.png",
    "--img-coordinadora-celebrar": "assets/oficina/personajes/animacion/coordinadora-celebrar.png",
    "--img-operador-celebrar": "assets/oficina/personajes/animacion/operador-celebrar.png",
    "--img-escritorio": "assets/oficina/items/escritorio.webp",
    "--img-silla": "assets/oficina/items/silla.webp",
    "--img-planta": "assets/oficina/items/planta.webp",
    "--img-cafe": "assets/oficina/items/cafe.webp",
    "--img-archivador": "assets/oficina/items/archivador.webp",
}
# familia -> (archivo, rango de pesos)
FUENTES = {
    "Pixelify Sans": ("assets/fuentes/PixelifySans-latin.woff2", "400 700"),  # solo el letrero SPARKFLOW
    "Fredoka": ("assets/fuentes/Fredoka-latin.woff2", "500 700"),  # títulos
}
MIME = {".webp": "image/webp", ".png": "image/png", ".woff2": "font/woff2"}


def data_uri(ruta: str) -> str:
    archivo = RAIZ / ruta
    datos = base64.b64encode(archivo.read_bytes()).decode("ascii")
    return f"data:{MIME[archivo.suffix]};base64,{datos}"


def bloque() -> str:
    variables = "".join(f"{nombre}:url({data_uri(ruta)});" for nombre, ruta in IMAGENES.items())
    fuente = "".join(
        f"@font-face{{font-family:'{familia}';font-style:normal;font-weight:{pesos};"
        f"font-display:swap;src:url({data_uri(ruta)}) format('woff2')}}"
        for familia, (ruta, pesos) in FUENTES.items()
    )
    return f'{INICIO}\n<style id="sparkflow-assets">\n{fuente}\n:root{{{variables}}}\n</style>\n{FIN}'


def main() -> int:
    html = INDEX.read_text(encoding="utf-8")
    patron = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIN), re.S)
    if not patron.search(html):
        print("No encontré los marcadores sparkflow-assets en index.html", file=sys.stderr)
        return 1
    nuevo = patron.sub(lambda _: bloque(), html, count=1)
    INDEX.write_text(nuevo, encoding="utf-8")
    print(f"index.html actualizado: {len(nuevo.encode('utf-8')) / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
