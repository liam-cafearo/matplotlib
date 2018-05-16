# This imports the integral pyplot
# we import this as plt which is
# standard for python programs
import matplotlib.pyplot as plt

# this takes the '.plot' method of plypot to plot some coordinates.
# '.plot' can take many parameters but first two are x and y coordinates
# which we have placed into lists meaning we have three 
# coordinates '1,5' '2,7' '3,4
plt.plot([1,2,3],[5,7,4])

# '.plot' draws the plot in the 
# background we use '.show'
# to bring it to the screen when
# we're ready.
plt.show()