import numpy as np
import itertools

intputs = []
with open('input.txt', 'r') as intput_txt:
    in_views = []
    for line in intput_txt:
        if 'scanner' in line:
            intputs.append(in_views.copy())
            in_views = []
        else:
            try:
                in_views.append(np.array([int(i) for i in line[:-1].split(',')], dtype = np.longlong))
            except ValueError:
                pass
    intputs.append(in_views)
    intputs.pop(0)
    pass

def GetDistanceTable(input):
    shape = [len(input), len(input)]
    distances = np.zeros(shape, dtype = input[0].dtype)

    for i in range(len(input)):
        for j in range(len(input)):
            x = input[i] - input[j]
            distances[i][j] = (np.dot(x, x))

    return distances

tables = [GetDistanceTable(i) for i in intputs]

def DistSet(table):
    return set(list(itertools.chain(*table)))

dist_sets = [DistSet(t) for t in tables]


def TryMapping(dist_set, dist_table1, dist_table2):

    pass

for i in range(1, len(dist_sets)):
    for j in range(len(dist_sets)):
        intersect_set = sorted_dist[i].intersection(dist_sets[j])
        if len(intersect_set) > 3:
            TryMapping(intersect_set, )
            pass


test = 'test'
