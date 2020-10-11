def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
    return hipotenusa

def main():
    cateto1 = float(input("Digite o 1º Cateto: "))
    cateto2 = float(input("Digite o 2º Cateto: "))

    print(f"Hipotenusa: {calcular_hipotenusa(cateto1, cateto2)}")

if __name__ == "__main__":
    main()