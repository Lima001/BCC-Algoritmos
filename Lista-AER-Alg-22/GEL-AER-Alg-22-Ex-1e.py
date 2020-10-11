def remover_substring(string,caractere):
    return string.replace(caractere,"")

def main():
    string = input("Digite a string: ")
    caractere = input("Digite o caractere: ")
    print(remover_substring(string,caractere))

if __name__ == "__main__":
    main()