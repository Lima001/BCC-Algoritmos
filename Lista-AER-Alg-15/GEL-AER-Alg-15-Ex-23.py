n = int(input("Digite o valor de n: "))

soma = 0
dividendo = 1
sinal = 1

while dividendo <= n:
    soma += (1/dividendo)*sinal
    dividendo += 1
    sinal *= -1

print("A", soma)