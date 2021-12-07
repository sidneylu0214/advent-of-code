import numpy as np

inputs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        inputs = np.array([int(i) for i in line.split(',')])
    pass

inputs -= min(inputs)
max_i = max(inputs)

# part 1
print(min([sum(abs(inputs - i)) for i in inputs]))

# part 2
n = np.array(range(max_i + 1))
table = ((n[:] + 1) * n[:] ) // 2

print(min([sum([table[abs(i - m)] for i in inputs]) for m in range(max_i)]))
