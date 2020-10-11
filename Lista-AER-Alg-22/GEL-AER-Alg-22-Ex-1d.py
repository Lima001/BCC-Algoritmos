def imprimir_em_escada(string):
    for i in range(len(string)):
        print(string[0:len(string)-i])

def main():
    string = input("Digite a string: ")
    imprimir_em_escada(string)

if __name__ == "__main__":
    main()