# Synergy Task Phase

## Question
17. Given a1 = [[1,1],[2,2]] and a2 = [[3,3],[4,4]], produce the vstack result, the hstack result, and np.concatenate along axis=1.

## Aim
- To join two arrays vertically and horizontally using np.vstack, np.hstack and np.concatenate

## Program
```
import numpy as np
a1 = np.array([[1,1],[2,2]])
a2 = np.array([[3,3],[4,4]])
print("Vertical stack:")
print(np.vstack((a1,a2)))
print("Horizontal stack:")
print(np.hstack((a1,a2)))
print("Concatenate along axis=1:")
print(np.concatenate((a1,a2),axis=1))
```

## Output
```
C:\SynergyTP>python NumpyP17.py
Vertical stack:
[[1 1]
 [2 2]
 [3 3]
 [4 4]]
Horizontal stack:
[[1 1 3 3]
 [2 2 4 4]]
Concatenate along axis=1:
[[1 1 3 3]
 [2 2 4 4]]
```

## Explanation
- **np.array()**: used to create the two 2x2 arrays `a1` and `a2`
- **np.vstack((a1,a2))**: stacks the arrays vertically, one below the other, so `a2` is added as new rows under `a1`. The result has shape (4, 2)
- **np.hstack((a1,a2))**: stacks the arrays horizontally, side by side, so `a2` is added as new columns next to `a1`. The result has shape (2, 4)
- **np.concatenate((a1,a2), axis=1)**: joins the arrays along axis 1, which is the column direction, so it gives the same result as hstack here. With axis=0 it would match vstack
- The arrays are passed as a tuple, and their sizes must match along the other axis. The question asked for three ways of joining the two arrays, so I created both arrays and printed the result of each.
