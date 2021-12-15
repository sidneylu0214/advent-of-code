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


input_string = input_pairs[0]

# part 1
def Apply(table, input_string):
    outputs = input_string[0]    
    inputs = [((table[input_string[i: i + 2]])[0])[1] for i in range(len(input_string) - 1)]

    for i in range(len(inputs)):
        outputs += inputs[i]
        outputs += input_string[i + 1]

    return outputs


output = input_string
for i in range(10):
    output = Apply(transition, output)

cnt = [output.count(a) for a in string.ascii_uppercase if output.count(a) > 0]
print('part 1 is ' + str(max(cnt) - min(cnt)))



# part 2
convert_num = {}
i = 0
for key in transition.keys():    
    convert_num[key] = i
    i +=1

matrix_shape = [len(transition), len(transition)]
base_martix = np.zeros(matrix_shape, dtype=np.ulonglong)

for key in transition.keys():
    y_part = convert_num[key]
    x_parts = [convert_num[k] for k in transition[key]]
    for x_part in x_parts:
        base_martix[x_part][y_part] += 1
    pass


init_state = np.zeros([len(transition), 1], dtype=np.ulonglong)
for i in range(len(input_string) - 1):
    pair = input_string[i: i + 2]
    init_state[convert_num[pair]][0] += 1


def FastPower(in_matrix, times:int):
    if times == 0:
      return np.identity(in_matrix.shape[0], dtype=in_matrix.dtype)

    x = FastPower(in_matrix, times // 2)
    x = np.matmul(x, x)
    if times % 2:
      x = np.matmul(x, in_matrix)

    return x

final_state = np.matmul(FastPower(base_martix, 40), init_state)
output = list(itertools.chain(*final_state.tolist()))

cnt_tables = {}
for key in transition.keys():
    a, b = key
    cnt_tables[a] = 0
    cnt_tables[b] = 0
    pass

# head tail lack 1 time
cnt_tables[input_string[0]] += 1
cnt_tables[input_string[-1]] += 1

for key in transition.keys():
    a, b = key
    cnt = output[convert_num[key]]
    cnt_tables[a] += cnt
    cnt_tables[b] += cnt

diff = max(cnt_tables.values()) - min(cnt_tables.values())
print('part 2 is ' + str(diff // 2))
