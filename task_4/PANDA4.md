# SYNERGY TASK PHASE

## QUESTION
canteen = {'hour': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
           'sold': [40, 55, 35, 90, 210, 180, 60, 30, 70, 95],
           'prepared': [50, 60, 50, 100, 220, 230, 80, 60, 90, 110]}
Build the DataFrame and set hour as the index. Using loc, select sold for hours 11 to 13. Using iloc, select the rows at positions 3 and 4. Use a Boolean mask to find the busy hours (at least 90 items sold). Interpret: loc[11:13] and iloc[3:5] both look like slices ending at 13 and 5. Why do they return different numbers of rows?

## PROGRAM
```

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

canteen = {
    'hour': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    'sold': [40, 55, 35, 90, 210, 180, 60, 30, 70, 95],
    'prepared': [50, 60, 50, 100, 220, 230, 80, 60, 90, 110]
}

df = pd.DataFrame(canteen)
df = df.set_index('hour')

print("\nItems Sold from Hours 11 to 13:",df.loc[11:13, 'sold'])
print("\nRows at Positions 3 and 4:",df.iloc[3:5])

busy_hours = df[df['sold'] >= 90]
print("\nBusy Hours (at least 90 items sold):",busy_hours)
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python PANDA4.py

Items Sold from Hours 11 to 13: hour
11     90
12    210
13    180
Name: sold, dtype: int64

Rows at Positions 3 and 4:       sold  prepared
hour                
11      90       100
12     210       220

Busy Hours (at least 90 items sold):       sold  prepared
hour                
11      90       100
12     210       220
13     180       230
17      95       110
```

## EXPLAINATION OF MY CODE
First i created the data frame using the canteen details given in the question.Then i used set_index() to set the index to hour.Then i used loc[11:13,'sold] here loc will hold values of sold for hours of 11,12 and 13 only.Then i used iloc to display the rows 3 and 4.Then  i also calculated busy_hours using the provided condition data.

## INTERPRETATION
From research,I got to know that loc uses index labels and hence it in cludes the ending index values too but iloc follows zero-index rules ,it befins with zero and end at n-1 so it doesn't include the last index value.Therefore,two slicing operations follows two different index rules
