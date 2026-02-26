import pandas as pd

print(pd.__version__)

x = {"One": 1, "Two": 2, "Three": 3}
y = [10, 20, 30, 40, 50]

series = pd.Series(x)
series2 = pd.Series(y)

print(series)
print(series2)
