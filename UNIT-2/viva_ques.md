
# VIVA QUESTIONS 

## ARRAY 1D (OPERATIONS + SHIFTING COST)

## 1. WHY INDEX ACCESS IS O(1) ? 
**Answer :** Arrays store elements in contiguous memory. Given index i, CPU calculates exact memory address instantly: address = base_address + i * element_size. No traversal/loop needed - direct jump.

## 2. WHY INSERTION AT START IS O(N) ?
**Answer :** Inserting at position 0 requires shifting ALL n elements one position right: for i=n-1 down to 0: arr[i+1] = arr[i]. Worst case shifts entire array. End insertion = O(1), no shifting.

## 3. STATIC V/S DYNAMIC ARRAYS ?
**Answer :** Static: Fixed size declared at compile-time (C: int arr[100]). Overflow crashes.
Dynamic: Resizes automatically when full (Python lists, Java ArrayList). Doubles capacity on overflow → amortized O(1) append.

## ARRAY 2D (MATRIX TRAVERSAL + OPERATIONS)

## 1. COMPLEXITY OF SCANNING A MATRIX ?
**Answer :** O(rows × cols). Nested loops visit every element: for i in rows: for j in cols: visit(matrix[i][j]). No shortcuts for complete scan.

## 2. REAL-WORLD USE OF 2D ARRAYS ?
**Answer :** Images (RGB pixels), games (chess boards), tables/spreadsheets, distance matrices (GPS), pixel grids (graphics), game maps.

## 3. MEMORY LAYOUT IDEA (ROW-WISE) ?
**Answer :** Row-major order: Entire row0, row1, row2... stored continuously. matrix[i][j] = base + (i*cols + j)*size. Fast row access, column access jumps.

## DYNAMIC ARRAY SIMULATION (RESIZE + POP)

## 1. WHAT IS AMORTIZED COMPLEXITY ?
**Answer :** Average time over sequence of operations. Rare O(n) resize (when full) + many O(1) appends → total ~2n operations / n appends = O(1) average.

## 2. WHY DOUBLING HELPS ?
**Answer :** Resizes happen logarithmically: cap=4→8→16→32... Total copy cost: n/2 + n/4 + n/8... < 2n. Without doubling (increment by 1), every append copies → O(n²).

## 3. WHY POP-END IS O(1) ?
**Answer :** Just size--. No shifting/copying. Last element conceptually "removed" by moving size pointer. Internal array unchanged.

## SINGLY LINKED LIST (CORE OPERATIONS)

## 1. WHY SEARCH IS O(N) ?
**Answer :** 
## 2. WHY INSERT-AT-HEAD IS O(1) ?
**Answer :**
## 3. NODE STRUCTURE ?
**Answer :**

## DOUBLY LINKED LIST (EXTENDED OPERATIONS)

## 1. DLL ADVANTAGE OVER SLL ?
**Answer :**
## 2. BROWSER HISTORY MAPPING ?
**Answer :**
## 3. DELETION EASE IN DLL ?
**Answer :**

## STACK USING SLL + PARENTHESES CHECKER

## 1. WHY STACK IS IDEAL HERE ?
**Answer :**
## 2. WHAT FAILS IN "([)]" ?
**Answer :**
## 3. UNDERFLOW MEANING ?
**Answer :**

## QUEUE USING SLL (O(1) OPERATIONS)

## 1. BFS USES QUEUE ?
**Answer :**
## 2. FIFO MEANING ?
**Answer :**
## 3. SCHEDULING EXAMPLE ?
**Answer :**