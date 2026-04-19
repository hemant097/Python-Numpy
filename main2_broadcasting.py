import numpy as np

# Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions,
# so they match the larger array's shape

#the dimensions have the same size.
# OR
# One of the dimesion has a size of 1

array1 = np.array([ [1,2,3,4] ])
array2 = np.array([ [1],
                    [2],
                    [3],
                    [4] ])

print(array1.shape) #shape 1,4
print(array2.shape)# shape 4,1
#yes we can broadcast them, as one of them is 1

print(array1 * array2)

array1 = np.array([ [1,2,3,4] ,
                    [5,6,7,8]  ])
array2 = np.array([ [1],
                    [2],
                    [3],
                    [4] ])

# print(array1 * array2) #could not be broadcast together as shapes do not match 2,4 and 4,1 (4 and 1 are OK, but 2 and 4 not OK)

array1 = np.array([ [1,2,3,4] ,
                    [5,6,7,8] ,
                    [9,10,11,12],
                    [13,14,15,16] ])
array2 = np.array([ [1],
                    [2],
                    [3],
                    [4] ])

print(array1 * array2) # as they have shapes 4,4 and 4,1 now , 4 and 4 is OK (as equal) and 4 and 1 is also OK (as one of them is 1)


array1 = np.array([ [1,2,3,4] ,
                    [5,6,7,8] ,
                    [9,10,11,12],
                    [13,14,15,16] ])
array2 = np.array([ [1,2],
                    [2,3],
                    [3,4],
                    [4,5] ])

# print(array1 * array2) # ValueError: operands could not be broadcast together with shapes (4,4) (4,2)

arr1 = np.array([ [1,2,3,4,5,6,7,8,9,10] ])
arr2 = np.array([ [1],
                  [2],
                  [3],
                  [4],
                  [5],
                  [6],
                  [7],
                  [8],
                  [9],
                  [10]])

print(arr1.shape) # 1,10
print(arr2.shape) # 10,1
#Yes can be broadcasted

print(arr1*arr2)
