n = int(input("Digite o valor de n: "))

soma = 0

for i in range(0,n):
    soma += (n-i)/(i+1)

print("A = ",soma)