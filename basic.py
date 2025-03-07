import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

"""
Output

    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2


"""