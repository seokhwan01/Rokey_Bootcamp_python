import pandas as pd

# 기존 데이터 (merged)
merged = pd.DataFrame({
    'ID': [1, 3, 4, 5, 6],
    'Name': ['Alice', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [30, 25, 40, 28, 33],
    'Salary': [50000, 70000, 80000, 66666.67, 66666.67],
    'Department': ['HR', 'Sales', 'R&D', 'Finance', 'Planning']
})

# 새로운 데이터
data1 = {
    'ID': [1, 3],  # 기존 데이터와 중복 가능성이 있음
    'Name': ['Alice', 'Charlie'],
    'Age': [30, 25],
    'Salary': [50000, 70000],
    'Department': ['HR', 'Sales']
}

# 새로운 데이터프레임 생성
df1 = pd.DataFrame(data1)

# 기존 데이터(merged)와 새로운 데이터(df1) 병합
df1 = pd.concat([merged, df1])
df1_1=df1.drop_duplicates()
print(df1_1)
