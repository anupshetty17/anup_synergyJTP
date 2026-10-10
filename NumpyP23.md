# Synergy Task Phase

## Question
23. Create a 3x4 array with rng.random. Print its overall sum, mean, min, max, std and prod, then the column sums, the row maxima, and the index of the overall maximum.

## Aim
- To calculate summary statistics of an array, both overall and along an axis, using NumPy functions

## Program
```
import numpy as np
rng = np.random.default_rng()
a = rng.random((3, 4))
print("Array:")
print(a)
print("Sum:",a.sum())
print("Mean:",a.mean())
print("Min:",a.min())
print("Max:",a.max())
print("Std:",a.std())
print("Prod:",a.prod())
print("Column sums:",a.sum(axis=0))
print("Row maxima:",a.max(axis=1))
print("Index of overall maximum (flattened):",a.argmax())
r, c = np.unravel_index(a.argmax(), a.shape)
print("Index of overall maximum (row, column):",(int(r),int(c)))
```

## Output
```
C:\SynergyTP>python NumpyP23.py
Array:
[[0.65455709 0.96367867 0.41757909 0.30721264]
 [0.04491555 0.37865035 0.99418791 0.24038426]
 [0.81063824 0.08803979 0.63530336 0.30501123]]
Sum: 5.840158184100401
Mean: 0.48667984867503344
Min: 0.044915548588708054
Max: 0.9941879124526996
Std: 0.307774461488599
Prod: 4.548521579986989e-06
Column sums: [1.51011087 1.43036882 2.04707036 0.85260813]
Row maxima: [0.96367867 0.99418791 0.81063824]
Index of overall maximum (flattened): 6
Index of overall maximum (row, column): (1, 2)
```

## Explanation
- **rng.random((3, 4))**: creates a 3x4 array of random floats between 0 and 1 using the generator `rng`
- **a.sum(), a.mean(), a.min(), a.max()**: give the sum, average, smallest and largest value of all the elements in the array
- **a.std()**: gives the standard deviation, which tells how spread out the values are around the mean
- **a.prod()**: multiplies all the elements together. Since every value is below 1, the product is a very small number, which is why it is shown in scientific notation (e-06 means multiplied by 10 to the power -6)
- **a.sum(axis=0)**: adds going down each column, so it gives one sum for each of the 4 columns
- **a.max(axis=1)**: finds the largest value going across each row, so it gives one maximum for each of the 3 rows
- **a.argmax()**: gives the index of the largest value after the array is flattened to 1D. Here it is 6, which means the 7th element. `np.unravel_index` converts it into a (row, column) position, which is (1, 2)
- The values change on every run because they are random, so the output on another run will be different. The question asked for overall and axis-wise statistics, so I created the array once and used the matching function or axis for each item.
