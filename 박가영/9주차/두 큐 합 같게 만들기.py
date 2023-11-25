from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    count = 0
    max_count = len(q1) * 3
    
    # 각 큐의 원소합을 같게 만들 수 없는 경우
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    while True:
        if sum1 == sum2:
            return count 
        if count == max_count:
            return -1
        count += 1
        # 각 큐의 합을 비교 큰 쪽의 값을 꺼내 작은 쪽에 넣는다
        if sum1 > sum2:
            temp = q1.popleft()
            q2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            sum2 -= temp
            sum1 += temp
        
    return count