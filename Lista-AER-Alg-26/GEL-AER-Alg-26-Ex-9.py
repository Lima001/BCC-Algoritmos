from random import shuffle, randint

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

def gerar_lista_chamadas_validas():
    lista = [i for i in range(1,76)]
    shuffle(lista)

    return lista

def anunciar_numeros(cartela, lista_chamada):
    anuncios = 0
    for i in lista_chamada:
        anuncios += 1
        for j in cartela.values():
            if i in j:
                posicao = j.index(i)
                j[posicao] = 0
                break
        
        if verificar_cartela_vencedora(cartela):
            return anuncios

    return anuncios

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

#Apenas para fins de testes
def exibir_cartela(cartela:dict):
    for chave in cartela.keys():
        print(chave, end="  ")
    print()

    for i in range(5):
        for valor in cartela.values():
            print(valor[i], end=(3-len(str(valor[i])))*" ")
        print()

def main():
    qtd_anuncio = []
    for i in range(1000):
        cartela = gerar_cartela()
        lista_chamada = gerar_lista_chamadas_validas()

        #print(cartela)

        anuncios = anunciar_numeros(cartela, lista_chamada)
        qtd_anuncio.append(anuncios)

        #exibir_cartela(cartela)

    print("Minimo:", min(qtd_anuncio))
    print("Máximo:", max(qtd_anuncio))
    print("Média:", sum(qtd_anuncio)/1000)

if __name__ == "__main__":
    main()