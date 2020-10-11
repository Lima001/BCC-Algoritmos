def rfatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * rfatorial(numero-1)

def main():
    numero = -1
    while numero < 0:
        numero = int(input("Informe um numero inteiro positivo para calcular o fatorial: "))
        
    fatorial = rfatorial(numero)

    print(f"{numero}! = {fatorial}")

if __name__ == "__main__":
    main()