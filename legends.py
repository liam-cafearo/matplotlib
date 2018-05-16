# This imports the integral pyplot
# we import this as plt which is
# standard for python programs
import matplotlib.pyplot as plt

# first set of coordinates
x = [1,2,3]
y = [5,7,4]

# second set of coordinates
x2 = [1,2,3]
y2 = [10,14,12]

# Add label parameter to assign 
# a name to the line, which we 
# can later show in the legend.
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

# Assign labels to the correct axis
# with 'xlabel' and 'ylabel'
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
# assign the plots title
plt.title('Interesting Graph\nCheck it out')
# Invoke the default legend
plt.legend()
plt.show()
