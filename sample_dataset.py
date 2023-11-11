import numpy as np
import matplotlib.pyplot as plt

np.random.seed(24)
x = np.random.randint(100, 900, 250)
y= np.random.randint(50000, 100000, 250)
plt.scatter(x,y)
plt.show()