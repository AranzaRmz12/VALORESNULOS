import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("devoluciones.xlsx")
#print(df.head())
#print(df.isnull().sum())

# Para CVE_VEND decidí utilizar el backward fill para sustituir los 3 datos faltantes
df['CVE_VEND'] = df['CVE_VEND'].fillna(method = 'bfill')
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 6 valores nulos en la columna 'CVE_PEDI', por lo que dichos valores nulos se deben sustituir por un "No disponible"
df["CVE_PEDI"] = df["CVE_PEDI"].fillna("No disponible")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 187 valores nulos en la columna 'FECHA_CANCELA', por lo que dichos valores nulos se deben sustituir por un "No cancelado"
df["FECHA_CANCELA"] = df["FECHA_CANCELA"].fillna("No cancelado")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Hay 11 valores nulos en la columna 'DOC_ANT', por lo que dichos valores nulos se deben sustituir por un "No disponible"
df["DOC_ANT"] = df["DOC_ANT"].fillna("No disponible")
valores_nulos = df.isnull().sum()
print(valores_nulos)

