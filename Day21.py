import numpy as np

p1_pose = 8
p2_pose = 4

def Mod10(n:int):
    return (n - 1 ) % 10 + 1

def Dice100(n:int):
    return (n - 1 ) % 100 + 1

p1_score = 0
p2_score = 0
for n in range(1, 400):
    
    die_1 = Dice100(3 * (n - 1) + 1)
    die_2 = Dice100(3 * (n - 1) + 2)
    die_3 = Dice100(3 * (n - 1) + 3)
    res = die_1 + die_2 + die_3

    if n % 2 : 
        p1_pose = Mod10(p1_pose + res)
        p1_score += p1_pose
        print('die ' + str(3 * n) + ' Player1 rolls' + str(die_1) + ', ' + str(die_2) + ', ' +str(die_3) + ' move to ' + str(p1_pose) + ' score ' + str(p1_score))
    else:
        p2_pose = Mod10(p2_pose + res)
        p2_score += p2_pose
        print('die ' + str(3 * n) + ' Player2 rolls' + str(die_1) + ', ' + str(die_2) + ', ' +str(die_3) + ' move to ' + str(p2_pose) + ' score ' + str(p2_score))
    pass
