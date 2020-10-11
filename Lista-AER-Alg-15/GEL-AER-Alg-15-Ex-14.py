n_iteracao = 1
numero = int(input(f"Digite o {n_iteracao}º numero: "))

maior, menor = numero, numero

while n_iteracao <= 11:
    n_iteracao += 1
    numero = int(input(f"Digite o {n_iteracao}º numero: "))
    
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero


print("Menor:", menor)
print("Maior:", maior)