vlr_compra = int(input("Digite o valor da compra: "))
vlr_pago = int(input("Digite o valor pago: "))

troco = vlr_pago - vlr_compra

qtd_nota100 = troco//100
qtd_nota10 = (troco%100)//10
qtd_nota1 = (troco%100)%10

print("Valor da compra: ", vlr_compra)
print("Valor pago ao caixa: ", vlr_pago)
print("Troco:")
print(str(qtd_nota1) + " x R$ 1,00")
print(str(qtd_nota10) + " x R$ 10,00")
print(str(qtd_nota100) + " x R$ 100,00")