def prefix_sum(arr):
    prefix_sums = [0] * len(arr)
    prefix_sums[0] = arr[0]
    
    for i in range(1, len(arr)):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]
    
    return prefix_sums

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    print("Prefix sums:", prefix_sum(arr))