A_star1.py

import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue for open list (min-heap)
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))  # (f, node)

    # Dictionaries for g, parent, and closed list
    g_cost = {start: 0}
    parent = {start: None}
    closed_list = set()

    while open_list:
        # Select node with lowest f(n)
        f, current = heapq.heappop(open_list)

        # If goal found, reconstruct path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]

        # Move to closed list
        closed_list.add(current)

        # Expand neighbors
        for neighbor, cost in graph[current].items():
            tentative_g = g_cost[current] + cost
            f_value = tentative_g + heuristics[neighbor]

            if neighbor in closed_list:
                continue

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current
                heapq.heappush(open_list, (f_value, neighbor))

    # If open list empty and goal not found
    return None, float("inf")


# Example graph
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

# Run A*
start, goal = 'S', 'G'
path, cost = a_star_search(graph, heuristics, start, goal)

print("Optimal Path:", path)
print("Total Cost:", cost)


