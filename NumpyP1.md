# Synergy Task Phase

## Question
1. Create an array from [3, 6, 9, 12, 15]. Print its shape, ndim, size and dtype.

## Aim
- To determine shape,dimension,size andtype of a given array

## Program
```
import numpy as np
a=np.array([3,6,9,12,15])
print("Dimension of array:",a.ndim)
print("Shape of array:",a.shape)
print("Size of array:",a.size)
print("Type of array:",a.dtype)
```

## Output
```
C:\SynergyTP>python NumpyP1.py
Dimension of array: 1
Shape of array: (5,)
Size of array: 5
Type of array: int64
```
## Explaination
- **np.array()**:Used to create a Numpy array
- **a.ndim**: returns the number of dimensions whether it is 1,2 and so on
- **a.shape**: return the size along each dimension in the form of tuple
- **a.size**: return the size of an array
- **a.dtype**: return the data type of an element
- As question asked me to display the size,shape,type and dimension of an given array,I first created an array and then used Numpy function to find the required things and printed it 
