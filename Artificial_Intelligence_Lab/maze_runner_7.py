from collections import deque

# Function to find the start (S) and end (E) positions in the maze
def find_start_end(maze):
    start = None
    end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

# Check if a position is valid for traversal
def is_valid(r, c, maze, visited):
    rows, cols = len(maze), len(maze[0])
    return (
        0 <= r < rows and
        0 <= c < cols and
        maze[r][c] != '#' and
        (r, c) not in visited
    )

# BFS to find the shortest path
def bfs(maze):
    start, end = find_start_end(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path  # Found the shortest path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, maze, visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

# DFS to find any path
def dfs(maze):
    start, end = find_start_end(maze)
    stack = [(start, [start])]
    visited = set([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == end:
            return path  # Found a path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, maze, visited):
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

# Print maze with path marked as '*'
def print_path(maze, path):
    maze_copy = [list(row) for row in maze]
    for r, c in path:
        if maze_copy[r][c] not in ('S', 'E'):
            maze_copy[r][c] = '*'
    for row in maze_copy:
        print(''.join(row))

# Example maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', 'E', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

print("Original Maze:")
for row in maze:
    print(''.join(row))

# Solve using BFS
print("\nBFS Solution (Shortest Path):")
bfs_path = bfs(maze)
if bfs_path:
    print_path(maze, bfs_path)
else:
    print("No path found!")

# Solve using DFS
print("\nDFS Solution (Any Path):")
dfs_path = dfs(maze)
if dfs_path:
    print_path(maze, dfs_path)
else:
    print("No path found!")

