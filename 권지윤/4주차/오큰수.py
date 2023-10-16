from collections import deque
total = int(input())
num = list(map(int, input().split()))
que = deque()
answer =[-1] * total
for i in range(total):
    while que and num[que[-1]] < num[i]:
            answer[que.pop()] = num[i]
    que.append(i)
print(" ".join(map(str, answer)))