import pandas as pd
data ={"Name":["Spongebob","Patrick","squidwards"],
       "Age":[30,35,50]}
df = pd.DataFrame(data,index=["Employee1","Employee2","Employee3"])# DataFrame is a constructor
print(df.loc["Employee1"]) 
# Name    Spongebob
# Age            30
# Name: Employee1, dtype: object
#Add a new column
df["Job"] = ["cook","N/A","cashier"]

#Add a new row
new_row=pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},{"Name":"Eugene","Age":60,"Job":"Manager"}],index=["Employee4","Employee5"])
df = pd.concat([df,new_row])
print(df)