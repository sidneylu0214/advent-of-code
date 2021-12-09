import numpy as np
import queue

input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append([int(i) for i in line[:-1]])
    pass

intput_table = np.array(input_pairs)

# part 1
height, width = intput_table.shape
low_points = []
for h in range(height):
    for w in range(width):
        is_law = True        
        neighbor = []

        if(h > 0):
            neighbor.append([h - 1, w])
        
        if(h < height - 1):
            neighbor.append([h + 1, w])

        if(w > 0):
            neighbor.append([h, w - 1])
        
        if(w < width - 1):
            neighbor.append([h, w + 1])

        for th ,tw in neighbor:
            if intput_table[h][w] >= intput_table[th][tw]:
                is_law = False

        if is_law:
            low_points.append([h ,w])
            
    pass

ans_part1 = [intput_table[h][w] for h, w in low_points]
print(sum(ans_part1) + len(ans_part1))


# part 2
def BFS(intput_table, init_pose):
    pose_queue = queue.Queue()
    pose_queue.put(init_pose)
    
    sum = 0
    visited_pose = np.zeros(intput_table.shape)

    while not pose_queue.empty():
        h, w = pose_queue.get()
        sum += 1

        neighbors = []
        if(h > 0):
            neighbors.append([h - 1, w])
        
        if(h < height - 1):
            neighbors.append([h + 1, w])

        if(w > 0):
            neighbors.append([h, w - 1])
        
        if(w < width - 1):
            neighbors.append([h, w + 1])

        for th, tw in neighbors:
            neighbor = intput_table[th][tw]
            if neighbor < 9 and neighbor >= intput_table[h][w] and not visited_pose[th][tw]:
                pose_queue.put([th, tw])
                visited_pose[th][tw] += 1

    return sum

ans = [BFS(intput_table, l) for l in low_points]
ans.sort()
print(ans[-3] * ans[-2] * ans[-1])
