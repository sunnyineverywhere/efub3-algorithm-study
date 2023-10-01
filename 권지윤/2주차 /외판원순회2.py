import sys

# dfs
def dfs(start,cur,cost):
    global matrix, visit, minCost

    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)

    for i in range(n):
        if not matrix[cur][i] == 0 and not visit[i]:
            visit[i] = True
            dfs(start,i,cost+matrix[cur][i])
            visit[i] = False

# main
n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

# dfs
minCost = float('inf')
visit = [False for _ in range(n)]
dfs(0,0,0)

print(minCost)