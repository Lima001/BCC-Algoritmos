from random import randint

num = int(input("Digite um valor entre 1 e 10: "))
#Não sei se o professor quer que verifcamos se num está em [1,10]
#poderiamos criar um while que só tem sua condição quebrada quando o número
#digitado condiz com o esperado
#num = -1
#while num < 0 or num > 10:
#   num = int(input("..."))

soma = 0
aleatorio = -1

while aleatorio != num:
    aleatorio = randint(1,11)
    
    #Somente para testes
    #print(aleatorio, end=" ")
    
    if aleatorio == num:
        break
    soma += aleatorio

print("Soma:", soma)