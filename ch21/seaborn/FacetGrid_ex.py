import seaborn as sns
import matplotlib.pyplot as plt

# 샘플 데이터 로드
iris = sns.load_dataset("iris")

# FacetGrid 설정: species별로 col(열)을 나누고, 서브플롯의 높이는 4인치, 가로:세로 비율은 1:1
g = sns.FacetGrid(iris, col="species", height=4, aspect=1)

# 각 서브플롯에 히스토그램과 밀도 곡선 추가 (map_dataframe 사용)
g.map_dataframe(sns.histplot, x="sepal_length", kde=True)

# 서브플롯의 제목 설정 (col_template 사용)
g.set_titles(col_template="{col_name}")

# 그래프 표시
plt.show()
