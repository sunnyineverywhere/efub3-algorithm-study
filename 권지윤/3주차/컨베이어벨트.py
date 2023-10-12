import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
con = deque(list(map(int, input().split())))
robot = deque([0]*n)
count = 0
while True:
    con.rotate(1) #1= 한 번 이동
    robot.rotate(1)
    robot[-1] = 0 # 로봇 내려감
    if sum(robot):
        for i in range(n - 2, -1, -1):
            if robot[i] == 1:
                if robot[i+1] == 0 and con[i+1] >= 1: # 앞에 로봇이 없는 경우 +내구력 1 이상
                    robot[i+1] = 1 # 이동
                    robot[i] = 0
                    con[i+1] -=1
        robot[-1] = 0 # 내리기 2번

    if robot[0] == 0 and con[0] > 0: # 올리기
        robot[0] = 1
        con[0] -= 1
    count +=1
    if con.count(0) >= k:
        print(count)
        break