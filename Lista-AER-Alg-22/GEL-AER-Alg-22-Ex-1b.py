def imprimir_na_vertical(string):
    for letra in string:
        print(letra)

def main():
    string = input("Informe a string: ")
    imprimir_na_vertical(string)

if __name__ == "__main__":
    main()