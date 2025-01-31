import random
import time

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

import matplotlib.pyplot as plt

# Function to generate random weights and values
def generate_random_data(n, max_weight, max_value):
    weights = [random.randint(1, max_weight) for _ in range(n)]
    values = [random.randint(1, max_value) for _ in range(n)]
    return weights, values

random_weights, random_values = generate_random_data(10, 10, 100)
print("Random Weights:", random_weights)
print("Random Values:", random_values)
capacity = sum(random_weights) // 2  # Example capacity
print("Capacity of Knapsack =", capacity)
print("Maximum value in Knapsack =", knapsack(random_weights, random_values, capacity))

# Measure processing time for varying input sizes
input_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
times = []

for size in input_sizes:
    weights, values = generate_random_data(size, 100, 100)
    capacity = sum(weights) // 2  # Example capacity
    start_time = time.time()
    knapsack(weights, values, capacity)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting the results
plt.plot(input_sizes, times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Processing Time (seconds)')
plt.title('Knapsack Problem Processing Time')
plt.grid(True)
plt.show()