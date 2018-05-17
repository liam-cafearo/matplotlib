# This imports the integral pyplot
# we import this as plt which is
# standard for python programs
import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

# first we select the 'slices', these are the relevant sizes for each part
plt.pie(slices,
        labels=activities,
        # then we specify the color list for the corresponding slices
        colors=cols,
        # The start angle '90 degrees' means the first division will
        # be a vertical line
        startangle=90,
        # we add shadow to the plot for a bit of character
        shadow= True,
        # we can use explode to pull a slice out a bit we have four 
        # total slices, so if we didn't want to pull any out we would
        # do 0,0,0,0. If we wanted to pull out the first slice we would
        # do 0.1,0,0,0
        explode=(0,0.1,0,0),
        # 'autopct' optionally overlays the percentages onto 
        # the graph itself
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()