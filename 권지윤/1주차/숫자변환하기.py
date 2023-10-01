def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        temp = set()

        for i in s:
            if i + n <= y:
                temp.add(i + n)

            if i * 2 <= y:
                temp.add(i * 2)

            if i * 3 <= y:
                temp.add(i * 3)

        s = temp
        answer += 1

    return -1