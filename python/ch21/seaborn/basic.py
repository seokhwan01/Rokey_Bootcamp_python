import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

#기본 스타일 설정
sns.set_theme(style="whitegrid")

#그래프 표시
sns.scatterplot(data=iris,
                x="sepal_length",
                y="sepal_width",
                hue="species")
plt.title("Iris Dataset")
plt.show()