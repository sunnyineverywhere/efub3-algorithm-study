import sys
from collections import deque

input = sys.stdin.readline
total = int(input())
tree = [[] for _ in range(total + 1)]
parent = [0] * (total + 1)
qu = deque()
visited = [False] * (total + 1)

for _ in range(total - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs(start):
    qu = deque([start])
    visited[start] = True
    while qu:
        v = qu.popleft()
        for i in tree[v]:
            if not visited[i]:
                visited[i] = True
                parent[i] = v
                qu.append(i)


bfs(1)
for i in range(2, total + 1):
    print(parent[i])




