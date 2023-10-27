import collections

def solution(v):
    x = []
    y = []
    x_answer = []
    y_answer = []
    for i in range(len(v)):
        x.append(v[i][0])
        y.append(v[i][1])

        x_element = collections.Counter(v[i][0])
        y_element = collections.Counter(v[i][1])
        if x_element == 2:
            x.remove(v[i][0])

        if y_element == 2:
            y.remove(v[i][1])
    return x.extend(y)