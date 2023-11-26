import heapq
from math import inf

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    intensity = [inf] * (n + 1) 
    for i, j, w in paths:
        graph[i].append([j,w])
        graph[j].append([i, w])

    summits.sort()
    summits_set = set(summits)

    queue = []
    for gate in gates:
            heapq.heappush(queue, (0, gate))
            intensity[gate] = 0
    
    while queue:
         d, now = heapq.heappop(queue)
         if intensity[now] < d or now in summits_set:
              continue
         for weight, next in graph[now]:
              next = max(intensity[now], next)
              if next < intensity[weight]:
                intensity[weight] = next
                heapq.heappush(queue, (next, weight)) 
    
    result = [0, inf]
    for summit in summits:
         if intensity[summit] < result[1]:
              result[0] = summit
              result[1] = intensity[summit]
    return result
         

              


