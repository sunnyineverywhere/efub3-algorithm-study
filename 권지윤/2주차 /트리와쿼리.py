import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 이거 없으면 메모리 초과, 있으면 50퍼까지 갔다가 런타임 에러 -> Pypy는 적용 안됨

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
count = [0] * (N+1)
def precount(r):
    count[r] = 1
    for t in tree[r]:
        if not count[t]:
            precount(t)
            count[r] += count[t]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

precount(R)

for _ in range(Q):
    num = int(input())
    print(count[num])

