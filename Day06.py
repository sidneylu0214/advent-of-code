import numpy as np

inputs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        inputs = [int(i) for i in line.split(',')]
    pass


# part 1 brute force
# Time: O(n * 2^d)
# space: O(n * 2^d)

days = 80
reset_timer = 6
new_timer = 8

input_1 = np.array(inputs)
for d in range(days):
    new_element = [new_timer + 1] * list(input_1).count(0)
    input_1 = np.concatenate([input_1, np.array(new_element)])
    input_1[input_1 == 0] = 1 + reset_timer
    input_1 -= 1
    pass

print(len(input_1))


# part 1 fabonacci space O(1) method
# Time: O(d * n)
# Space: O(1)

slot = [0] * (new_timer + 1)

for i in inputs:
    slot[i] += 1

for d in range(days):
    slot = slot[1:] + slot[:1]
    slot[reset_timer] += slot[new_timer]
    pass

print(sum(slot))


# part 2 fabonacci Time O(n) method
# Time: O(d + n)
# Space: O(d)

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
