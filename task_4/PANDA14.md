# SYNERGY TASK PHASE

## QUESTION
Q14. Delhi's Traffic and Air Quality. Combine the two weekly logs with concat (reset the index) and add a week column. Compute the correlation between vehicles and PM2.5 and the mean PM2.5 for each week. Interpret: if the city declares an alert when the weekly mean exceeds 70, which week triggers it? Name one other factor besides traffic that could also influence PM2.5.

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

week1 = pd.DataFrame({'vehicles_k': [30, 35, 40, 45], 'pm25': [52, 55, 60, 63]})
week2 = pd.DataFrame({'vehicles_k': [50, 55, 60, 65], 'pm25': [68, 72, 75, 80]})

# Add the week label to each log, then stack them
week1['week'] = 1
week2['week'] = 2
combined = pd.concat([week1, week2], ignore_index=True)
print("Combined data:\n", combined)

# Correlation between vehicles and PM2.5
corr = combined['vehicles_k'].corr(combined['pm25'])
print("\nCorrelation (vehicles vs PM2.5):", round(corr, 4))

# Mean PM2.5 per week
weekly_mean = combined.groupby('week')['pm25'].mean()
print("\nMean PM2.5 per week:\n", weekly_mean)

# Alert rule: weekly mean above 70
alert_weeks = weekly_mean[weekly_mean > 70]
print("\nWeeks that trigger the alert (mean > 70):", list(alert_weeks.index))
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda14.py
Combined data:
    vehicles_k  pm25  week
0          30    52     1
1          35    55     1
2          40    60     1
3          45    63     1
4          50    68     2
5          55    72     2
6          60    75     2
7          65    80     2

Correlation (vehicles vs PM2.5): 0.9986

Mean PM2.5 per week:
 week
1    57.50
2    73.75
Name: pm25, dtype: float64

Weeks that trigger the alert (mean > 70): [2]
```

## Explaination
First I created the two DataFrames and added a `week` column to each one before combining them, so every row remembers which log it came from. Then I used `pd.concat()` to stack them, with `ignore_index=True` so the index runs 0 to 7 instead of repeating 0 to 3 twice. I used `Series.corr()` to get the correlation between vehicles_k and pm25 across all 8 rows. Then `groupby('week')['pm25'].mean()` gave the mean PM2.5 for each week. Finally I filtered the weekly means with `> 70` to find the weeks that trigger the alert.

## Interpretation
I believe that  by seeing the mean PM2.5 is **57.5** for week 1 and **73.75** for week 2. Since the alert threshold is a weekly mean above 70, **week 2 triggers the alert** and week 1 does not.There are many other factors that will affect PM2.5 for  example mainly weather, butdust of industrial and construction works too affect PM2.5