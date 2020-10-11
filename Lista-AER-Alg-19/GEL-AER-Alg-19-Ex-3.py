def formar_triangulo(comp1, comp2, comp3):
    if comp1 >= comp2 + comp3:
        return False
    elif comp2 >= comp1 + comp3:
        return False
    elif comp3 >= comp1 + comp2:
        return False
    else:
        return True

def main():
    lado1 = float(input("Digite o comprimento do 1º lado: "))
    lado2= float(input("Digite o comprimento do 2º lado: "))
    lado3 = float(input("Digite o comprimento do 3º lado: "))

    if formar_triangulo(lado1, lado2, lado3):
        print("Os lados informados formam um triângulo")
    else:
        print("Os lados informados não formam um triângulo")

if __name__ == "__main__":
    main()