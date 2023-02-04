frase = "Curso em Video Python"

#A função len() diz o comprimento em quantidade
print([len(frase)])

#Comando count('o') = contar a quantidade de "o" minúscula
print(frase.count('o'))

#Comando count('o', x, y) = contar a quantidade de "o" minúscula em um intervalo
print(frase.count('o', 0, 13))

#Encontra a posição inicial do termo
print(frase.find('deo')) # Se receber o valor -1, significa que não encontrou a string

# Comando in, vai dizer se existe com true ou false
print('Curso' in frase)
