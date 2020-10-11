#Letra a)
def soma_dig(n):
    alg1 = n // 10
    alg2 = n % 10
    
    return alg1 + alg2

#Letra b)
def gerar_senha(dia, mes, ano):
    a = str(soma_dig(dia))
    b = str(soma_dig(mes))
    c = str(soma_dig(ano%100))

    return a + b +c

def main():
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mes: "))
    ano = int(input("Informe o ano: "))

    print("Senha: ", gerar_senha(dia, mes, ano))

if __name__ == "__main__":
    main()