#문제에서 "가로로 자르기" 가 어떤 의미인지 정확히 파악하지 않았음
row , col = map(int, input().split())
num = int(input())
r = [0, col]
c = [0, row]
for _ in range(num):
    a, b = map(int,input().split())
    if a == 0:
        r.append(b)
    elif a == 1:
        c.append(b)

#가로
r.sort()
c.sort()
max_r = []
max_c = []
for i in range(1, len(r)):

    max_r.append(r[i]- r[i-1])
for j in range(1, len(c)):
    max_c.append( c[j] - c[j-1])

print(max(max_c) * max(max_r))