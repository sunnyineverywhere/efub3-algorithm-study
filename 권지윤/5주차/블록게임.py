# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#처음에는 2차원 배열로 하려고 했다가 -> "무한히"늘어날 수 있다고 해서 stack으로 변경
time = int(input())
direction = input()
scores = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
stack = []
x, y = 0, 0
stack.append((x, y, 1))
table = []
table.append((x, y))
for i in range(time):
    c = direction[i]
    if c == "R":
        x = dx[1] + x
        y = dy[1] + y

    if c == "L":
        x = dx[0] + x
        y = dy[0] + y


    if c == "U":
        x = dx[3] + x
        y = dy[3] + y

    if c == "D":
        x = dx[2] + x
        y = dy[2] + y
    while (x, y) in table:
        tx, ty, num = stack.pop()
        table.remove((tx, ty))
    stack.append((x, y, scores[i]))
    table.append((x, y))

total = 0
for i in range(len(stack)):
    tx, ty, num = stack.pop()
    total += num


print(total)