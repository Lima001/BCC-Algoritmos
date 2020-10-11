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

def data_magica(dia,mes,ano):
    return (dia * mes == ano % 100)

def main():
    contador = 0
    for ano in range(1901,2001):
        for mes in range(1,13):
            dia = quantidade_dias_mes(mes,ano)
            for dia in range(1,dia+1):
                if data_magica(dia,mes,ano):
                    contador += 1
                    print(f"Data Mágica {contador}: {dia}/{mes}/{ano}")

if __name__ == "__main__":
    main()