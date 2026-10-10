# Synergy Task Phase

## Question
3. With rng = np.random.default_rng(), create a 3x3 array of random floats and a 2x5 array of random integers from 0 to 9. Then use np.random.randint to create a 4x4 array of integers from 1 to 100.

## Aim
- To generate arrays of random floats and random integers of given shapes and ranges using NumPy

## Program
```
import numpy as np
rng = np.random.default_rng()
a=rng.random((3,3))
b=rng.integers(0,10,(2,5))
c=np.random.randint(1,101,(4,4))
print("Random float array:",a)
print("Random integer array:",b)
print("Random integer array between 1 and 100:",c)
```

## Output
```
C:\SynergyTP>python Numpy3.py
Random float array: [[0.24101306 0.80610871 0.45125125]
 [0.60912198 0.43949698 0.79745861]
 [0.16623903 0.86529365 0.52735876]]
Random integer array: [[9 0 9 1 8]
 [6 1 2 2 0]]
Random integer array between 1 and 100: [[89 26 38 80]
 [78  6 25 15]
 [68 32 56 76]
 [51 48  3 12]]
```

## Explanation
- **np.random.default_rng()**: creates a random number generator object, which I stored in `rng`
- **rng.random((3,3))**: gives a 3x3 array of random floats between 0 and 1
- **rng.integers(0,10,(2,5))**: gives a 2x5 array of random integers from 0 to 9, because the upper limit 10 is not included
- **np.random.randint(1,101,(4,4))**: gives a 4x4 array of random integers from 1 to 100, because the upper limit 101 is not included
- The question asked for three random arrays of different shapes and ranges, so I first created the generator and used it for the float and integer arrays. Then I used `np.random.randint` for the last one and printed all three. The values change on every run because they are random.
