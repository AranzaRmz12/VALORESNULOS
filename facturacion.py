import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("facturacion.xlsx")
#print(df.head())
print(df.isnull().sum())