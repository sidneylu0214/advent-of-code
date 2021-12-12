import itertools

input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(set([i for i in line[:-1].split('-')]))
    pass

start_nodes = [i for i in input_pairs if 'start' in i]
end_nodes = [i for i in input_pairs if 'end' in i]


# create graph
neighbors = {}
calculate_table = {}
for i in set.union(*input_pairs):
    neighbor = []
    for j in input_pairs:
        if i in j:
            node = set(j)
            node.discard(i)
            node = ''.join(list(node))
            neighbor.append(node)
    neighbors[i] = neighbor
    calculate_table[i] = 0


paths = []
def FindPath(path, calculate_table):
    if path[-1] == 'end':
        paths.append(path)
        print(calculate_table)
        print(path)
        return True

    if sum(calculate_table.values()) > len(calculate_table) + 1:
        return False

    for next_node in neighbors[path[-1]]:

        if path[-1] == next_node:
            continue
        if next_node.islower():
            if calculate_table[next_node] > 0:
                continue

        calculate_table = calculate_table.copy()
        path = path.copy()
        calculate_table[next_node] += 1
        path.append(next_node)
        FindPath(path, calculate_table)
    pass


calculate_table_start = calculate_table.copy()
path = ['start']
calculate_table_start['start'] += 1
FindPath(path, calculate_table_start)

test = 'test'
