import pandas as pd
df = pd.read_csv("data.csv")
tall_pokemon =  df[df["Height_m"]>=2]
legendary_pokemon = df[df["Legendary"] == True]
water_pokemon = df[(df["Type1"]=="Water") |
                (df["Type2"]=="Water")   ]
print(water_pokemon)