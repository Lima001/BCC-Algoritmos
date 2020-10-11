a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

soma = a+b
if soma > c:
    print("A soma de a+b é maior que c")
elif soma < c:
    print("A soma de a+b é menor que c")
else:
    print("A soma de a+b é igual a c")