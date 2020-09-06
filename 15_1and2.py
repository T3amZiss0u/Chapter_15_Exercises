import matplotlib.pyplot as plt

# Cubes
x_values = range(1, 5_000)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

plt.show()
