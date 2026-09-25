"""Genera catalogo/catalogo-autonomo.html: el catálogo en un solo archivo,
con el CSS y las fuentes incrustados, para compartirlo sin servidor."""
import base64
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def fuentes_incrustadas():
    css = (RAIZ / 'fuentes/fuentes.css').read_text(encoding='utf-8')

    def a_datos(m):
        datos = base64.b64encode((RAIZ / 'fuentes' / m.group(1)).read_bytes()).decode()
        return f"url('data:font/woff2;base64,{datos}')"

    return re.sub(r"url\('\./([^']+\.woff2)'\)", a_datos, css)


def main():
    html = (RAIZ / 'catalogo/index.html').read_text(encoding='utf-8')
    bloques = {
        '../fuentes/fuentes.css': fuentes_incrustadas(),
        '../nucleo/nucleo.css': (RAIZ / 'nucleo/nucleo.css').read_text(encoding='utf-8'),
        '../mesa/mesa.css': (RAIZ / 'mesa/mesa.css').read_text(encoding='utf-8'),
    }
    for ruta, css in bloques.items():
        html = html.replace(f'<link rel="stylesheet" href="{ruta}">', f'<style>\n{css}\n</style>')
    destino = RAIZ / 'catalogo/catalogo-autonomo.html'
    destino.write_text(html, encoding='utf-8')
    print(f'{destino.relative_to(RAIZ)} · {destino.stat().st_size / 1024:.0f} KB')


if __name__ == '__main__':
    main()
