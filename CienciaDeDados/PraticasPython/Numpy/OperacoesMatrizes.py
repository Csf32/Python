import numpy as np

vetor1 = np.array([[1,5], [2,6]])
vetor2 = np.array([[2,5], [6,7]])
somar = vetor1 + vetor2
print(somar)
print()

multiplicar = vetor1 * vetor2
print(multiplicar)
print("---------------------------------------")


rerranjo = np.arange(15).reshape((3,5))
print(rerranjo)
print()
print("---------------------------------------")

array1 = np.array(range(1, 16))
print(array1)
print()

embaralharArray = np.random.permutation(array1)
print(embaralharArray)
print()

redimensionarArray1 = np.reshape(embaralharArray, (3,5))
print(redimensionarArray1)
print()
print("---------------------------------------")

matrizTransposta = rerranjo.transpose((1,0))
print(matrizTransposta)
print()
print("---------------------------------------")


matrizPositivoNegativo = np.random.randn(4,4)
print(matrizPositivoNegativo)
print("---------------------------------------")

matrizBooleana = matrizPositivoNegativo > 0
print(matrizBooleana)
print("---------------------------------------")

intervaloMatriz = np.where(matrizBooleana > 0, 1, -1)
print(intervaloMatriz)
