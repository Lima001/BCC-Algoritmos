n = int(input("Digite o valor de n: "))

soma = 0
vlr = 0

while vlr < n:
    soma += (n-vlr)/(vlr+1)
    vlr += 1

print("A:", soma)