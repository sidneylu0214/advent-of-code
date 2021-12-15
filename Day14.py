import string
import itertools
import numpy as np

input_lines = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_lines.append(line[:-1])
    pass

generate = {}
cnt_tables = {}
for i in range(len(input_lines) - 2) :
    key, value = input_lines[i + 2].split(' -> ')
    generate[key] = [key[0] + value, value + key[1]]

    cnt_tables[key[0]] = 0
    cnt_tables[key[1]] = 0
    cnt_tables[value] = 0
    pass


# part 1
def Apply(table, input_string):
    outputs = input_string[0]    
    inputs = [((table[input_string[i: i + 2]])[0])[1] for i in range(len(input_string) - 1)]

    for i in range(len(inputs)):
        outputs += inputs[i]
        outputs += input_string[i + 1]

    return outputs

output = input_lines[0]
for i in range(10):
    output = Apply(generate, output)

cnt = [output.count(a) for a in string.ascii_uppercase if output.count(a)]
print('part 1 is ' + str(max(cnt) - min(cnt)))


# part 2
convert_num = dict(zip(generate.keys(), range(len(generate))))

transition_martix = np.zeros([len(generate), len(generate)], dtype=np.ulonglong)
for key in generate.keys():
    y_part = convert_num[key]
    x_parts = [convert_num[k] for k in generate[key]]
    for x_part in x_parts:
        transition_martix[x_part][y_part] += 1
    pass

input_string = input_lines[0]
init_state = np.zeros([len(generate), 1], dtype=np.ulonglong)
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

final_state = np.matmul(FastPower(transition_martix, 40), init_state).flatten().tolist()
for key, value in convert_num.items():
    cnt = final_state[value]
    cnt_tables[key[0]] += cnt
    cnt_tables[key[1]] += cnt

# head tail lack 1 time
cnt_tables[input_string[0]] += 1
cnt_tables[input_string[-1]] += 1

diff = max(cnt_tables.values()) - min(cnt_tables.values())
print('part 2 is ' + str(diff // 2))
