from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
#1 iris데이터 셋 로드
iris=load_iris() 
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target

#0,1,2로 표현된 label을 문자열로 매핑
target_names={
    0:iris.target_names[0], #setosa
    1:iris.target_names[1], #versicolor
    2:iris.target_names[2]  #viginica
}
df['target']=df['target'].map(target_names)
print(df.head())

#2필요한 열 추출
iris_data = df.iloc[:, :4]  # 첫 4개의 열만 추출
iris_label=df["target"]

#3 학습 전용 데이터와 테스트 전용 데이토로 나누기
train_data,test_data,train_label,test_label= \
    train_test_split(iris_data, iris_label)
    
#4 데이터 학습시키고 예측하기
clf=svm.SVC() #SVC : 서포트 벡터 분류(Support Vector Classification)
#데이터 집합 내에서 최대 마진을 가진 최적의 선(평면)을 찾아 데이터 분류 
clf.fit(train_data,train_label) #fit() : 주어진 훈련 데이터에 따라 모델을 피팅
pre=clf.predict(test_data) #predict() : 시험 데이터에 대해 분류를 수행

#5 정답률 구하기
as_score=metrics.accuracy_score(test_label,pre)
print("정답률 : ",as_score)