import numpy as np

input_lines = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_lines.append(list(str(line[:-1])))
    pass


input_table = np.array(input_lines, dtype = int)


# part1
result_table = np.zeros(input_table.shape, input_table.dtype)
path_table = np.zeros(input_table.shape, dtype = np.byte)
width = input_table.shape[0]
def UpdateTable1(pose, result, cost):
    x, y = pose

    result[x][y] += cost[x][y]

    if x == 0 and y == 0:
        pass

    elif x == 0:
        result[x][y] += result[x][y - 1]
        path_table[x][y] = 1

    elif y == 0:
        result[x][y] += result[x - 1][y]
        path_table[x][y] = 2

    else:
        l_part = result[x][y - 1]
        u_part = result[x - 1][y]

        if l_part < u_part:
            result[x][y] += l_part
            path_table[x][y] = 1
        else :
            result[x][y] += u_part
            path_table[x][y] = 2


def UpdateTable2(pose, result, cost):
    x, y = pose

    if x == 0 and y == 0:
        pass

    elif x == 0:
        result[x][y] += result[x][y - 1] + cost[x][y - 1]
        path_table[x][y] = 1

    elif y == 0:
        result[x][y] += result[x - 1][y] + cost[x - 1][y]
        path_table[x][y] = 2

    else:
        l_part = result[x][y - 1] + cost[x][y - 1]
        u_part = result[x - 1][y] + cost[x - 1][y]

        if l_part < u_part:
            result[x][y] += l_part
            path_table[x][y] = 1
        else :
            result[x][y] += u_part
            path_table[x][y] = 2

def UpdateTable3(pose, result, cost):
    x, y = pose

    if x == 0 and y == 0:
        pass

    elif x == 0:
        result[x][y] += result[x][y - 1] + cost[x][y]
        path_table[x][y] = 1

    elif y == 0:
        result[x][y] += result[x - 1][y] + cost[x][y]
        path_table[x][y] = 2

    else:
        l_part = result[x][y - 1] + cost[x][y]
        u_part = result[x - 1][y] + cost[x][y]

        if l_part < u_part:
            result[x][y] += l_part
            path_table[x][y] = 1
        else :
            result[x][y] += u_part
            path_table[x][y] = 2


UpdateTable = UpdateTable1
result_table = np.zeros(input_table.shape, input_table.dtype)
path_table = np.zeros(input_table.shape, dtype = np.byte)

for i in range(width * 2 - 1):
    x = 0
    y = 0

    if i < width:
        for j in range(i + 1):
            x = j
            y = i-j
            UpdateTable([x,y], result_table, input_table)

    else :
        for j in reversed(range(2 * width - i - 1)):
            j = width - 1 - j
            x = j
            y = i - j
            UpdateTable([x,y], result_table, input_table)
print(path_table)
print(result_table[width-1][width -1])

UpdateTable = UpdateTable2
result_table = np.zeros(input_table.shape, input_table.dtype)
path_table = np.zeros(input_table.shape, dtype = np.byte)
for i in range(width * 2 - 1):
    x = 0
    y = 0

    if i < width:
        for j in range(i + 1):
            x = j
            y = i-j
            UpdateTable([x,y], result_table, input_table)

    else :
        for j in reversed(range(2 * width - i - 1)):
            j = width - 1 - j
            x = j
            y = i - j
            UpdateTable([x,y], result_table, input_table)
print(path_table)
print(result_table[width-1][width -1])

UpdateTable = UpdateTable3
result_table = np.zeros(input_table.shape, input_table.dtype)
path_table = np.zeros(input_table.shape, dtype = np.byte)
for i in range(width * 2 - 1):
    x = 0
    y = 0

    if i < width:
        for j in range(i + 1):
            x = j
            y = i-j
            UpdateTable([x,y], result_table, input_table)

    else :
        for j in reversed(range(2 * width - i - 1)):
            j = width - 1 - j
            x = j
            y = i - j
            UpdateTable([x,y], result_table, input_table)
print(path_table)
print(result_table[width-1][width -1])
