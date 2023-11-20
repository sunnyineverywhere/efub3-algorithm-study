
total = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_val = -1e9
min_val = 1e9
def dfs(i, val):
    global max_val, min_val, add, mul, sub, div
    if i == total:
        min_val = min(val, min_val)
        max_val = max(val, max_val)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, val + num[i])
            add +=1
        if sub > 0:
            sub -=1
            dfs(i + 1, val - num[i])
            sub +=1
        if mul > 0:
            mul -= 1
            dfs(i + 1, int(val * num[i]))
            mul +=1
        if div > 0:
            div -= 1
            dfs(i + 1, int(val / num[i]))
            div +=1



dfs(1, num[0])
print(max_val)
print(min_val)

