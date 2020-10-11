def verificar_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

def quantidade_dias_mes(mes,ano):
    if mes in [4,6,9,11]:
        return 30
    elif mes == 2:
        if verificar_bissexto(ano):
            return 29
        else:
            return 28
    else:
        return 31 

def main():
    mes = int(input("Digite o mês(1-12): "))
    ano = int(input("Digite o ano: "))
    dias = quantidade_dias_mes(mes,ano)
    print("O mes {0} do ano {1} tem {2} dias".format(mes,ano,dias))

if __name__ == "__main__":
    main()