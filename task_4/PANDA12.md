# SYNERGY TASK PHASE

## QUESTION
Q12. The Misleading Conversion Rate. Jio compares two marketing channels. A teammate wrote the code below and concluded that Channel A wins. Run the code and note the result. Explain what is wrong with averaging the daily rates when the visitor counts differ so much. Fix the analysis by aggregating the right columns first and computing the rate afterwards. Decision: which channel should Jio invest in?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

funnel = pd.DataFrame({
    'channel': ['A', 'A', 'B', 'B'],
    'visitors': [10, 490, 100, 100],
    'signups': [6, 49, 20, 20]
})

# Teammate's flawed approach: average of row-level rates
funnel['rate'] = funnel['signups'] / funnel['visitors'] * 100
print("Flawed: mean of row rates\n", funnel.groupby('channel')['rate'].mean())
print("\nRow-level rates:\n", funnel)

# Fix: sum visitors and signups first, then compute the rate
fixed = funnel.groupby('channel')[['visitors', 'signups']].sum()
fixed['rate'] = fixed['signups'] / fixed['visitors'] * 100
print("\nCorrected (aggregate first, then divide):\n", fixed)

print("\nBest channel:", fixed['rate'].idxmax(), "->", fixed['rate'].max(), "%")
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda12.py
Flawed: mean of row rates
 channel
A    35.0
B    20.0
Name: rate, dtype: float64

Row-level rates:
   channel  visitors  signups  rate
0       A        10        6  60.0
1       A       490       49  10.0
2       B       100       20  20.0
3       B       100       20  20.0

Corrected (aggregate first, then divide):
          visitors  signups  rate
channel                         
A             500       55  11.0
B             200       40  20.0

Best channel: B -> 20.0 % 
```

## Explaination of my code
First I created the DataFrame and ran the teammate's code. It calculates a conversion rate for each row and then takes the mean of those rates per channel, which gives A = 35.0 and B = 20.0. To fix it, I used `groupby('channel')` and `sum()` on the visitors and signups columns first, so each channel has its total visitors and total signups. Only then did I divide signups by visitors and multiply by 100. `idxmax()` returns the channel with the highest corrected rate.

## Decision makinh 
Jio should unvest in channel B.Since havinfg 200 visitors with 20% rate is better than 11% rate having A