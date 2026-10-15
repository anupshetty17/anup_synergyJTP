# Synergy Task Phase

## Question
The organizers of a Tech Tatva want to know which events turn registrations into actual attendance.
events = {'event': ['City Scaping', 'salutes and ladders', 'Open Mic', '', 'Valorant tournament'],
          'registered': [180, 95, 140, 60, 210],
          'attended': [150, 70, 135, 52, 160],
          'fee': [200, 150, 0, 50, 100]}
Build a DataFrame and print its shape and dtypes. Add an attendance_rate column (attended ÷ registered × 100, rounded to 1 decimal). Find the event with the most registrations and the event with the highest attendance rate. Interpret: are they the same event, and what does that say about judging an event by registrations alone?
Expected: shape (5, 4) before the new column; Gaming Arena has the most registrations (210) with a rate of 76.2; Open Mic has the best rate (96.4).

## Program
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
events = {'event': ['City Scaping', 'salutes and ladders', 'Open Mic', '', 'Valorant tournament'],
          'registered': [180, 95, 140, 60, 210],
          'attended': [150, 70, 135, 52, 160],
          'fee': [200, 150, 0, 50, 100]}


df = pd.DataFrame(events)
print(df)
print(df.dtypes)
print(df.shape)
df['attendance_rate']=((df['attended']/df['registered'])*100).round(1)
print(df)
row = df['registered'].idxmax()
print("Most Registrations:", df.loc[row, 'event'], df.loc[row, 'registered'],df.loc[row,'attendance_rate'])
rate_row = df['attendance_rate'].idxmax()
print("Highest attendance rate:",
      df.loc[rate_row, 'event'],
      df.loc[rate_row, 'attendance_rate'], "%")
```

## Output
```
C:\Users\anups\SYNERGY>python Dataframe.py
                 event  registered  attended  fee
0         City Scaping         180       150  200
1  salutes and ladders          95        70  150
2             Open Mic         140       135    0
3                               60        52   50
4  Valorant tournament         210       160  100
event           str
registered    int64
attended      int64
fee           int64
dtype: object
(5, 4)
                 event  registered  attended  fee  attendance_rate
0         City Scaping         180       150  200             83.3
1  salutes and ladders          95        70  150             73.7
2             Open Mic         140       135    0             96.4
3                               60        52   50             86.7
4  Valorant tournament         210       160  100             76.2
Most Registrations: Valorant tournament 210 76.2
Highest attendance rate: Open Mic 96.4 %
```

## Interpretation
NO,Both are different events.In the given dataset,Gaming Arena has highest registrations with 76.2% attendance rate but Open Mic has highest attendance rate having less registrations.This makes us to conclude that attendance is not only judged by the factor of registrations but also attendance rates too.

## Explaination of my code
First as per the instructuions,i imported pandas,numpy and matplotlib.Then i hardcode the given event data into my program and used pd.DataFrame() to make it  like excel.it converts dictionary into table and next i printed the dataframe, its shape and dtypes as per the question
After that i created a new column attendance_rate using the calcuations given in the question and printed the updated dataframe 
Next i used .idmax() function to get the event name with most registrations
```
print("Most Registrations:",
      df.loc[row, 'event'],
      df.loc[row, 'registered'],
      df.loc[row, 'attendance_rate'])
```
This prints -  df.loc[row, 'event'] finds the event name in that row.
df.loc[row, 'registered'] finds the number of registrations.
df.loc[row, 'attendance_rate'] finds that event's attendance rate.
Exactly the same i printed the event name having attendace_rate highest.