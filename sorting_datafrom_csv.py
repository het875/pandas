import pandas as pd

df = pd.read_csv('data.csv')

pd.options.display.max_rows = 9

# Sorting by Calories in ascending order
sorted_df = df.sort_values(by='Calories')
print(sorted_df)

# it can sorting calories wise output like :
"""
     Duration  Pulse  Maxpulse  Calories
89         20     83       107      50.3
93         15     80       100      50.5
100        20     95       112      77.7
107        30     90       120      86.2
..        ...    ...       ...       ...
27         60    103       132       NaN
91         45    107       137       NaN
118        60    105       125       NaN
141        60     97       127       NaN
"""