
# COMPLEXITY DRILL (OPEATION COUNTING)

# DEVELOPING INTUITION FOR TIME/SPACE COMPLEXITY USING SIMPLE LOOP 
# STRUCTURES AND CASE ANALYSIS .

# 1. SINGLE LOOP - O(n)

def single_loop(n):

    count=0

    for i in range(n):
        count+=1

    print("Number of operations performed :",count)
    print("Time Complexity - O(n)")
    print(f"Justification : Loop runs {n} times exactly .")
    print("Linear growth with input size.")

single_loop(int(input("Enter the number of iterations :")))


# 2. NESTED LOOP - O(n^2)

def nested_loop(n):

    count=0

    for i in range(n):
        for j in range(n):
            count+=1

    print(f"Number of operations performed : {count}")
    print("Time Complexity - O(n^2)")
    print(f"Justification : Outer loop runs {n} times, inner loop runs {n} times each.")
    print("Quadratic Growth - disastrous for large n")

nested_loop(int(input("Enter the number of iterations :")))


# 3. TRIANGULAR LOOP - O(n^2)
# 4. HALVING LOOP - O(log(n))

