import string
import itertools
import numpy as np

input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(line[:-1])
    pass

transition = {}
for i in range(len(input_pairs) - 2) :
    key, value = input_pairs[i + 2].split(' -> ')
    transition[key] = [key[0] + value, value + key[1]]
    pass


# part 1

def Apply(table, input_string):
    outputs = input_string[0]    
    inputs = [((table[input_string[i: i + 2]])[0])[1] for i in range(len(input_string) - 1)]

    for i in range(len(inputs)):
        outputs += inputs[i]
        outputs += input_string[i + 1]

    return outputs


output = input_pairs[0]
for i in range(10):
    output = Apply(transition, output)
    pass

cnt = [output.count(a) for a in string.ascii_uppercase if output.count(a) > 0]

print('part 1 is' + str(max(cnt) - min(cnt)))



# part 2
convert_num = {}
i = 0
for key in transition.keys():    
    convert_num[key] = i
    i +=1
    pass

matrix_shape = [len(transition), len(transition)]
base_martix = np.zeros(matrix_shape, dtype=np.ulonglong)

for key in transition.keys():
    y_part = convert_num[key]
    x_parts = [convert_num[k] for k in transition[key]]

    test = 'test'
    for x_part in x_parts:
        base_martix[x_part][y_part] += 1
    pass


init_state = np.zeros([len(transition), 1], dtype=np.ulonglong)
for i in range(len(input_pairs[0]) - 1):
    pair = (input_pairs[0])[i: i + 2]
    init_state[convert_num[pair]][0] += 1

for i in range(40):
    init_state = np.matmul(base_martix, init_state)

output = list(itertools.chain(*init_state.tolist()))


cnt_tables = {}
for key in transition.keys():
    a, b = key
    cnt_tables[a] = 0
    cnt_tables[b] = 0

for key in transition.keys():
    a, b = key
    cnt = output[convert_num[key]]
    cnt_tables[a] += cnt
    cnt_tables[b] += cnt

head = (input_pairs[0])[0]
tail = (input_pairs[0])[-1]
cnt_tables[head] += 1
cnt_tables[tail] += 1

diff = max(cnt_tables.values()) - min(cnt_tables.values())

print('part 2 is' + str(diff // 2))