# Synergy Task Phase

## Question
18. Given x = np.arange(1, 25).reshape(2, 12), split it into 3 equal parts. Split it after the 3rd and 4th columns. Then split np.arange(1, 7) into 4 parts with np.array_split.

## Aim
- To split arrays into smaller arrays using np.split and np.array_split

## Program
```
import numpy as np
x = np.arange(1, 25).reshape(2, 12)

print("Split into 3 equal parts:")
for part in np.split(x, 3, axis=1):
    print(part)

print("Split after 3rd and 4th columns:")
for part in np.split(x, [3, 4], axis=1):
    print(part)

print("array_split of 1 to 6 into 4 parts:")
for part in np.array_split(np.arange(1, 7), 4):
    print(part)
```

## Output
```
C:\SynergyTP>python NumpyP18.py
Split into 3 equal parts:
[[ 1  2  3  4]
 [13 14 15 16]]
[[ 5  6  7  8]
 [17 18 19 20]]
[[ 9 10 11 12]
 [21 22 23 24]]
Split after 3rd and 4th columns:
[[ 1  2  3]
 [13 14 15]]
[[ 4]
 [16]]
[[ 5  6  7  8  9 10 11 12]
 [17 18 19 20 21 22 23 24]]
array_split of 1 to 6 into 4 parts:
[1 2]
[3 4]
[5]
[6]
```

## Explanation
- **np.arange(1, 25).reshape(2, 12)**: creates the numbers 1 to 24 arranged as 2 rows and 12 columns
- **np.split(x, 3, axis=1)**: splits the array into 3 equal parts along the columns. `axis=1` is needed because the default axis=0 would try to split the 2 rows into 3 parts, which is not possible. Each part has shape (2, 4)
- **np.split(x, [3, 4], axis=1)**: when a list of indices is given, the array is cut at those positions. Cutting at 3 and 4 gives columns 0 to 2, then column 3, then columns 4 to 11, so the parts have 3, 1 and 8 columns
- **np.array_split(np.arange(1, 7), 4)**: works like split but does not need equal parts. 6 elements cannot be divided equally into 4, so the first two parts get 2 elements each and the last two get 1 each. np.split would give an error here
- The question asked for three kinds of splitting, so I created the array and used each function, looping over the result to print each part on its own.
