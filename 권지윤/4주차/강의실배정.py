import heapq
n = int(input())
class_time = []
for _ in range(n):
    a, b = map(int, input().split())
    class_time.append([a, b])
class_time.sort()

room = []
heapq.heappush(room, class_time[0][1]) #끝나는 시간

for i in range(1, n):
    if class_time[i][0] < room[0]: #지금있는 회의끝 시간보다 빠르면
        heapq.heappush(room, class_time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, class_time[i][1])
print(len(room))

