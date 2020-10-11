def verificar_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Digite um numero inteiro positivo para ver se é primo: "))
    if verificar_primo(numero):
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")

if __name__ == "__main__":
    main()