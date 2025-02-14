import pandas as pd
import matplotlib.pyplot as plt

try:
    df_csv = pd.read_csv(
        r"week_assignment\week4,5.py\대구광역시 동구_연도별 체납차량 번호판 영치실적_20241201.csv", 
        encoding='cp949'
    )
except Exception as e:
    print(f"파일 읽기 중 오류 발생: {e}")
    
x=df_csv["년도"]
y=df_csv["영치대수"]
plt.plot(x,y)
plt.title("Yearly Seizure Count of License Plates") 
plt.xlabel("year") 
plt.ylabel("Seizure Count") 
plt.show() 