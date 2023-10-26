total = int(input())
buildings = []
for _ in range(total):
    buildings.append(int(input()))
stack = []
result = 0
for i in range(total):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    result += len(stack)
    stack.append(buildings[i])
print(result)