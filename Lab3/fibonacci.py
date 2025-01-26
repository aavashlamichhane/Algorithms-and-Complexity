def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def dynamic_fibonacci(n):
    fib = {}
    def fib_helper(n):
        if n in fib:
            return fib[n]
        if n == 0:
            fib[n] = 0
        elif n == 1:
            fib[n] = 1
        else:
            fib[n] = fib_helper(n-1) + fib_helper(n-2)
        return fib[n]
    return fib_helper(n)

