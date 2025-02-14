import pandas as pd
from openpyxl import Workbook, load_workbook

def create_student_data():
    data={
        "이름" : ["홍길동","김영희","이철수","박민수"],
        "국어" : [90,85,88,92],
        "영어" : [85,89,92,80],
        "수학" : [88,90,85,95]
    }
    df=pd.DataFrame(data)
    return df
df=create_student_data()
excel_path=r"C:\rokey\ch22\excel_with_pandas\student_score.xlsx"
df.to_excel(excel_path,index=False)