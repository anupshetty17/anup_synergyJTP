# Synergy Task Phase

## Question
10. Given marks = np.array([[45,80,67],[90,55,72],[38,60,85]]), print the marks that are 60 or above. Then count how many students scored 40 or more in each subject (column). Expected: [2 3 3].

## Aim
- To filter values of a 2D array using a condition and to count the values that satisfy a condition along each column

## Program
```
import numpy as np
marks = np.array([[45,80,67],[90,55,72],[38,60,85]])
print("Marks that are 60 or above:",marks[marks>=60])
print("Number of students with 40 or more marks in each subject:",np.count_nonzero(marks>=40, axis=0))
```

## Output
```
C:\SynergyTP>python NumpyP10.py
Marks that are 60 or above: [80 67 90 72 60 85]
Number of students with 40 or more marks in each subject: [2 3 3]
```

## Explanation
- **marks>=60**: compares every mark with 60 and gives a boolean mask of True/False values
- **marks[marks>=60]**: uses the mask to keep only the marks that are 60 or above. The result is a 1D array
- **marks>=40**: gives a mask of the students who scored 40 or more. The `>=` is used because 40 itself should be counted
- **np.count_nonzero(..., axis=0)**: counts the True values along axis 0, which means going down each column, so we get one count for each subject
- The question asked for the marks above a limit and then a count for each subject, so I first filtered the array with a condition. Then I applied the second condition and counted the True values column-wise. Subject 1 has 2 students (45 and 90), and subjects 2 and 3 have all 3 students, giving [2 3 3].
