"""Construye las fuentes del paquete a partir de los TTF originales.

Dos recortes por fuente, como hace Google Fonts, para que el navegador descargue
el extendido solo cuando una página lo necesita:
  · latin      español, portugués, puntuación, flechas y signos matemáticos
  · latin-ext  lenguas indígenas y otras escritas en latín: vocales nasales
               (ẽ ĩ ũ ỹ), largas (ā ē ī ō ū), ɨ, diacríticos combinables

Fuentes variables: Fraunces conserva el tamaño óptico (opsz 9–144) y el peso
(100–900), igual que la servía Google; SOFT y WONK se fijan en 0. EB Garamond
conserva el peso (400–800). Una sola cara cubre todos los pesos.

Andika se renombra «Dialegu Escolar»: la OFL reserva «Andika» para la fuente sin
modificar y el recorte es una modificación.

Uso: python scripts/fuentes.py <carpeta con los TTF originales>
Genera los .woff2, fuentes/fuentes.css (núcleo) y fuentes/fuentes-leer.css (tema
de Leer). Declarar una cara no cuesta: el navegador solo la descarga cuando
alguna letra de la página la usa.
"""
import pathlib
import sys

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / 'fuentes'

RANGOS = {
    'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02D9-02DC,U+2000-206F,U+20AC,U+2122,'
             'U+2190-2199,U+2200-22FF,U+FEFF,U+FFFD',
    'latin-ext': 'U+0100-0130,U+0132-0151,U+0154-024F,U+0250-02AF,U+02B0-02BA,U+02BD-02C5,U+02C7-02D8,U+02DD-02FF,'
                 'U+0300-036F,U+1E00-1EFF,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF',
}
RASGOS = ['kern', 'liga', 'calt', 'tnum', 'lnum', 'pnum', 'onum', 'ccmp', 'locl', 'mark', 'mkmk', 'rlig', 'rvrn']

# (grupo, archivo de origen, salida, familia, peso, estilo, renombrar, ejes fijos)
FUENTES = [
    ('nucleo', 'Andika-400', 'DialeguEscolar-400', 'Dialegu Escolar', '400', 'normal', True, None),
    ('nucleo', 'Andika-700', 'DialeguEscolar-700', 'Dialegu Escolar', '700', 'normal', True, None),
    ('nucleo', 'Shantell-400', 'Shantell-400', 'Shantell Sans', '400', 'normal', False, None),
    ('nucleo', 'Shantell-400i', 'Shantell-400i', 'Shantell Sans', '400', 'italic', False, None),
    ('nucleo', 'Shantell-500', 'Shantell-500', 'Shantell Sans', '500', 'normal', False, None),
    ('nucleo', 'Shantell-600', 'Shantell-600', 'Shantell Sans', '600', 'normal', False, None),
    ('nucleo', 'Instrument-400', 'Instrument-400', 'Instrument Sans', '400', 'normal', False, None),
    ('nucleo', 'Instrument-500', 'Instrument-500', 'Instrument Sans', '500', 'normal', False, None),
    ('nucleo', 'Instrument-600', 'Instrument-600', 'Instrument Sans', '600', 'normal', False, None),
    ('nucleo', 'Instrument-700', 'Instrument-700', 'Instrument Sans', '700', 'normal', False, None),
    ('nucleo', 'Fraunces-var', 'Fraunces-var', 'Fraunces', '100 900', 'normal', False, {'SOFT': 0, 'WONK': 0}),
    ('leer', 'EBGaramond-var', 'EBGaramond-var', 'EB Garamond', '400 800', 'normal', False, None),
    ('leer', 'EBGaramond-Italic-var', 'EBGaramond-italic-var', 'EB Garamond', '400 800', 'italic', False, None),
]

HOJAS = {'nucleo': 'fuentes.css', 'leer': 'fuentes-leer.css'}

COMENTARIOS = {
    'Dialegu Escolar': 'Diálogo: la «a» escolar en todo lo que se lee y se pulsa en una superficie\n'
                       '   de diálogo. Cifras del mismo ancho por defecto.',
    'Shantell Sans': 'Mano: lo que escribe una persona. Tarjetas de Metaplan, aportes, notas.\n'
                     '   Si le falta un glifo (por ejemplo la ɨ), lo dibuja Dialegu Escolar.',
    'Instrument Sans': 'Sitio: interfaz de las páginas institucionales y de producto.',
    'Fraunces': 'Títulos: la voz pública. Variable: tamaño óptico 9–144 y peso 100–900,\n'
                '   como la servía Google (SOFT y WONK en 0). `font-optical-sizing: auto` la ajusta\n'
                '   sola al tamaño del texto.',
    'EB Garamond': 'Lectura larga del tema de Leer: manifiestos y textos extensos. Variable,\n'
                   '   peso 400–800, redonda y cursiva.',
}

CABECERAS = {
    'nucleo': """/* Fuentes del sistema Dialegu, servidas desde el dominio de cada producto.
   Sin Google Fonts: ninguna visita envía datos a un tercero para leer una letra.
   Dos recortes por fuente con `unicode-range`: el latino se descarga siempre que
   se usa la fuente y el extendido (lenguas indígenas escritas en latín: ẽ ĩ ũ ỹ,
   ā ō, ɨ) solo cuando la página lo necesita. Cada cara se descarga solo si alguna
   letra la usa. Archivo generado por scripts/fuentes.py: no editar a mano.
   Licencias en ./licencias. «Dialegu Escolar» deriva de Andika (SIL International). */
""",
    'leer': """/* Fuentes propias del tema de Leer Dialegu. Se importa además de fuentes.css.
   Archivo generado por scripts/fuentes.py: no editar a mano. Licencias en ./licencias. */
""",
}


def renombrar(fuente):
    nombres = fuente['name']
    for registro in list(nombres.names):
        if registro.nameID in (1, 3, 4, 6, 16, 17, 18, 21, 22, 25):
            texto = registro.toUnicode().replace('Andika', 'Dialegu Escolar').replace('SIL', '').replace('  ', ' ').strip()
            registro.string = texto.replace(' ', '') if registro.nameID == 6 else texto
    nombres.setName('Derivada de Andika (SIL International), recortada y renombrada por la cláusula de nombre '
                    'reservado de la OFL 1.1.', 10, 3, 1, 0x409)


def escribir_css(generadas):
    for grupo, hoja in HOJAS.items():
        lineas = [CABECERAS[grupo]]
        familia_actual = None
        for g, familia, peso, estilo, archivo, tramo in generadas:
            if g != grupo:
                continue
            if familia != familia_actual:
                lineas.append(f"\n/* {COMENTARIOS[familia]} */")
                familia_actual = familia
            lineas.append(
                f"@font-face {{ font-family: '{familia}'; src: url('./{archivo}') format('woff2'); "
                f"font-weight: {peso}; font-style: {estilo}; font-display: swap; unicode-range: {RANGOS[tramo]}; }}"
            )
        (DESTINO / hoja).write_text('\n'.join(lineas) + '\n', encoding='utf-8', newline='\n')


def main(origen):
    origen = pathlib.Path(origen)
    for viejo in DESTINO.glob('*.woff2'):
        viejo.unlink()
    generadas = []
    for grupo, archivo, salida, familia, peso, estilo, cambiar_nombre, fijos in FUENTES:
        for tramo, rango in RANGOS.items():
            opciones = subset.Options()
            opciones.flavor = 'woff2'
            opciones.layout_features = RASGOS
            opciones.name_IDs = ['*']
            opciones.name_languages = ['*']
            fuente = TTFont(str(origen / f'{archivo}.ttf'))
            if cambiar_nombre:
                renombrar(fuente)
            recorte = subset.Subsetter(opciones)
            recorte.populate(unicodes=subset.parse_unicodes(rango))
            recorte.subset(fuente)
            # Fijar ejes después de recortar: al revés, el instanciador deja
            # referencias a glifos que el recorte ya quitó.
            if fijos:
                fuente = instancer.instantiateVariableFont(fuente, fijos)
            if len(fuente.getBestCmap() or {}) < 5:
                print(f'  (sin glifos en {tramo}) {salida}')
                continue
            destino = DESTINO / f'{salida}-{tramo}.woff2'
            fuente.flavor = 'woff2'
            fuente.save(str(destino))
            generadas.append((grupo, familia, peso, estilo, destino.name, tramo))
            ejes = ' · variable ' + ','.join(a.axisTag for a in fuente['fvar'].axes) if 'fvar' in fuente else ''
            print(f'  {destino.name:38} {destino.stat().st_size / 1024:6.1f} KB  {len(fuente.getBestCmap())} caracteres{ejes}')
    escribir_css(generadas)
    print(f'  {len(generadas)} caras en {", ".join(HOJAS.values())}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
