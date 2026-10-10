# Synergy Task Phase

## Question
24. Given A = [[1,2],[3,4]] and B = [[5,6],[7,8]], print the element-wise product, the matrix product with np.matmul ([[19 22] [43 50]]), and the determinant of A with np.linalg.det (-2.0).

## Aim
- To perform element-wise multiplication, matrix multiplication and find the determinant of a matrix using NumPy

## Program
```
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("Element-wise product:")
print(A*B)
print("Matrix product:")
print(np.matmul(A,B))
print("Determinant of A:",round(np.linalg.det(A),2))
```

## Output
```
C:\SynergyTP>python NumpyP24.py
Element-wise product:
[[ 5 12]
 [21 32]]
Matrix product:
[[19 22]
 [43 50]]
Determinant of A: -2.0
```

## Explanation
- **A*B**: the `*` operator multiplies the elements at the same position, so 1x5, 2x6, 3x7 and 4x8 give [[5 12] [21 32]]
- **np.matmul(A,B)**: does proper matrix multiplication, where each row of A is multiplied with each column of B and the products are added. For example the first value is 1x5 + 2x7 = 19
- **np.linalg.det(A)**: calculates the determinant of a square matrix. For a 2x2 matrix it is (1x4) - (2x3) = -2
- The determinant is calculated using floating point numbers, so the raw value comes out as -2.0000000000000004 because of a tiny rounding error. I used `round(..., 2)` so that it prints as -2.0
- The question asked for three different operations on the same two matrices, so I created both matrices once and used one operator or function for each result.
