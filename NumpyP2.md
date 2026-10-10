# Synergy Task phase

## Question
- 2. Create a 3x2 array of zeros, a 2x4 array of ones with dtype=int, and a 2x3 array filled with 7 using np.full.

## Aim
- To create an 2d array containing zeros,another containing one, and another containing all element as 7

## Program
```
import numpy as np
a=np.zeros((2,3))
b=np.ones((2,4),dtype=int)
c=np.full((2,3),7)
print("Array of zeros:",a)
print("Array of ones:",b)
print("Array of sevens:",c)
```

## Output
```
Array of zeros: [[0. 0. 0.]
 [0. 0. 0.]]
Array of ones: [[1 1 1 1]
 [1 1 1 1]]
Array of sevens: [[7 7 7]
 [7 7 7]]

```

## Explaination
- **np.zeros()**: used to create an array containing all elements as 0
- **np.ones()**: Used to create an array containing all element as 1
- **np.full()**: Used to create an array containing all element as given specified value
