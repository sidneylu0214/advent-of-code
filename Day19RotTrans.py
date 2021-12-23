import numpy as np

# camera1 see A, B, C, D and get A1, B1, C1, D1
# camera2 see A, B, C, D and get A2, B2, C2, D2

#
# method 1: base on high school knowledge
#
# camera1 is O1 = (0,0,0)
# camera2 is O2 is unknown
A1 = np.array([-763,-608,329])
A2 = np.array([-857,735,662])
B1 = np.array([382,-782,771])
B2 = np.array([-415,-410,836])
C1 = np.array([513,535,660])
C2 = np.array([-526,-541,-481])
D1 = np.array([370,550,692])
D2 = np.array([-494,-398,-496])

# Because we don't know how to move O1 to O2
# Need eliminate pose diff, that is, using vector
# Distance((B1 - O1) - (A1 - O1)) = Distance((B2 - O2) - (A2 - O2))
V1 = B1 - A1
V2 = C1 - A1
V3 = D1 - A1

U1 = B2 - A2
U2 = C2 - A2
U3 = D2 - A2

# to calculate roration matrix
# C_rot * V1 = U1
# C_rot * V2 = U2
# C_rot * V3 = U3

# S1 = [V1 V2 V3], S2 = [U1 U2 U3]
# C_rot * S1 = S2
# Thus, C_rot = S2 * inv(S1)
S1 = np.asmatrix([V1, V2, V3]).transpose()
S2 = np.asmatrix([U1, U2, U3]).transpose()
C_rot = np.matmul(S2, np.linalg.inv(S1))
# rot A1 to get A2 pose diff
C_trans = A2.transpose() - np.matmul(C_rot, A1.transpose())
# verify Rot(A1) - A2 = Rot(B1) - B2 = Rot(C1) - C2 = Rot(D1) - D2
print(C_trans)
print(B2.transpose()) - np.matmul(C_rot, B1.transpose())
print(C2.transpose()) - np.matmul(C_rot, C1.transpose())
print(D2.transpose()) - np.matmul(C_rot, D1.transpose())

# apply
print(str(np.matmul(C_rot, A1.transpose()) + C_trans) + ' = ' + str(A2))
print(str(np.matmul(C_rot, B1.transpose()) + C_trans) + ' = ' + str(B2))
print(str(np.matmul(C_rot, C1.transpose()) + C_trans) + ' = ' + str(C2))
print(str(np.matmul(C_rot, D1.transpose()) + C_trans) + ' = ' + str(D2))


#
# method 2: base on Graphics knowledge
#
# pose P is (px, py, pz, 1), vector V is (vx, vy, vz, 0)
# for any affine matrix A will sufficient both condition:
# A * P = Q  <-> both P, Q are pose
# A * V = U  <-> both U, V are vector

A1 = np.array([-763,-608,329, 1])
A2 = np.array([-857,735,662, 1])
B1 = np.array([382,-782,771, 1])
B2 = np.array([-415,-410,836, 1])
C1 = np.array([513,535,660, 1])
C2 = np.array([-526,-541,-481, 1])
D1 = np.array([370,550,692, 1])
D2 = np.array([-494,-398,-496, 1])

# Affine * A1 = A2 and so on
# let S1 [A1 B1 C1 D1], S2 = [A2 B2 C2 D2]
# Affine * S1 = S2
# Thus, Affine = S2 * inv(S1)
S1 = np.asmatrix([A1, B1, C1, D1]).transpose()
S2 = np.asmatrix([A2, B2, C2, D2]).transpose()
Affine = np.matmul(S2, np.linalg.inv(S1))

# verify Affine * S1 = S2
print(str(np.matmul(Affine, A1.transpose())) + ' = ' + str(A2))
print(str(np.matmul(Affine, B1.transpose())) + ' = ' + str(B2))
print(str(np.matmul(Affine, C1.transpose())) + ' = ' + str(C2))
print(str(np.matmul(Affine, D1.transpose())) + ' = ' + str(D2))
