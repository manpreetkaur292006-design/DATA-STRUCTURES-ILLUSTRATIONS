# o(n^2) sorts + couting - (using bubble sort)

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, comparisons, swaps

arr = [10,23,53,21,12,9]
sorted_arr, comparisons, swaps = bubble_sort(arr)

print("\nSorted List:", sorted_arr)
print("Total Comparisons:", comparisons)
print("Total Swaps:", swaps)
