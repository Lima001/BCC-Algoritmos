inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
soma = 0

if inicio%2 == 1:
    inicio += 1

while inicio <= fim:
    soma += inicio
    inicio += 2

print("Soma:", soma)