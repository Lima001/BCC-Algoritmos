#Inicialização de variáveis que serão utilizadas no processamento
# junto com as entradas
soma = 0
multiplicacao = 1
for i in range(4):
    #Entradas: Números que serão usados nas operações
    numero =  float(input("Digite o " + str(i+1) + " numero: "))
    
    #Processamento: Adição e multiplicação do valor digitado
    #  pelo valor atual das variáveis soma e multiplicação
    soma += numero
    multiplicacao *= numero

#Saídas: Mensagem com o valor da soma e multiplicação dos números
print("O valor da soma é: " + str(soma))
print("O valor da multiplicação é: " + str(multiplicacao))