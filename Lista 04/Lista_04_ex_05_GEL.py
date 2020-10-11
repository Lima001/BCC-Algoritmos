num1 = int(input("Digite o primeiro numero: "))
exe = True
while exe:
    num2 = int(input("Digite o segundo numero, diferente do primeiro: "))
    if num2 != num1:
        exe = False

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("Numeros são iguais")