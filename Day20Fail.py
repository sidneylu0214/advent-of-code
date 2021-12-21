import numpy as np

intput_txt = []
with open('input.txt', 'r') as lines:
    for line in lines:
        intput_txt.append([1 if i == '#' else 0 for i in line[:-1]])
    pass

enhancement = intput_txt[0]
input_image = np.array(intput_txt[2:], dtype = int)

expand = 3
c_expand = [np.zeros(input_image.shape[0])] * expand
input_image = np.c_[tuple(c_expand + [input_image]  + c_expand)]
r_expand = [[np.zeros(input_image.shape[1])]] * expand
input_image = np.r_[tuple(r_expand + [input_image] + r_expand)]
input_image = np.array(input_image, dtype = int)
height, width = input_image.shape

def Enhance(input, start_pose):
    height, width = input.shape
    result_image = np.zeros(input.shape, dtype = int)
    for y in range(start_pose + 1 , height - start_pose - 1):
        for x in range(start_pose + 1, width - start_pose - 1):
            r_s = y - 1
            r_e = y + 1
            c_s = x - 1
            c_e = x + 1

            block = input[r_s:r_e + 1, c_s:c_e + 1]
            bin_string = ''.join(str(e) for e in block.flatten().tolist())
            result_image[y][x] = enhancement[int(bin_string, 2)]

    return result_image


# print('0')
# print(input_image)
# print('1')
# print(Enhance(input_image, 1))
# print('2')
# print(Enhance(Enhance(input_image, 1), 0))

res_image = Enhance(Enhance(input_image, 1), 0)
print(np.where(res_image == 1)[0].size)
