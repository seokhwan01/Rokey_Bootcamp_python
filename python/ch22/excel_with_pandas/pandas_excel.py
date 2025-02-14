import pandas as pd
from openpyxl import Workbook, load_workbook
path = r"C:\rokey\ch22\excel\new_example.xlsx"
df=pd.read_excel(path, sheet_name="Sheet")
print(df.head())