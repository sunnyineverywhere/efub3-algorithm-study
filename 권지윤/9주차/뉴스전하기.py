import sys
sys.setrecursionlimit(10**6)
total = int(input())
com = [[] for _ in range(total)]
temp = list(map(int, input().split()))

for i in range(1, total):
    com[temp[i]].append(i)
    com[i].append(temp[i])


visited = [False] * total
dp = [0] * total

def dfs(start):
    child = []
    visited[start] = True
    for num in com[start]:
        if visited[num] == False:
            dfs(num)
            child.append(dp[num])

    if not child: #자식이 없으면 함수 끝냄
        return
    child.sort(reverse=True)
    max_num = 0

    for i in range(len(child)):
        if max_num < (child[i] + i+1):
            max_num = child[i] + 1+i
    dp[start] = max_num

dfs(0)

print(max(dp))