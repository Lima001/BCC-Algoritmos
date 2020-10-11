def contar_espacos_brancos(string):
    #Método built-in
    return string.count(" ")
    #Usando laços de repetição
    #cont = 0
    #for i in string:
    #   if i == " ":
    #       cont += 1
    #return cont

def main():
    string = input("Digite a string: ")
    print(contar_espacos_brancos(string))

if __name__ == "__main__":
    main()