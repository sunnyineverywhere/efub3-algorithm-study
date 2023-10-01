import sys

input = sys.stdin.readline
R, C, T = map(int, input().split())
table= []
cleaner = []
for i in range(R):
    table.append(list(map(int, input().split())))
    for j in range(C):
        if table[i][j] == -1:
            cleaner.append(i)


temp = []
def do_cleaner_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    up = cleaner[0]
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        table[x][y], before = before, table[x][y]
        x = nx
        y = ny

def do_cleaner_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    down  = cleaner[1]
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        table[x][y], before = before,table[x][y]
        x = nx
        y = ny

def do_dust():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    diffu = [[0] * C for _ in range(R)]
    for dr in range(R):
        for dc in range(C):
            if table[dr][dc] != -1 and table[dr][dc] != 0:
                count = 0
                for q in range(4):
                    nx = dr + dx[q]
                    ny = dc + dy[q]
                    if 0 <= nx < R and 0 <= ny < C:
                        if table[nx][ny] != -1:
                            diffu[nx][ny] += table[dr][dc] // 5
                            count += table[dr][dc] // 5
                table[dr][dc] -= count


    for i in range(R):
        for j in range(C):
            table[i][j] += diffu[i][j]




for _ in range(T):
    do_dust()
    do_cleaner_up()
    do_cleaner_down()

total = 0
for t in range(R):
    for tt in range(C):
        if table[t][tt] > 0:
            total += table[t][tt]

print(total)
