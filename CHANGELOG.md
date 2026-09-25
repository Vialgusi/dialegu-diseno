# Cambios

## 0.4.0 · 25-09-2026

- **Dialegu Escolar adoptada** como fuente de diálogo en todas las superficies de diálogo (decisión D12).
- **Cartulina de cuatro colores adoptada** con su tinta (decisión D3).
- Fuentes en dos recortes con `unicode-range`: latino (siempre) y extendido (lenguas indígenas escritas en latín: ẽ ĩ ũ ỹ, ā ō, ɨ), que solo se descarga cuando la página lo usa. Agrega signos matemáticos (≥ ≤ ≠ ∞ √).
- La mano cae en Dialegu Escolar cuando a Shantell le falta un glifo (por ejemplo la ɨ), así se conserva la «a» escolar.
- Mesa de noche (`.mesa--noche`) para proyectar en salas oscuras, con foco claro. Las cartulinas conservan su color y su tinta.
- Token `--mesa-foco`, separado de la tinta.
- Integración continua: contraste y peso en cada cambio, y comprobación de que la etiqueta coincide con la versión.

## 0.3.0 · 25-09-2026 · propuesta

- Primera versión del paquete: fuentes autoalojadas, núcleo, modo mesa y catálogo vivo.
