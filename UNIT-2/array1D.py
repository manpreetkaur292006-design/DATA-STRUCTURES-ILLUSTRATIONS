
# ARRAY 1D (OPERATIONS + SHIFTING COST)

# UNDERSTANDING HOW TO INSERT/DELETE IN ARRAYS CAUSES SHIFTING AND IMPACTS COMPLEXITY.

# 1-D ARRAY : A one-dimensional (1D) array is a linear data structure that
#             stores a sequence of elements of the same data type in contiguous memory locations, 
#             accessed using a single index (subscript).

# ANSWER : 

def print_array(arr):
    print(' '.join(map(str, arr)))

def insert_at(arr, pos, value, max_capacity):
    n = len(arr)
    if n == max_capacity or pos < 0 or pos > n:
        print("Insertion not possible")
        return arr, 0
    shifts = n - pos  # Exact shift count
    new_arr = arr[:pos] + [value] + arr[pos:]
    return new_arr, shifts

def delete_at(arr, pos):
    n = len(arr)
    if n == 0 or pos < 0 or pos >= n:
        print("Deletion not possible")
        return arr, 0
    shifts = n - pos - 1  # Exact shift count
    new_arr = arr[:pos] + arr[pos+1:]
    return new_arr, shifts

def print_complexity(pos, n, is_insert):
    if is_insert:
        print("Complexity: O(1)" if pos == n else "Complexity: O(n) (shifting)")
    else:
        print("Complexity: O(1)" if pos == n-1 else "Complexity: O(n) (shifting)")

# Main demo
arr = [10, 20, 30, 40, 50]
max_capacity = 100
print("Initial array:")
print_array(arr)

# All operations
print("\nInsert START:")
arr, shifts = insert_at(arr, 0, 5, max_capacity)
print("Updated:", end=' '); print_array(arr); print(f"Shifts: {shifts}"); print_complexity(0, 5, True)

print("\nInsert MIDDLE:")
arr, shifts = insert_at(arr, len(arr)//2, 99, max_capacity)
print("Updated:", end=' '); print_array(arr); print(f"Shifts: {shifts}"); print_complexity(2, 6, True)

print("\nInsert END:")
arr, shifts = insert_at(arr, len(arr), 999, max_capacity)
print("Updated:", end=' '); print_array(arr); print(f"Shifts: {shifts}"); print_complexity(6, 7, True)

print("\nDelete START:")
arr, shifts = delete_at(arr, 0)
print("Updated:", end=' '); print_array(arr); print(f"Shifts: {shifts}"); print_complexity(0, 7, False)

print("\nDelete END:")
arr, shifts = delete_at(arr, len(arr)-1)
print("Updated:", end=' '); print_array(arr); print(f"Shifts: {shifts}"); print_complexity(5, 6, False)
