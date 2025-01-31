import multiprocessing
import random
import time

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sequential_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sequential_merge_sort(arr[:mid])
    right = sequential_merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort_2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pool = multiprocessing.Pool(processes=2)
    left, right = pool.map(sequential_merge_sort, [arr[:mid], arr[mid:]])
    pool.close()
    pool.join()
    return merge(left, right)

def parallel_merge_sort_all(arr):
    if len(arr) <= 1:
        return arr

    num_workers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_workers)

    size = len(arr) // num_workers
    chunks = [arr[i * size:(i + 1) * size] for i in range(num_workers)]
    sorted_chunks = pool.map(sequential_merge_sort, chunks)

    while len(sorted_chunks) > 1:
        extra = sorted_chunks.pop() if len(sorted_chunks) % 2 == 1 else None
        sorted_chunks = [pool.apply(merge, (sorted_chunks[i], sorted_chunks[i + 1])) for i in range(0, len(sorted_chunks), 2)]
        if extra:
            sorted_chunks.append(extra)

    pool.close()
    pool.join()

    return sorted_chunks[0]

if __name__ == "__main__":
    # Generate a large list of random integers
    large_list = [random.randint(0, 1000000) for _ in range(10000000)]
    print("Generated a large list of 10,000,000 random integers ranging from 0 to 1,000,000")

    # Built-in sort
    print("Sorting the list using built-in sort...")
    start_time = time.time()
    sorted_list_builtin = sorted(large_list)
    print(f"Built-in sort took {time.time() - start_time} seconds")

    # Sequential merge sort
    print("Sorting the list using sequential merge sort...")
    start_time = time.time()
    sorted_list_sequential = sequential_merge_sort(large_list)
    print(f"Sequential merge sort took {time.time() - start_time} seconds")

    # Parallel merge sort
    print("Sorting the list using parallel merge sort...")
    start_time = time.time()
    sorted_list_parallel = parallel_merge_sort_2(large_list)
    print(f"Parallel merge sort took {time.time() - start_time} seconds")
    
    #Totally Parallel merge sort
    print("Sorting the list using totally parallel merge sort...")
    start_time = time.time()
    sorted_list_parallel_all = parallel_merge_sort_all(large_list)
    print(f"Totally Parallel merge sort took {time.time() - start_time} seconds")