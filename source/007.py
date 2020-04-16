import numpy as np

A = np.array([[1, 1], [1, 1]])
B = np.array([[2, 2], [2, 2]])

print(A.dot(B))

C = np.arange(3, 15)
print(C)
print(C.T)
for row in C:
    print(row)

for column in C.T:
    print(column)

for item in C.flat:
    print(item)

D = np.arange(5,17).reshape(3, 4)
print(D)
print(np.min(D))
print(np.argmin(D)) # 最小值所在的索引
print(np.mean(D, axis = 1)) # 求每一行的平均值
print(np.argmax(D)) # 最大值所在的索引

print(D[2, 3]) # 第3行，第4列
print(D[2:3,1:3])