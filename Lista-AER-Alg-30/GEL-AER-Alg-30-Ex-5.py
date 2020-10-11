fat_memorizado = {0:1, 1:1}

def rfatorial(numero):
    if numero in fat_memorizado:
        return fat_memorizado[numero]
    
    val = numero * rfatorial(numero-1)
    fat_memorizado[numero] = val

    return val

def main():
    numero = -1
    while numero < 0:
        numero = int(input("Informe um numero inteiro positivo para calcular o fatorial: "))
        
    fatorial = rfatorial(numero)

    print(f"{numero}! = {fatorial}")

if __name__ == "__main__":
    main()