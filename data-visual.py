import os
os.environ['MPLCONFIGDIR'] = "/tmp/matplotlib_cache"
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# Creating a new figure with width = 10 inches
# and height = 4 inches
fig = plt.figure(figsize =(10, 4))

# Creating first axes for the figure on the left
ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.8])

# Creating second axes for the figure on the right
ax2 = fig.add_axes([0.55, 0.1, 0.4, 0.8])

# Adding the data to be plotted
ax1.plot(x, y)
ax2.plot(y, x)
plt.show()

