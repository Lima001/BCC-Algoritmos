def retornar_data_extenso(data):
    nome_mes = {"01":"Janeiro","02":"Fevereiro","03":"Março","04":"Abril","05":"Maio","06":"Junho",
                "07":"Julho","08":"Agosto","09":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}
    dia,mes,ano = data.split("/")
    return f"{dia} de {nome_mes[mes]} de {ano}"

def main():
    data = input("Informe a data(dd/mm/aaaa): ")
    print(retornar_data_extenso(data))

if __name__ == "__main__":
    main()