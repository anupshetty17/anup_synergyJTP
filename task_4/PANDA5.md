# SYNERGY TASK PHASE

## QUESTION
Using the Q4 data, add waste (prepared − sold) and waste_pct (waste ÷ prepared × 100). Identify (a) the hour with the most items sold, (b) the hour with the highest absolute waste, and (c) the hour with the highest waste percentage. Decision: the canteen can cut preparation in only one hour. Which hour would you choose and why?

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

df['waste'] = df['prepared'] - df['sold']
df['waste_pct'] = (df['waste'] / df['prepared'] * 100).round(2)

print("\nDataFrame with waste columns:\n", df)

most_sold_hour = df['sold'].idxmax()
most_waste_hour = df['waste'].idxmax()
most_waste_pct_hour = df['waste_pct'].idxmax()

print("\n(a) Hour with most items sold:", most_sold_hour, "->", df.loc[most_sold_hour, 'sold'], "items")
print("(b) Hour with highest absolute waste:", most_waste_hour, "->", df.loc[most_waste_hour, 'waste'], "items wasted")
print("(c) Hour with highest waste percentage:", most_waste_pct_hour, "->", df.loc[most_waste_pct_hour, 'waste_pct'], "%")
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python Panda5.py

DataFrame with waste columns:
       sold  prepared  waste  waste_pct
hour                                  
8       40        50     10      20.00
9       55        60      5       8.33
10      35        50     15      30.00
11      90       100     10      10.00
12     210       220     10       4.55
13     180       230     50      21.74
14      60        80     20      25.00
15      30        60     30      50.00
16      70        90     20      22.22
17      95       110     15      13.64

(a) Hour with most items sold: 12 -> 210 items
(b) Hour with highest absolute waste: 13 -> 50 items wasted
(c) Hour with highest waste percentage: 15 -> 50.0 %
```

## EXPAINATION OF MY CODE
irst I created the DataFrame from the canteen data and used set_index() to make hour the index. Then I added a new column waste by subtracting sold from prepared. Then I added waste_pct by dividing waste by prepared and multiplying by 100 (rounded to 2 decimals). To answer (a), (b) and (c), I used idxmax() on the sold, waste and waste_pct columns. idxmax() returns the index label (the hour) of the largest value, so it gives the hour directly instead of the row position. Finally I used loc to print the value for each of those hours.

## DECISION MAKING
I would cut 15.00 hour preparation since around 50% of items are wasted and around this time there is less demand too.so,I believe that cutting prepartion would be better than running out since there is no much demand around that period
