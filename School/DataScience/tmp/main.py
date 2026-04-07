import pandas as pd

df = pd.read_csv("./census/adult.data",header=None)

missingData = 0

for index, row in df.iterrows():
    for value in row.isnull():
        if value == False:
            missingData+=1



#print(missingData)