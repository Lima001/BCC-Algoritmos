numero = int(input("Digite o numero: "))

qtd_digitos = 0
while numero > 0:
    qtd_digitos += 1
    numero = numero//10

print(qtd_digitos)