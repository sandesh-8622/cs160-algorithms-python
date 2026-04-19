"""
DFS --> Depth First Search

Go as deep as poosible first and then backtrack
like exploreing a maze need to go down one path until the dead end.

Real world use---> Finding connected components, cycle detection.
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def dfs(graph, start, visited=[]):
    """Depth First Search---> Go deep first, then you have to backtrack."""
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)
    return visited

if __name__ == "__main__":
    print(dfs(graph, 'A', []))