# Synergy Task Phase

## Question
11. Given s = np.array([2, 5, 8, 11, 14]), use np.searchsorted to find where 9 would be inserted. Then do it for [1, 12, 5] in one call. Expected: 3, then [0 4 1].

## Aim
- To find the positions where values can be inserted into a sorted array while keeping it sorted, using np.searchsorted

## Program
```
import numpy as np
s = np.array([2, 5, 8, 11, 14])
print("Insert position of 9:",np.searchsorted(s,9))
print("Insert positions of [1, 12, 5]:",np.searchsorted(s,[1,12,5]))
```

## Output
```
C:\SynergyTP>python NumpyP11.py
Insert position of 9: 3
Insert positions of [1, 12, 5]: [0 4 1]
```

## Explanation
- **np.searchsorted(s, value)**: returns the index at which the value should be inserted in the sorted array `s` so that the array stays sorted. It does not change the array
- **np.searchsorted(s, 9)**: 9 is bigger than 2, 5 and 8 but smaller than 11, so it goes at index 3
- **np.searchsorted(s, [1,12,5])**: if a list is given instead of a single value, it returns one position for each value, so all three are found in one call
- 1 goes at index 0 because it is smaller than everything, 12 goes at index 4 because it lies between 11 and 14, and 5 gives index 1 because it is already present and by default the position before the existing value is returned
- The array `s` must already be sorted for the answer to be correct. The question asked for the insert position of one value and then of several values, so I first used a single value and then passed a list to get all positions at once.
