def rpalindromo(string):
    
    def formatar_string(string):
        nova_string = ""
        for i in string.lower():
            if i.isalpha():
                nova_string += i.lower()

        return nova_string

    string = formatar_string(string)

    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and rpalindromo(string[1:-1])

def main():
    string = input("Informe a string: ")
    if rpalindromo(string):
        print("É palíndromo")
    else:
        print("NÃO é palíndromo")

if __name__ == "__main__":
    main()