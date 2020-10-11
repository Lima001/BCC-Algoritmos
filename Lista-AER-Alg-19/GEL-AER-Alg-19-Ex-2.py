def calcular_vlr_total(qtd_produto):
    total = 0
    for i in range(qtd_produto):
        if i != 0:
            total += 2.95
        else:
            total += 10.95
    return total

def main():
    qtd_itens = int(input("Digite a quantidade de itens: "))
    print("Total:", calcular_vlr_total(qtd_itens))

if __name__ == "__main__":
    main()