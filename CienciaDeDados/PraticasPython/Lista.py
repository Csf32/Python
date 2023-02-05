
lista1 = [2,4,5,6,8]
print(lista1)

lista2 = [2,4,"5",6,True]
print(lista2)

lista3 = [2,4,"5",[10, 11, 50], 6,True]
print(lista3)

lista4 = list(range (0, 10))
print(lista4)

print(len(lista4))

print(lista3[2])

lista3[2] = 7
print(lista3)


for i in range(0, len(lista4)):
    print(lista4[i] + 1)