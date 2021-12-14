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
    print(len(output))
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
    x_part = convert_num[key]
    y_parts = [convert_num[k] for k in transition[key]]

    test = 'test'
    for y_part in y_parts:
        base_martix[x_part][y_part] += 1
    pass


init_state = np.zeros([len(transition), 1], dtype=np.ulonglong)
for i in range(len(input_pairs[0]) - 1):
    pair = (input_pairs[0])[i: i + 2]
    init_state[convert_num[pair]][0] += 1


for i in range(10):
    init_state = np.matmul(base_martix, init_state)
    print(sum(init_state))

output = list(itertools.chain(*init_state.tolist()))

cnt = [o for o in output if o > 0]

print('part 2 is' + str(max(cnt) - min(cnt)))