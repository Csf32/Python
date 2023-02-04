#Função com valor defult: Senão passar o parâmetro para a função será default

def intervalo(inic=1, fim=10):
    for i in range(1, fim+1):
        print(i)
#Pode imprimir um intervalo com parâmetro
intervalo(1, 10)

#E pode imprimir um intervalo sem parâmetro
intervalo()
