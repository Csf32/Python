import numpy as np

matrizBidimensional = np.array([[18, 29, 40, 30], [11, 20, 30, 50]])
print(matrizBidimensional)
print()

print(matrizBidimensional[1][1])
print()


print(matrizBidimensional.shape)
print()

print(matrizBidimensional.max())
print(matrizBidimensional.min())
print(matrizBidimensional.sum())
print()

print(matrizBidimensional.mean())

print(matrizBidimensional.std())
print()

vetor = np.array([12, 33, 45, 78])
print(np.sqrt(vetor))
print(np.exp(vetor))