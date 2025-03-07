import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df.to_string())

print(pd.options.display.max_rows)  # output : 60


# First 3 rows
print(df.head(3))

# Last 3 rows
print(df.tail(3))

"""
both output like :
Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
     Duration  Pulse  Maxpulse  Calories
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
"""


# Summary statistics for numerical columns
print(df.describe())

#output 
"""
         Duration       Pulse    Maxpulse     Calories
count  169.000000  169.000000  169.000000   164.000000
mean    63.846154  107.461538  134.047337   375.790244
std     42.299949   14.510259   16.450434   266.379919
min     15.000000   80.000000  100.000000    50.300000
25%     45.000000  100.000000  124.000000   250.925000
50%     60.000000  105.000000  131.000000   318.600000
75%     60.000000  111.000000  141.000000   387.600000
max    300.000000  159.000000  184.000000  1860.400000

"""

# Check for missing values in the dataset
print(df.isnull().sum())

#output
"""
Duration    0
Pulse       0
Maxpulse    0
Calories    5
dtype: int64

here calories have 5 missing item
"""



# Accessing a specific column (e.g., Pulse)
print(df['Pulse'])

# that can print only single colume name as a Pluse



# Filter rows where Pulse is greater than 110
filtered_df = df[df['Pulse'] > 130]
print(filtered_df)

# that can print who pluse colume have a more then 130 value 
#output
"""
     Duration  Pulse  Maxpulse  Calories
54         30    136       175     238.0
58         20    153       172     226.4
80         30    159       182     319.2
81         45    149       169     344.0
85         30    151       170     300.0
94         20    150       171     127.4
95         20    151       168     229.4
97         25    152       168     244.2
109       210    137       184    1860.4
135        20    136       156     189.0
139        20    141       162     222.4
144        60    136       170     470.2
153        30    150       167     275.8
"""



# Adding a new column for "Calories per Minute"
df['Calories per Minute'] = df['Calories'] / df['Duration']
print(df)

# that can add new colume in t otable like output :
"""
Duration  Pulse  Maxpulse  Calories  Calories per Minute
0          60    110       130     409.1             6.818333
1          60    117       145     479.0             7.983333
2          60    103       135     340.0             5.666667
"""

