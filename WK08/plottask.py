# simple program to plot linear, square and cube functions
# This is the solution to Weekly Task 8

# Author: Przemyslaw Bil

# importing numpy to create the array data set
import numpy as np
# importing the pyplot from matplotlib library to plot the functions
import matplotlib.pyplot as plt

# create points for the x axis. The X axis range will be 0-4,
# but to make the plot smooth, creating 400 data points between 0 and 4 in equal 0.01 intervals
xPoints = np.array(range(0, 400))/100
# calculating the data points for the square function 
ySquares = xPoints*xPoints
# calculating the data points for the cube function
yCubes = ySquares*xPoints

# adding linear function to the plot. Note: there was no need to calculate the y values for linear function as y=x
plt.plot(xPoints, xPoints)
# adding square function to the plot
plt.plot(xPoints, ySquares)
# adding cube function to the plot
plt.plot(xPoints, yCubes)


# Adding the plot title
plt.title("Functions examples")

# Adding mathematical expressions for describing the functions 
# using TeX markup as per https://matplotlib.org/stable/tutorials/text/mathtext.html
plt.text(3.5, 4, r'$f(x)=x$',fontsize=10)
plt.text(3.5, 16, r'$g(x)=x^{2}$',fontsize=10)
plt.text(3.5, 64, r'$h(x)=x^{3}$',fontsize=10)

# Setting up the x and y axix label simply as 'X' and 'Y'
plt.xlabel("X")
plt.ylabel("Y")
plt.label.set_rotation(10)
# Setting the layout to tight (smaller margins)
plt.tight_layout()

# Adding the discreet grid lines (green dashed line with a narrow line width)
plt.grid(color='green', linestyle='--', linewidth=0.1)

# Show the plot
plt.show()