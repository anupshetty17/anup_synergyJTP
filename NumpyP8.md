# Synergy Task Phase

## Question
8. Use arr = np.array([4, 15, 8, 23, 42, 16, 7, 30]). Print the values greater than 10, the even values, and the values from 10 to 30 inclusive.

## Aim
- To filter the elements of an array using boolean masking based on given conditions

## Program
```
import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print("Array values greater than 10:",arr[arr>10])
print("Array even values:",arr[arr%2==0])
print("Array values between 10 and 30:",arr[(arr>=10) & (arr<=30)])
```

## Output
```
C:\SynergyTP>python NumpyP8.py
Array values greater than 10: [15 23 42 16 30]
Array even values: [ 4  8 42 16 30]
Array values between 10 and 30: [15 23 16 30]
```

## Explanation
- **arr>10**: compares every element with 10 and gives an array of True/False values, called a boolean mask
- **arr[arr>10]**: uses that mask to keep only the elements where the condition is True
- **arr%2==0**: the remainder after dividing by 2 is 0 only for even numbers, so this mask selects the even values
- **(arr>=10) & (arr<=30)**: combines two conditions with `&` so that only values from 10 to 30, including both 10 and 30, are selected. Each condition needs its own brackets
- The question asked for three different filters on the same array, so I created the array and wrote a condition for each one. Then I used the condition as a mask to pick the matching values and printed them.
