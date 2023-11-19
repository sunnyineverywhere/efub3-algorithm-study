T = int(input())
for tc in range(1,T+1):

    N = int(input())
    result = [[0]*N for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    dir =0
    r, c = 0, 0
    num = 1


    while num <= N*N:


        if (0 <= r < N and 0 <= c < N) and result[r][c] == 0:
            result[r][c] = num
            num += 1


        else:

            r -= dr[dir]
            c -= dc[dir]

            dir = (dir + 1) % 4

        r += dr[dir]
        c += dc[dir]

    print(f'#{tc}')
    for row in result:
        print(*row)