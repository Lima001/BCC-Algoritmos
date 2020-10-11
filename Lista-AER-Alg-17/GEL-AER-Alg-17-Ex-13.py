menor = int(input("Digite o 1º numero: "))
for i in range(2,13):
    numero = int(input(f"Digite o {i}º numero: "))

    if numero < menor:
        menor = numero

print("menor:", menor)