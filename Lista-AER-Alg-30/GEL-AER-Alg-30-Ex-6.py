pot_memorizado = {0:1}

def rpotenciacao(base, expoente):
    if expoente in pot_memorizado:
        return pot_memorizado[expoente]
    
    val = base * rpotenciacao(base, expoente-1)
    pot_memorizado[expoente] = val

    return val

def main():
    x = float(input("Digite a base x: "))
    n = -1
    while n < 0:
        n = int(input("Digite o expoente n positivo e inteiro: "))

    pot_memorizado[1] = x

    print(f"{x} ^ {n} = {rpotenciacao(x,n)}")

if __name__ == "__main__":
    main()