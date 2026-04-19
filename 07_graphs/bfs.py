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