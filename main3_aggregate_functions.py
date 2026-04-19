import numpy as np

array = np.array( [[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) #standard deviation
print(np.var(array)) #variance
print(np.median(array)) #median
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) #position of the minimum argument

print(np.sum(array ,axis = 0)) #prints sum of each column elements
print(np.sum(array ,axis = 1)) #prints sum of each row element