# Synergy Task Phase

## Question
19. Given a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20]), print the unique values, how many times each occurs, and the first index of each. Expected counts: [3 2 2 2 1 1 1 1 1 1].

## Aim
- To find the unique values of an array, their counts and their first positions using np.unique

## Program
```
import numpy as np
a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20])
values, first_index, counts = np.unique(a, return_index=True, return_counts=True)
print("Unique values:",values)
print("Count of each value:",counts)
print("First index of each value:",first_index)
```

## Output
```
C:\SynergyTP>python NumpyP19.py
Unique values: [11 12 13 14 15 16 17 18 19 20]
Count of each value: [3 2 2 2 1 1 1 1 1 1]
First index of each value: [ 0  2  3  4  5  6  7 12 13 14]
```

## Explanation
- **np.unique(a)**: returns the distinct values of the array in sorted order, with the repeated values removed
- **return_counts=True**: also returns how many times each unique value occurs in the array, in the same order as the unique values. For example 11 occurs 3 times, and 12, 13 and 14 occur 2 times each
- **return_index=True**: also returns the index of the first occurrence of each unique value in the original array. For example 11 first appears at index 0, 12 at index 2 and 18 at index 12
- When both options are used, np.unique returns three arrays in this order: the values, the first indices and the counts, so I unpacked them in that order
- The question asked for the unique values, their counts and their first positions, so I used a single np.unique call with both options and printed the three results. The counts match the expected [3 2 2 2 1 1 1 1 1 1].
