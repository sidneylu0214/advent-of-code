import numpy as np

intput_txt = []
with open('input.txt', 'r') as lines:
    for line in lines:
        intput_txt.append([1 if i == '#' else 0 for i in line[:-1]])
    pass

enhancement = intput_txt[0]
input_image = np.array(intput_txt[2:], dtype = int)

expand = 100
c_expand = [np.zeros(input_image.shape[0])] * expand
input_image = np.c_[tuple(c_expand + [input_image]  + c_expand)]
r_expand = [[np.zeros(input_image.shape[1])]] * expand
input_image = np.r_[tuple(r_expand + [input_image] + r_expand)]
input_image = np.array(input_image, dtype = int)
height, width = input_image.shape

def Enhance(input):
    height, width = input.shape
    result_image = np.zeros(input.shape, dtype = int)
    for y in range(1 , height - 1):
        for x in range(1, width - 1):
            r_s = y - 1
            r_e = y + 1
            c_s = x - 1
            c_e = x + 1

            block = input[r_s:r_e + 1, c_s:c_e + 1]
            bin_string = ''.join(str(e) for e in block.flatten().tolist())
            result_image[y][x] = enhancement[int(bin_string, 2)]

    return result_image


r = expand // 2

# part 1
res_image = input_image
for i in range(2):
    res_image = Enhance(res_image)
    pass
print(np.where(res_image[r:-r, r:-r] == 1)[0].size)

# part 2
res_image = input_image
for i in range(50):
    res_image = Enhance(res_image)
    pass

print(np.where(res_image[r:-r, r:-r] == 1)[0].size)
