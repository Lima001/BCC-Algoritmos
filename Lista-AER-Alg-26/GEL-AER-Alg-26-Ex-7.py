from random import randint

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

def main():
    cartela = gerar_cartela()
    exibir_cartela(cartela)

if __name__ == "__main__":
    main()