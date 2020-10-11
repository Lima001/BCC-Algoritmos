nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

#Não sei se tem que verificar se as notas estão em um intervalo válido
#if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
#   print("Notas Inválidas") 
#   exit()

media = (nota1 + nota2)/2

print(f"Notas: {nota1}, {nota2}")
print(f"Média: {media}")