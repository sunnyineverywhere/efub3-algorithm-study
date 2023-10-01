# 한 개를 기준으로 그 뒤에 있는 것들이 더 큰지 확인했다. -> 시간 오버 -> stack에 넣고 조건에 만족하지 않은 애들을 저장하여 관리
def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num # 가까운 큰값 넣기
        stack.append(i)
    return answer

