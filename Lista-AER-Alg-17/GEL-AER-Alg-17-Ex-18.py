soma_positivos = 0
qtd_negativos = 0

for i in range(1,21):
    numero = int(input(f"Digite o {i}º número: "))

    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        qtd_negativos += 1

print("Soma Positivos:", soma_positivos)
print("Qtd Negativos:", qtd_negativos)