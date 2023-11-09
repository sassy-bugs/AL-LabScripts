import os
os.environ['MPLCONFIGDIR'] = "/tmp/matplotlib_cache"

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

fig = plt.figure(figsize=(5, 4))

# Adding the axes to the figure
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Adjust the coordinates and size

# plotting 1st dataset to the figure
ax.plot(x, y, label="Line 1")

# plotting 2nd dataset to the figure
ax.plot(y, x, label="Line 2")

# Setting Title
ax.set_title("Linear Graph")

# Setting Label
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

# Adding Legend
ax.legend(labels=('line 1', 'line 2'))

plt.show()
