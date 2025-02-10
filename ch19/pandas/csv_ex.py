import pandas as pd
df_csv=pd.read_csv('C:\\rokey\\ch19\\data.csv')
droped_df=df_csv.drop(3)
print(droped_df)

