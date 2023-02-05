import numpy as np

matriz = np.array([12, 29, 30, 60])
print(matriz)
print(type(matriz))
print()

matrizfloat = np.array([10, 20, 40], dtype= np.float64)
print(matrizfloat)
print(type(matrizfloat))
print()  

matrizInteiro = np.array([10, 50, 40], dtype= np.int32)    
print(matrizInteiro) 
print(type(matrizInteiro)) 
print() 

transformarMatriz = np.array([1.2, 0.9995, 8.88, 9.1])
print(transformarMatriz)
print() 

transformarMatrizInt = transformarMatriz.astype(np.int32)
print(transformarMatrizInt) 
print()

matrizNumeroInteiro = np.array([5, 8, 6, 11])
print(matrizNumeroInteiro)
print()

matrizInteiroParaFloat = matrizNumeroInteiro.astype(np.float64)
print(matrizInteiroParaFloat)