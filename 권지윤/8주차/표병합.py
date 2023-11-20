def solution(commands):
    answer = []
    sheet = [[(i, j) for j in range(51)] for i in range(51)]
    values = {(i, j): '' for j in range(51) for i in range(51)}

    for cmd in commands:
        cmd = cmd.split(sep=' ')
        if cmd[0] == "UPDATE" and len(cmd) == 3:
            source = cmd[1]
            target = cmd[2]
            for k, v in values.items():
                if v == source:
                    values[k] = target
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            r = int(cmd[1])
            c = int(cmd[2])
            v = cmd[3]
            source = sheet[r][c]
            values[source] = v
        elif cmd[0] == "PRINT":
            r = int(cmd[1])
            c = int(cmd[2])
            source = sheet[r][c]
            if values[source] != '':
                answer.append(values[source])
            else:
                answer.append("EMPTY")
        elif cmd[0] == "MERGE":
            r1 = int(cmd[1])
            c1 = int(cmd[2])
            r2 = int(cmd[3])
            c2 = int(cmd[4])
            source1 = sheet[r1][c1]
            source2 = sheet[r2][c2]
            if source1 == source2:
                continue
            if values[source1] != '':
                v_source1 = values[source1]
                for i in range(51):
                    for j in range(51):
                        if sheet[i][j] == source2:
                            sheet[i][j] = source1
            else:
                v_source2 = values[source2]
                for i in range(51):
                    for j in range(51):
                        if sheet[i][j] == source1:
                            sheet[i][j] = source2
        elif cmd[0] == "UNMERGE":
            r = int(cmd[1])
            c = int(cmd[2])
            source = sheet[r][c]
            v = values[source]
            for i in range(51):
                for j in range(51):
                    if sheet[i][j] == source:
                        sheet[i][j] = (i, j)
                        values[(i, j)] = ''
            values[(r, c)] = v

    return answer