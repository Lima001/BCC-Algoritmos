nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
media = (nota1 + nota2 + nota3)/3

print("Nome: " + nome)
print("Notas:", nota1,nota2,nota3)
print("Média:", media)

if nota1 != 5 and nota2 != 5 and nota3 != 5 and media > 7:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")