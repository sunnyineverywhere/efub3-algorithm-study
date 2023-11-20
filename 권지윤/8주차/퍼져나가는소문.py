# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
total = int(input())
rel = int(input())
friend = [[] for i in range(0, total+1)]
visited = [False for _ in range(total+1)]
for _ in range(rel):
	a, b = map(int, input().split())
	friend[a].append(b)
	friend[b].append(a)
cnt = 1
def dfs(idx):
	global cnt
	if idx > total:
		return
	for f in friend[idx]:
		if visited[f] == False:
			visited[f] = True
			dfs(f)
			cnt +=1
visited[1] = True
dfs(1)

print (cnt)