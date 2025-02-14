import pandas as pd
data={
    'ID':[1,2,3],
    'Name':['Alice','Bob','Charlie'],
    'Age':[30,35,25]
}
data2={
    'ID':[5,6],
    'Name':['Eve','Frame'],
    'Age':[28,33]
}
data3={
    'ID':[1,2,3,4,5,6],
    'Department' : ['HR','Engineering','Sales','R&D','Finace','Planning']
}
df=pd.DataFrame(data)
df['Salary']=[4000,5000,6000]
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)
concated=pd.concat([df,df2])
merged=pd.merge(concated,df3)
print(merged.isnull().sum())
meanVal=merged['Salary'].mean()
merged['salary']=merged['Salary'].fillna(meanVal)
print(merged)