# Synergy Task Phase

## Question
21. Given m = np.arange(1, 10).reshape(3, 3), add the row [10, 20, 30] to every row. Then add the column [[100], [200], [300]] to every column.

## Aim
- To add arrays of different shapes to a 2D array using NumPy broadcasting

## Program
```
import numpy as np
m = np.arange(1, 10).reshape(3, 3)
row = np.array([10, 20, 30])
col = np.array([[100], [200], [300]])
print("Original array:")
print(m)
print("After adding the row to every row:")
print(m + row)
print("After adding the column to every column:")
print(m + col)
```

## Output
```
C:\SynergyTP>python NumpyP21.py
Original array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
After adding the row to every row:
[[11 22 33]
 [14 25 36]
 [17 28 39]]
After adding the column to every column:
[[101 102 103]
 [204 205 206]
 [307 308 309]]
```

## Explanation
- **np.arange(1, 10).reshape(3, 3)**: creates the numbers 1 to 9 arranged as 3 rows and 3 columns
- **m + row**: `row` has shape (3,) while `m` has shape (3, 3). NumPy uses broadcasting, which stretches the row so that it is added to every row of `m`. So 10 is added to the first column, 20 to the second and 30 to the third
- **m + col**: `col` has shape (3, 1), so NumPy stretches it across the columns. Each row gets its own value added to all its elements, which means 100 goes to the first row, 200 to the second and 300 to the third
- Broadcasting works when the shapes match or when one of the sizes is 1, and it saves us from writing loops or repeating the row and column by hand
- The question asked for two additions, so I added the row to `m` and then the column to `m`. The second addition uses the original `m`, so the results do not build on each other.
