#Pensei em utilizar expressões regulares, mas achei que ficaria mais interessante
#desenvolver sem utilizar a biblioteca re. De toda forma
#deixei comentado o código usando essa outra maneira...
#import re
#def retornar_lista_palavras_re(string):
#    lista_palavras = []
#    for sentenca in string.split(" "):
#        palavra = re.sub("[^\w]","",sentenca)
#        lista_palavras.append(palavra)

#    return lista_palavras

def retornar_lista_palavras(string):
    lista_palavras = []
    for sentenca in string.split(" "):
        palavra = ""
        for letra in sentenca:
            if letra.isalpha():
                palavra += letra
        
        lista_palavras.append(palavra)

    return lista_palavras            

def main():
    string = input("Informe seu texto: ")
    lista_palavras = retornar_lista_palavras(string)
    print(lista_palavras)

if __name__ == "__main__":
    main()