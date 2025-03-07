"""
1. Creating a Pandas DataFrame from a Dictionary
A common way to create a DataFrame is by passing a dictionary of lists or arrays, where keys represent column names and values represent data for those columns.
"""

import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print(df)

"""
      Name  Age  Salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000
3    David   40   80000

"""



# 2. Creating a DataFrame from a List of Lists
# You can also create a DataFrame from a list of lists (or arrays). You specify column names separately.
import pandas as pd

# Creating a DataFrame from a list of lists
data = [[25, 'Alice', 50000], [30, 'Bob', 60000], [35, 'Charlie', 70000], [40, 'David', 80000]]
columns = ['Age', 'Name', 'Salary']
df = pd.DataFrame(data, columns=columns)
print(df)

"""
   Age     Name  Salary
0   25    Alice   50000
1   30      Bob   60000
2   35  Charlie   70000
3   40    David   80000

"""



"""
3. Creating a DataFrame from NumPy Arrays
You can also use NumPy arrays to create a DataFrame. The structure is similar to the previous example, but the data is provided as NumPy arrays."
"""
import pandas as pd
import numpy as np

# Creating a DataFrame from NumPy arrays
data = np.array([[25, 'Alice', 50000], [30, 'Bob', 60000], [35, 'Charlie', 70000], [40, 'David', 80000]])
columns = ['Age', 'Name', 'Salary']
df = pd.DataFrame(data, columns=columns)
print(df)


"""
   Age     Name Salary
0   25    Alice  50000
1   30      Bob  60000
2   35  Charlie  70000
3   40    David  80000
"""





"""4. Accessing Data in a DataFrame
You can access data in a DataFrame using column names, .loc[], or .iloc[].

4.1 Accessing a Column
To access a specific column, you can use the column name."""


# Accessing a column
print(df['Age'])
"""
Output:

0    25
1    30
2    35
3    40
Name: Age, dtype: object"
"""

"""
4.2 Accessing a Row by Index (using .iloc[])
You can access rows by integer index using .iloc[]."""


# Accessing a row by index
print(df.iloc[1])  # Access second row (index 1)
"""
Output:

Age          30
Name        Bob
Salary    60000
Name: 1, dtype: object"
"""

"""
4.3 Accessing Rows by Label (using .loc[])
You can also access rows by their index labels using .loc[].
"""

# Accessing a row by label
print(df.loc[1])  # Access second row by label
"""
Output:
Age          30
Name        Bob
Salary    60000
Name: 1, dtype: object"
"""





"""
5. Modifying Data in a DataFrame
5.1 Adding a New Column
You can easily add a new column to a DataFrame.


# Adding a new column
df['Department'] = ['HR', 'IT', 'Finance', 'Marketing']
print(df)


Output:
   Age     Name  Salary Department
0   25    Alice   50000        HR
1   30      Bob   60000        IT
2   35  Charlie   70000   Finance
3   40    David   80000  Marketing



5.2 Modifying an Existing Column
You can modify an existing column by directly assigning new values.

# Modifying a column
df['Salary'] = [55000, 65000, 75000, 85000]
print(df)

Output:
   Age     Name  Salary Department
0   25    Alice   55000        HR
1   30      Bob   65000        IT
2   35  Charlie   75000   Finance
3   40    David   85000  Marketing

"""
