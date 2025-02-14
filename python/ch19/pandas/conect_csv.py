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
df=pd.DataFrame(data)
df['Salary']=[4000,5000,6000]
df2=pd.DataFrame(data2)
concated=pd.concat([df,df2])
print(concated)