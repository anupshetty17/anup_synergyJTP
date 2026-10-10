# Synergy Task Phase

## Question
4. Create the numbers 0 to 9 as int8 and as int64. Print the nbytes of each.

## Aim
- To create arrays of the same numbers with different data types and compare the memory they use

## Program
```
import numpy as np
a=np.array([0,1,2,3,4,5,6,7,8,9],dtype=np.int8)
b=np.array([0,1,2,3,4,5,6,7,8,9],dtype=np.int64)
print("Number of bytes of array a:",a.nbytes)
print("Number of bytes of array b:",b.nbytes)
```

## Output
```
C:\SynergyTP>python NumpyP4.py
Number of bytes of array a: 10
Number of bytes of array b: 80
```

## Explanation
- **np.array()**: used to create a NumPy array
- **dtype=np.int8**: stores each element as an 8-bit integer, which takes 1 byte per element
- **dtype=np.int64**: stores each element as a 64-bit integer, which takes 8 bytes per element
- **a.nbytes**: returns the total number of bytes used by the elements of the array (number of elements x bytes per element)
- Both arrays have the same 10 numbers, so array a uses 10 x 1 = 10 bytes and array b uses 10 x 8 = 80 bytes. This shows that choosing a smaller data type saves memory when the values are small enough to fit in it.
