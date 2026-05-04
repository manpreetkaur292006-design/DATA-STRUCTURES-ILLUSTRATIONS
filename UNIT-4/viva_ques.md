# 🎯  VIVA QUESTIONS 

## ➡️ BST insert/search/inorder

## 1. Why inorder gives sorted ?
**Answer:** BST property: left < root < right. Inorder (Left→Root→Right) visits left subtree (smaller), root, right subtree (larger) → ascending order guaranteed.

## 2. Worst-case BST height ?
**Answer:** O(n) - skewed tree (sorted input like 1,2,3,... creates linked list).

## 3. Average complexity ?
**Answer:** O(log n) for insert/search/delete (balanced random insertions).


## ➡️ BST Delete (All cases)

## 1. Inorder successor meaning ?
**Answer:** Smallest node in right subtree (next in sorted inorder traversal). Used in 2-child delete: copy successor value, delete successor leaf.

## 2. Why delete is tricky ?
**Answer:** Must maintain BST property. 2-child case hardest: replace with inorder successor/predecessor, then delete that successor (always 0/1 child).

## 3. How to verify correctness ?
**Answer:** Print inorder traversal before/after → must remain sorted. Check BST property: all left < node < all right recursively.


## ➡️ Heap/Priority Queue (Industry)

## 1. Why heap for priority queues ?
**Answer:** Complete binary tree guarantees min/max root. Insert/extract O(log n) vs linear scan O(n) in arrays/lists.

## 2. Insert/extract complexity ?
**Answer:** Both O(log n). Insert: heapify-up from leaf. Extract: heapify-down from root.

## 3. Where used in industry ?
**Answer:** Task scheduling (Kubernetes), Dijkstra's algorithm, median maintenance, event processing, job queues (RabbitMQ).


## ➡️ Graph Build (Adjacency list)

## 1. List vs matrix ?
**Answer:** List: O(V+E) space (sparse graphs), O(deg) neighbors. Matrix: O(V²) space (dense graphs), O(1) edge check.

## 2. Directed vs undirected ?
**Answer:** Directed: edge A→B ≠ B→A (adj list stores one way). Undirected: store both directions.

## 3. Weighed graph use ?
**Answer:** Dijkstra, shortest path, MST (Prim/Kruskal). Weights in tuples: graph[A] = [('B',4), ('C',2)].


## ➡️ BFS traversal

## 1. Why queue in BFS ?
**Answer:** FIFO queue processes level-by-level: closer nodes first, ensures shortest path by #edges.

## 2. Shortest path relation ?
**Answer:** Finds shortest path (fewest edges) in unweighted graphs. Weighted needs Dijkstra.

## 3. Complexity O(V+E) ?
**Answer:** Visit each vertex V once + each edge E once (adj list traversal).


## ➡️ DFS Traversal 

## 1. DFS vs BFS ?
**Answer:** DFS: deep first (stack/recursion), good for paths/Maze. BFS: level first (queue), shortest path.

## 2. Recursion depth issue ?
**Answer:** Stack overflow if graph depth > recursion limit (~1000). Use iterative stack DFS for safety.

## 3. Use case of DFS ?
**Answer:** Cycle detection, topological sort, connected components, path finding, maze solving.


## ➡️ Hash Table (separate chaining)

## 1. Collision meaning ?
**Answer:**  Different keys hash to same index. Chaining: linked list per bucket holds all collided keys.

## 2. Why chaining works ?
**Answer:** Degrades gracefully to linear search in bucket. Average O(1+α) where α=load factor <1.

## 3. Load factor ?
**Answer:** Degrades gracefully to linear search in bucket. Average O(1+α) where α=load factor <1.


## ➡️ Trie (prefix tree)

## 1. Trie vs hash map for prefix ?
**Answer:** Trie: O(L) prefix traversal (shared paths). Hashmap: O(nL) scan all strings for prefix.

## 2. Space trade-off ?
**Answer:** Trie: O(ALPHABET × total chars) worst case, but saves space on common prefixes vs n×L strings.

## 3. Autocomplete use ?
**Answer:** Google search, IDE intellisense, mobile keyboards. Prefix → suggest completions from subtree.


## ➡️ Bloom Filter (Concept + Toy Demo)

## 1. Can bloom filter have false negatives ?
**Answer:** No - "definitely not present" is always correct. False positives only ("possibly present").

## 2. Why memory efficient ?
**Answer:** Bit array (1 bit/item) vs full items. Trade accuracy for ~10-100× space savings.

## 3. Industry use (DB, cache, security) ?
**Answer:** Cassandra (avoid disk reads), Redis (set membership), Google Chrome (malware URLs), Bitcoin (UTXO set).