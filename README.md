# @dialegu/diseno

Sistema de diseño compartido de Dialegu para la web y plataforma (dialegu.com), Leer Dialegu (leer.dialegu.com) y Sistematízame (sistematiza.dialegu.com).

La norma, con sus motivos, está en `docs/SISTEMA-DISENO-DIALEGU.md` de Dialegu-Platform. Este paquete es su implementación. Toda decisión se justifica desde el viaje de la persona: llegar, entender, aportar, ver que llegó, leer a los demás y volver.

## Qué trae

| Archivo | Qué es |
|---|---|
| `fuentes/fuentes.css` + `*.woff2` | Fuentes autoalojadas, sin Google Fonts. Dos recortes por fuente: latino (siempre) y extendido (lenguas indígenas escritas en latín), que solo se descarga si la página lo usa |
| `nucleo/nucleo.css` | Tokens `--dlg-*`: papeles tipográficos, estados, foco, radios, área mínima; foco visible y movimiento reducido |
| `mesa/mesa.css` | Modo mesa: papel, cartulina Bristol de cuatro colores con su tinta, mesa de noche y los objetos para aportar (hoja, filtros, postit, aviso, muro tipo corcho, muro de aportes con `.muro` y `.nota`) |
| `catalogo/index.html` | El sistema funcionando, para revisar y decidir |

**Tipografía de diálogo:** en toda superficie donde se lee en común, se conversa o se cocrea, la interfaz usa **Dialegu Escolar** (la «a» escolar, cifras del mismo ancho) y lo que escribe una persona va en **Shantell Sans**, como una tarjeta de Metaplan. Una superficie de diálogo en español descarga unos 87 KB de fuentes.

## Cómo se instala

Como dependencia de Git con versión etiquetada. `npm` fija el commit exacto en `package-lock.json` y verifica su integridad.

```json
"dependencies": {
  "@dialegu/diseno": "github:Vialgusi/dialegu-diseno#semver:^0.7.0"
}
```

Para actualizar: `npm update @dialegu/diseno`.

## Cómo se usa

En el CSS de entrada (Vite resuelve y copia las fuentes):

```css
@import '@dialegu/diseno/fuentes.css';
@import '@dialegu/diseno/fuentes-leer.css'; /* solo Leer: EB Garamond */
@import '@dialegu/diseno/fuentes-sistematiza.css'; /* solo Sistematízame: Atkinson Hyperlegible */
@import '@dialegu/diseno/nucleo.css';
@import '@dialegu/diseno/mesa.css';   /* solo en rutas con superficie de diálogo */
@import './tema.css';                 /* los valores del tema del producto */
```

- La mesa se aplica con la clase `.mesa` en su contenedor, y `.mesa--noche` para proyectar en salas oscuras.
- Cada cartulina: `.cartulina--verde`, `--amarilla`, `--azul`, `--roja`. El significado de cada color lo decide el producto, y siempre va escrito.
- Tailwind v4: exponer los tokens en `@theme` apuntando a `var(--dlg-*)`. Tailwind v3: en `tailwind.config.js`, por ejemplo `colors: { dlg: { error: 'var(--dlg-error)' } }`.

**Símbolos que las fuentes no tienen:** «＋» ancho, ①, ❶, ℹ, ⟳. Se dibujan con otra fuente del sistema. Usar «+» común o íconos en SVG.

## Cómo se cambia

- Los archivos del paquete no se editan dentro de un producto. Lo propio va en el tema.
- `python scripts/verificar.py` comprueba contraste (día y noche) y peso. Corre en cada cambio en GitHub Actions.
- `python scripts/fuentes.py <carpeta con los TTF>` reconstruye las fuentes y sus recortes. `fuentes.css` se genera: no se edita a mano.
- Versiones: **mayor** si se renombra o retira un token o cambia un estado; **menor** si se agrega; **parche** si se corrige sin efecto. La etiqueta `vX.Y.Z` debe coincidir con `package.json`.

## Fuentes y licencias

Todas bajo SIL Open Font License 1.1 (`fuentes/licencias/`). **Dialegu Escolar** deriva de Andika (SIL International): la OFL reserva el nombre «Andika» para la fuente sin modificar y el recorte es una modificación, así que se renombró. Conserva el aviso de copyright y la licencia.
