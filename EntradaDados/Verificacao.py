verificacaoDeEntrada = input("Digite qualquer letra: ")

print("Qual a classe?", type(verificacaoDeEntrada))
print("É um número?", verificacaoDeEntrada.isnumeric())
print("Está em maiúsculo?", verificacaoDeEntrada.isupper())
print("Está em minúsculo?", verificacaoDeEntrada.islower())
print("Está capitalizaa?", verificacaoDeEntrada.istitle())
