# Synergy Task Phase

## Question
14. Reshape np.arange(1, 13) into (3, 4), (2, 6), (2, 3, 2) and (4, -1). Print the shape of each.

## Aim
- To reshape a 1D array into different shapes using reshape() and to understand the use of -1 in reshape

## Program
```
import numpy as np
a = np.arange(1, 13)
b = a.reshape(3, 4)
c = a.reshape(2, 6)
d = a.reshape(2, 3, 2)
e = a.reshape(4, -1)
print("Shape of (3,4) reshape:",b.shape)
print("Shape of (2,6) reshape:",c.shape)
print("Shape of (2,3,2) reshape:",d.shape)
print("Shape of (4,-1) reshape:",e.shape)
```

## Output
```
C:\SynergyTP>python NumpyP14.py
Shape of (3,4) reshape: (3, 4)
Shape of (2,6) reshape: (2, 6)
Shape of (2,3,2) reshape: (2, 3, 2)
Shape of (4,-1) reshape: (4, 3)
```

## Explanation
- **np.arange(1, 13)**: creates the numbers 1 to 12, so the array has 12 elements
- **reshape()**: changes the shape of an array without changing its data. The new shape must use exactly the same number of elements, so the product of the dimensions must be 12 (3x4, 2x6 and 2x3x2 all give 12)
- **reshape(4, -1)**: the -1 tells NumPy to work out that dimension by itself. Here 12 elements split into 4 rows leaves 12/4 = 3 columns, so the shape becomes (4, 3)
- **.shape**: returns the size of each dimension as a tuple
- The question asked for four different shapes of the same 12 numbers, so I created the array once, reshaped it four times and printed the shape of each. Only one -1 can be used in a reshape.
