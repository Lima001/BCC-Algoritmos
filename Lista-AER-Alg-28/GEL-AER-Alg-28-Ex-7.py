import sys

def mapear_frequencia_letras(arquivo):
    dicionario_frequencia = {}

    for linha in arquivo.readlines():
        for palavra in linha:
            for caractere in palavra:
                if caractere.isalpha():
                    if caractere.lower() not in dicionario_frequencia.keys():
                        dicionario_frequencia[caractere.lower()] = 1
                    else:
                        dicionario_frequencia[caractere.lower()] += 1
    
    return dicionario_frequencia


def exibir_em_percentual(dicionario_frequencia):
    total = sum(dicionario_frequencia.values())

    print("Frequência Percentual das Letras")
    for chave in sorted(dicionario_frequencia.keys()):
        print(f"Letra {chave} = {dicionario_frequencia[chave] / total * 100}%")

def main():
    if len(sys.argv) > 1:
        try:
            arquivo = open(sys.argv[1], "r")
            dicionario_frequencia = mapear_frequencia_letras(arquivo)
            arquivo.close()
            exibir_em_percentual(dicionario_frequencia)           
        
        except:
            print("ERRO! Problemas ao abrir e efetuar o processamento do arquivo")
            print("verifique se o caminho informado está correto...")

    else:
        print("ERRO! É necessaŕio informar um caminho de arquivo via linha de comando...")

if __name__ == "__main__":
    main()