# Fichas de herramientas

Una misma herramienta vive en más de un producto del ecosistema: la mesa de Encuentros (dialegu.com), Sistematízame y Leer. Sin un lugar común, cada producto la mejora por su lado y la mejora no vuelve a los otros. El muro de presentación es el ejemplo: nació en la mesa de Encuentros, Sistematízame lo pasó al modo mesa y lo probó en producción (R15), y Encuentros siguió con el diseño anterior hasta que se portó.

Cada herramienta compartida tiene aquí **una ficha**. La norma general está en `docs/SISTEMA-DISENO-DIALEGU.md` de Web-Dialegu (§6.6, decisión R18); la ficha es su aplicación a una herramienta concreta.

| Herramienta | Ficha | Productos |
|---|---|---|
| Muro de presentación | [muro-presentacion.md](muro-presentacion.md) | Encuentros, Sistematízame |

Próximas fichas: muro de aportes (Encuentros, Sistematízame, Leer) y galería (Encuentros).

## Qué lleva una ficha

1. **Para qué sirve y en qué momento del viaje.** La persona antes que la interfaz.
2. **Quién hace qué:** quien participa, quien facilita y la proyección.
3. **Anatomía:** lo que se ve, en orden de lectura.
4. **Comportamientos comunes:** lo que toda implementación debe hacer. Es la parte normativa.
5. **Configuración:** lo que decide quien prepara.
6. **Tabla de paridad:** qué tiene hoy cada producto, verificado en el código y con la referencia.
7. **Brechas y siguiente paso.**
8. **Decisiones que la afectan** (R y D del registro).

## Cómo se mantiene

1. Quien cambia una herramienta en un producto actualiza su ficha en el mismo trabajo, o anota la brecha en la tabla de paridad.
2. Lo que ya se probó en un producto se trae a los otros desde la ficha; no se rediseña.
3. Cuando dos productos comparten el mismo aspecto, el objeto pasa al paquete (como `.muro` y `.nota` en la 0.7.0).
4. La tabla de paridad se verifica leyendo el código, no la documentación, y dice de qué rama y fecha sale.
