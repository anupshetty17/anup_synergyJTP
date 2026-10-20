# SYNERGY TASK PHASE

## QUESTION
 Do MidSem Averages Hide Inconsistency? Group by subject and compute the mean, standard deviation, minimum and maximum marks in one agg call. Rank the subjects by mean, then by standard deviation. Interpret: two subjects have almost the same average. Which one would a teacher need to investigate further and why?

## PROGRAM
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

marks = pd.DataFrame({
    'subject': ['Maths']*4 + ['Physics']*4 + ['Pps']*4,
    'marks': [72, 74, 70, 73, 60, 95, 50, 85, 80, 78, 82, 84]
})

# One agg call: mean, std, min, max
summary = marks.groupby('subject')['marks'].agg(
    mean='mean', std='std', min='min', max='max'
).round(2)
summary['range'] = summary['max'] - summary['min']
print("Summary:\n", summary)

# Rank by mean (highest first)
print("\nRanked by mean (highest first):\n",
      summary.sort_values('mean', ascending=False)[['mean']])

# Rank by std (lowest = most consistent first)
print("\nRanked by std (most consistent first):\n",
      summary.sort_values('std')[['std']])
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda10.py
Summary:
           mean    std  min  max  range
subject                               
Maths    72.25   1.71   70   74      4
Physics  72.50  21.02   50   95     45
Pps      81.00   2.58   78   84      6

Ranked by mean (highest first):
           mean
subject       
Pps      81.00
Physics  72.50
Maths    72.25

Ranked by std (most consistent first):
            std
subject       
Maths     1.71
Pps       2.58
Physics  21.02
```

## Explaination of my code
First I created the DataFrame. Then I used `groupby('subject')` and a single `agg()` call with named aggregation to get the mean, standard deviation, minimum and maximum of marks for each subject in one table. I also added a range column (max − min) to make the spread easy to see. To rank by mean, I used `sort_values('mean', ascending=False)`, so the highest average comes first. To rank by standard deviation, I used `sort_values('std')` in ascending order, so the most consistent subject comes first. Note that pandas `std()` is the sample standard deviation (ddof=1) by default.

## Interpretation
I believe that since physics and maths hve nearly the same average, Physics must be investigated rather than maths becuase there is huge gap of the students scoring from 50-95 but maths all the students are scored betwween 70-74 thus i would say that teacher should investigage the physics subject
