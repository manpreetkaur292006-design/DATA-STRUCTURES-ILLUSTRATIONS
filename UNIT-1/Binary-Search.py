
# RECURSSIvE BINARY SEARCH

# IMPLEMENTING THE BINARY SEARCH RECURSSIVELY 
# AND EXPLAINING ITS TIME COMPLEXITY - O(LOG(N))

def binarySearch(arr, key, low, high):
    if low > high:
        print(f"Key {key} NOT FOUND")
        return -1
    
    mid = low + (high - low) // 2
    
    print(f"low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarySearch(arr, key, low, mid-1)
    else:
        return binarySearch(arr, key, mid+1, high)

print("=== BINARY SEARCH DEMO ===")
arr = [1, 3, 5, 7, 9, 11, 13, 15]

print("\n1. FOUND case:")
print("Index:", binarySearch(arr, 7, 0, len(arr)-1))

print("\n2. NOT FOUND case:")
print("Index:", binarySearch(arr, 8, 0, len(arr)-1))

print("\n3. EMPTY array:")
empty_arr = []
print("Index:", binarySearch(empty_arr, 5, 0, len(empty_arr)-1))

print("\n=== RECURRENCE EXPLANATION ===")
print("T(n) = T(n/2) + O(1)")
print("n=8 → 4 → 2 → 1 → O(log n)")
