# 대상이 많음
def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n

    while True:
        if right < left:
            break
        mid = (right + left) // 2

        people = 0
        for time in times:
            people += mid // time

        if people >= n: # 딱 n이 되지 않을 수도 있다. n보다 큰 경우도 최소가 될 경우가 있음
            right = mid - 1
            answer = mid
        elif people < n:
            left = mid + 1

    return answer