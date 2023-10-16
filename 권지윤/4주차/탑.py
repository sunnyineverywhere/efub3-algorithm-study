#자기보다 낮으면 0
#자기보다 높으면
#전체로 하면
from collections import deque
n = int(input())
top = list(map(int, input().split()))
stack = []
answer =[0] * n
cnt = 0

for i in range(n):
    while stack:
        if stack[-1][1] < top[i]:
            stack.pop()
        else:
            answer[i]= stack[-1][0] +1
            break
    stack.append((i, top[i]))

print(" ".join(map(str, answer)))