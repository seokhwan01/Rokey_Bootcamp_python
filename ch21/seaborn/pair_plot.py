import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

#그래프 표시
sns.pairplot(iris,hue="species")
plt.show()