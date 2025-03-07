import pandas as pd
import numpy as np

# Generate random data
np.random.seed(42)  # Set seed for reproducibility

# Example size of data
n = 10

# Random data for 'Age', 'Gender', 'Height', and 'Weight'
ages = np.random.randint(18, 70, size=n)  # Random ages between 18 and 70
genders = np.random.choice(['Male', 'Female'], size=n)  # Random genders
heights = np.random.uniform(150, 190, size=n)  # Random heights between 150cm and 190cm
weights = np.random.uniform(45, 100, size=n)  # Random weights between 45kg and 100kg

# Create a dictionary from the random data
data = {
    'Age': ages,
    'Gender': genders,
    'Height (cm)': heights,
    'Weight (kg)': weights
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print(df)



"""

Sample Output:

   Age  Gender  Height (cm)  Weight (kg)
0   56    Male     183.640350    89.587296
1   27  Female     173.548407    71.560342
2   57  Female     177.654102    53.744270
3   29    Male     162.446130    72.645615
4   35    Male     184.606022    72.894075
5   21    Male     154.314127    58.728242
6   58  Female     181.077624    59.978187
7   25  Female     171.731556    74.542895
8   42  Female     157.136776    82.547418
9   66  Female     161.589319    68.489456

"""


"""

Explanation:

1.Data Generation:
    ages: Random integers between 18 and 70 for the age column.
    genders: Randomly selected values from ['Male', 'Female'].
    heights: Random floating-point numbers between 150 and 190 for height (in cm).
    weights: Random floating-point numbers between 45 and 100 for weight (in kg).


2.Creating DataFrame:
    We create a Pandas DataFrame from the generated dictionary data containing the columns Age, Gender, Height, and Weight.


3. Displaying DataFrame:
    The print(df) will display the DataFrame with the generated data.


"""

 
