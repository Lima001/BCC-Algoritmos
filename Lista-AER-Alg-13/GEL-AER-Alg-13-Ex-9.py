gm = float(input("Digite o valor gasto com material: "))
tc = float(input("Digite o tempo de duração em horas: "))
cmo = float(input("Digite o custo de mão de obra por hora: "))
ac = float(input("Digite a metragem de área construida: "))

if ac/tc < 0.035:
    cmo += cmo * 0.30

ct = gm + cmo * tc
r = gm / (cmo * tc)
lucro = 0

if r > 1.5:
    lucro = gm * 0.05

elif r >= 0.5 and r <= 1.5:
    lucro = ct * 0.08

elif r < 0.5:
    lucro = (cmo * tc) * 0.10

preco_venda_imovel = ct + lucro

print(f"Preço de venda do imóvel: {preco_venda_imovel}")