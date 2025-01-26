import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(10000)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

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
            fib[n] = fib_helper(n - 1) + fib_helper(n - 2)
        return fib[n]

    result = fib_helper(n)
    return result

def measure_time(func, n, k = 1):
    start = time.time()
    for i in range(k):
        func(n)
    end = time.time()
    return (end - start)/k

input_sizes = list(range(5, 40))
print(input_sizes)
recursive_times = [measure_time(fibonacci, n, 5) for n in input_sizes]
dynamic_times = [measure_time(dynamic_fibonacci, n, 5) for n in input_sizes]

plt.figure(figsize=(12, 6))

# Plot recursive times (skipping None values)
plt.plot(
    input_sizes,
    recursive_times,
    label="Recursive Fibonacci",
    marker="o",
    color="red"
)

# Plot dynamic times
plt.plot(input_sizes, 
         dynamic_times, 
         label="Dynamic Fibonacci", 
         marker="o", 
         color="blue")

# Graph formatting
plt.title("Performance Comparison: Recursive vs Dynamic Fibonacci")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
