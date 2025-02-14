def my_dfs(graph, start_node):
    stack=list()
    visited=list()
    
    stack.append(start_node)
    
    while stack:
        node=stack.pop()
        
        if node not in visited:
            stack.extend(reversed(graph[node]))
            #graph['A'] = ['B', 'C', 'D']
            #스택은 LIFO (Last-In-First-Out) /
            #구조이므로 마지막에 추가된 노드부터 먼저 탐색합니다.
            visited.append(node)
    print("dfs - ",visited)
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
my_dfs(myGraph,"A")
