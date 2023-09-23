from collections import deque
def bfs(distance, graph):
    qu = deque()
    qu.append(1)
    distance[1] =1
    while qu:
        a = qu.popleft()
        for k in graph[a]:
            if distance[k] == -1:
                distance[k] = distance[a] + 1
                qu.append(k)
    return distance