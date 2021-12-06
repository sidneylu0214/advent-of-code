import numpy as np
import copy

inputs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        inputs.append(int(line, base=2))


# part 1
gamma = 0
epsilon = 0
for b in reversed(range(12)):
    bits_1 = 0

    mask = 1 << b
    for i in inputs:        
        if i & mask :
            bits_1 = bits_1 + 1

    if bits_1 > len(inputs) / 2:
        gamma = gamma + mask;
    else:
        epsilon = epsilon + mask

print(gamma * epsilon)


# part 2
list_current = inputs.copy()
for b in reversed(range(12)):
    mask = 1 << b
    bits_1 = 0
    bits_0 = 0

    for i in list_current:
        if i & mask :
            bits_1 = bits_1 + 1
        else:
            bits_0 = bits_0 + 1

    list_temp = []
    for i in list_current:
        if (i & mask) and (bits_1 >= bits_0):
            list_temp.append(i)

        if (not(i & mask)) and (bits_0 > bits_1):
            list_temp.append(i)

    list_current = list_temp

oxygen = list_current[0]



list_current = inputs.copy()
for b in reversed(range(12)):
    mask = 1 << b
    bits_1 = 0
    bits_0 = 0

    for i in list_current:
        if i & mask :
            bits_1 = bits_1 + 1
        else:
            bits_0 = bits_0 + 1

    list_temp = []
    for i in list_current:
        if (i & mask) and (bits_0 > bits_1):
            list_temp.append(i)

        if (not(i & mask)):
            if (bits_1 > bits_0) or (bits_1 > bits_0):
                list_temp.append(i)

        #special case
        if (bits_1 + bits_0) == 1:
            list_temp.append(i)

    list_current = list_temp

CO2 = list_current[0]

print(oxygen * CO2)
