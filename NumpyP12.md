# Synergy Task Phase

## Question
12. Create a = np.arange(1, 9) and b = a[2:6]. Set b[0] = 99 and print a. Repeat with b = a[2:6].copy() and print a again.

## Aim
- To understand the difference between a view and a copy of a NumPy array

## Program
```
import numpy as np
a = np.arange(1, 9)
b = a[2:6]
b[0] = 99
print("a after changing the slice (view):",a)

a = np.arange(1, 9)
b = a[2:6].copy()
b[0] = 99
print("a after changing the copy:",a)
```

## Output
```
C:\SynergyTP>python NumpyP12.py
a after changing the slice (view): [ 1  2 99  4  5  6  7  8]
a after changing the copy: [1 2 3 4 5 6 7 8]
```

## Explanation
- **np.arange(1, 9)**: creates the numbers 1 to 8, because the upper limit 9 is not included
- **b = a[2:6]**: slicing a NumPy array gives a view, not a new array. `b` shares the same memory as `a`, so it holds the elements at index 2 to 5 of `a`
- **b[0] = 99**: since `b` is a view, changing its first element also changes `a[2]`, so `a` becomes [1 2 99 4 5 6 7 8]
- **a[2:6].copy()**: `.copy()` makes a completely separate array with its own memory
- **b[0] = 99 (on the copy)**: only `b` changes, so `a` stays [1 2 3 4 5 6 7 8]
- I created `a` again before the second part so that the 99 from the first part would not be left in it. The question asked to compare slicing with and without `.copy()`, so I changed the first element of `b` in both cases and printed `a` to see whether it was affected.
