from itertools import combinations


def dfs(graph, start, visited):
    visited[start] = True
    cnt = 1
    for next_node in graph[start]:
        if not visited[next_node]:
            cnt += dfs(graph, next_node, visited)
    return cnt


def solution(n, wires):
    answer = float('inf')

    for w in wires:
        # 간선을 하나 끊어보기
        temp_wires = wires.copy()
        temp_wires.remove(w)

        # 그래프 초기화
        graph = [[] for _ in range(n + 1)]
        for a, b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)

        # 방문 여부 초기화
        visited = [False] * (n + 1)

        # 각 연결 요소의 크기를 저장할 리스트
        component_sizes = []

        for start in range(1, n + 1):
            if not visited[start]:
                component_sizes.append(dfs(graph, start, visited))

        # 두 개의 하위 그래프를 선택하여 노드 개수의 차이를 계산
        for size1, size2 in combinations(component_sizes, 2):
            answer = min(answer, abs(size1 - size2))

    return answer
