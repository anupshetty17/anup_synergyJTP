# Synergy Task Phase

## Question
16. Given a 3x4 array of 1 to 12, print np.flip with no axis, with axis=0 and with axis=1.

## Aim
- To reverse the order of elements of a 2D array along different axes using np.flip

## Program
```
import numpy as np
a = np.arange(1, 13).reshape(3, 4)
print("Original array:")
print(a)
print("Flip with no axis:")
print(np.flip(a))
print("Flip with axis=0:")
print(np.flip(a, axis=0))
print("Flip with axis=1:")
print(np.flip(a, axis=1))
```

## Output
```
C:\SynergyTP>python NumpyP16.py
Original array:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Flip with no axis:
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]
Flip with axis=0:
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
Flip with axis=1:
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]
```

## Explanation
- **np.arange(1, 13).reshape(3, 4)**: creates the numbers 1 to 12 and arranges them as 3 rows and 4 columns
- **np.flip(a)**: with no axis given, it reverses the order of elements along all axes, so the rows and the columns are both reversed. The result is the array turned upside down and left to right
- **np.flip(a, axis=0)**: reverses the order of the rows, so the last row comes first and the first row comes last. The numbers inside each row stay in the same order
- **np.flip(a, axis=1)**: reverses the order of the columns, so each row is read backwards, but the rows stay in the same place
- The question asked for the three kinds of flip on the same array, so I created the array once and printed the result of each flip. np.flip does not change the original array `a`.
