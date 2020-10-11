def calcular_divisores(n):
    divisores = []
    
    for i in range(1,(n//2)+1):
        if n%i == 0:
            divisores.append(i)

    return divisores

def verificar_perfeito(n):
    divisores = calcular_divisores(n)
    
    return sum(divisores) == n

def main():
    print("Números perfeitos de 1 a 10.000")
    for i in range(1,10001):
        if verificar_perfeito(i):
            print(i)

if __name__ == "__main__":
    main()