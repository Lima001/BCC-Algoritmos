import sys

def cat_python(lista_nome_arquivos):
    for nome_arquivo in lista_nome_arquivos:
        try:
            arquivo = open(nome_arquivo, "r")
            print(arquivo.read(),end="")
            arquivo.close()
        
        except:
            print(f"Arquivo {nome_arquivo} não encontrado")


def main():
    
    parametros = sys.argv[1:]

    if len(parametros) == 0:
        print("ERRO! Necessário passar caminho de arquivos como parâmtro...")
    else:
        cat_python(parametros)
    
    
if __name__ == "__main__":
    main()