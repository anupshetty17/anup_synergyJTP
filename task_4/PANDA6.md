# SYNERGY TASK PHASE

## QUESTION

The store manager asks four questions. Answer each with one filter: (a) products whose name contains Pro; (b) products in the Stationery or Home categories (isin); (c) products priced between 300 and 1500 inclusive (between); (d) Pro products that sold fewer than 70 units. Interpret: what does (d) suggest about premium products in this store?

## PROGRAM
```
import pandas as pd
import numpy as np
import matplotlib.pylot as plt

catalog = {
    'product': ['USB-C Hub Pro', 'Notebook A5', 'Gel Pen Pack', 'Laptop Stand Pro',
                'Desk Lamp', 'Mouse Pad XL', 'Webcam Pro', 'Sticky Notes'],
    'category': ['Electronics', 'Stationery', 'Stationery', 'Electronics',
                 'Home', 'Accessories', 'Electronics', 'Stationery'],
    'price': [1299, 120, 90, 1599, 899, 349, 2499, 60],
    'units_sold': [85, 400, 520, 60, 110, 230, 25, 610]
}

df = pd.DataFrame(catalog)

# (a) name contains "Pro"
pro_products = df[df['product'].str.contains('Pro')]

# (b) category is Stationery or Home
stat_home = df[df['category'].isin(['Stationery', 'Home'])]

# (c) price between 300 and 1500 (inclusive)
mid_price = df[df['price'].between(300, 1500)]

# (d) Pro products with fewer than 70 units sold
slow_pro = df[df['product'].str.contains('Pro') & (df['units_sold'] < 70)]

print("\n(a) Products containing 'Pro':\n", pro_products)
print("Count:", len(pro_products))

print("\n(b) Stationery or Home products:\n", stat_home)
print("Count:", len(stat_home))

print("\n(c) Priced between 300 and 1500:\n", mid_price)
print("Count:", len(mid_price))

print("\n(d) Pro products with fewer than 70 units sold:\n", slow_pro)
print("Count:", len(slow_pro))
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda6.py

(a) Products containing 'Pro':
             product     category  price  units_sold
0     USB-C Hub Pro  Electronics   1299          85
3  Laptop Stand Pro  Electronics   1599          60
6        Webcam Pro  Electronics   2499          25
Count: 3

(b) Stationery or Home products:
         product    category  price  units_sold
1   Notebook A5  Stationery    120         400
2  Gel Pen Pack  Stationery     90         520
4     Desk Lamp        Home    899         110
7  Sticky Notes  Stationery     60         610
Count: 4

(c) Priced between 300 and 1500:
          product     category  price  units_sold
0  USB-C Hub Pro  Electronics   1299          85
4      Desk Lamp         Home    899         110
5   Mouse Pad XL  Accessories    349         230
Count: 3

(d) Pro products with fewer than 70 units sold:
             product     category  price  units_sold
3  Laptop Stand Pro  Electronics   1599          60
6        Webcam Pro  Electronics   2499          25
Count: 2
```

## Explaination of my code
First I created the DataFrame from the catalog data. For (a), I used `str.contains('Pro')` to build a Boolean mask on the product column. For (b), I used `isin(['Stationery', 'Home'])` so one filter can match several categories instead of chaining `==` checks with `|`. For (c), I used `between(300, 1500)`, which is inclusive on both ends by default, so a price of exactly 300 or 1500 would also be included. For (d), I combined two conditions with `&`, putting each condition in its own parentheses because `&` binds more tightly than `<`. `len()` on each result gives the counts.
