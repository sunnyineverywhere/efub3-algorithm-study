#다익스트라 알고리즘을 출발지의 개수만큼 실행하면 시간초과
import heapq
from collections import defaultdict


def solution(n, paths, gates, summits):
    INF = 10000001
    intensity = [INF] * (n + 1)
    graph = defaultdict(list)
    for path in paths:
        graph[path[0]].append((path[2], path[1]))  # weight, a->b 지점
        graph[path[1]].append((path[2], path[0]))
    summits.sort()
    check = set(summits)


    def get_intensity():
        queue = []


        for gate in gates:
            heapq.heappush(queue, (0, gate))
            intensity[gate] = 0
        result = [0, INF]
        while queue:
            weight, now = heapq.heappop(queue)
            if now in check or weight > intensity[now]:
                continue

            for i in graph[now]:
                new_intensity = max(weight, i[0])
                if new_intensity < intensity[i[1]]:
                    intensity[i[1]] = new_intensity
                    heapq.heappush(queue, (new_intensity, i[1]))

        for summit in summits:
            if intensity[summit] < result[1]:
                result[0] = summit
                result[1] = intensity[summit]
        return result


    return get_intensity()