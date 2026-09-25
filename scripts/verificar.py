"""Verifica que el paquete cumpla lo que el documento promete.

Lee los valores reales de nucleo.css y mesa.css (no una copia) y comprueba:
  · contraste de cada par autorizado (texto ≥ 4,5 · foco y gráficos ≥ 3),
    de día y en la mesa de noche
  · peso de cada archivo frente a su presupuesto
Sale con código 1 si algo falla, para usarlo en CI.
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = pathlib.Path(__file__).resolve().parent.parent


def bloque(css, selector):
    m = re.search(re.escape(selector) + r'\s*\{(.*?)\n\}', css, re.S)
    return dict(re.findall(r'(--[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})', m.group(1))) if m else {}


def tokens():
    nucleo = (RAIZ / 'nucleo/nucleo.css').read_text(encoding='utf-8')
    mesa = (RAIZ / 'mesa/mesa.css').read_text(encoding='utf-8')
    dia = {**bloque(nucleo, ':root'), **bloque(mesa, ':root'), '#FFFFFF': '#FFFFFF'}
    noche = {**dia, **bloque(mesa, '.mesa--noche')}
    return dia, noche


def luminancia(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def contraste(a, b):
    x, y = luminancia(a), luminancia(b)
    return (max(x, y) + .05) / (min(x, y) + .05)


# (primer plano, fondo, mínimo, qué es)
PARES_DIA = [
    ('--mesa-verde-tinta', '--mesa-verde', 4.5, 'texto en cartulina verde'),
    ('--mesa-amarilla-tinta', '--mesa-amarilla', 4.5, 'texto en cartulina amarilla'),
    ('--mesa-azul-tinta', '--mesa-azul', 4.5, 'texto en cartulina azul'),
    ('--mesa-roja-tinta', '--mesa-roja', 4.5, 'texto en cartulina roja'),
    ('--mesa-tinta', '--mesa-papel', 4.5, 'texto sobre papel'),
    ('--mesa-tinta', '--mesa-hoja', 4.5, 'texto sobre hoja'),
    ('--mesa-tinta-suave', '--mesa-papel', 4.5, 'rótulo sobre papel'),
    ('--dlg-error', '--dlg-error-fondo', 4.5, 'error sobre su fondo'),
    ('--dlg-aviso', '--dlg-aviso-fondo', 4.5, 'aviso sobre su fondo'),
    ('--dlg-exito', '--dlg-exito-fondo', 4.5, 'éxito sobre su fondo'),
    ('--dlg-info', '--dlg-info-fondo', 4.5, 'información sobre su fondo'),
    ('--dlg-accion-texto', '--dlg-accion', 4.5, 'texto del botón de acción'),
    ('--mesa-foco', '--mesa-verde', 3, 'foco sobre cartulina verde'),
    ('--mesa-foco', '--mesa-amarilla', 3, 'foco sobre cartulina amarilla'),
    ('--mesa-foco', '--mesa-azul', 3, 'foco sobre cartulina azul'),
    ('--mesa-foco', '--mesa-roja', 3, 'foco sobre cartulina roja'),
    ('--mesa-foco', '--mesa-papel', 3, 'foco sobre papel'),
    ('--dlg-foco-sobre-oscuro', '--mesa-tinta', 3, 'foco blanco sobre tinta'),
    ('--dlg-foco-sobre-oscuro', '--dlg-accion', 3, 'foco blanco dentro del botón de acción'),
]
PARES_NOCHE = [
    ('--mesa-tinta', '--mesa-papel', 4.5, 'noche: texto sobre la mesa'),
    ('--mesa-tinta', '--mesa-hoja', 4.5, 'noche: texto sobre hoja'),
    ('--mesa-tinta-suave', '--mesa-papel', 4.5, 'noche: rótulo sobre la mesa'),
    ('--mesa-foco', '--mesa-papel', 3, 'noche: foco sobre la mesa'),
    ('--mesa-foco', '--mesa-hoja', 3, 'noche: foco sobre hoja'),
    ('--mesa-verde-tinta', '--mesa-verde', 4.5, 'noche: la cartulina conserva su tinta'),
]

PRESUPUESTOS = {
    'nucleo/nucleo.css': 6_000,
    'mesa/mesa.css': 16_500,
    'fuentes/fuentes.css': 12_000,
}
PRESUPUESTO_FUENTE = {'latin': 48_000, 'latin-ext': 72_000}


def main():
    dia, noche = tokens()
    fallas = 0
    print('Contraste')
    for valores, pares in ((dia, PARES_DIA), (noche, PARES_NOCHE)):
        for a, b, minimo, que in pares:
            va, vb = valores.get(a), valores.get(b)
            if not va or not vb:
                print(f'  FALTA  {que}: {a if not va else b} no está definido')
                fallas += 1
                continue
            r = contraste(va, vb)
            ok = r >= minimo
            fallas += not ok
            print(f"  {'ok   ' if ok else 'FALLA'}  {r:5.2f} ≥ {minimo:<3}  {que}")
    print('Peso')
    archivos = dict(PRESUPUESTOS)
    for fuente in sorted((RAIZ / 'fuentes').glob('*.woff2')):
        tramo = 'latin-ext' if fuente.stem.endswith('latin-ext') else 'latin'
        archivos[f'fuentes/{fuente.name}'] = PRESUPUESTO_FUENTE[tramo]
    for ruta, limite in archivos.items():
        peso = (RAIZ / ruta).stat().st_size
        ok = peso <= limite
        fallas += not ok
        print(f"  {'ok   ' if ok else 'FALLA'}  {peso / 1024:6.1f} KB ≤ {limite / 1024:5.1f} KB  {ruta}")
    print('Resultado:', 'todo cumple' if not fallas else f'{fallas} fallas')
    sys.exit(1 if fallas else 0)


if __name__ == '__main__':
    main()
