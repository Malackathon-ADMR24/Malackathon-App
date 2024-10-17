from difflib import get_close_matches

import pandas as pd

# Cargar los archivos CSV
listado_path = "listadoUTF8-3.csv"
embalses_path = "embalsesUTF8.csv"

# Leer ambos CSVs
listado = pd.read_csv(listado_path)
embalses = pd.read_csv(embalses_path)

# Analizar diferencias entre los valores de las columnas 'NOMBRE' del listado y 'EMBALSE_NOMBRE' de embalses
nombres_listado = listado['NOMBRE'].unique()
nombres_embalses = embalses['EMBALSE_NOMBRE'].unique()

# Ajustar el proceso para eliminar registros sin una coincidencia clara
# Consideraremos coincidencias si la similitud es alta (cutoff ajustado a 0.9 para mayor precisión)
nombre_map = {}
for nombre in nombres_listado:
    match = get_close_matches(nombre, nombres_embalses, n=1, cutoff=0.9)
    if match:
        nombre_map[nombre] = match[0]

# Crear la columna 'NOMBRE_NORMALIZADO' usando el mapeo encontrado
listado['NOMBRE_NORMALIZADO'] = listado['NOMBRE'].map(nombre_map)

# Eliminar las filas que no tienen un valor normalizado (es decir, sin correspondencia adecuada)
listado_limpio = listado.dropna(subset=['NOMBRE_NORMALIZADO'])

# Guardar el CSV limpio con los nombres normalizados
output_path = "listado_normalizado.csv"
listado_limpio.to_csv(output_path, index=False)

# Mostrar la cantidad de registros eliminados y los primeros registros del dataframe limpio
registros_eliminados = len(listado) - len(listado_limpio)
listado_limpio_preview = listado_limpio[['NOMBRE', 'NOMBRE_NORMALIZADO']].head(20)

print(f"Registros eliminados: {registros_eliminados}")
print(listado_limpio_preview)
print(f"Archivo guardado en: {output_path}")
