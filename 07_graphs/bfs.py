"""
BFS --> Breadth First Search

Visit all neighbors first, then their neigbors.
Like ripples in water --> spreads out level by level.

Real Word use: Finding shortest path (Google Maps)
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

from collections import deque

def bfs(graph, start):
    """
    Breadth First Search
    Visit all neighbors first, then their neighbors.
    Like ripples in water - level by level.
    """
    visited = []
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited

if __name__ == "__main__":
    print(bfs(graph, 'A'))