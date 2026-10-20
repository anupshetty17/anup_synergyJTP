# SYNERGY TASK PHASE

## QUESTION
An online store investigates which product to promote. Create revenue and profit columns per row, then group by product and sum both. Sort to find the leader for each measure and compute each product's profit margin (total profit ÷ total revenue × 100). Decision: which product deserves the promotion budget, and which one looks successful only because of its price?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plts

sales = pd.DataFrame({
    'product': ['Phone Case', 'Phone Case', 'Earbuds', 'Earbuds', 'Smart Watch', 'Smart Watch',
                'Power Bank', 'Power Bank', 'Screen Guard', 'Screen Guard'],
    'month': ['Aug', 'Sep'] * 5,
    'units': [180, 120, 100, 50, 50, 40, 90, 110, 300, 200],
    'price': [299, 299, 1499, 1499, 2999, 2999, 999, 999, 99, 99],
    'cost': [120, 120, 1300, 1300, 2700, 2700, 650, 650, 40, 40]
})

# Row-level columns (vectorized)
sales['revenue'] = sales['units'] * sales['price']
sales['profit'] = sales['units'] * (sales['price'] - sales['cost'])

# Group by product and sum both
summary = sales.groupby('product')[['revenue', 'profit']].sum()

# Profit margin = total profit / total revenue * 100
summary['margin_pct'] = (summary['profit'] / summary['revenue'] * 100).round(1)

print("Sorted by revenue:\n", summary.sort_values('revenue', ascending=False))
print("\nSorted by profit:\n", summary.sort_values('profit', ascending=False))
print("\nSorted by margin:\n", summary.sort_values('margin_pct', ascending=False))

print("\nRevenue leader:", summary['revenue'].idxmax(), "->", summary['revenue'].max())
print("Profit leader :", summary['profit'].idxmax(), "->", summary['profit'].max())

# Supporting check: monthly units trend
print("\nUnits by month:\n", sales.pivot(index='product', columns='month', values='units')[['Aug', 'Sep']])
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda11.py
Sorted by revenue:
               revenue  profit  margin_pct
product                                  
Smart Watch    269910   26910        10.0
Earbuds        224850   29850        13.3
Power Bank     199800   69800        34.9
Phone Case      89700   53700        59.9
Screen Guard    49500   29500        59.6

Sorted by profit:
               revenue  profit  margin_pct
product                                  
Power Bank     199800   69800        34.9
Phone Case      89700   53700        59.9
Earbuds        224850   29850        13.3
Screen Guard    49500   29500        59.6
Smart Watch    269910   26910        10.0

Sorted by margin:
               revenue  profit  margin_pct
product                                  
Phone Case      89700   53700        59.9
Screen Guard    49500   29500        59.6
Power Bank     199800   69800        34.9
Earbuds        224850   29850        13.3
Smart Watch    269910   26910        10.0

Revenue leader: Smart Watch -> 269910
Profit leader : Power Bank -> 69800

Units by month:
 month         Aug  Sep
product               
Earbuds       100   50
Phone Case    180  120
Power Bank     90  110
Screen Guard  300  200
Smart Watch    50   40
```

## Explaination of my code
First I created the DataFrame and added two row-level columns with vectorized operations: revenue (units × price) and profit (units × (price − cost)). Then I used `groupby('product')` and `sum()` on both columns, which adds up August and September for each product. The profit margin is total profit divided by total revenue × 100. I computed it from the grouped totals, not by averaging the row-level margins, so products are weighted by how much they actually sold. I then sorted the summary three times (by revenue, profit and margin) to find the leader of each measure, and used `idxmax()` to get the leader's name directly. The extra pivot table of monthly units supports the decision by showing whether sales are rising or falling.

## Decision making
Powe bank product deserves the promotion budget, and Smart watch looks successful only because of its price