def rfibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfibonacci(n-1) + rfibonacci(n-2)

def main():
    n = int(input("Digite o valor de n para achar o enéssimo termo de fibonacci: "))
    fibonacci = rfibonacci(n)
    print(f"O {n}º da sequência de Fibonacci é {fibonacci}")

if __name__ == "__main__":
    main()