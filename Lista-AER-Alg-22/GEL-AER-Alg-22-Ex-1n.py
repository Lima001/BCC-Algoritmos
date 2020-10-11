def achar_string_em_outra(string1,string2):
    nova_string = ""
    pos_string1 = 0
    for i in string2:
        if i == string1[pos_string1]:
            nova_string += i
            pos_string1 += 1
        
        if len(nova_string) == len(string1):
            break
    
    return nova_string == string1

def main():
    string1 = input("Digite a 1º string: ")
    string2 = input("Digite a 2º string: ")
    print(achar_string_em_outra(string1,string2))

if __name__ == "__main__":
    main()