import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("clientes.xlsx")
#print(df.head())
#print(df.isnull().sum())

# Al ser sólo un valor nulo en la columna de 'NOMBRE', se sustituirá por 'NOMBRE DESCONOCIDO'
df["NOMBRE"] = df["NOMBRE"].fillna("NOMBRE DESCONOCIDO")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 15 valores nulos en la columna 'RFC', por lo que dichos valores nulos se deben sustituir por un RFC estándar
df["RFC"] = df["RFC"].fillna("XAXX010101000")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Convertir DataFrame a CSV
df.to_csv('clientes_limpio.csv')