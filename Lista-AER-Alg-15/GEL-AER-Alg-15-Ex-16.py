print("Solução I")
inicio = 100
while inicio >= 0:
    print(inicio, end=" ")
    inicio -= 5

print("\n\nSolução II")

inicio = 100
while inicio >= 0:
    if inicio%5 != 0:
        inicio -= 1
        continue
    
    print(inicio, end=" ")
    inicio -= 1