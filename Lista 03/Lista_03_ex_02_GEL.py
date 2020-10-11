n = int(input("Digite o valor de n: "))

c = n//100
d = (n%100)//10
u = (n%10)
m = (u*100) + (d*10) + c

print("N:", n)
print("M:", m)