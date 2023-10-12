'''
n명
심사관 한 명이 심사하는데 걸리는 시간 times
'''


def solution(n, times):
    answer = 0
    times.sort()
    
    start = 1 # (절대이렇게나올리가없지만) 최소값
    end = times[-1] * n # 10 * 6 => 최대로 오래 걸리는 시간
    
    while start < end:
        mid = (start + end) // 2 # 30
        
        total = 0
        for t in times:
            total += mid // t # 4 + 3 = 7
        
        if total >= n: # total 수가 사람 수보다 많거나 같을 때
            end = mid
        else: # total 수가 사람 수보다 적을 때
            start = mid + 1
    
    answer = start
    
    return answer
