numero = int(input("Digite um numero de 5 algarismo: "))

a = numero//10000
b = (numero%10000)//1000
c = ((numero%10000)%1000)//100
d = (((numero%10000)%1000)%100)//10
e = (((numero%10000)%1000)%100)%10

s = (6*a + 5*b + 4*c + 3*d + 2*e)
digitoV = s%7

print("DigitoV:", digitoV)