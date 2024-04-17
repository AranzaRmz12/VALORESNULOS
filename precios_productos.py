import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("precios_productos.xlsx")
#print(df.head())
#print(df.isnull().sum())

# Al ser sólo dos valores nulos en la columna de 'NOMBRE_VENDEDOR', decidí utilizar el backward fill para sustituir los 2 datos faltantes
df["NOMBRE_VENDEDOR"] = df["NOMBRE_VENDEDOR"].fillna("NOMBRE DESCONOCIDO")
valores_nulos = df.isnull().sum()
print(valores_nulos)