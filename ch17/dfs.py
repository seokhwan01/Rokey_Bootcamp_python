def my_dfs(graph, start_node):
    stack = list()      # 탐색을 위한 스택(Stack) 생성
    visited = list()    # 방문한 노드를 저장할 리스트 생성

    stack.append(start_node)  # 시작 노드를 스택에 추가

    while stack:   # 스택이 비어있지 않은 동안 반복
        node = stack.pop()  # 스택에서 마지막 원소(노드)를 꺼냄

        if node not in visited:  # 방문하지 않은 노드라면
            stack.extend(reversed(graph[node]))  # 인접 노드들을 스택에 추가 (역순으로 추가)
            visited.append(node)  # 방문한 노드 리스트에 추가

    print("dfs - ", visited)  # DFS 탐색 경로 출력
    return visited  # 방문한 노드 리스트 반환

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


my_dfs(myGraph, 'A')  # 'A' 노드에서 시작하는 DFS 실행
