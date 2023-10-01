n, m=map(int, input().split())

maze=[]

for i in range(n):
    maze.append(list(map(int, input()))) #미로 정보 입력

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4): #큐에서 꺼낸 노드의 상하좌우 체크
            nx=x+dx[i]
            ny=y+dy[i]
            if 0>nx or nx>=n or 0>ny or ny>=m: #미로 밖은 제외. 0~n-1 0~m-1 범위에서 움직여야
                continue
            if maze[nx][ny]==0: #괴물이 있는 부분도 피해서
                continue
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1 #다음 나아갈 곳에 현재의 최단거리 +1 값 넣기
                queue.append((nx,ny))

    return maze

print(bfs(0,0))