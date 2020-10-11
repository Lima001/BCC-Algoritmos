#Entrada: distância
distancia = float(input("Digite a distância em km: "))

#Processamento: Calculo do gasto de combustivel através da divisão
# do valor da entrada pela eficiência do veículo(dado pelo problema)
#Saída: Mensagem com o total de litros gastos
print("A quantidade de litros gasta foi: " + str(distancia/12) + " L")