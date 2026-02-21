
# TOWER OF HANOI (N=3 TRACE + COMPLEXITY)

# Tower of Hanoi is a simple game:

# 3 rods (A, B, C) + some circles of different sizes (disks)

# START: All circles stacked on rod A (biggest at bottom, smallest at top)
# GOAL: Move ALL circles to rod C (same order)

# 3 SIMPLE rules:
# 1. Move only 1 circle at a time
# 2. NEVER put bigger circle on smaller circle
# 3. Can only move the topmost circle from any rod


def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    
    hanoi(n-1, src, dst, aux)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n-1, aux, src, dst)

print("=== TOWER OF HANOI n=3 (7 moves) ===")
hanoi(3, 'A', 'B', 'C')

move_count = [0]
def hanoi_count(n, src, aux, dst, count):
    if n == 1:
        count[0] += 1
        return
    hanoi_count(n-1, src, dst, aux, count)
    hanoi_count(n-1, aux, src, dst, count)

print("\n=== MOVE COUNT n=4 ===")
move_count[0] = 0
hanoi_count(4, 'A', 'B', 'C', move_count)
print(f"n=4 needs {move_count[0]} moves")

print("\n=== COMPLEXITY ===")
print("Time Complexity: O(2^n)")
print("n=1: 1 move, n=2: 3 moves, n=3: 7 moves, n=4: 15 moves")
print("Pattern: 2^n - 1 = EXPONENTIAL GROWTH!")
