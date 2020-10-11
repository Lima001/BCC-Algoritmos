from random import randint

def verificar_cartela_vencedora(cartela:dict):
    
    def verificar_vertical(cartela):
        for i in cartela.values():
            if sum(i) == 0:
                return True
        
        return False

    def verificar_horizontal(cartela):
        for i in range(5):
            soma = 0
            
            for j in cartela.values():
                soma += j[i]  
                if soma != 0:
                    break
            
            if soma == 0:
                return True
        
        return False

    def verificar_diagonal(cartela):
        soma1 = 0
        soma2 = 0
        posicao = 0
        
        for i in cartela.values():
            soma1 += i[posicao]
            soma2 += i[4-posicao]
            posicao += 1
            
        return soma1 == 0 or soma2 == 0

    return verificar_diagonal(cartela) or verificar_horizontal(cartela) or verificar_vertical(cartela)


def gerar_cartela():
    cartela = {"B":[], "I":[], "N":[], "G":[], "O":[]}
    
    inicio = 1
    fim = 15

    for chave in cartela.keys():
        
        while len(cartela[chave]) != 5:
            numero = randint(inicio, fim)
        
            if numero not in cartela[chave]:
                cartela[chave].append(numero)

        cartela[chave] = sorted(cartela[chave])

        inicio += 15
        fim += 15

    return cartela


def exibir_cartela(cartela:dict):
    for chave in cartela.keys():
        print(chave, end="  ")
    print()

    for i in range(5):
        for valor in cartela.values():
            print(valor[i], end=(3-len(str(valor[i])))*" ")
        print()


def preencher_cartela_com_zeros(cartela:dict, modo):
    #Preenche cartela vencedora com 0 na coluna
    if modo == 0:
        coluna = randint(0,4)
        coluna_chave = {0:"B", 1:"I", 2:"N", 3:"G", 4:"O"}
        cartela[coluna_chave[coluna]] = [0,0,0,0,0]
             

    #Preenche cartela vencedora com 0 em linha
    elif modo == 1:
        linha = randint(0,4)
        for i in cartela.values():
            i[linha] = 0
    
    #Preenche cartela vencedora com 0 na diagonal
    elif modo == 2:
        diagonal = randint(0,1)
        posicao = 0
        
        if diagonal == 0:
            for i in cartela.values():
                i[posicao] = 0
                posicao += 1
        else:
            for i in cartela.values():
                i[4-posicao] = 0
                posicao += 1
        
    
    #Preenche com 0, mas não torna a cartela vencedora
    else:
        cartela["B"][0] = 0
        cartela["I"][2] = 0
        cartela["N"][1] = 0
        cartela["G"][4] = 0
        cartela["O"][3] = 0


def main():
    #Professor, para este problema decidi utilizar as funções já criadas nos
    #exercícios anteriores, porém para gerar as cartelas com 0 para verificar depois
    #Eu criei a função preencher_cartela_com_zeros... Nela eu posso criar
    #cartelas com 0 na diagonal, vertical e horizontal de maneira aleatória mas que são vencedoras.
    #Além disso, ela cria uma cartela com 0 mas que não é vencedora de maneira fixa.
    #Ela possui uns comentários que podem ajudar o professor entender melhor como eu fiz isso.

    #Criando cartelas básicas, sem presença de 0 - Função criada em exercício anterior
    cartelas = [gerar_cartela() for i in range(4)]

    #Preenche as cartelas com 0, conforme desejado
    for i in range(len(cartelas)):
        #1º cartela - 0s na vertical - vencedora
        #2º cartela - 0s na horizontal - vencedora
        #3º cartela - 0s na diagonal - vencedora
        #4º cartela - 0s espalhados - NÃO é vencedora
        preencher_cartela_com_zeros(cartelas[i],i)

    #Exibe todas as cartelas geradas e se são vencedoras
    for i in cartelas:
        exibir_cartela(i)
        if verificar_cartela_vencedora(i):
            print("Vencedora!!!")
        print("\n"*2)

    continurar = int(input("Desejar ver o teste em cartelas geradas manualmente? 1-sim, 0-Não: "))
    if continurar != 1:
        exit()

    #Abaixo coloco exemplos manuais, caso o professor queira avaliar também...
    cartela1 = {"B":[1,2,3,4,5], "I":[16,17,18,19,20], "N":[31,32,33,34,35], "G":[0,0,0,0,0], "O":[61,62,63,64,65]}
    cartela2 = {"B":[1,2,0,4,5], "I":[16,17,0,19,20], "N":[31,32,0,34,35], "G":[46,47,0,49,50], "O":[61,62,0,64,65]}
    cartela3 = {"B":[0,2,3,4,5], "I":[16,0,18,19,20], "N":[31,32,0,34,35], "G":[46,47,48,0,50], "O":[61,62,63,64,0]}
    cartela4 = {"B":[1,2,3,0,0], "I":[0,0,18,19,20], "N":[31,0,33,34,35], "G":[0,47,48,49,50], "O":[61,62,0,0,0]}

    print(verificar_cartela_vencedora(cartela1))
    print(verificar_cartela_vencedora(cartela2))
    print(verificar_cartela_vencedora(cartela3))
    print(verificar_cartela_vencedora(cartela4))

if __name__ == "__main__":
    main()