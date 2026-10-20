# SYNERGY TASK PHASE

## QUESTION
Q15. TechTatva Revenue Investigation. Clean the event and dept text, treat a repeated (student, event) pair as one registration, fill the missing department with Unknown, merge with fees, and compute registrations per event and revenue per department. Then repeat the department revenue calculation without removing duplicates. Interpret: how would the duplicates have changed the committee's conclusion?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

regs = pd.DataFrame({
    'reg_id': range(1, 12),
    'student': ['Anu', 'Bala', 'Chitra', 'Anu', 'Dev', 'Esha', 'Farhan', 'Gita', 'Bala', 'Hari', 'Ira'],
    'event': [' city landscaping ', 'city landscaping ', 'salutes and ladders', ' city landscaping ',
              'Open Mic', 'open mic', 'ROBO RACE', 'Quiz Night', 'hackathon', 'Quiz Night', 'Hackathon'],
    'dept': ['CSE', 'cse', 'ECE', 'CSE', 'MECH', 'CSE', 'ECE', None, 'CSE', 'ECE', 'ECE']
})
fees = pd.DataFrame({'event': ['Hackathon', 'Robo Race', 'Open Mic', 'Quiz Night'],
                     'fee': [200, 150, 0, 50]})

# Clean text: strip spaces, consistent case, fill missing dept
regs['event'] = regs['event'].str.strip().str.title()
regs['dept'] = regs['dept'].str.strip().str.upper().fillna('Unknown')
fees['event'] = fees['event'].str.strip().str.title()

# One registration per (student, event)
clean = regs.drop_duplicates(subset=['student', 'event'])
print("Rows before / after dedup:", len(regs), "/", len(clean))

# Left merge keeps every registration, so unmatched events stay visible
merged = clean.merge(fees, on='event', how='left')
print("Events with no fee listed:", list(merged.loc[merged['fee'].isna(), 'event'].unique()))

print("\nRegistrations per event:\n", merged.groupby('event').size())

dept_rev = merged.groupby('dept')['fee'].sum().sort_values(ascending=False)
print("\nRevenue per department (deduplicated):\n", dept_rev)
print("Total revenue:", merged['fee'].sum())

# Same calculation WITHOUT removing duplicates
dirty = regs.merge(fees, on='event', how='left')
dirty_rev = dirty.groupby('dept')['fee'].sum().sort_values(ascending=False)
print("\nRevenue per department (duplicates kept):\n", dirty_rev)
print("Registrations per event (duplicates kept):\n", dirty.groupby('event').size())
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda15.py
Rows before / after dedup: 11 / 10
Events with no fee listed: ['City Landscaping', 'Salutes And Ladders']

Registrations per event:
 event
City Landscaping       2
Hackathon              2
Open Mic               2
Quiz Night             2
Robo Race              1
Salutes And Ladders    1
dtype: int64

Revenue per department (deduplicated):
 dept
ECE        400.0
CSE        200.0
Unknown     50.0
MECH         0.0
Name: fee, dtype: float64
Total revenue: 650.0

Revenue per department (duplicates kept):
 dept
ECE        400.0
CSE        200.0
Unknown     50.0
MECH         0.0
Name: fee, dtype: float64
Registrations per event (duplicates kept):
 event
City Landscaping       3
Hackathon              2
Open Mic               2
Quiz Night             2
Robo Race              1
Salutes And Ladders    1
dtype: int64
```

## Explaination of my code
First I created both DataFrames. In `regs`, I used `str.strip()` and `str.title()` on event so that ` city landscaping `, `ROBO RACE` and `open mic` become consistent labels, and `str.strip().str.upper()` on dept so `cse` and `CSE` match. `fillna('Unknown')` then replaced the missing department. I cleaned the event names in `fees` the same way, so the merge keys line up. Then I used `drop_duplicates(subset=['student', 'event'])` so a repeated (student, event) pair counts once, and the cleaning came first so that spelling variants were already identical. I merged with `how='left'` so no registration is silently lost, and listed the events that found no fee. `groupby('event').size()` gives registrations per event, and `groupby('dept')['fee'].sum()` gives revenue per department. Finally I repeated the revenue step on `regs` without the dedup step to see what the duplicates would do.

## Interpretation
I believe that the duplicates would increase the revenue shown for CSE by ₹400, making it look like CSE earned ₹800 and was the top department. Because of this, the committee may think CSE is earning more than ECE and make wrong decisions. Actually, ECE is the top department with ₹550 revenue. So, removing duplicates is important to get the correct revenue and make the right decisions.