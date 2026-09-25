"""Construye las fuentes del paquete a partir de los TTF originales.

Dos recortes por fuente, como hace Google Fonts, para que el navegador descargue
el extendido solo cuando una página lo necesita:
  · latin      español, portugués, puntuación, flechas y signos matemáticos
  · latin-ext  lenguas indígenas y otras escritas en latín: vocales nasales
               (ẽ ĩ ũ ỹ), largas (ā ē ī ō ū), ɨ, diacríticos combinables

Andika se renombra «Dialegu Escolar»: la OFL reserva «Andika» para la fuente sin
modificar y el recorte es una modificación.

Uso: python scripts/fuentes.py <carpeta con los TTF originales>
Espera: Andika-400.ttf, Andika-700.ttf, Shantell-400.ttf, Shantell-600.ttf,
        Instrument-400.ttf, Instrument-600.ttf, Instrument-700.ttf,
        Fraunces-400.ttf, Fraunces-600.ttf
"""
import pathlib
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

sys.stdout.reconfigure(encoding='utf-8')
RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / 'fuentes'

RANGOS = {
    'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02D9-02DC,U+2000-206F,U+20AC,U+2122,'
             'U+2190-2199,U+2200-22FF,U+FEFF,U+FFFD',
    'latin-ext': 'U+0100-0130,U+0132-0151,U+0154-024F,U+0250-02AF,U+02B0-02BA,U+02BD-02C5,U+02C7-02D8,U+02DD-02FF,'
                 'U+0300-036F,U+1E00-1EFF,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF',
}
RASGOS = ['kern', 'liga', 'calt', 'tnum', 'lnum', 'pnum', 'ccmp', 'locl', 'mark', 'mkmk', 'rlig']

FUENTES = [
    # (archivo de origen, nombre de salida, renombrar)
    ('Andika-400', 'DialeguEscolar-400', True),
    ('Andika-700', 'DialeguEscolar-700', True),
    ('Shantell-400', 'Shantell-400', False),
    ('Shantell-600', 'Shantell-600', False),
    ('Instrument-400', 'Instrument-400', False),
    ('Instrument-600', 'Instrument-600', False),
    ('Instrument-700', 'Instrument-700', False),
    ('Fraunces-400', 'Fraunces-400', False),
    ('Fraunces-600', 'Fraunces-600', False),
]


def renombrar(fuente):
    nombres = fuente['name']
    for registro in list(nombres.names):
        if registro.nameID in (1, 3, 4, 6, 16, 17, 18, 21, 22, 25):
            texto = registro.toUnicode().replace('Andika', 'Dialegu Escolar').replace('SIL', '').replace('  ', ' ').strip()
            registro.string = texto.replace(' ', '') if registro.nameID == 6 else texto
    nombres.setName('Derivada de Andika (SIL International), recortada y renombrada por la cláusula de nombre '
                    'reservado de la OFL 1.1.', 10, 3, 1, 0x409)


def main(origen):
    origen = pathlib.Path(origen)
    for viejo in DESTINO.glob('*.woff2'):
        viejo.unlink()
    for archivo, salida, cambiar_nombre in FUENTES:
        for tramo, rango in RANGOS.items():
            opciones = subset.Options()
            opciones.flavor = 'woff2'
            opciones.layout_features = RASGOS
            opciones.name_IDs = ['*']
            opciones.name_languages = ['*']
            fuente = subset.load_font(str(origen / f'{archivo}.ttf'), opciones)
            if cambiar_nombre:
                renombrar(fuente)
            recorte = subset.Subsetter(opciones)
            recorte.populate(unicodes=subset.parse_unicodes(rango))
            recorte.subset(fuente)
            if len(fuente.getBestCmap() or {}) < 5:
                print(f'  (sin glifos en {tramo}) {salida}')
                continue
            destino = DESTINO / f'{salida}-{tramo}.woff2'
            subset.save_font(fuente, str(destino), opciones)
            print(f'  {destino.name:34} {destino.stat().st_size / 1024:6.1f} KB  {len(fuente.getBestCmap())} caracteres')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
