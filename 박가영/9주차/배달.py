import heapq
from math import inf

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [inf] * (N+1)

    for a, b, time in road:
        graph[a].append([b, time])
        graph[b].append([a, time])
    
    queue = []
    start = 1
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        d, now = heapq.heappop(queue)
        if distance[now] < d:
            continue
        for node, cost in graph[now]:
            new_cost = d + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(queue, (new_cost, node))

    for d in distance:
        if d <= K: # 배달이 가능한 마을
                answer += 1
    
    return answer




