def verificar_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

def main():
    ano = int(input("Digite o ano(aaaa): "))
    if verificar_bissexto(ano):
        print(f"{ano} é bissexto")
    else:
        print(f"{ano} não é bissexto")

if __name__ == "__main__":
    main()