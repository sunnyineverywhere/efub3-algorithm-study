# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import copy
n, m = map(int, input().split())
ant = deque(map(int, input().split()))
ant.sort()
start, end = 0, 0
length = 0
while start < n and end < n:
    if ant[end] - ant[start] <= m:
        length = max(length, end - start + 1)
        end += 1
    else:
        start += 1
print(n - length)


