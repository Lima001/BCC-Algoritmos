def numerar_linhas_arquivo(arquivo_entrada, arquivo_saida):
    contador = 1
    for linha in arquivo_entrada.readlines():
        linha_numerada = f"{contador}: {linha}"
        arquivo_saida.write(linha_numerada)
        contador += 1


def main():
    entrada = input("Digite o arquivo de entrada: ")
    saida = input("Digite o arquivo de saída: ")

    try:
        arquivo_entrada = open(entrada, "r")
        arquivo_saida = open(saida, "w")
        numerar_linhas_arquivo(arquivo_entrada, arquivo_saida)
        arquivo_entrada.close()
        arquivo_saida.close()         
    
    except:
        print("ERRO! Problemas ao abrir e efetuar o processamento do arquivo.", end=" ")
        print("Verifique se o caminho informado está correto...")

if __name__ == "__main__":
    main()