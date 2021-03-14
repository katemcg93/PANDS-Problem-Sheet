import matplotlib.pyplot as plt
import numpy as np

straightLineX = np.array(range(0,5))
straightLineY = straightLineX*1

squaredX = np.array(range(0,4))
squaredY = squaredX * squaredX

cubedX = np.array(range(0,4))
cubedY = cubedX *cubedX* cubedX



plt.plot(straightLineX, straightLineY)
plt.plot(squaredX, squaredY)
plt.plot(cubedX, cubedY)

plt.show()