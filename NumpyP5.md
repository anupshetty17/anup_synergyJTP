# Synergy Task Phase

## Question
5. Use a = np.arange(1, 36).reshape(5, 7). Print the 3rd row, the 4th column, the last row and the last column.

## Aim
- To create a 2D array and access its rows and columns using indexing

## Program
```
import numpy as np
a=np.arange(1,36).reshape(5,7)
print("3rd row:",a[2])
print("4th column:",a[:,3])
print("Last row:",a[-1])
print("Last column:",a[:,-1])
```

## Output
```
C:\SynergyTP>python NumpyP5.py
3rd row: [15 16 17 18 19 20 21]
4th column: [ 4 11 18 25 32]
Last row: [29 30 31 32 33 34 35]
Last column: [ 7 14 21 28 35]
```

## Explanation
- **np.arange(1,36)**: creates the numbers from 1 to 35, because the upper limit 36 is not included
- **reshape(5,7)**: arranges those 35 numbers into 5 rows and 7 columns
- **a[2]**: gives the 3rd row, because indexing starts from 0
- **a[:,3]**: the `:` selects all rows and `3` selects the column at index 3, which is the 4th column
- **a[-1]**: negative index counts from the end, so it gives the last row
- **a[:,-1]**: selects all rows of the last column
- The question asked for specific rows and columns of a 5x7 array, so I first created the array and reshaped it. Then I used indexing, remembering that it starts at 0, to pick the 3rd row, 4th column, last row and last column and printed them.
