import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("facturacion.xlsx")
#print(df.head())
#print(df.isnull().sum())

# Para "CVE_VEND" decidí rellenar los valores nulos con la mediana
# Esto para poder mantener dichos datos con el valor central de los datos ya incluidos
df["CVE_VEND"] = df["CVE_VEND"].fillna(round(df["CVE_VEND"].median(), 1))
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 2 valores nulos en la columna 'FECHA_ENTREGA', por lo que dichos valores nulos se deben sustituir por un "No entregado"
df["FECHA_ENTREGA"] = df["FECHA_ENTREGA"].fillna("No entregado")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 10603 valores nulos en la columna 'FECHA_CANCELA', por lo que dichos valores nulos se deben sustituir por un "No cancelado"
df["FECHA_CANCELA"] = df["FECHA_CANCELA"].fillna("No cancelado")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Convertir DataFrame a CSV
df.to_csv('facturacion_limpio.csv')