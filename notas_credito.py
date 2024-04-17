import pandas as pd
import numpy as np

# Carga desde un archivo .xlsx sin índice
df = pd.read_excel("notas_credito.xlsx")
#print(df.head())
print(df.isnull().sum())