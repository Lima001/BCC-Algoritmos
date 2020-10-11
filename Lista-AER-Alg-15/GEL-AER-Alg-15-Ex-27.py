base = int(input("Base: "))
expoente = int(input("Expoente: "))

atual = 0
potencia = 1

while atual < expoente:
    potencia *= base 
    atual += 1

print(potencia)