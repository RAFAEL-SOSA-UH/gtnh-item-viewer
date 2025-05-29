# NBTExplorer

## ¿Qué es?

[NBTExplorer](https://github.com/jaquadro/NBTExplorer) es una herramienta de escritorio para explorar y editar archivos `.dat` de Minecraft, los cuales están codificados en formato NBT (Named Binary Tag).

## Uso en este proyecto

Se usó para explorar:

- `saves/GregtechNewHorizons/level.dat`
- `saves/GregtechNewHorizons/playerdata/`
- `saves/GregtechNewHorizons/DIM*/`

## Hallazgos iniciales

- Los ítems del inventario del jugador están en `playerdata/[UUID].dat` bajo la etiqueta `Inventory`.
- Cada ítem tiene campos como `id`, `Count`, `Slot`, `tag` (si aplica).
- `level.dat` contiene información global como el nombre del mundo, tiempo, reglas, etc.
- No hay recetas directamente visibles aquí, pero podría rastrear ítems generados por mods.

## Próximos pasos

- Analizar si el inventario refleja correctamente ítems de GregTech.
- Ver si las máquinas o configuraciones de GregTech dejan huella NBT.

## Capturas o ejemplos

