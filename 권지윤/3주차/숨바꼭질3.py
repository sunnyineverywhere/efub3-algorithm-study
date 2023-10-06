from collections import deque

n, k = map(int, input().split())
#순서에 영향이 있음 -> 경우의 수가 많음 -> 이진 탐색? -> 하지만 경우의 수가 많음 -> 실패
#bfs로 하기 -> 단순 +1만 되는게 아니라 3가지 경우가 있으므로 queue에 담을 때


MAX = 100001 # -1인 경우도 있으므로
dist = [-1 for _ in range(100001)]
#원래는 방문 확인 배열 1개와 거리를 업데이트하는 배열 2개를 두고 얬는데

qu = deque()
qu.append(n)
 # BFS 알고리즘의 핵심은 "가장 먼저 방문한 경로가 최단 경로"입니다. 만약 한 번 방문한 위치를 다시 방문하게 되면, 그것은 무조건 원래 방문했던 경로보다 길거나 같은 경로일 것입니다.
dist[n] = 0 #과정을 업데이트하는 배열

while qu:
    num = qu.popleft()
    if num == k:
        print(dist[k])
        break
    if 0 <= num-1 < MAX and dist[num-1] == -1: # 2로 곱할 수 있게 만들어주는 것이므로 2보다 우선순위 높음
        qu.append(num-1)

        dist[num-1] = dist[num] +1
    if 0 < num*2 < MAX and dist[num*2] == -1: # 가장 우선순위 높음
        # 0일 때 곱하면 소용없음
        qu.appendleft(num*2) #높은 우선순위를 위해
        dist[num*2] = dist[num]
    if 0 <= num+1 < MAX and dist[num+1] == -1:
        qu.append(num+1)

        dist[num+1] = dist[num] +1


