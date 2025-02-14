import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ["Group A", "Group B", "Group C", "Group D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()
    