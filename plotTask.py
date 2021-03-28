import matplotlib.pyplot as plt
import numpy as np

straightLineX = np.array(range(0,4))
straightLineY = straightLineX*1

squaredX = np.array(range(0,4))
squaredY = squaredX * squaredX

cubedX = np.array(range(0,4))
cubedY = cubedX *cubedX* cubedX


plt.plot(straightLineX, straightLineY, label = "f(x)", linewidth = 3, color = "#89d2d1")
plt.plot(squaredX, squaredY, label = "f$(x^2)$", linewidth = 3, color = "#898ad2")
plt.plot(cubedX, cubedY, label = "f$(x^3)$", linewidth = 3, linestyle = "dashed", color = "#d289c7")

plt.title(label = "Function Graph", pad = 2, linespacing = 2, fontsize = 30, color = "#d2cfd3")
plt.xlabel("x axis")
plt.ylabel("y axis")


plt.legend()
plt.show()