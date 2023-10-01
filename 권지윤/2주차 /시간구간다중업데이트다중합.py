import sys

input = sys.stdin.readline

N = int(input())
prefix_sum = [0] * (86400 + 1) # [00:00:00, 23:59:59]의 각 초를 저장할 리스트 (24시간 * 60분 * 60초 + 1) == (전체 시간 + 누적합을 위해 )
prefix_sum[0] = -1
while N:
    q = input().split()

    if q[0] == '1':
        start = int(q[1][0:2]) * 3600 + int(q[1][3:5]) * 60 + int(q[1][6:8])
        end = int(q[2][0:2]) * 3600 + int(q[2][3:5]) * 60 + int(q[2][6:8])
        prefix_sum[start + 1] += 1
        prefix_sum[end + 1] -= 1
    else:
        start = int(q[1][0:2]) * 3600 + int(q[1][3:5]) * 60 + int(q[1][6:8])
        end = int(q[2][0:2]) * 3600 + int(q[2][3:5]) * 60 + int(q[2][6:8])
        if prefix_sum[0] == -1:
            prefix_sum[0] = 0
            for _ in range(2):
                for i in range(1, len(prefix_sum)):
                    prefix_sum[i] += prefix_sum[i - 1]
        ans = prefix_sum[end] - prefix_sum[start]
        print(ans)
    N -= 1
