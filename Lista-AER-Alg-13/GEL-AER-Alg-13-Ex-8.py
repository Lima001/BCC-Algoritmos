unidades = int(input("Digite a quantidade de produtos comprados: "))
vlr_unitario = float(input("Digite o valor unitário do produto: "))

vlr_total_compra = unidades * vlr_unitario
vlr_com_desconto = vlr_total_compra

if unidades > 15:
    vlr_com_desconto -= vlr_total_compra * 0.10

if vlr_total_compra > 100:
    vlr_com_desconto -= vlr_com_desconto * 0.20

print(f"Valor total: {vlr_total_compra}")
print(f"Valor com descontos calculados: {vlr_com_desconto}")