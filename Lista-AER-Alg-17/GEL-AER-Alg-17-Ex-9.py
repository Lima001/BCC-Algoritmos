n = int(input("Digite n: "))
soma = 0
impar = 1

for i in range(1,n+1):
    soma += impar
    impar += 2

print("Soma", soma)