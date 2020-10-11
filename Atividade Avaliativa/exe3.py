def formatar_data(string):
    mes_escrito = {
        "01":"Janeiro",
        "02":"Fevereiro",
        "03":"Março",
        "04":"Abril",
        "05":"Maio",
        "06":"Junho",
        "07":"Julho",
        "08":"Agosto",
        "09":"Setembro",
        "10":"Outubro",
        "11":"Novembro",
        "12":"Dezembro"
    }

    dia,mes,ano = string.split("/")

    return f"{dia} de {mes_escrito[mes]} de {ano}"

def main():
    data = input("Informe a data(dd/mm/aaaa): ")
    print(formatar_data(data))

if __name__ == "__main__":
    main()