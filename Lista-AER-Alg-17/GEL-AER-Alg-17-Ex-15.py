inicio = int(input("Digite um número qualquer: "))
fim = int(input("Digite um número qualquer: "))
soma = 0

if inicio%2 != 0:
    inicio += 1

for i in range(inicio,fim+1,2):
    soma += i

print("Soma:", soma)