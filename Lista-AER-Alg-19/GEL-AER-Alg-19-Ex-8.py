def calcula_percent(valor, porcentagem):
    return valor * (porcentagem/100)

#Letra a)
def adicionar_taxas(vlr_base):
    total = vlr_base
    total += calcula_percent(vlr_base, 50) #Adição Imposto Importação
    imposto_circulacao = calcula_percent(total, 3) #Imposto Circulação
    total += imposto_circulacao #Adicação do Imposto Circulação
    #Adição Taxa de Entrega
    total += calcula_percent(vlr_base, 10) + calcula_percent(imposto_circulacao, 2)

    return total

#Letra b)
def dar_desconto(codigo):
    xx = codigo // 100
    yy = codigo % 100

    preco_basico = xx * 15 + yy
    percentual_desconto = yy

    total = preco_basico - calcula_percent(preco_basico, percentual_desconto)
    
    return total

def main():
    print("Letra a)")
    vlr_produto = float(input("Digite o valor do produto: "))
    print("Valor + Taxas:", adicionar_taxas(vlr_produto), end="\n"*2)
    
    print("Letra b)")
    codigo_produto = int(input("Digite o código do produto(4 digitos): "))
    print("Valor promoção:", dar_desconto(codigo_produto))

if __name__ == "__main__":
    main()