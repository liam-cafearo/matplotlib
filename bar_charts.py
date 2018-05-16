# This imports the integral pyplot
# we import this as plt which is
# standard for python programs
import matplotlib.pyplot as plt
# 'plt.bar' creates a bar chart for us.
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")

# second bar but we have added a color customization.
# colors can be g for green, b for blue etc
# or we can use hexcodes like '#191970'
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nAnother Line!...')

plt.show()