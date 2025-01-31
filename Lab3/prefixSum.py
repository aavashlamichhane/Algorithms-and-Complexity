import time
from multiprocessing import Pool
import random

def prefix_sum(arr):
    prefix_sums = [0] * len(arr)
    prefix_sums[0] = arr[0]
    
    for i in range(1, len(arr)):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]
    
    return prefix_sums

def parallel_prefix_sum(arr):
    def partial_sum(start, end):
        partial = [0] * (end - start)
        partial[0] = arr[start]
        for i in range(1, end - start):
            partial[i] = partial[i - 1] + arr[start + i]
        return partial

    num_workers = 4
    chunk_size = len(arr) // num_workers
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_workers)]
    chunks[-1] = (chunks[-1][0], len(arr))  # Ensure the last chunk covers the end of the array

    with Pool(processes=num_workers) as pool:
        partial_sums = pool.starmap(partial_sum, chunks)

    prefix_sums = [0] * len(arr)
    offset = 0
    for i, partial in enumerate(partial_sums):
        for j in range(len(partial)):
            prefix_sums[i * chunk_size + j] = partial[j] + offset
        offset = prefix_sums[(i + 1) * chunk_size - 1] if (i + 1) * chunk_size - 1 < len(arr) else offset

    return prefix_sums

# Example usage and comparison
if __name__ == "__main__":

    arr = [random.randint(1, 100) for _ in range(1000000)]
    print("Generated list of 1,000,000 elements ranging from 1 to 100")
    
    print("Running prefix sum algorithms...")
    start_time = time.time()
    normal_result = prefix_sum(arr)
    normal_time = time.time() - start_time
    print(f"Normal prefix sum time: {normal_time:.4f} seconds")
    
    print("Running parallel prefix sum algorithm...")
    start_time = time.time()
    parallel_result = parallel_prefix_sum(arr)
    parallel_time = time.time() - start_time
    print(f"Parallel prefix sum time: {parallel_time:.4f} seconds")
    
    assert normal_result == parallel_result, "Results do not match!"