total, goal = map(int, input().split())
wire = []
for _ in range(total):
    wire.append(int(input()))
high = max(wire)

low = 1

while low <= high:
    mid = (low + high) //2
    result = 0
    for num in wire:
        result += (num//mid)
    if goal <= result:
        low = mid + 1
        answer = mid
    else:
        high = mid-1

print(answer)


