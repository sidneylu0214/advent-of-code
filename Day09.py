import numpy as np

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
        here = intput_table[h][w]

        is_law = True
        
        if(h > 0):
            up = intput_table[h - 1][w]
            if here >= up:
                is_law = False
        
        if(h < height - 1):
            down = intput_table[h + 1][w]
            if here >= down:
                is_law = False

        if(w > 0):
            left = intput_table[h][w - 1]
            if here >= left:
                is_law = False
        
        if(w < width - 1):
            right = intput_table[h][w + 1]
            if here >= right:
                is_law = False

        if is_law:
            low_points.append([h ,w])
            
    pass

ans_part1 = [intput_table[h][w] for h, w in low_points]
print(sum(ans_part1) + len(ans_part1))



# part 2
class Queue:
    def __init__(self):
        self.queue = []
    
    def PushBack(self, item):
        self.queue.append(item)
    
    def PopFront(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item
       
    pass

def DFS(intput_table, init_pose):    
    pose_queue = Queue()
    pose_queue.PushBack(init_pose)
    
    output_heights = []    

    height, width = intput_table.shape
    visited_pose = np.zeros(intput_table.shape)

    while len(pose_queue.queue):
        h, w = pose_queue.PopFront()
        here_height = intput_table[h][w]
        output_heights.append(here_height)

        if(h > 0):
            up = intput_table[h - 1][w]
            if up < 9 and up >= here_height and not visited_pose[h - 1][w]:
                pose_queue.PushBack([h - 1, w])
                visited_pose[h - 1][w] +=1
        
        if(h < height - 1):
            down = intput_table[h + 1][w]
            if down < 9 and down >= here_height and not visited_pose[h + 1][w]:
                pose_queue.PushBack([h + 1, w])
                visited_pose[h + 1][w] += 1

        if(w > 0):
            left = intput_table[h][w - 1]
            if left < 9 and left >= here_height and not visited_pose[h][w - 1]:
                pose_queue.PushBack([h, w - 1])
                visited_pose[h][w - 1] += 1
        
        if(w < width - 1):
            right = intput_table[h][w + 1]
            if right < 9 and right >= here_height and not visited_pose[h][w + 1]:
                pose_queue.PushBack([h, w + 1])
                visited_pose[h][w + 1] += 1

    return output_heights

ans = [len(DFS(intput_table, l)) for l in low_points]
ans.sort()
print(ans[-3] * ans[-2] * ans[-1])
