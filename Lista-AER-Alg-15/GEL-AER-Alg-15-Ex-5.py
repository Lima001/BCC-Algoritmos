numero = 1
fim = 10
somatorio = 0

while numero <= fim:
    print(numero, end=" ")
    somatorio += numero
    print("Soma Parcial:", somatorio)
    numero += 1

print("\nSomatorio:", somatorio)