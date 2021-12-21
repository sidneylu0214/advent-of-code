import numpy as np

input_lines = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_lines.append([1 if i == '#' else 0 for i in line[:-1]])
    pass

enhancement = input_lines[0]
input_image = np.array(input_lines[2:], dtype = int)

height, width = input_image.shape
expand = 3
c_expand = [np.zeros(height)] * expand
r_expand = [[np.zeros(width + 2 * expand)]] * expand

input_image = np.c_[tuple(c_expand + [input_image]  + c_expand)]
input_image = np.r_[tuple(r_expand + [input_image] + r_expand)]
input_image = np.array(input_image, dtype = int)
height, width = input_image.shape


def Enhance(input_image):
    result_image = np.zeros(input_image.shape, dtype = int)
    for y in range(1 , height - 1):
        for x in range(1, width - 1):
            r_s = y - 1
            r_e = y + 1
            c_s = x - 1
            c_e = x + 1

            block = input_image[r_s:r_e + 1, c_s:c_e + 1]
            bin_string = ''.join(str(e) for e in block.flatten().tolist())
            query_table = int(bin_string, 2)

            result_image[y][x] = enhancement[query_table]

    return result_image


res_image = Enhance(Enhance(input_image))
print(np.where(res_image == 1)[0].size)

print('0')
print(input_image)
print('1')
print(Enhance(input_image))
print('2')
print(Enhance(Enhance(input_image)))
