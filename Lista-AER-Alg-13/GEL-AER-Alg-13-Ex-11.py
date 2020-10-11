def verificar_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano(aaaa): "))

A = ano - 1900
B = A//4

if verificar_bissexto(ano) and ((dia <= 29 and mes == 2) or (dia <= 31 and mes == 1)):
    B -= 1

dicionario_mes = {1:0, 2:3, 3:3, 4:6, 5:1, 6:4,
                    7:6, 8:2, 9:5, 10:0, 11:3, 12:5}

C = dicionario_mes[mes]
D = dia-1

S = A+B+C+D
R = S%7

dicionario_dia = {0:"2º Feira" ,1:"3º Feira" ,2:"4º Feira" ,3:"5º Feira", 4:"6º Feira", 5:"Sábado", 6:"Domingo"}

print(f"Hoje é: {dicionario_dia[R]}")
if R == 3 or R == 4:
    print("Hoje haverá aula de algortimos")
    if R == 3:
        print("Hoje haverá lab")