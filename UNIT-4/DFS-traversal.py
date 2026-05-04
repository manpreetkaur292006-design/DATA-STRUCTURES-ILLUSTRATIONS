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

def dfs_recursive(graph, node, visited, traversal_order):
    visited.add(node)
    traversal_order.append(node)
    print("Visiting", node)

    for neighbor, weight in graph.get(node, []):
        if neighbor not in visited:
            print(" -> Recur to", neighbor, "(w =", weight, ")")
            dfs_recursive(graph, neighbor, visited, traversal_order)

def dfs(graph, start_node):
    visited = set()
    traversal_order = []

    print("Starting DFS from:", start_node)
    dfs_recursive(graph, start_node, visited, traversal_order)

    return traversal_order, visited

start_node = 'A'
dfs_order, visited_nodes = dfs(graph, start_node)

print("\nFinal DFS traversal order:", dfs_order)
print("Visited nodes:", sorted(visited_nodes))
print("All nodes visited:", len(dfs_order) == len(graph))