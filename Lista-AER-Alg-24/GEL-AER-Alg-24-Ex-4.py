entradas = [[],[],[]]
exe = True
while exe:
    n = input("Informe um dígito, ou digite apenas enter para cancelar: ")
    if n != "":
        n = int(n)
        if n < 0:
            entradas[0].append(n)
        elif n == 0:
            entradas[1].append(n)
        else:
            entradas[2].append(n)
    else:
        exe = False

for grupo in entradas:
    for numero in grupo:
        print(numero)