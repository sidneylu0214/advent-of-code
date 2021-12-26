import numpy as np
import copy

input_txt = []
with open('input.txt', 'r') as lines:
    for line in lines:
        input_txt.append(list(line[:-1]))
    pass

def Update(table):
    rows = len(table)
    cols = len(table[0])

    if_update = False

    # right first
    temp_table = copy.deepcopy(table)
    for r in range(rows):
        for c in range(cols):
            if (table[r])[c] == '.' and (table[r])[c - 1] == '>':
                (temp_table[r])[c] = '>'
                (temp_table[r])[c - 1] = '.'
                if_update = True
        pass
    output = copy.deepcopy(temp_table)

    # do down
    for r in range(rows):
        for c in range(cols):
            if (temp_table[r])[c] == '.' and (temp_table[r - 1])[c] == 'v':
                (output[r])[c] = 'v'
                (output[r - 1])[c] = '.'
                if_update = True
        pass

    return output, if_update

update = 1
i = 0
while update > 0:
    i +=1     
    input_txt, update = Update(input_txt)

print(i)
