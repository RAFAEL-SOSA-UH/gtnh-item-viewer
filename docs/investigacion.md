# Investigación: Fuentes de datos en GregTech: New Horizons

## Objetivo

Encontrar dónde están almacenados los datos de los ítems y recetas.


## Archivos explorados


### Potencialmente relevantes

- `/config/`  
  Contiene muchos archivos `.json`, `.cfg`, `.bak`. Puede incluir configuraciones de mods como **Applied Energistics 2** y **GregTech**.  
  **Explorar más a fondo.**

- `/saves/`  
  Carpeta donde se guardan los mundos. Contiene subdirectorios y archivos `.dat` (por ejemplo, `level.dat`, `playerdata/`, `DIM*/`).  
  Podría contener información NBT relevante.

- `/scripts/`  
  Esta carpeta normalmente contiene archivos `.zs` de **CraftTweaker/MineTweaker**, donde pueden definirse recetas o modificaciones.  
  Actualmente aparece vacía, pero **debería haber contenido** si GTNH modificó recetas vía scripts. Tal vez están comprimidos o deshabilitados.

- `/mods/`  
  Contiene los `.jar` de cada mod. Se pueden abrir como `.zip` para explorar posibles recursos internos (`assets/modid/lang`, `recipes/`, etc).  
    Es una fuente más técnica, pero puede ser útil si se automatiza.

### 📁 Informativas o no prioritarias

- `/backups/`, `/screenshots/`, `/shaderpacks/`, `/texturepacks/`, `/fonts/`, `/logs/`, `/crash-reports/`  
  → No contienen información directa sobre ítems, solo metainformación o datos visuales.

- `/jorneymap/`, `/TCNodeTracker/`, `/visualprospecting/`  
  → Datos útiles para la experiencia del jugador (mapa, ores, nodos), pero **no contienen ítems ni recetas**.

- `/schematics/`, `/blueprints/`  
  → Solo relevantes si deseas reconstruir estructuras, no para visualización de ítems.


