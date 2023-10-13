# 프로그래머스
#

angle = [0, 90, 180, 270]

# 2차원 리스트 회전
def rotate(array, x):
    n = len(array)
    result = [[0] * n for _ in range(n)]

    if x == 90:
        for r in range(n):
            for c in range(n):
                result[c][n - r - 1] = array[r][c]

    elif x == 180:
        for r in range(n):
            for c in range(n):
                result[n - r - 1][n - c - 1] = array[r][c]
    elif x == 270:
        for r in range(n):
            for c in range(n):
                result[n - c - 1][r] = array[r][c]
    else:
        for r in range(n):
            for c in range(n):
                result[r][c] = array[r][c]

    return result

def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    m, n = len(key), len(lock)

    new_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    
    for i in range(1, n * 2):
        for j in range(1, n * 2):
            # 열쇠를 0, 90, 180, 270도로 회전시키며 확인
            for k in angle:
                rotate_key = rotate(key, k)
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += rotate_key[x][y]
                
                if check(new_lock):
                    return True
                
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] -= rotate_key[x][y]

    return False