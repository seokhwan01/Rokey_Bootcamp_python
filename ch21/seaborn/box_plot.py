import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

#그래프 표시
sns.set_context("notebook", rc={"figure.figsize": (10, 6)})
sns.boxplot(data=iris,
                x="species", #x 축 : 붓꽃 종
                y="sepal_length",) #y 축 : 꽃받침 길이
plt.title("Box Plot Example")
plt.show()