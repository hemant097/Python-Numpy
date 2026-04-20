import numpy as np

rng = np.random.default_rng()

# print(rng.integers(1,7)) #high is exclusive
print(rng.integers(1,8,5)) #size is number of elements, we will get an 1D array
print(rng.integers(1,7,(3,4))) # we'll get 2D array now

#we can use seed to get the same result again, if required by doing np.random.default_rng(seed=1)

#For floating numbers
# np.random.seed(1)
print (np.random.uniform()) #returns a random floating point number between 0,1
print (np.random.uniform(-1,1))

print (np.random.uniform(-1,1,5))
print (np.random.uniform(-1,1,(5,2)))


#shuffling
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "banana", "cherry","coconut","pineapple"])

fruit = rng.choice(fruits)
print(fruit)

three_random_fruits = rng.choice(fruits,3)
print(three_random_fruits)

matrix_random_fruits = rng.choice(fruits,(3,3))
print(matrix_random_fruits)