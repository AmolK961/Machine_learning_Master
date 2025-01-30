import pandas as pd


# add data path 
md_path="melb_data.csv"

mlb_data=pd.read_csv(md_path)

print(mlb_data)


print(mlb_data.describe())