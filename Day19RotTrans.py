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