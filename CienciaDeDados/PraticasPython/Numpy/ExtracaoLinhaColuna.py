import numpy as np

vetor = np.array([[3,5], [6,1], [4,3]])
           
print(vetor)
print()

primeiraLinhaComColunas = vetor[0, :]
print(primeiraLinhaComColunas)
print()

segundaLinhaComColunas = vetor[1, :]
print(segundaLinhaComColunas)
print()

terceiraLinhaComColunas = vetor[2, :]
print(terceiraLinhaComColunas)
print()

primeiraColunaComLinhas = vetor[:, 0]
print(primeiraColunaComLinhas)
print()

segundaColunaComLinhas = vetor[:, 1]
print(segundaColunaComLinhas)