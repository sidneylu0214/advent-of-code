import numpy as np
import sys
import bisect

input_lines = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_lines.append(list(str(line[:-1])))
    pass


class KeyWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key
    def __getitem__(self, i):
        return self.key(self.it[i])
    def __len__(self):
        return len(self.it)

class SortedList:
    def __init__(self, keyfun):
        self.keyfun = keyfun
        self.data = []

    def Insert(self, item):
        bslindex = bisect.bisect_left(KeyWrapper(self.data, key=self.keyfun), self.keyfun(item))
        self.data.insert(bslindex, item)

def DijkstraOneRound(current_nodes:SortedList, distance, source, cost):
    x, y, d = current_nodes.data.pop(0)

    target = []
    if(x > 0):
        target.append([x - 1, y])
        
    if(x < height - 1):
        target.append([x + 1, y])

    if(y > 0):
        target.append([x, y - 1])
        
    if(y < width - 1):
        target.append([x, y + 1])

    for tx, ty in target:
        if distance[tx][ty] > cost[tx][ty] + d:
            distance[tx][ty] = cost[tx][ty] + d
            source[tx][ty] = [x, y]
            current_nodes.Insert([tx, ty, cost[tx][ty] + d])
    pass

# part1
cost = np.array(input_lines, dtype = int)
distance = np.array(np.full(cost.shape, 1 << 30, cost.dtype))
distance[0][0] = 0

height, width = cost.shape
source =  np.zeros([height, width , 2], cost.dtype)

current_nodes = SortedList(keyfun = lambda x : x[2])
current_nodes.Insert([0,0,0])
while len(current_nodes.data):
    DijkstraOneRound(current_nodes, distance, source, cost)

print(distance[height - 1][width - 1])

# part2
def Enlarger(terrain, direction, size):
    merge_list = []
    for i in range(size):
        a = terrain + i 
        a[a > 9] -= 9
        merge_list.append(a)

    output = np.concatenate(merge_list, axis=direction)    
    return output

cost = Enlarger(Enlarger(cost, 1, 5), 0, 5)
distance = np.array(np.full(cost.shape, 1 << 30, cost.dtype))
distance[0][0] = 0

height, width = cost.shape
source =  np.zeros([height, width , 2], cost.dtype)

current_nodes = SortedList(keyfun = lambda x : x[2])
current_nodes.Insert([0,0,0])

while len(current_nodes.data):
    DijkstraOneRound(current_nodes, distance, source, cost)

print(distance[height - 1][width - 1])
