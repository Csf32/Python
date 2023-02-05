import numpy as np

valorZeroUm = np.random.random((5))
print(valorZeroUm)
print()

valor = np.random.randn((5))
print(valor)
print()

matrizAleatoria = 10*np.random.random((3,4))
print(matrizAleatoria)
print()

print("-------------------------------------------")
print()

gerarSemente = np.random.default_rng(1)

matriz = gerarSemente.random(3)
print(matriz)
print()

matrizBidimensional = gerarSemente.integers(10, size=(3,4))
print(matrizBidimensional)
print()

vetorRepetido = np.array([11, 22, 39, 40, 28, 11, 28, 48])
vetorSemRepeticao = np.unique(vetorRepetido)
print(vetorSemRepeticao)