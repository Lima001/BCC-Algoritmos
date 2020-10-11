def verificar_anagrama(string1, string2):
    
    def gerar_dicionario_letras(string):
        dicionario = {}
        for i in string:
            if i.isalnum():
                if i.lower() not in dicionario.keys():
                    dicionario[i.lower()] = 1
                else:
                    dicionario[i.lower()] += 1
        
        return dicionario

    letras_string1 = gerar_dicionario_letras(string1)
    letras_string2 = gerar_dicionario_letras(string2)

    return letras_string1 == letras_string2

def main():
    string1 = input("Informe a primeira frase: ")
    string2 = input("Informe a segunda frase: ")

    if verificar_anagrama(string1, string2):
        print("As frases são anagramas")
    else:
        print("As frases NÃO são anagramas")

if __name__ == "__main__":
    main()