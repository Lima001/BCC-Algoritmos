matricula = int(input("Digite o valor da matricula: "))

ano = matricula//10000
semestre = (matricula%10000)//1000

if semestre == 1:
    print("20"+"{:02}".format(ano)+" Primeiro Semestre")
else:
    print("20"+"{:02}".format(ano)+" Segundo Semestre")