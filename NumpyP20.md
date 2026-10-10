# Synergy Task Phase

## Question
20. Given a = np.array([1,2,3,4,5]) and b = np.array([4,5,6,7]), compute the union, intersection, difference (a minus b) and symmetric difference. Expected: [1..7], [4 5], [1 2 3], [1 2 3 6 7].

## Aim
- To perform set operations on arrays using np.union1d, np.intersect1d, np.setdiff1d and np.setxor1d

## Program
```
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7])
print("Union:",np.union1d(a,b))
print("Intersection:",np.intersect1d(a,b))
print("Difference (a minus b):",np.setdiff1d(a,b))
print("Symmetric difference:",np.setxor1d(a,b))
```

## Output
```
C:\SynergyTP>python NumpyP20.py
Union: [1 2 3 4 5 6 7]
Intersection: [4 5]
Difference (a minus b): [1 2 3]
Symmetric difference: [1 2 3 6 7]
```

## Explanation
- **np.union1d(a,b)**: returns all the values that are in a or b, sorted and without repeats
- **np.intersect1d(a,b)**: returns only the values that are present in both arrays, which are 4 and 5
- **np.setdiff1d(a,b)**: returns the values that are in `a` but not in `b`. The order matters here, because b minus a would give [6 7]
- **np.setxor1d(a,b)**: the symmetric difference, which returns the values that are in only one of the two arrays, so the common values 4 and 5 are left out
- All four functions return a sorted array of unique values. The question asked for four set operations on the same two arrays, so I created the arrays once and used one function for each operation.
- 
