exe = True
while exe:

    n = int(input("Digite um número: "))
    divisor = 1
    primo = True

    print(f"Divisores de {n}:")

    while divisor <= n:
        if n%divisor == 0:
            print(divisor, end=" ")
            
            if divisor != 1 and divisor != n:
                primo = False

        divisor += 1

    if primo:
        print()
        print(f"{n} é primo")

    continuar = int(input("\nDeseja analisar outro numero (0 Não, 1 Sim): "))
    if continuar == 0:
        exe = False