def calcular_IMC(altura, peso):
    return peso / altura**2

altura = float(input("Digite sua altura em metros: "))
massa = float(input("Digite seu peso em Kg: "))

imc = calcular_IMC(altura, massa)
print(f"Seu IMC: {imc}")

if imc < 18.5:
    print("Alerta! Você está abaixo do peso Ideal")
else:
    print("Você não está abaixo do peso")