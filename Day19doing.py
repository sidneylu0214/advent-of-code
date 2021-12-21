import numpy as np
import re

intput_txt = []
with open('input.txt', 'r') as lines:
    in_views = []

    for line in lines:
        if 'scanner' in line:
            intput_txt.append(in_views.copy())
            in_views = []
        else:
            try:
                in_views.append(np.array([line[:-1].split(',')], dtype = int))
            except ValueError:
                pass
    intput_txt.append(in_views)
    pass

intput_txt = intput_txt[1:]

def Dist(A):
    A = A[0]
    return np.dot(A, A)

def GetDistanceSet(input):
    distances = []

    for i in range(len(input)):
        for j in range(len(input)):
            distances.append(Dist(input[i] - input[j]))
    
    distances.sort()
    return distances[::2]

dis = GetDistanceSet(intput_txt[0])

test = 'test'
