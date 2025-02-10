import statsmodels.api as sm
data = sm.datasets.get_rdataset("mtcars").data
X = data[['hp', 'wt']]
y = data['mpg']
#독립 변수가 여러 개인 경우, [['hp', 'wt']]와 같이 선택
X = sm.add_constant(X)
#sm.add_constant(): 독립 변수에 상수항(절편)을 추가
model = sm.OLS(y, X).fit()
#sm.OLS(): 선형 회귀 모델을 생성 / fit(): 모델을 학습
print(model.summary())