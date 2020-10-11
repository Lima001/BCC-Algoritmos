n = int(input("Digite o valor de n: "))
impar = 1
somatorio = 0

while 0 < n:
    somatorio += impar
    n -= 1
    impar += 2

print(somatorio)