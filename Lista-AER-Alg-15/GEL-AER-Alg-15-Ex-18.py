n_iteracoes = 1
qtd_negativo = 0
soma_positivo = 0

while n_iteracoes <= 20:
    numero = int(input(f"Digite o {n_iteracoes}º número inteiro (Positivo ou Negativo): "))

    if numero < 0:
        qtd_negativo +=1
    elif numero > 0:
        soma_positivo += numero

    n_iteracoes += 1

print()
print("Soma Positivos:", soma_positivo)
print("Qtd Negativos:", qtd_negativo)