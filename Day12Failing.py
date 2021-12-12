input_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        input_pairs.append(set([i for i in line[:-1].split('-')]))
    pass

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


def FindPath(path, calculate_table, result_paths):
    calculate_table[path[-1]] +=1

    if path[-1] == 'end':
        result_paths.append(path)
        print(calculate_table)
        print(path)
        return True

    else:
        if sum(calculate_table.values()) > len(calculate_table) + 1:
            return False

        print('node ' + str(path[-1]) + ' neighbors are ' + str(neighbors[path[-1]]))

        for next_node in neighbors[path[-1]]:
            if next_node.islower() and calculate_table[next_node]:
                pass
            else:
                calculate_table = calculate_table.copy()
                print('path ' + str(path) + ' append ' + str(next_node))
                path = path.copy()
                path.append(next_node)
                FindPath(path, calculate_table, result_paths)
    pass

result_paths = []
FindPath(['start'], calculate_table, result_paths)

test = 'test'
