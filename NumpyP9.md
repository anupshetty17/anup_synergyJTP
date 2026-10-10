# Synergy Task Phase

## Question
9. Find the indices of values greater than 15 using np.nonzero, then again using np.where. Expected: [1 3 4 5 7].

## Aim
- To find the positions (indices) of elements that satisfy a condition using np.nonzero and np.where

## Program
```
import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print("Positions using np.nonzero:",np.nonzero(arr>10)[0])
print("Positions using np.where:",np.where(arr>10)[0])
```

## Output
```
C:\SynergyTP>python NumpyP9.py
Positions using np.nonzero: [1 3 4 5 7]
Positions using np.where: [1 3 4 5 7]
```

## Explanation
- **arr>10**: compares every element with 10 and gives a boolean mask of True/False values
- **np.nonzero()**: returns the indices of the elements that are non-zero, which for a boolean mask means the positions where the condition is True
- **np.where(condition)**: when given only a condition, it also returns the indices where the condition is True
- Both functions return a tuple with one array for each dimension. Since the array is 1D, the tuple has only one array, so I used `[0]` to get the plain array of indices
- The question asked for the positions of the matching values by two methods, so I applied the same condition to the array and passed it to np.nonzero and np.where. Both gave the same indices, [1 3 4 5 7].
