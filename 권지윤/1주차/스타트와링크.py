from itertools import combinations

n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

member = [k for k in range(1, n + 1)]
answer = float('inf')

#중복 계산을 피하기 위한 사전 계산
pre_calculated = {}
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        pre_calculated[(i, j)] = table[i - 1][j - 1] + table[j - 1][i - 1]
def cal(li):
    result = 0
    for mem1, mem2 in combinations(li, 2):
        result += pre_calculated[(min(mem1, mem2), max(mem1, mem2))]
    return result

for start in combinations(member, n//2):
    remaining = [x for x in member if x not in start]
    for link in combinations(remaining, n//2):
        start_able = cal(start)
        link_able = cal(link)
        answer = min(answer, abs(start_able - link_able))

print(answer)
