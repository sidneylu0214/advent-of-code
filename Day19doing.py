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

dist_tables = [GetDistanceTable(i) for i in intputs]

def LayerListsToSet(lists):
    return set(list(itertools.chain(*lists)))

dist_sets = [LayerListsToSet(t) for t in dist_tables]


test = np.array([1,2,1,2,1,2,2,3,4,5,6,4,4,23,2,2,32,1,2,2,342,1])
set1 = np.where(test == 2)


max = 0

def TryMapping(dist_set, dist_table_l, dist_table_w):
    dist_list = list(dist_set)
    dist_list.sort()
    pair_set = []
    l_list = set()
    w_list = set()

    for d in dist_list:
        set1 = [i.tolist() for i in np.where(dist_table_l == d)]
        set2 = [i.tolist() for i in np.where(dist_table_w == d)]
        pair_set.append([set1, set2])
        l_list = l_list.union(LayerListsToSet(set1))
        w_list = w_list.union(LayerListsToSet(set2))
    print(l_list)
    print(w_list)
    global max
    if(max < len(w_list)):
        max = len(w_list)
    
    return pair_set

for local in range(1, len(dist_sets)):
    for world in range(len(dist_sets)):
        
        intersect_set = dist_sets[local].intersection(dist_sets[world])
        intersect_set.remove(0)
    
        if len(intersect_set) >= 4 and local != world:
            print('set of ' + str(local) + ', ' + str(world))
            TryMapping(intersect_set, dist_tables[local], dist_tables[world])
            pass


test = 'test'



import numpy as np

A1 = np.array([-763,-608,329])
A2 = np.array([-857,735,662])
B1 = np.array([382,-782,771])
B2 = np.array([-415,-410,836])
C1 = np.array([513,535,660])
C2 = np.array([-526,-541,-481])
D1 = np.array([370,550,692])
D2 = np.array([-494,-398,-496])

V1 = B1 - A1
V2 = C1 - A1
V3 = D1 - A1

U1 = B2 - A2
U2 = C2 - A2
U3 = D2 - A2

S1 = np.asmatrix([V1, V2, V3]).transpose()
S2 = np.asmatrix([U1, U2, U3]).transpose()

Xrot = np.matmul(S2, np.linalg.inv(S1))
Xtrans = np.matmul(Xrot, A1.transpose()) - A2.transpose()


print(Xrot)
print(Xtrans)
print(np.matmul(Xrot, B1.transpose()) - B2.transpose())
print(np.matmul(Xrot, C1.transpose()) - C2.transpose())
print(np.matmul(Xrot, D1.transpose()) - D2.transpose())


A1 = np.array([-763,-608,329, 1])
A2 = np.array([-857,735,662, 1])
B1 = np.array([382,-782,771, 1])
B2 = np.array([-415,-410,836, 1])
C1 = np.array([513,535,660, 1])
C2 = np.array([-526,-541,-481, 1])
D1 = np.array([370,550,692, 1])
D2 = np.array([-494,-398,-496, 1])

S1 = np.asmatrix([A1, B1, C1, D1]).transpose()
S2 = np.asmatrix([A2, B2, C2, D2]).transpose()

Xall = np.matmul(S2, np.linalg.inv(S1))

print(Xall)


print(np.matmul(Xall, A1.transpose()))
print(A2)

print(np.matmul(Xall, B1.transpose()))
print(B2)

print(np.matmul(Xall, C1.transpose()))
print(C2)

print(np.matmul(Xall, D1.transpose()))
print(D2)
