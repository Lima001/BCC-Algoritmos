fib_memorizado = {0:0, 1:1}

def rfibonacci(n):
    if n in fib_memorizado:
        return fib_memorizado[n]

    val = rfibonacci(n-1) + rfibonacci(n-2)
    fib_memorizado[n] = val
    
    return val

def main():
    n = int(input("Digite o valor de n para achar o enéssimo termo de fibonacci: "))
    fibonacci = rfibonacci(n)
    
    print(f"O {n}º da sequência de Fibonacci é {fibonacci}")

if __name__ == "__main__":
    main()