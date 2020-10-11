numero = 86
soma = 0

while numero < 907:
    print(numero, end=" ")
    soma += numero
    numero += 2

print("\nSoma", soma)

#Poderia, como nos exercícios anteriores também utilizar % == 0, mas acredito que
#usa mais recursos devida as diversas comparações, então preferi usar algo mais simples