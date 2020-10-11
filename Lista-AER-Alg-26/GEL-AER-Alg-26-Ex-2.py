def diferenca_simetrica(conjunto1, conjunto2):
    #Usando o metodo built-in para conjuntos
    return list(conjunto1.symmetric_difference(conjunto2))

    #Usando operações de conjuntos
    #return sorted(conjunto1.union(conjunto2) - conjunto1.intersection(conjunto2))

    #Usando laços de repetição
    #unicos_1 = [i for i in conjunto1 if i not in conjunto2]
    #unicos_2 = [i for i in conjunto2 if i not in conjunto1]
    #return sorted(unicos_1 + unicos_2)

def main():
    #Pegando a lista de entrada e transformando em conjunto
    conjunto1 = input("Digite os elementos do conjunto 1 (x,y,z...): ").split(",")
    conjunto2 = input("Digite os elementos do conjunto 2 (x,y,z...): ").split(",")

    #Mapeando elementos da entrada para inteiros elementos de um conjunto
    conjunto1 = set(map(int, conjunto1))
    conjunto2 = set(map(int, conjunto2))

    #Chamada e apresentação do resultado
    diferenca = diferenca_simetrica(conjunto1, conjunto2)
    print("Diferença Simétrica:", diferenca)
    

if __name__ == "__main__":
    main()