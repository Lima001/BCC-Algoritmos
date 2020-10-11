#Entradas: Valor de cada parte da refeição
vlr_prato_principal = float(input("Digite o valor do prato principal: "))
vlr_sobremesa = float(input("Digite o valor da sobremesa: "))
vlr_suco = float(input("Digite o valor do suco: "))

#Processamento: Soma das entradas e adição da taxa de 10% sobre o valor da soma
soma = vlr_prato_principal+vlr_sobremesa+vlr_suco
soma += soma*0.10

#Saída: Mensagem com o valor total da conta
print("O valor total a ser pago é: " + str(soma) + " R$")