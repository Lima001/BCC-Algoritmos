def duplicar_vogais(string):
    vogais = "aeiou"
    nova_string = ""
    for i in string:
        if i in vogais:
            nova_string += i
        nova_string += i

    return nova_string

def main():
    string = input("Digite a string: ")
    print(duplicar_vogais(string))

if __name__ == "__main__":
    main()