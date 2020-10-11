def rsoma(lista_valores):
    if len(lista_valores) == 1:
        return lista_valores[0]
    
    return lista_valores[0] + rsoma(lista_valores[1:])

def main():
    n = int(input("Informe quantos valores deseja adicionar a lista: "))
    
    if n >= 1:
        lista_valores = []
        
        for i in range(n):
            numero = float(input(f"Digite o {i+1}º numero: "))
            lista_valores.append(numero)

        print("Resultado:", rsoma(lista_valores))
    
    else:
        print("Quantidade informada inválida!")

if __name__ == "__main__":
    main()