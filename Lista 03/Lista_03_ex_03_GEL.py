data = int(input("Digite a data em formato DDMMAA: "))

d = data//10000
m = (data//100)%100
a = data%100

data_inversa = (a*10000)+(m*100)+(d)

print("AAMMDD:", '{:06}'.format(data_inversa))