import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B)) # 纵向上下合并
D = np.hstack((A, B)) # 横向左右合并

print(C)
print(D)

print(np.vstack(A))
print(A.reshape(3, 1))
print(A.reshape(A.size, 1))
print(A.reshape(-1, 1))
print(np.mat(A).T)

E = np.arange(12).reshape(3, 4)
print(E)
# split只能等分，例如4列只能分成1，2，4，不能分成3
print(np.split(E, 2, axis=1)) # 把E分成左右两部分，按列操作，保留列数据
print(np.split(E, 3, axis=0)) # 把E分成上下三部分，按行操作，保留行数据，其实E一共3行，分成上下3部分，就是每一行是一个部分

# array_split可以实现不等分，例如：4列可以分为2，1，1
print(np.array_split(E, 3, axis=1))

# 纵向分割，按行操作
print(np.vsplit(E, 3))
# 横向风格，按列操作
print(np.hsplit(E, 2))
