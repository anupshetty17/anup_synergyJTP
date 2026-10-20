# SYNERGY TASK PHASE

## QUESTION
Using a vectorized operation, add score_per_min. Using apply with a small function, add a tier column: Elite for scores of 6000 or more, Skilled for 3000 to 5999, Rookie otherwise. Using map, convert the tier into bonus points (Elite 500, Skilled 200, Rookie 50) and compute the total bonus. Interpret: is the top scorer also the most efficient player?

## PROGRAM
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


players = pd.DataFrame({
    'player': ['A', 'B', 'C', 'D', 'E', 'F'],
    'score': [4200, 1800, 7600, 3100, 5900, 900],
    'minutes': [30, 45, 60, 20, 40, 15]
})

# Vectorized: score per minute
players['score_per_min'] = (players['score'] / players['minutes']).round(2)

# apply with a small function: tier
def get_tier(score):
    if score >= 6000:
        return 'Elite'
    elif score >= 3000:
        return 'Skilled'
    else:
        return 'Rookie'

players['tier'] = players['score'].apply(get_tier)

# map: tier -> bonus points
bonus_map = {'Elite': 500, 'Skilled': 200, 'Rookie': 50}
players['bonus'] = players['tier'].map(bonus_map)

print("DataFrame:\n", players)
print("\nTotal bonus:", players['bonus'].sum())

# Top scorer vs most efficient player
top_scorer = players.loc[players['score'].idxmax()]
most_efficient = players.loc[players['score_per_min'].idxmax()]
print("\nTop scorer:", top_scorer['player'], "->", top_scorer['score'])
print("Most efficient:", most_efficient['player'], "->", most_efficient['score_per_min'], "per min")

print("\nRanking by score_per_min:\n",
      players.sort_values('score_per_min', ascending=False)[['player', 'score_per_min']])
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda9.py
DataFrame:
   player  score  minutes  score_per_min     tier  bonus
0      A   4200       30         140.00  Skilled    200
1      B   1800       45          40.00   Rookie     50
2      C   7600       60         126.67    Elite    500
3      D   3100       20         155.00  Skilled    200
4      E   5900       40         147.50  Skilled    200
5      F    900       15          60.00   Rookie     50

Total bonus: 1200

Top scorer: C -> 7600
Most efficient: D -> 155.0 per min

Ranking by score_per_min:
   player  score_per_min
3      D         155.00
4      E         147.50
0      A         140.00
2      C         126.67
5      F          60.00
1      B          40.00
```

## Explaination of my code
First I created the DataFrame. For score_per_min, I divided the score column by the minutes column directly. This is a vectorized operation, so pandas does the division for all rows at once without a loop. Then I wrote a small function `get_tier()` that returns Elite for 6000 or more, Skilled for 3000 to 5999 and Rookie otherwise, and used `apply()` on the score column to run it on every value. Next I used `map()` with a dictionary to turn each tier into its bonus points (Elite 500, Skilled 200, Rookie 50), and `sum()` on the bonus column gave the total bonus. Finally I used `idxmax()` to find the top scorer and the most efficient player.

## Interpretation
No,  the top scorer isn't the most effcient player since efficiency is decided by score per minutes whichi is highest for D rather than C hence D is most efficient player not the top scorer C