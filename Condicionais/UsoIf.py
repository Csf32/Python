numero = int(input("Digite um número inteiro: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

if 1000 <= numero <=9999:

    print("Analisando o {} \n Unidade:{} \n Dezena:{}\n Centena:{}\n Milhar: {}".format(numero, unidade, dezena, centena, milhar ))

elif 100 <= numero <= 999:
    print("Analisando o número {} \n Unidade:{} \n Dezena:{}\n Centena:{}".format(numero,  unidade, dezena, centena))

elif 10 <= numero <= 99:
    print("Analisando o número {} \n Unidade:{} \n Dezena: {}".format(numero, unidade, dezena))

else:
    print("Analisando o número {} \n Unidade:{}".format(numero, unidade))



