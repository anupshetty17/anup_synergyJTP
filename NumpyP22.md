# Synergy Task Phase

## Question
22. Write code that tries each of these additions and prints the result shape or the error message: (4,3)+(3,), (4,3)+(4,), (4,3)+(4,1), (2,3,4)+(3,1). Use np.ones for the arrays.

## Aim
- To understand the rules of broadcasting by checking which array shapes can be added and which cause an error

## Program
```
import numpy as np
pairs = [((4,3),(3,)), ((4,3),(4,)), ((4,3),(4,1)), ((2,3,4),(3,1))]
for s1, s2 in pairs:
    x = np.ones(s1)
    y = np.ones(s2)
    try:
        print(s1,"+",s2,"-> shape",(x+y).shape)
    except ValueError as e:
        print(s1,"+",s2,"-> Error:",e)
```

## Output
```
C:\SynergyTP>python NumpyP22.py
(4, 3) + (3,) -> shape (4, 3)
(4, 3) + (4,) -> Error: operands could not be broadcast together with shapes (4,3) (4,) 
(4, 3) + (4, 1) -> shape (4, 3)
(2, 3, 4) + (3, 1) -> shape (2, 3, 4)
```

## Explanation
- **np.ones(shape)**: creates an array of the given shape filled with 1s, so I could make the arrays directly from their shapes
- **Broadcasting rule**: NumPy compares the shapes from the right-most dimension to the left. Two dimensions are compatible if they are equal or if one of them is 1. If a shape has fewer dimensions, it is treated as having 1s added on its left
- **(4,3)+(3,)**: the last dimensions are 3 and 3, which match, and the missing dimension is treated as 1, so the result has shape (4, 3)
- **(4,3)+(4,)**: the last dimensions are 3 and 4, which are different and neither is 1, so NumPy raises a ValueError. To make it work, the (4,) array would have to be reshaped into (4,1)
- **(4,3)+(4,1)**: the last dimensions are 3 and 1, which is fine, and the first dimensions are 4 and 4, so the result has shape (4, 3)
- **(2,3,4)+(3,1)**: the (3,1) shape is treated as (1,3,1). Comparing from the right gives 4 and 1, 3 and 3, and 2 and 1, which are all compatible, so the result has shape (2, 3, 4)
- I used try and except to catch the ValueError so that the program keeps running and prints the error message instead of stopping at the incompatible case.
