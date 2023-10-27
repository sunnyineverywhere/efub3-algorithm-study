import math
def solution(progresses, speeds):
    work = []
    answer = []

    for p in range(len(progresses)):
        remain = (100 - progresses[p])
        work.append(math.ceil(remain / speeds[p]))

    start = work[0]
    total = 0
    answer.append(1)
    print(work)
    for i in range(1, len(work)):
        if start >= work[i]:
            answer[total] += 1
        else:
            start = work[i]
            total += 1
            answer.append(1)

    return answer


print(solution([93, 30, 55], 	[1, 30, 5]))
