
import math
num = int(input("Digite um número: "))

raiz = math.sqrt(num)
print(raiz)

print("{}".format(math.ceil(raiz)))

print("{}".format(math.floor(raiz)))

print("Aproximando a raíz: {} com duas casas decimais: {:.2f}".format(raiz, raiz))
