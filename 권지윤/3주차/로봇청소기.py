N, M = map(int, input().split())
direct_X = [-1, 0, 1, 0]
direct_Y = [0, 1, 0, -1]

start_x, start_y, direct = map(int, input().split())
table = []

for _ in range(N):
    table.append(list(map(int, input().split())))

def clean(x, y, d):
    global total

    if table[x][y] == 0: # 1) 아직 청소하지 않는 경우 청소
        table[x][y] = 2
        total += 1

    for _ in range(4): # 주변 탐색
        d = (d + 3) % 4 #회전 후
        nx = x + direct_X[d]#전진
        ny = y + direct_Y[d]
        #왜 여기서 주변 4칸 중 청소되지 않은 빈칸이 있는 경우까지 확인해야하지 않나? -> 다 확인할 필요없이 90도 돌린 값 체크한 김에 체크하면 한 번에 된다.

        if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 0: #그게 청소되지 않는다면
            clean(nx, ny, d)
            return

    nx = x - direct_X[d]
    ny = y - direct_Y[d]

    if 0 <= nx < N and 0 <= ny < M and table[nx][ny] != 1:
        clean(nx, ny, d)
    else:
        return

total = 0
clean(start_x, start_y, direct)
print(total)
