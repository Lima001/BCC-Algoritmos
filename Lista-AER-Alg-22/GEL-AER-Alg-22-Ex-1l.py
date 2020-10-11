def validar_cpf(cpf):

    def achar_digito_verificador(numeros):
        multiplicador = len(numeros) + 1
        total = 0
        for i in numeros:
            total += int(i)*multiplicador
            multiplicador -= 1

        digito = 11 - (total %11)
        if digito >= 10:
            return 0
        
        return digito

    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-" or len(cpf) != 14:
        return False

    numeros = cpf[0:3] + cpf[4:7] + cpf[8:11]
    digitos_verificadores = cpf[12:]

    if len(set(numeros+digitos_verificadores)) == 1:
        return False

    primeiro_digito_verificador = str(achar_digito_verificador(numeros))
    numeros += digitos_verificadores[0]
    ultimo_digito_verificador = str(achar_digito_verificador(numeros))

    return primeiro_digito_verificador == digitos_verificadores[0] and \
        ultimo_digito_verificador == digitos_verificadores[1]


def main():
    cpf = input("Digite o CPF: ")
    if validar_cpf(cpf):
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")

if __name__ == "__main__":
    main()