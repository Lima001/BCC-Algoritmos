n_iteracao = 1
menor = int(input(f"Digite o {n_iteracao}º numero: "))

while n_iteracao <= 11:
    n_iteracao += 1
    numero = int(input(f"Digite o {n_iteracao}º numero: "))
    if numero < menor:
        menor = numero


print("Menor:", menor)