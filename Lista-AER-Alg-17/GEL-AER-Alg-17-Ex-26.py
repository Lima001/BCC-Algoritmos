#Conforme a conversa no email, o professor pediu para deixar essa questão de lado
#devido não fazer sentido utilizar for para verificar se usuário gostaria de executar novamente uma analise
#Todavia implementei a solução utilizando for para a parte de analise, e usei um while para repetir o processo

exe = True
while exe:
    numero = int(input("Digite o numero: "))
    primo = True

    for i in range(1,numero+1):
        if numero%i == 0:
            print(i, end=" ")
            if i != 1 and i != numero:
                primo = False

    if primo:
        print(f"\n{numero} é primo", end="")

    executar_novamente = int(input("\nDeseja analisar outro numero (0 Não, 1 Sim): "))

    if executar_novamente == 0:
        exe = False