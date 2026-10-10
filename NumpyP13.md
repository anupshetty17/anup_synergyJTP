# Synergy Task Phase

## Question
13. Given x = np.array([[1,2,3],[4,5,6]]), create f = x.flatten() and r = x.ravel(). Set f[0] = 100 and r[1] = 200, then print x.

## Aim
- To understand the difference between flatten() and ravel() when converting a 2D array into 1D

## Program
```
import numpy as np
x = np.array([[1,2,3],[4,5,6]])
f = x.flatten()
r = x.ravel()
f[0] = 100
r[1] = 200
print("Array x:")
print(x)
```

## Output
```
C:\SynergyTP>python NumpyP13.py
Array x:
[[  1 200   3]
 [  4   5   6]]
```

## Explanation
- **x.flatten()**: converts the 2D array into a 1D array and always returns a copy, so `f` has its own memory
- **x.ravel()**: also converts the array into 1D, but it returns a view whenever possible, so `r` shares memory with `x`
- **f[0] = 100**: changes only the copy `f`, so `x` is not affected and the 1 stays in `x`
- **r[1] = 200**: changes the view `r`, so the second element of `x` also changes from 2 to 200
- That is why the printed `x` shows only the change made through `r`. The question asked to change one element through each of the two methods and then print `x`, so I created both, modified them, and printed `x` to see which change reached the original array.
