import numpy as np

rng = np.random.default_rng()

# print(rng.integers(1,7)) #high is exclusive
print(rng.integers(1,8,5)) #size is number of elements, we will get an 1D array
print(rng.integers(1,7,(3,4))) # we'll get 2D array now

#we can use seed to get the same result again, if required by doing np.random.default_rng(seed=1)
