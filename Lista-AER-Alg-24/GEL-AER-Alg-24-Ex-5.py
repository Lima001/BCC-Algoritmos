def calcular_divisores(n):
    divisores = []
    
    for i in range(1,n//2+1):
        if n%i == 0:
            divisores.append(i)
    
    return divisores

def main():
    n = int(input("Digite um número: "))
    divisores = calcular_divisores(n)
    for i in divisores:
        print(i)

if __name__ == "__main__":
    main()