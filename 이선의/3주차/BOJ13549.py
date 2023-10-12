'''
현재 = 점 N
동생 = 점 K
INPUT = (N, K)

1초 후 -> X-1, X+1
순간이동 -> 0초 후에 2*X
'''

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100000
array = [-1] * (MAX + 1)  # 인덱스마다 걸린 시간 저장

q = deque()
q.append(n)  # 시작 지점
array[n] = 0

while q:
    x = q.popleft()  # 첫번째 위치
    if x == k:  # 동생 위치와 같을 때
        print(array[x])
        break
    if 0 < x*2 <= MAX and array[x*2] == -1:
        array[x*2] = array[x]
        q.appendleft(x*2)
    for nx in (x - 1, x + 1):
        if 0 <= nx <= MAX and array[nx] == -1:
            array[nx] = array[x] + 1
            q.append(nx)
