import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here



# This will draw the graph
plt.plot( xdata, ydata, 'bo')
plt.plot( [0,1], [-5,-1], 'k-' )
plt.plot( [0,1], [1,5], 'k-' )
plt.savefig("correlated_variables.png")
