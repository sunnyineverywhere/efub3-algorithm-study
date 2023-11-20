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
    if goal <= result: #goal < result와 goal == result를 분리하여 처리할 경우, goal이 정확히 일치하는 순간에 탐색을 멈추게 되어, 가능한 더 긴 길이를 놓칠 위험
        low = mid + 1
        answer = mid
    else:
        high = mid-1

print(answer)


