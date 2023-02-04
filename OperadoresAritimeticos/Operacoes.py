n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))
s1 = n1**n2
s2 = n1 % n2
s3 = n1 // n2
s4 = n1 / n2

#Para dar 2 prints colado estilo o print do Java utiliza-se no final o end = "":

print("A potência entre {} e {} é {}:".format(n1, n2, s1), end=" ")
print("O Resto da divisão entre {} e {} é {}:".format(n1, n2, s2), end=" ")
print("E a Divisão exata entre {} e {} é: {}".format(n1, n2, s3))

# O \n faz a quebra da linha
n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))
s1 = n1**n2
s2 = n1 % n2
s3 = n1 // n2
s4 = n1 / n2


print("A potência entre {} e {} é {}:".format(n1, n2, s1), end=" ")
print("O Resto da divisão entre {} e {} é {}:".format(n1, n2, s2), end=" ")
print("E a Divisão exata entre {} e {} é: {}".format(n1, n2, s3))

