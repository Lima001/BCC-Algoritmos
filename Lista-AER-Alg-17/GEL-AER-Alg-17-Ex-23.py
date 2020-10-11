n = int(input("Digite o valor de n: "))

soma = 0
sinal = 1

for i in range(1,n+1):
    soma += (1/i) * sinal
    sinal *= -1

print("Soma", soma)