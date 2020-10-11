n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
f = int(input("Digite o número de faltas: "))

m = (n1 + n2)/2

if m < 5 or n1 < 3 or n2 < 3 or f >= 15:
    print("Infelizmente você não foi aprovado")
    
    if f < 15:
        nf = 10 - m
        print("Mas você não foi reprovado por faltas, e tem direito a prova final")
        print(f"Para ser aprovado na prova final, sua nota deve ser >= {nf}")
    
    else:
        print(f"Você excedeu o limite de faltas, totalizando {f} faltas")
        print(f"Sua média foi {m}")

else:
    print(f"Parabéns, você foi aprovado! Sua média final foi {m}")