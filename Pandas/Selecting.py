import pandas as pd
#SELECTION BY COLUMN
# df = pd.read_csv("data.csv")
# print(df["Name"].to_string())
# print(df[["Name","Height_m","Weight_kg"]].to_string())# the column names should be exactly the same as the csv file
df = pd.read_csv("data.csv",index_col="Name")
# print(df.loc["Pikachu"])
# print(df.loc["Pikachu",["Height","Weight"]])
# print(df.iloc[0:11:2,0:3])
pokemon = input("Enter pokemon name")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")