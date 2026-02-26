import pandas as pd

data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]

df = pd.DataFrame(data, columns=["name", "age"])

print(type(df.loc[0]))
print(df.loc[0])
