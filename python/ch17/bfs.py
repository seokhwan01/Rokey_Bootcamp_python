def my_bfs(graph, start_node):
    queue = list()  # BFS에서 사용할 큐(Queue) 생성
    visited = list()  # 방문한 노드를 저장할 리스트 생성

    queue.append(start_node)  # 시작 노드를 큐에 추가

    while queue:  # 큐가 비어있지 않은 동안 반복
        node = queue.pop(0)  # 큐의 첫 번째 원소(노드)를 꺼냄 (FIFO 방식)

        if node not in visited:  # 방문하지 않은 노드라면
            queue.extend(graph[node])  # 현재 노드의 인접 노드들을 큐에 추가
            visited.append(node)  # 방문한 노드 리스트에 추가

    print("bfs - ", visited)  # BFS 탐색 경로 출력
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
my_bfs(myGraph, 'A')  # 'A' 노드에서 시작하는 BFS 실행