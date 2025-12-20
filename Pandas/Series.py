import pandas as pd

# data = [100.1,102.2,104.3,200,300,199]
# # series = pd.Series(data)# data + index+ datatype
# # 0    100
# # 1    102
# # 2    104
# # dtype: int64
# series = pd.Series(data,index=["a","b","c","d","e","f"])
# # a    100.1
# # b    102.2
# # c    104.3
# # dtype: float64
# # series.loc["c"]=200
# # a    100.1
# # b    102.2
# # c    200.0
# # dtype: float64

# # print(series.iloc[1])
# print(series[series>200])
calories = {"Day 1":1750,"Day 2":2100,"Day 3":1700} 
series = pd.Series(calories)
print(series[series>2000])
#  Day 2    2100
# dtype: int64