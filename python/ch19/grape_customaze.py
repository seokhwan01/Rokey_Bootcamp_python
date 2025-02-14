import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
x1 = [1, 2, 3, 4]
y2 = [3, 5, 9, 7]
plt.plot(x, y, label="Data 1")
plt.plot(x1, y2, label="Data 2")
plt.legend(loc="upper left")
plt.savefig("ch19\\my_plot.png")
plt.show()
