import numpy as np

# camera1 see A, B, C, D and get A1, B1, C1, D1 as S1
# camera2 see A, B, C, D and get A2, B2, C2, D2 as S2

# To find T let T(X1) -> X2
#         where X1 X2 are the same point and X1 ∈ S1 and X2 ∈ S2

#
# method 1: base on high school math knowledge
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
# Thus, Distance(B1 - A1) = Distance(B2 - A2)
U1 = B1 - A1
V1 = C1 - A1
W1 = D1 - A1
U2 = B2 - A2
V2 = C2 - A2
W2 = D2 - A2

# roration matrix will sufficient:
# T_rot * V1 = V2
# T_rot * U1 = U2
# T_rot * W1 = W2
# reshape for 3x3 matrix for inverse operator
# S1 = [U1 V1 W1], S2 = [U2 V2 W2]
# T_rot * S1 = S2
# Thus, T_rot = S2 * inv(S1)
S1 = np.asmatrix([U1, V1, W1]).transpose()
S2 = np.asmatrix([U2, V2, W2]).transpose()
T_rot = np.matmul(S2, np.linalg.inv(S1))
# rot A1 to get A2 pose diff
T_trans = A2.transpose() - np.matmul(T_rot, A1.transpose())
# verify Rot(A1) - A2 = Rot(B1) - B2 = Rot(C1) - C2 = Rot(D1) - D2
print(T_trans)
print(B2.transpose() - np.matmul(T_rot, B1.transpose()))
print(C2.transpose() - np.matmul(T_rot, C1.transpose()))
print(D2.transpose() - np.matmul(T_rot, D1.transpose()))

# apply T
print(str(np.matmul(T_rot, A1.transpose()) + T_trans) + ' = ' + str(A2))
print(str(np.matmul(T_rot, B1.transpose()) + T_trans) + ' = ' + str(B2))
print(str(np.matmul(T_rot, C1.transpose()) + T_trans) + ' = ' + str(C2))
print(str(np.matmul(T_rot, D1.transpose()) + T_trans) + ' = ' + str(D2))


#
# method 2: base on Graphics knowledge
#

# pose P is (px, py, pz, 1), vector V is (vx, vy, vz, 0)
# for any affine matrix T will sufficient both conditions:
# T * P = Q  <->  both P, Q are pose
# T * V = U  <->  both U, V are vector

A1 = np.array([-763,-608,329, 1])
A2 = np.array([-857,735,662, 1])
B1 = np.array([382,-782,771, 1])
B2 = np.array([-415,-410,836, 1])
C1 = np.array([513,535,660, 1])
C2 = np.array([-526,-541,-481, 1])
D1 = np.array([370,550,692, 1])
D2 = np.array([-494,-398,-496, 1])

# T * A1 = A2 and so on
# let S1 [A1 B1 C1 D1], S2 = [A2 B2 C2 D2]
# T * S1 = S2
# Thus, T = S2 * inv(S1)
S1 = np.asmatrix([A1, B1, C1, D1]).transpose()
S2 = np.asmatrix([A2, B2, C2, D2]).transpose()
T = np.matmul(S2, np.linalg.inv(S1))

# apply T
print(str(np.matmul(T, A1.transpose())) + ' = ' + str(A2))
print(str(np.matmul(T, B1.transpose())) + ' = ' + str(B2))
print(str(np.matmul(T, C1.transpose())) + ' = ' + str(C2))
print(str(np.matmul(T, D1.transpose())) + ' = ' + str(D2))
