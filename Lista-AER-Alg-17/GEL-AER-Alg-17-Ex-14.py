numero = int(input("Digite o 1º numero:  "))

maior, menor = numero, numero

for i in range(2,13):
    numero = int(input(f"Digite o {i}º numero:  "))

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print("Maior:", maior)
print("Menor:", menor)