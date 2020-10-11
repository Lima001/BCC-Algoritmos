def verificar_igual(string1,string2):
    if len(string1) != len(string2):
        return False
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False

    return True

def main():
    string1 = input("Digite a 1º string: ")
    string2 = input("Digite a 2º string: ")
    print(verificar_igual(string1,string2))

if __name__ == "__main__":
    main()