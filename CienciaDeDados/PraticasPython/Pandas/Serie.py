import numpy as np
import pandas as pd

dados = pd.read_csv("C:\\Users\\abigo\OneDrive\\Programação\\Ciência de Dados I - Docs\\7.Prática em Python\\dados\\Credit.csv")

arrayNumpy = np.array([2, 5, 6, 11, 7, 10])
seriePandas1 = pd.Series(arrayNumpy)
print(seriePandas1)
print("--------------------------------------------------")

seriePandas2 = dados["purpose"]
print(seriePandas2)
print(type(seriePandas2))
print("--------------------------------------------------")

dataFrame = dados[["purpose"]]
print(dataFrame)
print(type(dataFrame))
print("--------------------------------------------------")

print(dados.rename(columns={"duration": "duração", "purpose": "propósito"}))
print("--------------------------------------------------")

dados.rename(columns={"duration": "duração", "purpose": "propósito"},inplace = True)
print(dados.head(1))
print("--------------------------------------------------")

dados.drop("checking_status",axis = 1, inplace=True)
print(dados.head(1))
print("--------------------------------------------------")

print(dados.isnull())
print("--------------------------------------------------")

print(dados.isnull().sum())
print("--------------------------------------------------")

print(dados.dropna())
print("--------------------------------------------------")

print(dados["duração"].fillna(0, inplace = True))
print("--------------------------------------------------")

loc = dados.loc[[1,3]]
print(loc)
print(type(loc))
print("--------------------------------------------------------")

iloc = dados.iloc[0:3, 0:5]
print(iloc)
print(type(iloc))
print("--------------------------------------------------------")

print(dados.iloc[[0,1,2,4,6], 0:5])
