def verificar_palindromo(string):
    #Usando slices
    string = string.replace(" ","")
    if string == string[-1::-1]:
        return True
    return False

    #Usando laçoes de repeticao
    #string = string.replace(" ","")
    #tamanho = len(string)
    #for i in range(tamanho):
    #   if string[i] != string[tamanho-i-1]:
    #       return False
    #return True

def main():
    string = input("Digite uma string: ")
    print(verificar_palindromo(string))

if __name__ == "__main__":
    main()