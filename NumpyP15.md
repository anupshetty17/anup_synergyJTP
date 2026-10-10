# Synergy Task Phase

## Question
15. Given a = np.array([1, 2, 3, 4, 5, 6]), make a row vector (1, 6) and a column vector (6, 1). Do it once with np.newaxis and once with np.expand_dims.

## Aim
- To convert a 1D array into a row vector and a column vector by adding a new axis, using np.newaxis and np.expand_dims

## Program
```
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])

row1 = a[np.newaxis, :]
col1 = a[:, np.newaxis]
print("Row vector using np.newaxis:",row1,"Shape:",row1.shape)
print("Column vector using np.newaxis:")
print(col1)
print("Shape:",col1.shape)

row2 = np.expand_dims(a, axis=0)
col2 = np.expand_dims(a, axis=1)
print("Row vector using np.expand_dims:",row2,"Shape:",row2.shape)
print("Column vector using np.expand_dims:")
print(col2)
print("Shape:",col2.shape)
```

## Output
```
C:\SynergyTP>python NumpyP15.py
Row vector using np.newaxis: [[1 2 3 4 5 6]] Shape: (1, 6)
Column vector using np.newaxis:
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
Shape: (6, 1)
Row vector using np.expand_dims: [[1 2 3 4 5 6]] Shape: (1, 6)
Column vector using np.expand_dims:
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
Shape: (6, 1)
```

## Explanation
- **a**: the original array is 1D with shape (6,), so it is neither a row nor a column
- **np.newaxis**: adds a new axis of length 1 wherever it is placed while slicing. `a[np.newaxis, :]` puts it in front, giving shape (1, 6), which is a row vector. `a[:, np.newaxis]` puts it after, giving shape (6, 1), which is a column vector
- **np.expand_dims(a, axis)**: does the same thing with a function, where `axis` is the position of the new axis. `axis=0` gives (1, 6) and `axis=1` gives (6, 1)
- The data stays the same in all four results and only the shape changes
- The question asked for both a row and a column vector by two different methods, so I created the array once and used each method for both. Both methods gave the same shapes.
