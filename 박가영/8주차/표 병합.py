parent = [[(r,c) for c in range(51)] for r in range(51)]
cells = [['EMPTY'] * 51 for _ in range(51)]
answer = []


# 특정 원소가 속한 집합을 찾기
def find(r,c ):
    if (r, c) == parent[r][c]:
        return parent[r][c]
    low, column = parent[r][c]
    parent[r][c] = find(low, column)
    return parent[r][c]

def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]

# UPDATE r c value
def update_to_val(r, c, data):
    row, column = find(r,c)
    cells[row][column] = data

# UPDATE value1 value2
def update_val1_to_val2(data1, data2):
    for r in range(51):
        for c in range(51):
            row, column = find(r,c)
            if cells[row][column] == data1:
                cells[row][column] = data2

# MERGE r1 c1 r2 c2
def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if r1 == r2 and c1 == c2: # 같은 셀인 경우 패스
        return
    if cells[r1][c1] != 'EMPTY':
        union(r1, c1, r2, c2)
    else: # 두 셀 모두 값을 가지는 경우 &  (r2, c2)가 EMPTY인 경우
        union(r2, c2, r1, c1)

# UNMERGE r c
def unmerge(r, c):
    row, column = find(r, c)
    data = cells[row][column]

    merge_list = list()
    # 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가짐
    for i in range(51):
            for j in range(51):
                pi, pj = find(i, j)
                if (pi, pj) == (row, column):
                    merge_list.append((i,j))

    for i,j in merge_list:
        parent[i][j] = (i,j)
        if (i, j) != (r, c):
            cells[i][j] = 'EMPTY'
        else:
            cells[i][j] = data

def print(r,c):
    row, column = find(r, c)
    answer.append(cells[row][column])

def solution(commands):
    for command in commands:
        tokens = command.split()
        
        # UPDATE r c value
        if len(tokens) == 4 and tokens[0] == 'UPDATE':
            r, c = map(int, tokens[1:3])
            data = tokens[-1]
            update_to_val(r, c, data)

        # UPDATE value1 value2
        elif len(tokens) == 3 and tokens[0] == 'UPDATE':
            data1 = tokens[1]
            data2 = tokens[2]
            update_val1_to_val2(data1, data2)
        
        # MERGE r1 c1 r2 c2
        elif tokens[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, tokens[1:])
            merge(r1, c1, r2, c2)

        # UNMERGE r c
        elif tokens[0] == 'UNMERGE':
            r1, c1 = map(int, tokens[1:])
            unmerge(r1, c1)
        
        else:
            r1, c1 = map(int, tokens[1:])
            print(r1, c1)

    return answer
                    


