import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#f(x) function
straightLineX = np.array(range(0,5))
straightLineY = straightLineX*1

#f(x^2) function
squaredX = np.array(range(0,5))
squaredY = squaredX * squaredX

#f(x^3) function
cubedX = np.array(range(0,5))
cubedY = cubedX * cubedX * cubedX

#Plotting graph and specifying widths, colours and labels for legend
plt.plot(straightLineX, straightLineY, label = "f(x)", linewidth = 3, color = "#89d2d1")
plt.plot(squaredX, squaredY, label = "f$(x^2)$", linewidth = 3, color = "#898ad2")
plt.plot(cubedX, cubedY, label = "f$(x^3)$", linewidth = 3, linestyle = "dashed", color = "#d289c7")

#Adjusting plot size to make it longer, think this is better suited to a linear graph
plt.subplots_adjust(left = 0.098, bottom = 0.24,  right = 0.952)

#Title and axis labels
plt.title(label = "Function Graph", pad = 2, linespacing = 2, fontsize = 20, color = "#978a84")
plt.xlabel("x axis", color = "#978a84")
plt.ylabel("y axis", color = "#978a84")

#making plot slightly wider 
plt.subplots_adjust(left = 0.098, bottom = 0.24,  right = 0.952)

#Changing x and y axis color to match title, hiding top and right spines
ax = plt.axes()

ax.spines["bottom"].set_color("#978a84")
ax.spines["left"].set_color("#978a84")
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

#setting ticks on axis to match spine color
ax.tick_params(labelcolor = "#d2cfd3", color ="#978a84")


#Changing font color on legend labels
legend = plt.legend()
plt.setp(legend.get_texts(), color = "#978a84")

plt.show()