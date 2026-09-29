# Muro de presentación

> Ficha de herramienta · revisión 1 · 29-09-2026
> Productos: mesa de Encuentros (dialegu.com) y Sistematízame. Leer no la tiene.
> Decisiones: R1, R2, R7, R15 (resuelve D20), R18. Ver `docs/SISTEMA-DISENO-DIALEGU.md` de Web-Dialegu.

## 1. Para qué sirve

Es el primer gesto de un grupo que va a trabajar junto: cada persona dice quién es, desde dónde llega y qué espera. Al ver las tarjetas juntas, el grupo toma rostro.

**Momento del viaje:** llegar y reconocerse, antes de aportar. Por eso la tarjeta es cálida, se lee de un vistazo y ninguna tarjeta tapa a las demás.

## 2. Quién hace qué

| Rol | Qué hace |
|---|---|
| Quien participa | Pone su tarjeta (foto opcional), la edita y la retira. Lee las de las demás, busca y ordena |
| Quien facilita | Prepara el muro, lo proyecta y cuida lo que se muestra |
| Proyección | Muestra solo las tarjetas, con letra y fotos para leer a distancia |

## 3. Anatomía de la tarjeta

En orden de lectura:

1. **Franja de cartulina** arriba (amarilla, verde, azul, roja, en ese orden). Da color y ritmo, no significado.
2. **Foto pegada como polaroid**: marco blanco, leve giro, entera y sin recortar, con **altura máxima**. Casi todas las fotos son verticales, de celular; sin tope, una tarjeta medía más de una pantalla.
3. **Sin foto**: la inicial a mano sobre la cartulina. Nunca un hueco vacío ni un círculo gris.
4. **Nombre** a mano.
5. **Datos breves** (rol, lugar). El rol va como un trocito de cartulina.
6. **Lo que la persona escribe**, a mano. Si la herramienta pregunta varias cosas, la pregunta va pequeña y en minúsculas: en versales competía con la respuesta en cada tarjeta.
7. **«Leer completo»** cuando algo se corta.
8. **Marca propia**: «Tu tarjeta» o «Mi tarjeta».

Material: papel de la mesa, esquinas de papel asimétricas, sombras de tinta y relato, giro pequeño que se endereza al señalar (§6.4 de la norma).

## 4. Comportamientos comunes (norma)

| Comportamiento | Qué debe pasar | Por qué |
|---|---|---|
| **Foto** | Entera, sin recortar, altura máxima de 17rem (21rem al proyectar, menos en el teléfono) | Que la cara se vea sin que una tarjeta domine el muro |
| **Leer completo** | Los textos se pliegan a cuatro líneas. El botón aparece solo si el texto **de verdad se corta**, midiendo, no contando caracteres | Proteger la composición sin esconder nada |
| **Buscar** | Ignora tildes y mayúsculas y recorre nombre, datos y respuestas. Si nada coincide, lo dice | Ubicar a alguien por municipio, rol o institución |
| **Ordenar** | Endereza las tarjetas para leerlas de corrido | Leer muchas tarjetas seguidas cansa menos sin giro |
| **Proyectar** | Solo las tarjetas: sin buscador, sin tarjeta para añadir y sin acciones. Letra y fotos más grandes | Lo que ve el salón es el grupo, no la interfaz |
| **Añadir** | Una tarjeta punteada «por llenar» mientras la persona no tiene la suya. Se oculta al buscar y al proyectar | Invita sin parecer la tarjeta de alguien |
| **Actualización** | Las tarjetas nuevas llegan solas, sin interrumpir a quien está llenando el formulario o subiendo la foto | La foto tarda; recargar a mitad la perdería |
| **Privacidad** | Quien elige no mostrar su nombre aparece como «Una persona del grupo». Retirar u ocultar se ve en el muro al momento | La persona decide qué muestra |
| **Foto en proceso** | La tarjeta queda guardada y dice que la foto aparecerá. Pasados dos minutos, lo dice y ofrece otra salida | No prometer lo que no llega |

## 5. Configuración

| Qué | Encuentros | Sistematízame |
|---|---|---|
| Preguntas | De 1 a 4, libres, con su etiqueta | Fijas: quién eres, rol, desde dónde llegas, qué esperas |
| Foto obligatoria | Opcional por muro (`require_photo`) | Opcional |
| Permitir editar | Por muro (`allow_edits`) | Cada persona edita la suya; no es configurable |

## 6. Tabla de paridad

Verificada en el código el 29-09-2026: Encuentros en `develop` más Vialgusi/Web-Dialegu#158 (abierto); Sistematízame en `main` (`resources/views/spaces/espacio-muro.blade.php`, `resources/js/muro-mesa.js`, `EspacioMuro.php`).

| Comportamiento | Encuentros | Sistematízame | Leer |
|---|---|---|---|
| Hoja con franja de cartulina | ✓ #158 | ✓ | — |
| Foto polaroid con altura máxima | ✓ #158 (17 / 21 / 14rem) | ✓ (17 / 21rem) | — |
| Inicial sobre cartulina sin foto | ✓ #158 | ✓ | — |
| Nombre y respuestas a mano | ✓ #158 | ✓ (nombre y expectativa) | — |
| Rol como trocito de cartulina | ✗ Las preguntas son libres: no sabe cuál es el rol | ✓ | — |
| «Leer completo» medido | ✓ #158 | ✓ | — |
| Buscar sin tildes | ✓ #158 | ✓ | — |
| Ordenar | ✓ #158 | ✓ | — |
| Agrupar por municipio o rol | ✗ | ✗ | — |
| Proyectar solo tarjetas | ✓ #158 («Pantalla completa» y proyección clásica) | ✓ (Proyectar, solo quien facilita) | — |
| Mesa de noche | ✗ | ✓ | — |
| Tarjeta para añadir | ✓ punteada, al inicio | ✓ «Poner mi tarjeta», al final | — |
| Actualización automática | ✓ cada 5 s (mesa completa) | ✓ cada 30 s, pausada con el formulario abierto | — |
| Retirar la propia tarjeta | Borra la tarjeta y su foto | Oculta; se puede volver a mostrar | — |
| Quien facilita oculta una tarjeta | ✗ No encontrado en el código | ✓ Ocultar, con confirmación | — |
| Nombre oculto | ✓ «Una persona del grupo» | Nombre o correo de la cuenta | — |
| Foto en proceso con aviso a los dos minutos | ✓ | Sin verificar | — |
| Proyección viva | Muestra la llegada de cada persona (nombre sobre el paisaje), no la tarjeta | — | — |

✓ lo tiene · ✗ no lo tiene · — no aplica

## 7. Brechas y siguiente paso

1. **Rol y lugar en Encuentros.** Permitir marcar en la configuración qué pregunta es el rol y cuál el lugar, o que la respuesta sea una opción de una lista. Con eso: el rol como trocito de cartulina y **«Agrupar por»** rol o municipio, que hoy no tiene ningún producto.
2. **Retirar y ocultar.** Encuentros borra la tarjeta de forma permanente; Sistematízame la oculta y permite volver a mostrarla, como decidió R13 para los aportes. Conviene llevar a Encuentros el ocultar reversible y la moderación de quien facilita.
3. **Mesa de noche en Encuentros**, para salas oscuras.
4. **Objeto en el paquete.** Los dos productos ya comparten el aspecto: `.tarjeta-presentacion` puede pasar a `mesa/mesa.css`, como `.muro` y `.nota` en la 0.7.0. Así la próxima mejora llega a los dos a la vez.
5. **Datos de ejemplo para revisar.** Encuentros tiene un sembrador local de diez tarjetas con fotos de proporciones distintas (`videos-dialegu/piezas/mesa/herramientas/sembrar_presentacion.php`). Conviene uno igual en Sistematízame para revisar con los mismos casos.

## 8. Historial

| Fecha | Cambio |
|---|---|
| 25-09-2026 | Sistematízame pasa el muro al modo mesa (R15, Vialgusi/Sistematizame-Platform#20) y ajusta fotos verticales y textos largos |
| 29-09-2026 | Encuentros trae el mismo diseño, con búsqueda, «Ordenar» y «Leer completo» medido (Vialgusi/Web-Dialegu#158). Primera versión de esta ficha |
