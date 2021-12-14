import string
import copy

input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(line[:-1])
    pass

convert_table = {}
for i in range(len(input_pairs) - 2) :
    key, value = input_pairs[i + 2].split(' -> ')
    convert_table[key] = value



def Apply(table, input_string):

    outputs = input_string[0]
    
    inputs = [table[input_string[i: i + 2]] for i in range(len(input_string) - 1)]

    for i in range(len(inputs)):
        outputs += inputs[i]
        outputs += input_string[i + 1]

    return outputs



output = input_pairs[0]
for i in range(10):
    output = Apply(convert_table, output)
    pass

cnt = [output.count(a) for a in string.ascii_uppercase if output.count(a) > 0]

print(max(cnt) - min(cnt))
