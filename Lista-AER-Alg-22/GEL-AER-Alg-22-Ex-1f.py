def duplicar_caracteres(string):
    nova_string = ""
    for i in string:
        nova_string += i*2
    
    return nova_string

def main():
    string = input("Digite a string: ")
    print(duplicar_caracteres(string))

if __name__ == "__main__":
    main()