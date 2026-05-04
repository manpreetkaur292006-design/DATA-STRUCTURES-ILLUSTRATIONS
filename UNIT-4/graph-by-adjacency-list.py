graph = {}
edges = [
    ('A', 'B', 4),   
    ('A', 'C', 2),
    ('B', 'D', 5),
    ('B', 'E', 3),
    ('C', 'D', 1),
    ('C', 'F', 6),
    ('D', 'E', 2),
    ('E', 'F', 4),
    ('F', 'A', 7)
]

for source, destination, weight in edges:
    if source not in graph:
        graph[source] = []
    graph[source].append((destination, weight))
    
    if destination not in graph:
        graph[destination] = []

print("Directed Weighted Graph (Adjacency List):")
for node in sorted(graph.keys()):
    if graph[node]:  # Has outgoing edges
        neighbors = []
        for to_node, weight in graph[node]:
            neighbors.append(f"{to_node}({weight})")
        neighbor_str = ', '.join(neighbors)
        print(f"{node}: {neighbor_str}")
    else:
        print(f"{node}: (no outgoing edges)")

print("\nGraph Summary:")
print("Nodes:", sorted(graph.keys()))
print("Total edges:", sum(len(graph[node]) for node in graph))