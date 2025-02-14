import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

sns.lmplot(data=iris,
                x="sepal_length",
                y="sepal_width",
                hue="species",
                height=6)
plt.title("Linear Regression Plot")
plt.show()