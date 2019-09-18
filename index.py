import numpy
import random
from matplotlib import pyplot as plt

x = range(51)
y = []
for num in x:
    add = random.randrange(-5, 5)
    y.append(num+ add)
plt.scatter(x, y)
plt.show()
