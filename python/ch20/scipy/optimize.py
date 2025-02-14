from scipy.optimize import minimize
# 단순 2차 함수 최적화
def f(x):
    return x**2 +4*x+4
result=minimize(f,x0=0) # x0는 함수의 독립변수(x)의 초기 값(시작점)

print(f"Optimize value : {result.x}")
print(result)