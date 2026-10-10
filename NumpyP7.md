# Synergy Task Phase

## Question
7. Given arr = np.arange(1, 13).reshape(2, 2, 3), print 6, then the first row of the second block ([7 8 9]), then the last element using negative indices (12).

## Aim
- To access elements of a 3D array using positive and negative indexing

## Program
```
import numpy as np
arr = np.arange(1, 13).reshape(2, 2, 3)
print("Element:",arr[0,1,2])
print("First row of second block:",arr[1,0,:])
print("Last element:",arr[-1,-1,-1])
```

## Output
```
C:\SynergyTP>python NumpyP7.py
Element: 6
First row of second block: [7 8 9]
Last element: 12
```

## Explanation
- **np.arange(1,13).reshape(2,2,3)**: creates the numbers 1 to 12 and arranges them as 2 blocks, each with 2 rows and 3 columns
- The array looks like this: first block is `[[1 2 3] [4 5 6]]` and second block is `[[7 8 9] [10 11 12]]`
- **arr[0,1,2]**: the three indices are block, row and column, so this picks the first block, second row and third column, which is 6
- **arr[1,0,:]**: picks the second block and its first row, and `:` takes all the columns, giving [7 8 9]
- **arr[-1,-1,-1]**: negative indices count from the end, so this picks the last block, last row and last column, which is 12
- The question asked for three specific elements of a 3D array, so I first created the array and worked out the block, row and column of each value. Then I used indexing to pick them and printed them.
