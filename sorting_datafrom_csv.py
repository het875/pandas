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



"""
Sorting by Multiple Columns
You can also sort by multiple columns, for example, first by Duration and then by Calories.
"""
# Sorting by 'Duration' and 'Calories'
sorted_df = df.sort_values(by=['Duration', 'Calories'], ascending=[True, False])
print(sorted_df)
#output:
"""
Duration  Pulse  Maxpulse  Calories
112        15    124       139     124.2
93         15     80       100      50.5
95         20    151       168     229.4
58         20    153       172     226.4
..        ...    ...       ...       ...
109       210    137       184    1860.4
60        210    108       160    1376.0
79        270    100       131    1729.0
69        300    108       143    1500.2
"""


# Export DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)



# Fill missing values with a specific value
df_filled = df.fillna(0)
print(df_filled)
print(df.info()) 
