def my_bfs(graph,start_node):
    queue=list()
    visited=list()
    
    queue.append(start_node)
    
    while queue:
        node=queue.pop(0)
        
        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    print("bfs - ",visited)
    return visited

myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}
my_bfs(myGraph,"A")