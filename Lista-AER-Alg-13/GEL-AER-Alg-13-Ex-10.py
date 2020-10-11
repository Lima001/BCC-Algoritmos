from math import pi, ceil

altura = float(input("Digite a altura do  cilindro metros: "))
raio = float(input("digite o raio do cilindro em metros: "))

#Calculo da area total do cilindro
area_base = 2 * pi * raio**2
area_largura = 2 * pi * raio * altura
area_total = area_base + area_largura

#Descobrir quantos litros são necessários
qtd_litros = area_total/3

#Descobrir quantas latas serão necessárias
#Observando que foi considerado só podemos comprar latas inteiras
#Foi utilziada a função ceil para arredondar o valor
qtd_latas = ceil(qtd_litros/5)
custo = qtd_latas * 20.0

print(f"Para pintar o cilindro de {area_total}m², será necessário {qtd_litros} litros de tintas")
print(f"Sendo necessário a compra de {qtd_latas} latas, totalizando um preço de R$ {custo}")