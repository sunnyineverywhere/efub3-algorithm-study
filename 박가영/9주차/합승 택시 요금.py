import heapq
from math import inf

def solution(n, s, a, b, fares): # 지점개수, 출발지점, A 도착지점, B 도착지점, 예상 택시 요금
    def dijkstra(src, dst):
        distance = [inf] * (n+1)
        queue = []
        distance[src] = 0
        heapq.heappush(queue, (0, src))

        while queue:
            d, now = heapq.heappop(queue)

            if distance[now] < d:
                continue

            for node, cost in graph[now]:
                cost += d
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(queue, [cost, node])
        
        return distance[dst]
    
    global graph
    graph = [[] for _ in range(n+1)]
    for i, j, fare in fares:
            graph[i].append([j, fare])
            graph[j].append([i, fare])
    

    # 아예 따로 가는 경우
    cost =  dijkstra(s, a) + dijkstra(s, b)

    # i까지 합승하고, 이후 따로 가는 경우
    for i in range (1, n+1):
         if s != i: # 출발지는 경유지에서 제외
              cost_i = dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)
              cost = min(cost, cost_i)
    
    return cost


