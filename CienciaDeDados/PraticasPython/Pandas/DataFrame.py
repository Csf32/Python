import pandas as pd

dados = pd.read_csv("C:\\Users\\abigo\OneDrive\\Programação\\Ciência de Dados I - Docs\\7.Prática em Python\\dados\\Credit.csv")

print(dados.shape)
print("--------------------------------------------------------")

print(dados.describe())
print("--------------------------------------------------------")

print(dados.head())
print("--------------------------------------------------------")

print(dados.tail(2))
print("--------------------------------------------------------")

print(dados[["duration"]])
print("--------------------------------------------------------")

print(dados.loc[[1,3]])
print("--------------------------------------------------------")

print(dados.loc[0:3])
print("--------------------------------------------------------")

print(dados.loc[dados["purpose"] == "radio/tv"])
print("--------------------------------------------------------")

print(dados.loc[dados["credit_amount"] > 18000])
print("--------------------------------------------------------")

colunaSecundaTerceira = dados[["checking_status", "duration"]].loc[dados["credit_amount"] > 18000]
print(colunaSecundaTerceira)
