# SYNERGY TASK PHASE -4

## QUESTION
A fitness tracker exports one week of data as a NumPy array with columns steps, sleep_hours, active_minutes.
data = np.array([[8200, 7.5, 40], [10400, 6.5, 55], [6100, 8.0, 20], [12000, 6.0, 70],
                 [9800, 7.0, 50], [3000, 9.0, 10], [7500, 8.5, 35]])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Build a DataFrame from the array using days as the index and proper column names. The array stores everything as float, so convert steps and active_minutes to integers. Use describe() to read the average steps and sleep, then use idxmax / idxmin to find the day with the most steps and the day with the least sleep. Interpret: seven days are too few to claim that busy days cause short sleep. What extra data would you want?

## Program
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = np.array([[8200, 7.5, 40], [10400, 6.5, 55], [6100, 8.0, 20], [12000, 6.0, 70],
                 [9800, 7.0, 50], [3000, 9.0, 10], [7500, 8.5, 35]])
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df=pd.DataFrame(data,index=days,columns=['steps','sleep_hours','active_minutes'])
df['steps']=df['steps'].astype(int)
df['active_minutes']=df['active_minutes'].astype(int)
print("Average steps:",df['steps'].describe()['mean'])
print("Average Sleep Hours:",df['sleep_hours'].describe()['mean'])
print("days with most steps:",df['steps'].idxmax())
print("days with low sleep:",df['sleep_hours'].idxmin())
```

## Output
```
C:\Users\anups\SYNERGY>python panda2.py
Average steps: 8142.857142857143
Average Sleep Hours: 7.5
days with most steps: Thursday
days with low sleep: Thursday
```

## Interpretation
seven days are too few to claim that busy days cause short sleep. What extra data would you want?
Yeah it is true to conclude that busy days cause short sleeps in the data with seven days. So as my thought, we need extra data about previous months their sleep hours and also their schedules of each day with time distinction from which i can get to know how their busy days afftected the sleep hours.I believe that not only steps affect the sleep hours there will be other factors too.

## Explaination of my code
First of all,As task specified i imported all the python's built in library next i hardcode the data given in the question as it is.Next,Since question was asked me to change data types of steps and active_hours from float to int,I changed it using astype().Next I was told to calculated the Average values of sleep hours and steps,where i was given hint to use describe() from which i use ['mean'] method.Then, i founded the day with most steps and day with less sleep using idxmax() and idxmin() respectively.