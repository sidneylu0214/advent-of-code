import numpy as np

inputs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        inputs = [int(i) for i in line.split(',')]
    pass

days = 256
# wait one more day to create new fish
reset_timer = 6 + 1
new_timer = 8 + 1

# initialize tables
fabonacci = [1]
fabonacci += [2] * reset_timer
fabonacci += [3] * (new_timer - reset_timer)
fabonacci += list(range(days))

for d in range(new_timer + 1, len(fabonacci)):
    f = fabonacci
    f[d] = f[d - new_timer] + f[d - reset_timer]

print(sum([fabonacci[days - i] for i in inputs]))
