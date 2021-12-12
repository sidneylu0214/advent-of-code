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


# part 1
def FindPath(path, calculate_table, result_paths):
    calculate_table = calculate_table.copy()   

    current_node = path[-1]
    calculate_table[current_node] +=1

    if current_node == 'end':
        result_paths.append(path)
        return True
    
    for next_node in neighbors[current_node]:
        if next_node.islower() and calculate_table[next_node]:
            pass
        else:
            path_local = path.copy()
            path_local.append(next_node)
            FindPath(path_local, calculate_table, result_paths)
    return False

result_paths = []
FindPath(['start'], calculate_table.copy(), result_paths)

print(len(result_paths))



# part 2
def FindPath2(result_paths, current_node, calculate_table):
    calculate_table = calculate_table.copy()   

    calculate_table[current_node] += 1

    smalls = [v for k, v in calculate_table.items() if k.islower()]
    if smalls.count(2) > 1:
        return False

    if current_node == 'end':
        result_paths.append(1)
        return True
    
    for next_node in neighbors[current_node]:
        if next_node.islower() and calculate_table[next_node] > 1:
            pass
        elif next_node == 'start':
            pass
        else:
            FindPath2(result_paths, next_node, calculate_table)
    return False

result_paths = []
FindPath2(result_paths, 'start', calculate_table.copy())

print(len(result_paths))
