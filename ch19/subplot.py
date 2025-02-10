import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
categories = ["A", "B", "C", "D"]
values = [3, 6, 7, 5]

# 2x2 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# 첫 번째 그래프 (선 그래프)
axs[0, 0].plot(x, y)

# 두 번째 그래프 (막대 그래프)
axs[0, 1].bar(categories, values)

# 세 번째 그래프 (산점도)
axs[1, 0].scatter(x, y)

# 네 번째 그래프 (막대 그래프)
axs[1, 1].bar(x, range(1, 5))

# 서브플롯 간격 자동 조정
plt.tight_layout()

# 그래프 출력
plt.show()
