# SYNERGY TASK PHASE

## QUESTION
songs = {'song': ['Neon Drive', 'Monsoon Loop', 'Gravity', 'Night Bus', 'Cherry Static', 'Dust Roads', 'Run It Back', 'Paper Moon'],
         'genre': ['Pop', 'LoFi', 'Rock', 'LoFi', 'Pop', 'Folk', 'HipHop', 'Folk'],
         'streams_k': [520, 310, 450, 280, 610, 150, 390, 205],
         'skip_pct': [18, 9, 32, 12, 41, 7, 27, 10],
         'duration_sec': [201, 245, 289, 198, 176, 310, 187, 262]}
Create the DataFrame and report its shape, dtypes and the number of distinct genres. List the top 3 songs by streams. Then find songs that are popular (more than 400k streams) and frequently skipped (skip rate above 25%). Interpret: what risk does the platform take if it recommends songs using stream counts only?

## PROGRAM
```

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

songs = {
    'song': ['Neon Drive', 'Monsoon Loop', 'Gravity', 'Night Bus',
             'Cherry Static', 'Dust Roads', 'Run It Back', 'Paper Moon'],
    'genre': ['Pop', 'LoFi', 'Rock', 'LoFi', 'Pop', 'Folk', 'HipHop', 'Folk'],
    'streams_k': [520, 310, 450, 280, 610, 150, 390, 205],
    'skip_pct': [18, 9, 32, 12, 41, 7, 27, 10],
    'duration_sec': [201, 245, 289, 198, 176, 310, 187, 262]
}
df = pd.DataFrame(songs)
print("\nShape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nNumber of Distinct Genres:", df['genre'].nunique())


top_3 = df.nlargest(3, 'streams_k')
print("\nTop 3 Songs by Streams:")
print(top_3[['song', 'streams_k']])


popular_skipped = df[(df['streams_k'] > 400) & (df['skip_pct'] > 25)]
print("\nPopular but Frequently Skipped Songs:")
print(popular_skipped[['song', 'streams_k', 'skip_pct']])
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda3.py

Shape: (8, 5)

Data Types:
song              str
genre             str
streams_k       int64
skip_pct        int64
duration_sec    int64
dtype: object

Number of Distinct Genres: 5

Top 3 Songs by Streams:
            song  streams_k
4  Cherry Static        610
0     Neon Drive        520
2        Gravity        450

Popular but Frequently Skipped Songs:
            song  streams_k  skip_pct
2        Gravity        450        32
4  Cherry Static        610        41
```

## EXPLAINATION OF MY CODE
First pf all, I created the dataframe of songs.Then as asked in the question to display the shape and data type i used df.shape and df.dtypes which returned me the desired output.After that, i used nunique() to calculate the unique values of genre, it gives me the value not the names which are uniques.Next as per the question i need to list the top 3 songs by comparing column of streams_k so i used nlargest() in which there are two aarguments one is the number of rows required and second one is the column from which we required.Then i displayed it using both columns songs and streams_k.Then, I need to look for songs that have strams greater than 400k but skips rate above 25%,thus i used relational operators with logical and operator since we need to test two conditions at a time.Then I displayed it with respective columns and rows

## INTERPRETATION
I believe that if it recommends songs using streams counts only, it will recommend the user to listen the songs that are skipped by the other user in the present days which will reduce user satisfaction.So i believe it neccessary to recommend the songs having more information about it.