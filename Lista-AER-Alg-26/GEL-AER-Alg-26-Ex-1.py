def caracteres_unicos(string):
    string = string.lower()
    return len(set(string)) == len(string)

def main():
    string = input("Informe a string: ")
    print(caracteres_unicos(string))

if __name__ == "__main__":
    main()