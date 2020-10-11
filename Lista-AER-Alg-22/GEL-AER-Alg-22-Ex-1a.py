def contar_ocorrencias(string,caractere):
    #Usando método built-in
    return string.count(caractere)
    #Usando laços de repetição
    #cont = 0
    #for i in string:
    #   if i == caractere:
    #       cont += 1
    #return cont

def main():
    string = input("Digite a string: ")
    caractere = input("Digite o caractere: ")
    print(contar_ocorrencias(string,caractere))

if __name__ == "__main__":
    main()