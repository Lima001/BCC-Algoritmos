n = int(input("Digite o valor de n: "))

dividendo = 1
soma = 0

while dividendo <= n:
    soma += 1/dividendo
    dividendo += 1

print("A:", soma)