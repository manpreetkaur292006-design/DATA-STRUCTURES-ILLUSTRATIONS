# 🎯  VIVA QUESTIONS 

## ➡️ Sorts + Counting

## 1. STABLE V/S UNSTABLE ?
**Answer :** Stable sorting keeps equal elements in same relative order after sorting. Unstable sorting may change their order. Bubble sort is stable because it swaps only adjacent unequal elements.

## 2. IN-PLACE MEANING ?
**Answer :** In-place means algorithm uses very little extra memory (usually O(1)). Sorting happens inside same array without creating another array.

## 3. WHY O(N²) IS SLOW ?
**Answer :** Nested loops compare elements repeatedly. For n elements, comparisons ≈ n × n. Large inputs cause huge number of operations, making it slow.


## ➡️ INSERTION SORT

## 1. WORST-CASE INPUT ?
**Answer :** Reverse sorted array. Every new element must shift all previous elements right, causing maximum comparisons and shifts.

## 2. IS INSERTION STABLE ?
**Answer :** Yes. Equal elements are not swapped unnecessarily, so their original relative order remains same.

## 3. SPACE COMPLEXITY ?
**Answer :** O(1). Uses only a temporary variable for shifting/insertion. No extra array required.


## ➡️ MERGE SORT

## 1. WHY STABLE ?
**Answer :** During merging, if two elements are equal, left-side element is chosen first. Original order of equal elements is preserved.

## 2. WHY NEEDS EXTRA MEMORY ?
**Answer :** Merge process creates temporary arrays to combine sorted halves. Extra storage required for copying elements.

## 3. USE IN EXTERNAL SORTING ?
**Answer :** Used for huge files/data stored on disk. Merge sort efficiently merges sorted chunks without loading complete data into RAM.


## ➡️ QUICK SORT

## 1. WORST-CASE FOR QUICK SORT ?
**Answer :** Already sorted or reverse sorted array with bad pivot choice (first/last element). Partitions become highly unbalanced.

## 2. IS QUICK SORT STABLE ?
**Answer :** No. Equal elements may swap across partitions, changing original order.

## 3. AVERAGE TIME ?
**Answer :** O(N log N). Balanced partitions divide array efficiently, giving fast average performance.


## ➡️ HEAP SORT

## 1. WHY HEAP SORT NOT STABLE ?
**Answer :** Heap operations swap distant elements. Equal elements may change relative order during heapify/extraction.

## 2. HEAP V/S BST FOR TOP-K ?
**Answer :** Heap is better for top-k because insertion/removal is O(log k). BST may become unbalanced and slower.

## 3. REAL PRIORITY QUEUE USE ?
**Answer :** CPU scheduling, Dijkstra shortest path, printer queues, task scheduling systems.


## ➡️ SORTING CONCEPT QUESTIONS

## 1. WHY REVERSE IS WORST FOR INSERTION ?
**Answer :** Every element must shift all previous elements right before insertion. Maximum shifts/comparisons occur.

## 2. WHY QU8ICK MAY DEGRADE ON SORTED WITH BAD PIVOT ?
**Answer :** Bad pivot creates one large partition and one empty partition repeatedly → recursion depth becomes n → O(N²).

## 3. WHY MERGE STABLE BUT USES MEMORY ?
**Answer :** Stable because merge keeps equal elements in order. Extra memory needed for temporary arrays during merging.