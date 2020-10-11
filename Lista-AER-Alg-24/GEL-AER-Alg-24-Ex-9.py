def countRange(lista,vlr_minimo,vlr_maximo):
    count = 0
    
    for numero in lista:
        if numero >= vlr_minimo and numero <= vlr_maximo:
            count += 1

    return count


def main():
    lista = [] 

    exe = True
    while exe:
        n = input("Digite um numero para adiconar a lista, ou enter para parar: ")
        if n != "":
            lista.append(int(n))
        else:
            exe = False

    vlr_minimo = int(input("Digite o valor minimo: ")) 
    vlr_maxio = int(input("Digite o valor maximo: "))

    print("Resultado:",countRange(lista,vlr_minimo,vlr_maxio))
    
if __name__ == "__main__":
    main()