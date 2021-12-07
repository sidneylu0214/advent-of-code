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
    input_1 -= 1
    new_element = [new_timer] * list(input_1).count(-1)
    input_1 = np.concatenate([input_1, np.array(new_element)])
    input_1[input_1 == -1] = reset_timer
    
    pass

slow_answer = len(input_1)


# part 1 fabonacci space O(1) method
# Time: O(d * n)
# Space: O(1)

fish_time = [0] * (new_timer + 1)

for i in inputs:
    fish_time[i] += 1

for d in range(days):
    fish_time = fish_time[1:] + fish_time[:1]
    fish_time[reset_timer] += fish_time[new_timer]
    pass

print(sum(fish_time))


# part 2 fabonacci Time O(1) method
# Time: O(d + n * 1)
# Space: O(d)

days = 256
# wait one more day to create new fish
reset_timer = 6 + 1
new_timer = 8 + 1

# initialize table
fabonacci_table = [1]
fabonacci_table += [2] * reset_timer
fabonacci_table += [3] * (new_timer - reset_timer)
fabonacci_table += [0] * days

for d in range(new_timer + 1, days):
    f = fabonacci_table
    f[d] = f[d - new_timer] + f[d - reset_timer]

print(sum([fabonacci_table[days - i] for i in inputs]))
