import pandas as pd

df = pd.read_csv("retail_data.csv")
df = df.fillna("null")
print(df.head())

for index,row in df.iterrows():
    value = row.to_dict()
    print(value)