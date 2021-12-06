line_pairs = []
with open('input.txt', 'r') as input_txt:
    for line in input_txt:
	    # replace many space to one space
        pairs = line.split(' ')
        line_pairs.append([pairs[0] , int(pairs[1])])
    pass

# part 1
horizontal = 0
depth = 0
for direction, data in line_pairs:    
    if direction == 'forward':
        horizontal += data    
    elif direction == 'down':
        depth += data
    else:
        depth -= data
    pass

print(depth  * horizontal)

# part 2
horizontal = 0
depth = 0
aim = 0
for direction, data in line_pairs:    
    if direction == 'forward':
        horizontal += data
        depth += aim * data    
    elif direction == 'down':
        aim += data
    else:
        aim -= data
    pass

print(depth  * horizontal)
