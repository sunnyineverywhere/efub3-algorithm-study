import sys
import heapq

INF = int(1e9)
# MAX_POSITION = int(100000)

n, k = map(int, input().split())




#제너레이터
def adj_move(x): 
    yield(x-1, 1) #걸어서 x-1로 이동
    yield(x+1, 1) #걸어서 x+1로 이동
    yield(2*x, 0) #순간이동으로 2x로 이동

def is_valid(x):
    return 0 <= x and x<= 100000

def dijkstra(n,k):
    time = [INF] * (100001) # 동생 위치는 최대 10만
    time[n] = 0 # 시작점 n, 시간 0
    q = [(n,0)]

    while q:
        current_x, current_time = heapq.heappop(q)

        if current_time > time[current_x]:
            continue

        for adj_x, adj_time in adj_move(current_x): #걸으면 가중치 1, 순간이동 가중치 0
            cal_time = current_time + adj_time

            if is_valid(adj_x) and cal_time < time[adj_x]:
                time[adj_x] = cal_time
                heapq.heappush(q, (adj_x, cal_time))

    return time[k]

print(dijkstra(n,k))
