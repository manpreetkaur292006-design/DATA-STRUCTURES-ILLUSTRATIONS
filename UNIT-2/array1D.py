
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
    shifts = 0
    # Shift right from end to pos
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]
        shifts += 1
    arr[pos] = value
    return arr[:n + 1], shifts  # Return sliced to new length

def delete_at(arr, pos):
    n = len(arr)
    if n == 0 or pos < 0 or pos >= n:
        print("Deletion not possible")
        return arr, 0
    shifts = 0
    # Shift left from pos to end
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]
        shifts += 1
    return arr[:n - 1], shifts  # Slice off last

def print_complexity(pos, n, is_insert):
    if is_insert:
        if pos == n:
            print("Complexity: O(1) (at end)")
        else:
            print("Complexity: O(n) (shifting)")
    else:
        if pos == n - 1:
            print("Complexity: O(1) (at end)")
        else:
            print("Complexity: O(n) (shifting)")

# Main demo
arr = [10, 20, 30, 40, 50]
max_capacity = 100
print("Initial array:")
print_array(arr)

shifts = 0

# Insert START (pos=0)
print("\nInsert at START:")
arr, shifts = insert_at(arr, 0, 5, max_capacity)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(0, len(arr), True)

# Insert MIDDLE (pos = len/2)
print("\nInsert at MIDDLE:")
mid_pos = len(arr) // 2
arr, shifts = insert_at(arr, mid_pos, 99, max_capacity)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(mid_pos, len(arr), True)

# Insert END (pos=len)
print("\nInsert at END:")
arr, shifts = insert_at(arr, len(arr), 999, max_capacity)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(len(arr)-1, len(arr), True)

# Delete START (pos=0)
print("\nDelete at START:")
arr, shifts = delete_at(arr, 0)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(0, len(arr), False)

# Delete MIDDLE
print("\nDelete at MIDDLE:")
mid_pos = len(arr) // 2
arr, shifts = delete_at(arr, mid_pos)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(mid_pos, len(arr), False)

# Delete END
print("\nDelete at END:")
arr, shifts = delete_at(arr, len(arr)-1)
print("Updated array:")
print_array(arr)
print(f"Shift count: {shifts}")
print_complexity(len(arr), len(arr), False)
