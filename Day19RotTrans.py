import numpy as np

#
# method 1: base on high school knowledge
#
# camera1 is O1 = (0,0,0)
# camera2 is O2 and unknown
# camera1 see A1, B1, C1, D1
# camera2 see A2, B2, C2, D2

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
V1 = B1 - A1
V2 = C1 - A1
V3 = D1 - A1

U1 = B2 - A2
U2 = C2 - A2
U3 = D2 - A2

# Xrot * V1 = U1
# Xrot * V2 = U2
# Xrot * V3 = U3

# S1 = [V1 V2 V3], S2 = [U1 U2 U3]
# Xrot * S1 = S2
S1 = np.asmatrix([V1, V2, V3]).transpose()
S2 = np.asmatrix([U1, U2, U3]).transpose()

# Thus, Xrot = S2 * inv(S1)
Xrot = np.matmul(S2, np.linalg.inv(S1))
# rot A1 to get A2
Xtrans = np.matmul(Xrot, A1.transpose()) - A2.transpose()
# verify Rot(A1) - A2 = Rot(B1) - B2 = Rot(C1) - C2 = Rot(D1) - D2
print(Xtrans)
print(np.matmul(Xrot, B1.transpose()) - B2.transpose())
print(np.matmul(Xrot, C1.transpose()) - C2.transpose())
print(np.matmul(Xrot, D1.transpose()) - D2.transpose())

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
S1 = np.asmatrix([A1, B1, C1, D1]).transpose()
S2 = np.asmatrix([A2, B2, C2, D2]).transpose()

# Affine = S2 * inv(S1)
Affine = np.matmul(S2, np.linalg.inv(S1))

# verify Affine * S1 = S2
print(str(np.matmul(Affine, A1.transpose())) + ' = ' + str(A2))
print(str(np.matmul(Affine, B1.transpose())) + ' = ' + str(B2))
print(str(np.matmul(Affine, C1.transpose())) + ' = ' + str(C2))
print(str(np.matmul(Affine, D1.transpose())) + ' = ' + str(D2))
