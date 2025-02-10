import seaborn as sns
import matplotlib.pyplot as plt

#샘플 데이터 로드
iris=sns.load_dataset("iris")
sns.set_palette("pastel")
sns.scatterplot(data=iris,
                x="sepal_length",
                y="sepal_width",
                hue="species",
                style="species")
plt.title("Scatter Plot Example")
plt.show()