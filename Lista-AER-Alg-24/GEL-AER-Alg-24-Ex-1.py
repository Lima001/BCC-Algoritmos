def ordenar_crescente(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]

def main():
    print("Digite 0 para parar...")
    numeros = []
    
    exe = True
    while exe:
        n = int(input("Informe um número: "))
        if n != 0:
            numeros.append(n)
        else:
            exe = False

    ordenar_crescente(numeros)
    for n in numeros:
        print(n)

if __name__ == "__main__":
    main()