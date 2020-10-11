lista_palavras = []
exe = True
while exe:
    palavra = input("Digite uma palavra: ")
    if palavra != "":
        if palavra not in lista_palavras:
            lista_palavras.append(palavra)
    else:
        exe = False

for i in lista_palavras:
    print(i)