def buscaReversa(dicionario, elemento):
    chaves_resultado = []
    for chave, valor in dicionario.items():
        if valor == elemento:
            chaves_resultado.append(chave)

    return chaves_resultado

def main():
    qtd_itens = int(input("Quantos items deseja ter no dicionario: "))
    dicionario = {}
    
    for i in range(qtd_itens):
        chave = input(f"Digite a chave do item {i+1}: ")
        valor = input(f"Digite o valor do item {i+1}: ")
        
        dicionario[chave] = valor
        
        print("-"*5)
    
    elemento = input("Digite o elementos que deseja buscar: ")
    resultado = buscaReversa(dicionario,elemento)
    
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()