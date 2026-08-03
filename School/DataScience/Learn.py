import pandas as pd

df = pd.read_csv("census/adult.data", header=None)

print(pd.isnull(df).sum())

print(df.dtypes)

tmp = pd.get_dummies(df)
