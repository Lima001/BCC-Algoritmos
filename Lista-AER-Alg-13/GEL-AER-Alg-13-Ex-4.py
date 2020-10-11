#Criei uma função mais geral, que funciona para mais de duas notas
def calcular_media(*notas):
    '''
    Dadas n notas, calcula e retorna a média aritmética entre elas
    '''
    soma = 0
    for n in notas:
        soma += n
    
    media = soma/len(notas)
    return media

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

media = calcular_media(nota1,nota2)

if media >= 5 and nota1 >= 3 and nota2 >= 3.0:
    print(f"Parabéns, você foi aprovado! Sua média foi {media}")
    if media >= 9.0:
        print("Tmabém convidamos você para ser monitor no próximo semestre")
else:
    print(f"Infelizmente você não foi aprovado. Sua média foi {media}")
    print(f"E suas notas foram {nota1}, {nota2}")