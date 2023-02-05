import numpy as np

matrizBidimensional = np.array([[7, 2, 23], [12, 27, 4], [5, 34, 24]])
print(matrizBidimensional)
print()

naoInicia = np.empty([3,2], dtype= int)
print(naoInicia) 
print()

valorZero = np.zeros([4,3])
print(valorZero)
print()

valorUm = np.ones([5,6])
print(valorUm)
print()

diagonalPrincipal = np.eye(5)
print(diagonalPrincipal)