#Entradas: Idade informada em qtd ano, mes e dia
ano = int(input("Digite o valor dos anos: ")) 
mes = int(input("Digite o valor dos meses: "))
dia = int(input("Digite o valor dos dias: "))

#Processamento: Soma das Multiplicação vindas da entradas 
#pelo seu respectivo valor de correspondência em dias
idade_em_dias = ano*365 + mes*30 + dia

#Saída: Mensagem + idade total calculada em dias
print("SUa idade em dias é: " + str(idade_em_dias)) 