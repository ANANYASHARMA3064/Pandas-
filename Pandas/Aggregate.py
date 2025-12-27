import pandas as pd
df = pd.read_csv("data.csv")
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
#print(df.count())# does not include null values
#Single column
# print(df["Height_m"].mean())
group = df.groupby("Type1")
print(group["Height_m"].mean())

