import numpy as np

# print(np.__version__)

my_list = [1,2,3,4]
my_list =my_list*2
print(my_list) #normal array

array = np.array([1,2,3,4,5]) #numpy array
array*=2
print(array)

arr = np.array('A')
print(arr.ndim) #0-dimensional array
print(arr.shape)

arr = np.array(['A','B','C','D','E'])
print(arr.ndim) #1-D array
print(arr.shape) #gives (columns) or we can say the number of elements in this case

arr = np.array([['A','B','C','D','E'],
                ['G','H','I','J','K']])
print(arr.ndim) #2-D array
print(arr.shape) #gives ( rows, columns)

arr = np.array([[['A','B','C'],['D','E','F'], ['G','H','I']],
                [['J','K','L'],['M','N','O'],['P','Q','R']],
                [['S','T','U'],['V','W','X'],['Y','Z','_']]
                ])
print(arr.ndim) #3-dimensional array

print(arr.shape) #gives (layers, rows, columns)

print (arr[0][0][0]) #using chain indexing of array

print(arr[0,0,1]) #using multidimensional indexing of numpy array
#we can do string concatenation also

numbers = np.array(
       [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
)

#array[start : end : step]

#accessing rows
print(numbers[1]) #prints second row
# print(numbers[0:])    #prints all rows
print(numbers[0:3])     #prints 0,1,2 row
print(numbers[0:4:2]) #can be also used as numbers[::2] , this prints every second row
print(numbers[::-2]) ##prints every second row starting from lsat

#accessing columns
print(numbers[:, 1]) #print 1st column 2,6,10,14
print(numbers[:, 0:3]) #prints 0,1,2 column
print(numbers[:, 1:4]) #prints 1,2,3 column
print(numbers[:, 1:]) #print column 1 till the end
print(numbers[:, ::2]) #prints every second column starting from col 0
print(numbers[:, 1::2]) #prints every second column starting from col 1
print(numbers[:, ::-1]) #prints all columns starting from last
print(numbers[:, ::-2])#prints every second column starting from last

#accessing both rows and columns

print(numbers[ 0:2 , 0:2])#prints row 0,1 and col 0,1 (4 elements)
print(numbers[ 0:2 , 2:4]) #prints row 0,1  and col 2,3
print(numbers[ 2: , 0:2]) #print row 2,3 and col 0,1 , if we're going till the last index, we can skip that , but we need to give :
print(numbers[ 2:, 2:]) #print row 2,3 and col 2,3 as going till last row,column, omitted those indices
print(numbers[ 0:, 0:]) #prints all rows, cols

#scalar arithemetic

new_arr = np.array([1,2,3,4,5])

print(new_arr + 1)
print(new_arr * 2)
print(new_arr - 1)
print(new_arr / 2)
print(new_arr ** 4)

# vector math function
print( np.sqrt(new_arr))
print(np.round(np.sqrt(new_arr)))
#can use floor and ceil
print(np.pi)

radii = np.array([1,2,3,4,5])

print( np.pi * radii **2)

# element wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) #adds each corresponding element
print(array1 * array2) #multiplies them, prints [ 1*4 2*5 3*6 ]
print(array1 ** array2) # prints [ 1**4 2**5 3**6 ]

#Comparison operators

scores = np.array([91 , 55 , 100 ,73 ,82, 64])

print(scores == 100) #returns an array of boolean
print(scores >= 60)

scores[scores < 60] = 0 #sets the scores of all the elements which are
print(scores)


