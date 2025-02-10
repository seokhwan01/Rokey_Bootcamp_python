# import pandas as pd
# data=[
#     [1,'Alice',30],
#     [2,'Bob',35],
#     [3,'Charlie',25]
# ]
# df=pd.DataFrame(data,columns=['ID','Name','Age'])
# print(df)

import pandas as pd
data={
    'ID':[1,'Alice',30],
    'Name':[2,'Bob',35],
    'Age':[3,'Charlie',25]
}
df=pd.DataFrame(data)
print(df)