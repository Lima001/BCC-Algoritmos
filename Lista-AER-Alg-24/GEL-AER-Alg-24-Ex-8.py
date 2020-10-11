def formatar_lista_string(lista):
    string = ""
    
    for i in range(len(lista)):
        string += lista[i]
        
        if i < len(lista)-2:
            string += ", "
        elif i == len(lista)-2:
            string += " e "

    return string

def main():
    lista = []
    
    exe = True
    while exe:
        palavra = input("Digite palavras para adionar a lista, ou pressione enter para cancelar: ")
    
        if palavra != "":
            lista.append(palavra)
        else:
            exe = False
    
    print(formatar_lista_string(lista))

if __name__ == "__main__":
    main()