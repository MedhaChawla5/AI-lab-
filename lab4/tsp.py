from queue import Queue

def tsp_bfs(graph, start):
    # Create a queue for BFS
    queue = Queue()
    
    # Initialize the queue with the starting node and its path
    queue.put((start, [start], 0))

    # Initialize the minimum cost
    min_cost = float('inf')

    # Perform BFS
    while not queue.empty():
        current_node, path, cost = queue.get()

        # Check if all nodes are visited
        if set(path) == set(graph.keys()):
            # Add the cost to return to the starting node
            cost += graph[current_node][start]
            # Update the minimum cost
            min_cost = min(min_cost, cost)
        else:
            # Enqueue neighbors of the current node
            for neighbor, weight in graph[current_node].items():
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_cost = cost + weight
                    queue.put((neighbor, new_path, new_cost))

    return min_cost

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}

start_node = 'A'
result = tsp_bfs(graph, start_node)
print(f"Minimum TSP cost starting from {start_node}: {result}")
