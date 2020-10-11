def imprimir_em_escada(string):
    for pos in range(1,len(string)+1):
        print(string[0:pos])

def main():
    string = input("Digite a string: ")
    imprimir_em_escada(string)

if __name__ == "__main__":
    main()