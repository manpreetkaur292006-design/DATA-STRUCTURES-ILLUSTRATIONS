from collections import deque
graph = {}
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 5), ('B', 'E', 3),
    ('C', 'D', 1), ('C', 'F', 6),
    ('D', 'E', 2),
    ('E', 'F', 4),
    ('F', 'A', 7)
]

for src, dest, weight in edges:
    if src not in graph:
        graph[src] = []
    graph[src].append((dest, weight))
    if dest not in graph:
        graph[dest] = []

def bfs(graph, start_node):
    visited = set()         
    queue = deque()       
    traversal_order = []     
    
    queue.append(start_node)
    visited.add(start_node)
    
    print(f"Starting BFS from: {start_node}")
    print("Queue:", queue)
    
    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        print(f"Dequeued {current}, Order so far: {traversal_order}")
        
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor) 
                print(f"  Enqueued {neighbor} (from {current}, w={weight})")
    
    return traversal_order

start_node = 'A'
bfs_order = bfs(graph, start_node)

print(f"\nFinal BFS traversal order: {bfs_order}")
print("All nodes visited:", len(bfs_order) == len(graph))