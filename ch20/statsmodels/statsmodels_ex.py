import statsmodels.api as sm
data = sm.datasets.get_rdataset("mtcars").data #1974년 모터트랜드 US 매거진에서 가져온 데이터
#mpg(연비), cyl(실린더수), disp(배기량), hp(마력) 등
#print(data.head())
X = data['hp'] #마력
y = data['mpg'] #연비
X = sm.add_constant(X)#X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
#sm.OLS(): 선형 회귀 모델을 생성
#fit(): 모델을 학습
print(model.summary())#summary(): 모델 결과를 요약하여 출력
