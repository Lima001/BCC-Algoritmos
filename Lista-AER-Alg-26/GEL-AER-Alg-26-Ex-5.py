def verificar_anagrama(string1, string2):
    
    def gerar_dicionario_letras(string):
        dicionario = {}
        for i in string:
            if i not in dicionario.keys():
                dicionario[i] = 1
            else:
                dicionario[i] += 1
        
        return dicionario

    letras_string1 = gerar_dicionario_letras(string1)
    letras_string2 = gerar_dicionario_letras(string2)

    return letras_string1 == letras_string2

def main():
    string1 = input("Informe a primeira palavra: ")
    string2 = input("Informe a segunda palavra: ")

    if verificar_anagrama(string1, string2):
        print("As palavras são anagramas")
    else:
        print("As palavras NÃO são anagramas")

if __name__ == "__main__":
    main()