print("Primeira maneira...")

for i in range(100,-1,-5):
    print(i, end=" ")


print("\nSegunda maneira...")

for i in range(100,-1,-1):
    if i%5 == 0:
        print(i, end=" ")