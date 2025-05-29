import nbtlib
import pandas as pd

def nbt_to_py(obj):
    from nbtlib import Compound, List
    from nbtlib.tag import IntArray
    
    if isinstance(obj, Compound):
        return {k: nbt_to_py(v) for k, v in obj.items()}
    elif isinstance(obj, List):
        return [nbt_to_py(v) for v in obj]
    elif isinstance(obj, IntArray):
        # IntArray es como una lista de enteros
        return list(obj)
    else:
        # Otros tipos NBT como Long, Short, Byte, Float son objetos que envuelven el valor
        # Intentamos obtener su valor interno
        try:
            return obj.py()  # nbtlib permite convertir con .py()
        except AttributeError:
            # Si no tiene método .py(), devolvemos el objeto tal cual
            return obj


# Ruta al archivo level.dat
path = "C:/Users/pinea/AppData/Roaming/PrismLauncher/instances/GT_New_Horizons_2.7.3(1)/.minecraft/saves/GregtechNewHorizons/level.dat"

nbt_file = nbtlib.load(path)

data = nbt_file['Data']  # Accedemos al Compound principal 'Data'

data_py = nbt_to_py(data)  # Convertimos todo a tipos Python "puros"


# Cada item es un diccionario, podemos convertirlos directo en DataFrame
df_items = pd.DataFrame(data_py)

print(df_items)