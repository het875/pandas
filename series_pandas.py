import pandas as pd

# Create a Pandas Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

"""
0    10
1    20
2    30
3    40
4    50
dtype: int64


"""


# 2. Creating a Series with Custom Index
import pandas as pd

# Create a Pandas Series with custom indices
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)


"""
a    10
b    20
c    30
d    40
e    50
dtype: int64


"""


#3 . Creating a Pandas Series from a Dictionary

import pandas as pd

# Create a Pandas Series from a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series = pd.Series(data)
print(series)

"""
a    10
b    20
c    30
d    40
e    50
dtype: int64


"""

# 4. Operations on Pandas Series
    # 4.1 Element-wise Operations

import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Add 5 to each element
print(series + 5)

# Multiply each element by 2
print(series * 2)

"""
0    15
1    25
2    35
3    45
4    55
dtype: int64

0    20
1    40
2    60
3    80
4    100
dtype: int64

"""


    #4.2 Applying NumPy Functions
import pandas as pd
import numpy as np

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Applying NumPy functions
print(np.log(series))  # Logarithm
print(np.sqrt(series))  # Square root

"""
0    2.302585
1    2.995732
2    3.401197
3    3.688879
4    3.912023
dtype: float64

0    3.162278
1    4.472136
2    5.477226
3    6.324555
4    7.071068
dtype: float64

"""



# 5. Handling Missing Values in Pandas Series
    # 5.1 Detecting Missing Values

import pandas as pd
import numpy as np

# Create a Pandas Series with NaN values
data = [10, np.nan, 30, 40, np.nan]
series = pd.Series(data)

# Check for missing values
print(series.isnull())  # True if value is missing (NaN)

"""
0    False
1     True
2    False
3    False
4     True
dtype: bool

"""

    # 5.2 Filling Missing Values
    # You can fill missing values using .fillna().

import pandas as pd
import numpy as np

# Create a Pandas Series with NaN values
data = [10, np.nan, 30, 40, np.nan]
series = pd.Series(data)

# Fill NaN values with 0
print(series.fillna(0))

"""
0    10.0
1     0.0
2    30.0
3    40.0
4     0.0
dtype: float64
"""




"""
6. Indexing and Slicing a Pandas Series
    6.1 Indexing by Label
    You can access elements by their label (index).
"""

import pandas as pd

# Create a Pandas Series with custom indices
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)

# Access an element by label
print(series['b'])  # Access by label 'b'
"""
20
"""

# 6.2 Slicing a Series

import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Slice the Series
print(series[1:4])  # Access elements from index 1 to 3

"""
1    20
2    30
3    40
dtype: int64

"""



"""
7. Sorting a Pandas Series
    7.1 Sorting by Index
    You can sort a Series by its index using .sort_index()."""

import pandas as pd

# Create a Pandas Series with custom indices
data = [10, 20, 30, 40, 50]
index = ['b', 'e', 'a', 'd', 'c']
series = pd.Series(data, index=index)

# Sort by index
print(series.sort_index())

"""
a    30
b    10
c    50
d    40
e    20
dtype: int64

"""



"""
7.2 Sorting by Values
You can also sort the Series by values using .sort_values().
"""
import pandas as pd

# Create a Pandas Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Sort by values
print(series.sort_values())


"""
0    10
1    20
2    30
3    40
4    50
dtype: int64

"""




