def calcular_divisores(n):
    divisores = []
    
    for i in range(1,(n//2)+1):
        if n%i == 0:
            divisores.append(i)

    return divisores

def main():
    n = 0
    while n <= 0:
        n = int(input("Informe um inteiro positivo: "))

    divisores = calcular_divisores(n)
    
    print(divisores)

if __name__ == "__main__":
    main()