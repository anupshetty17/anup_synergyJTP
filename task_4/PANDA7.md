# SYNERGY TASK PHASE

## QUESTION
Q7. The Faulty Manipal Weather Station. Count missing values per column and the number of rows with at least one missing value. Drop rows where both readings are missing. Then fill the remaining missing temp_c and humidity values with the median of each column. Day 6 (55.0 °C) is almost certainly a sensor fault. Interpret: compare the temperature mean and median. Why is the median the safer fill value here?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.DataFrame({
    'day': range(1, 11),
    'temp_c': [28.1, 29.0, np.nan, 30.2, 29.5, 55.0, np.nan, 27.8, 28.6, 29.3],
    'humidity': [64, 61, 63, np.nan, 60, 58, np.nan, 66, 65, 62]
})

cols = ['temp_c', 'humidity']

# Missing values
print("Missing values per column:\n", weather.isna().sum())
print("\nRows with at least one missing value:", weather.isna().any(axis=1).sum())

# Drop rows where BOTH readings are missing
weather = weather.dropna(how='all', subset=cols)
print("\nAfter dropping rows with both readings missing:\n", weather)

# Mean vs median of temperature
print("\nTemp mean  :", round(weather['temp_c'].mean(), 2))
print("Temp median:", weather['temp_c'].median())

# Fill remaining gaps with each column's median
weather[cols] = weather[cols].fillna(weather[cols].median())
print("\nAfter filling with median:\n", weather)
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda7.py
Missing values per column:
 day         0
temp_c      2
humidity    2
dtype: int64

Rows with at least one missing value: 3

After dropping rows with both readings missing:
    day  temp_c  humidity
0    1    28.1      64.0
1    2    29.0      61.0
2    3     NaN      63.0
3    4    30.2       NaN
4    5    29.5      60.0
5    6    55.0      58.0
7    8    27.8      66.0
8    9    28.6      65.0
9   10    29.3      62.0

Temp mean  : 32.19
Temp median: 29.15

After filling with median:
    day  temp_c  humidity
0    1   28.10      64.0
1    2   29.00      61.0
2    3   29.15      63.0
3    4   30.20      62.5
4    5   29.50      60.0
5    6   55.00      58.0
7    8   27.80      66.0
8    9   28.60      65.0
9   10   29.30      62.0
```

## Explaination of my code
First I created the DataFrame and used `isna().sum()` to count missing values per column. Then `isna().any(axis=1).sum()` counts the rows with at least one missing value (days 3, 4 and 7). To drop only the rows where both readings are missing, I used `dropna(how='all', subset=cols)`. The `subset` is important: the `day` column is never empty, so without it `how='all'` would drop nothing. This removed day 7 only. Then I compared the mean and median of temp_c. Finally I used `fillna()` with `median()` of the two columns, which fills each column with its own median (29.15 for temp_c on day 3, and 62.5 for humidity on day 4).

## Interpretation 
from the above data,I got to know that temperature mean is 32.19 °C but the median is 29.15 °C and also seeing the readings of temperature, it is only between 28.10 to 30.20 except one reading which affected the mean value.From this,I got to know that mean are much affected bu outliers from median since they use sorted middle values only.