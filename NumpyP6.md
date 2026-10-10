# Synergy Task Phase

## Question
6. Use the same array from Question 5. Print every second element of the first row. Print the 2x3 block from rows 1 to 2 and columns 2 to 4.

## Aim
- To use slicing to extract elements and sub-blocks from a 2D array

## Program
```
import numpy as np
a = np.arange(1, 36).reshape(5, 7)
print("Every second element of first row:",a[0,::2])
print("Block from array:",a[1:3,2:5])
```

## Output
```
C:\SynergyTP>python NumpyP6.py
Every second element of first row: [1 3 5 7]
Block from array: [[10 11 12]
 [17 18 19]]
```

## Explanation
- **np.arange(1,36).reshape(5,7)**: creates the numbers 1 to 35 arranged as 5 rows and 7 columns
- **a[0,::2]**: `0` picks the first row and `::2` takes every second element from start to end (step of 2)
- **a[1:3,2:5]**: slicing is written as `start:stop` and the stop is not included, so `1:3` picks rows 1 and 2 and `2:5` picks columns 2, 3 and 4 (indexing starts from 0)
- The block has 2 rows and 3 columns, so its shape is 2x3 as the question asked
- The question asked for a stepped slice of the first row and a 2x3 block, so I first created the array and then used slicing with a step for the row and start:stop for the block, and printed both.
