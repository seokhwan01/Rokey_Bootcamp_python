import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")

sns.set_theme(style="darkgrid", palette="muted")
sns.histplot(data=iris,
                x="sepal_length",
                hue="species",
                kde=True)
plt.title("Histogram Example")
plt.show()