# Benchmark Harness

# Measure execution time fairly and compare algorithms on different input types.


import random
import time

# INSERTION SORT
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
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

# QUICK SORT 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)

# TIMING FUNCTION 
def measure_time(sort_function, data):
    copied_data = data[:]
    start = time.time()
    sort_function(copied_data)
    end = time.time()
    total_time = end - start
    return total_time

# MAIN PROGRAM 
sizes = [1000, 5000, 10000]
data = []
for i in range(sizes):
    number = random.randint(1, 10000)

    data.append(number)
algorithms = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}
dataset_types = ["Random", "Sorted", "Reverse"]

# Print table header
print("\n========== TIMING TABLE ==========\n")
print(f"{'Algorithm':<18} {'Dataset':<12} {'1000':<12} {'5000':<12} {'10000':<12}")
print("-" * 60)

# Run benchmarks
for algo_name, algo_func in algorithms.items():
    for dtype in dataset_types:
        times = []
        for size in sizes:
            # Generate datasets
            if dtype == "Random":
                data = [random.randint(1, 100000) for _ in range(size)]
            elif dtype == "Sorted":
                data = list(range(size))
            elif dtype == "Reverse":
                data = list(range(size, 0, -1))
            # Measure execution time
            t = measure_time(algo_func, data)
            times.append(t)
        # Print row
        print(f"{algo_name:<18} {dtype:<12} {times[0]:<12} {times[1]:<12} {times[2]:<12}")