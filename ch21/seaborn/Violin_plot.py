import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

#그래프 표시
sns.violinplot(data=iris,
                x="species", #x 축 : 붓꽃 종
                y="sepal_length",
                inner="quart") #y 축 : 꽃받침 길이
plt.title("Violin Plot Example")
plt.show()