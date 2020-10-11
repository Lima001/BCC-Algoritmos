#Aluno: Gabriel Eduardo Lima

#Questão 1
def calcular_divisores(n):
    divisores = []
    
    for i in range(1,(n//2)+1):
        if n%i == 0:
            divisores.append(i)

    return divisores


#Questão 2
def verificar_perfeito(n):
    divisores = calcular_divisores(n) #Uso da função desenvolvida na questão 1
    return sum(divisores) == n

def main():
    print("Números perfeitos de 1 a 10.000")
    for i in range(1,10001):
        if verificar_perfeito(i):
            print(i)


#Questão 3
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


#Questão 4
def buscaReversa(dicionario, elemento):
    chaves_resultado = []
    for chave, valor in dicionario.items():
        if valor == elemento:
            chaves_resultado.append(chave)

    return chaves_resultado