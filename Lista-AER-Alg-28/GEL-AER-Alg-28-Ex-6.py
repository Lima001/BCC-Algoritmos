def gerar_dicionário_tamanho_pavaras(nom_arquivo):
    dicionario_palavras = {}
    try:
        arquivo = open(nom_arquivo, "r")
        for linha in arquivo.readlines():
            palavras = linha.split(" ")
            for p in palavras:
                if len(p) not in dicionario_palavras.keys():
                    dicionario_palavras[len(p)] = [p]
                else:
                    dicionario_palavras[len(p)].append(p)

        arquivo.close()
        return dicionario_palavras
    
    except:
        return None

def achar_grupo_maior_tamanho(dicionario):
    maior = max(dicionario.keys())
    return (maior, dicionario[maior])

def main():
    nom_arquivo = input("Informe o nome do arquivo: ")
    
    dic = gerar_dicionário_tamanho_pavaras(nom_arquivo)
    grupo_maior = achar_grupo_maior_tamanho(dic)
    
    print(f"A(s) maior(es) palavra(s) tem tamanho {grupo_maior[0]} sendo ela(s):")
    for palavra in grupo_maior[1]:
        print(palavra, end="")

if __name__ == "__main__":
    main()