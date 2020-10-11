import sys

def head_python(arquivo):
    for linha in arquivo.readlines()[:10]:
        print(linha, end="")

def main():
    if len(sys.argv) > 1:
        try:
            arquivo = open(sys.argv[1], "r")
            head_python(arquivo)
            arquivo.close()         
        
        except:
            print("ERRO! Problemas ao abrir e efetuar o processamento do arquivo.", end=" ")
            print("Verifique se o caminho informado está correto...")

    else:
        print("ERRO! É necessaŕio informar um caminho de arquivo via linha de comando...")


if __name__ == "__main__":
    main()