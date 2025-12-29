import pandas as pd
df = pd.read_csv("data.csv")
#droping irrelevant columns
# df = df.drop(columns=["Legendary","ID"])
# print(df)
#HANDLE MISSING DATA
# df=df.dropna(subset=["Type2"])

# df=df.fillna({"Type2":"None"})
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS ","Fire":"FIRE"})
# df["Name"]=df["Name"].str.lower( )
# df["Legendary"]=df["Legendary"].astype(bool)
df=df.drop_duplicates()
print(df.to_string()) 
 
