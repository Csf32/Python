import random
maquina = random.randint(0, 5) 

nomeUsuario = str(input("Usuario, escreva o seu nome: "))
print()

numeroUsuario = int(input("Agora, escreva um número entre 0 e 5: "))
print()

print("Máquina, escolha também um número entre 0 e 5 = {} ".format(maquina))
print()

iguais = numeroUsuario == maquina
if iguais:
    print("Parabéns {}, você acertou o mesmo número da máquina, que foi = {} ".format(nomeUsuario, iguais))
print("\033[31mDesculpe {}, tente novamente".format(nomeUsuario))
