from sklearn import svm
from sklearn import metrics
import pandas as pd
#데이터 준비
xor_data=[
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
#데이터 가공-학습을 위한 데이터와 레이블 분리
xor_df=pd.DataFrame(xor_data) #매개변수 : 입력 데이터
#xor_df.loc[전체 데이터, 추출할 데이터]
#학습 데이터
data = xor_df.loc[:, 0:1]
#레이블(정답)
label=xor_df.loc[:,2]

#학습 알고리즘-분류(classification)
#모델 생성
clf=svm.SVC()
clf.fit(data,label)

#답 예측
pre=clf.predict(data)
print("예측결과 : ",pre)
#정답률 확인
as_score=metrics.accuracy_score(label, pre)
print(f"정답률 = {as_score}")