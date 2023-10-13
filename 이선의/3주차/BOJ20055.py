# 컨테이너 벨트 위의 로봇
# 1 -> N -> N+1 -> 2N -> 1
# 내리는 위치에 도달하면 즉시 내린다
# 칸의 내구도 감소
"""
1. 벨트가 칸 위의 로봇과 함께 회전
2. 가장 먼저 벨트에 올라간 로봇부터 회전 방향으로 이동
- 이동하기 위해서는 내구도
3. 칸의 내구도가 0이 아니면 로봇 올림
4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
1번 = 올리는 위치
N번 = 내리는 위치
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
steps = 0

while True:
    # 단계 카운트
    steps += 1

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    belt.rotate(1)
    robot.rotate(1)

    # 로봇이 n번째 인덱스에 존재한다면 로봇 내림
    robot[-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터 회전 방향으로 한 칸 이동
    if sum(robot) > 0:
        for i in range(n-2, -1, -1):
            # 이동할 수 있는 조건
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1

        # 이동 후에 내리는 위치 체크
        robot[-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    if belt.count(0) >= k:
        break

print(steps)
