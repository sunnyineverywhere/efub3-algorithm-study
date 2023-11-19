
def getBinaryString(n):
    binaryNumList = []
    while n != 1:
        binaryNumList.append(str(n % 2))
        n //= 2
    binaryNumList.append("1")
    binaryString = ''.join(binaryNumList[::-1])
    return binaryString
    
    
def makeBinaryTree(number):
    binaryString = getBinaryString(number)

    treeSize = 1
    while treeSize < len(binaryString):
        treeSize = (treeSize +1 ) * 2 -1
    binaryString = "0" * (treeSize - len(binaryString)) + binaryString
    return binaryString

def checkBinaryTreePossible(start, end, binaryString):
    if start == end:
        return binaryString[start]

    mid = (start + end) // 2
    left = checkBinaryTreePossible(start, mid-1, binaryString)
    if not left or (binaryString[mid] == "0" and left == "1"):
        return False

    right = checkBinaryTreePossible(mid+1, end, binaryString)
    if not right or (binaryString[mid] == "0" and right == "1"):
        return False

    if left == "0" and right == "0" and binaryString[mid] == "0":
        return "0"

    return "1"
    

def solution(numbers):
    answer = []
    for number in numbers:
        binaryString = makeBinaryTree(number)
        isPossible = checkBinaryTreePossible(0, len(binaryString)-1, binaryString)
    
        if isPossible:
            answer.append(1)
        else:
            answer.append(0)

    return answer
