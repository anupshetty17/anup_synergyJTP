# SYNERGY TASK PHASE

## QUESTION
First call drop_duplicates() on the raw data and note the row count. Then clean the text (strip spaces, consistent capitalization) in customer and product, and remove duplicates again. Compute total revenue before cleaning and after cleaning. Interpret: by what percentage did bad data inflate the revenue figure, and why did the first attempt miss a duplicate?

## PROGRAM
```
import numpy as np
import pandas as pd
import matplotlib.pypot as plt

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 101, 104, 105, 106, 105],
    'customer': ['Asha', 'ravi', 'Meera', 'Asha', 'Kiran', 'ravi', 'Meera', 'Ravi'],
    'product': ['laptop bag', 'Laptop Bag ', 'desk lamp', 'laptop bag',
                'DESK LAMP', 'notebook', 'Notebook', 'Notebook '],
    'amount': [1200, 1200, 900, 1200, 900, 150, 150, 150]
})

# Raw data
print("Raw rows:", len(orders))
raw_revenue = orders['amount'].sum()
print("Raw revenue:", raw_revenue)

# First attempt: drop duplicates on the raw data
first_try = orders.drop_duplicates()
print("\nRows after first drop_duplicates():", len(first_try))
print("Revenue after first drop_duplicates():", first_try['amount'].sum())

# Clean the text, then drop duplicates again
clean = orders.copy()
clean['customer'] = clean['customer'].str.strip().str.title()
clean['product'] = clean['product'].str.strip().str.lower()
clean = clean.drop_duplicates()

print("\nCleaned data:\n", clean)
print("Rows after cleaning + drop_duplicates():", len(clean))
print("Distinct products:", clean['product'].nunique())

clean_revenue = clean['amount'].sum()
print("\nRevenue before cleaning:", raw_revenue)
print("Revenue after cleaning :", clean_revenue)

overstatement = (raw_revenue - clean_revenue) / clean_revenue * 100
print("Overstatement:", round(overstatement, 2), "%")
```

## OUTPUT
```
C:\Users\anups\SYNERGY>python panda8.py
Raw rows: 8
Raw revenue: 5850

Rows after first drop_duplicates(): 7
Revenue after first drop_duplicates(): 4650

Cleaned data:
    order_id customer     product  amount
0       101     Asha  laptop bag    1200
1       102     Ravi  laptop bag    1200
2       103    Meera   desk lamp     900
4       104    Kiran   desk lamp     900
5       105     Ravi    notebook     150
6       106    Meera    notebook     150
Rows after cleaning + drop_duplicates(): 6
Distinct products: 3

Revenue before cleaning: 5850
Revenue after cleaning : 4500
Overstatement: 30.0 %
```

## Explaination of my code
First I created the DataFrame and noted the raw row count (8) and raw revenue (5850). Then I called `drop_duplicates()` on the raw data, which gave 7 rows. Next I cleaned the text columns. `str.strip()` removes leading and trailing spaces. `str.title()` makes every customer name start with a capital letter (so `ravi` and `Ravi` match), and `str.lower()` makes every product name lowercase (so `DESK LAMP`, `Laptop Bag ` and `Notebook ` match their clean versions). I used a copy so the raw data stays available for the "before" revenue. After cleaning, I called `drop_duplicates()` again, which gave 6 rows. Finally I used `sum()` on the amount column before and after cleaning, and `nunique()` to count the distinct products (3).

## Interpretation
i got to know that Revenue was 5850 before cleaning and 4500 after cleaning, so bad data inflated revenue by 30%. The first drop_duplicates() removed only exact duplicate rows. It missed order 105 because the customer and product names had different capitalization and extra spaces. Pandas treated them as different values. So, we should clean the text first and then remove duplicates to get the correct revenue.