from collections import deque

n, k = map(int, input().split())
#순서에 영향이 있음 -> 경우의 수가 많음 -> 이진 탐색? -> 하지만 경우의 수가 많음 -> 실패
#bfs로 하기 -> 단순 +1만 되는게 아니라 3가지 경우가 있으므로 queue에 담을 때


MAX = 100001 # -1인 경우도 있으므로
check = [False] * MAX
dist = [-1] * MAX

qu = deque()
qu.append(n)
check[n] = True # BFS 알고리즘의 핵심은 "가장 먼저 방문한 경로가 최단 경로"입니다. 만약 한 번 방문한 위치를 다시 방문하게 되면, 그것은 무조건 원래 방문했던 경로보다 길거나 같은 경로일 것입니다.
dist[n] = 0 #과정을 업데이트하는 배열

while qu:
    num = qu.popleft()


    if num+1 <= MAX and check[num+1] == False:
        qu.append(num+1)
        check[num+1] = True
        dist[num+1] = dist[num] +1
    if num-1 <= MAX and check[num-1] == False:
        qu.append(num-1)
        check[num-1] = True
        dist[num-1] = dist[num] +1
    if num*2 <= MAX and check[num*2] == False:
        qu.append(num*2)
        check[num * 2] = True
        dist[num*2] = dist[num]

print(dist[k])
