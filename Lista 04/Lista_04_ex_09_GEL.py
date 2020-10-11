corretor1 = float(input("Digite o valor de vendas do corretor1: "))
corretor2 = float(input("Digite o valor de vendas do corretor2: "))
corretor3 = float(input("Digite o valor de vendas do corretor3: "))

lista_corretores = []
lista_corretores.append([corretor1])
lista_corretores.append([corretor2])
lista_corretores.append([corretor3])

for i in lista_corretores:
    if i[0] > 500000.00:
        i.append(i[0]*0.12)
    elif i[0] > 30000.00 and i[0] < 50000.00:
        i.append(i[0]*0.095)
    else:
        i.append(i[0]*0.07)

total = 0
for i in range(3):
    print("Corretor" + str(i+1)+ ": ", end=" ")
    print("Valor venda: ", lista_corretores[i][0], end=" ")
    print("Comissao: ", lista_corretores[i][1])
    total += lista_corretores[i][0]

print("Total: ", total)