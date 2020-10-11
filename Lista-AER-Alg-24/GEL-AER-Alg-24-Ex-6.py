def calcular_divisores(n):
    divisores = []
    
    for i in range(1,n//2+1):
        if n%i == 0:
            divisores.append(i)
    
    return divisores

def verificar_perfeito(n):
    divisores = calcular_divisores(n)
    #Usando função built-in para soma
    soma = sum(divisores)
    
    #Usando laços de repetição
    #soma = 0
    #for i in divisores:
    #   soma += i
    
    return soma == n

def main():
    for i in range(1,10001):
        if verificar_perfeito(i):
            print(i)

if __name__ == "__main__":
    main()