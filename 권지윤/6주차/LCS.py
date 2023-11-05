first = input()
second = input()
cache = [0] * len(second)

for i in range(len(first)):
    cnt = 0
    for j in range(len(second)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif second[j] == first[i]:
            cache[j] = cnt + 1
print(max(cache))