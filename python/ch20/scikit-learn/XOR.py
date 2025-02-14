from sklearn import svm
from sklearn import metrics

#데이터 학습
clf=svm.SVC() #알고리즘 선택
#fit(학습데이터, 레이블)
clf.fit([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ],
    [0,1,1,0]
)

#데이터 예측하기
pre=clf.predict([
    [0,1],
    [1,1]
])
print(pre)
#결과 확인
as_score=metrics.accuracy_score([1,0],pre)
print(f"정답률 : {as_score}")