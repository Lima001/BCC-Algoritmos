maior = 0
iteracao = 1

#Como comentei com o professor por meio de emails
#Estava em dúvida se deveria verificar se o número informado era positivo
#Como o professor deixou a minha escolha, abaixo implementei a solução
#que utiliza dessa verificação
while iteracao <= 12:
    num = 0
    while num <= 0:
        num = int(input(f"Digite o {iteracao}º número inteiro POSITIVO: "))

    if num > maior:
        maior = num

    iteracao += 1

print("Maior:", maior)