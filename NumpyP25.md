# Synergy Task Phase

## Question
25. In one line of NumPy, compute the mean squared error for predictions = np.array([2.5, 0.0, 2.1, 7.8]) and labels = np.array([3.0, -0.5, 2.0, 8.0]). Expected: 0.1375.

## Aim
- To calculate the mean squared error between predicted values and actual values using a single line of NumPy

## Program
```
import numpy as np
predictions = np.array([2.5, 0.0, 2.1, 7.8])
labels = np.array([3.0, -0.5, 2.0, 8.0])
print("Mean squared error:",np.mean((predictions-labels)**2))
```

## Output
```
C:\SynergyTP>python NumpyP25.py
Mean squared error: 0.1375
```

## Explanation
- **predictions-labels**: subtracts the arrays element by element, giving the error of each prediction: [-0.5, 0.5, 0.1, -0.2]
- **(...)**2**: squares each error, so negative errors do not cancel out the positive ones. This gives [0.25, 0.25, 0.01, 0.04]
- **np.mean(...)**: takes the average of the squared errors, which is 0.55 / 4 = 0.1375
- This is the formula for mean squared error, which is the average of (prediction - label) squared. Because NumPy works on whole arrays at once, the entire calculation fits in one line without any loop
- The question asked for the mean squared error in one line, so I created the two arrays and computed it in a single print statement. The result matches the expected 0.1375.
