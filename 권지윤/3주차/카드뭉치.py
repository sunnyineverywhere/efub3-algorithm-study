def solution(cards1, cards2, goal):
    for g in range(len(goal)):
        if len(cards2) > 0 and cards2[0] == goal[g]:
            cards2.pop(0)
        elif len(cards1) > 0 and cards1[0] == goal[g]:
            cards1.pop(0)
        else:
            return "No"
    return "Yes"