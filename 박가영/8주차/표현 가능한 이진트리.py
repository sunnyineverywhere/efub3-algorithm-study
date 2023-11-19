# def makeBinaryNumberList(number):
#     binaryNumberList = getBinaryNum(number, [])
#     binaryNumberList.sort(reverse=True)
#     print(binaryNumberList)

# def getBinaryNum(n, numberList):
#     a = n // 2
#     b = n % 2
#     numberList.append(b)
#     if a == 0:
#         return numberList
#     else:
#         return getBinaryNum(a, numberList)

# answerList = []
# answer = getBinaryNum(58,answerList)
# answer.sort(reverse=True)

# print(answer)

def getBinaryNum(n, lists):
    a = n // 2
    b = n % 2
    lists.append(b)
    if a == 1 :
        return lists
    else :
        return getBinaryNum(a, lists)

answerList = []
answer = getBinaryNum(58,answerList)
answer.sort(reverse=True)

print("".join([str(_) for _ in answer]))