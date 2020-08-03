import numpy as np
arr1 = np.array([2,3,4],dtype=np.int64)
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2, 2.3, 3.4])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1 + arr2)
#
# print(arr2 * 10)
#
# data = [[1,2,3],[2,3,4]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

#将所有矩阵置为0
# print(np.zeros((3,5)))
#
# #将所有矩阵置为1
# print(np.ones((4,6)))
#
# #将所有矩阵置为空值，且三维
# print(np.empty((2,3,3)))

arr4 = np.arange(10)

arr4[5:8] = 10

print(arr4)

arr_slice = arr4[5:8].copy()

arr_slice[:] = 15

print(arr_slice)
print(arr4)