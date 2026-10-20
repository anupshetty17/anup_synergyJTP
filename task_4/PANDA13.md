# SYNERGY TASK PHASE

## QUESTION
Q13. The Catalog Gap. Merge the tables with an inner, a left and an outer join, and record the row count of each. The platform wants a report listing every catalog track, including tracks never played. Choose the correct join, fill missing plays with 0, and compute total plays per artist. Interpret: what does the unmatched track_id 5 tell you about the data, and which join type hides it?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tracks = pd.DataFrame({
    'track_id': [1, 2, 3, 4],
    'title': ['Neon Drive', 'Gravity', 'Night Bus', 'Dust Roads'],
    'artist': ['Aria', 'Vega', 'Aria', 'Mohan']
})
plays = pd.DataFrame({'track_id': [1, 2, 3, 5], 'plays': [520, 450, 280, 90]})

# Three joins on track_id
inner = tracks.merge(plays, on='track_id', how='inner')
left = tracks.merge(plays, on='track_id', how='left')
outer = tracks.merge(plays, on='track_id', how='outer', indicator=True)

print("Inner rows:", len(inner))
print("Left rows :", len(left))
print("Outer rows:", len(outer))
print("\nOuter join with indicator:\n", outer)

# Report: every catalog track, so use the LEFT join
report = left.copy()
report['plays'] = report['plays'].fillna(0).astype(int)
print("\nCatalog report:\n", report)

# Total plays per artist
artist_total = report.groupby('artist')['plays'].sum().sort_values(ascending=False)
print("\nTotal plays per artist:\n", artist_total)

# Plays that cannot be linked to the catalog
orphans = outer[outer['_merge'] == 'right_only']
print("\nOrphan play records:\n", orphans[['track_id', 'plays']])
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda13.py
Inner rows: 3
Left rows : 4
Outer rows: 5

Outer join with indicator:
    track_id       title artist  plays      _merge
0         1  Neon Drive   Aria  520.0        both
1         2     Gravity   Vega  450.0        both
2         3   Night Bus   Aria  280.0        both
3         4  Dust Roads  Mohan    NaN   left_only
4         5         NaN    NaN   90.0  right_only

Catalog report:
    track_id       title artist  plays
0         1  Neon Drive   Aria    520
1         2     Gravity   Vega    450
2         3   Night Bus   Aria    280
3         4  Dust Roads  Mohan      0

Total plays per artist:
 artist
Aria     800
Vega     450
Mohan      0
Name: plays, dtype: int64

Orphan play records:
    track_id  plays
4         5   90.0
```

## Explaination of my code
First I created the two DataFrames and merged them on track_id with three join types. The inner join keeps only the ids found in both tables (3 rows). The left join keeps every row of `tracks` and adds plays where they exist (4 rows). The outer join keeps every id from either table (5 rows). I added `indicator=True` to the outer join, which creates a `_merge` column showing whether each row came from both tables, only the left table, or only the right table. For the report I used the left join, because the left table is the catalog and every catalog track must appear. Track 4 had no match, so its plays were NaN. I used `fillna(0)` and then `astype(int)`, because the NaN had turned the column into floats. Then `groupby('artist')` with `sum()` gave the total plays per artist.

## Interpretation
Track ID 5 has 90 plays but it is not present in the catalog, so, I believe that it may be a missing track or a wrong ID. Because of this, I dont know which artist the plays belong to. Both inner join and left join hide this record because it has no matching track in the catalog. Only the outer join shows the unmatched track and helps us find this data problem.
