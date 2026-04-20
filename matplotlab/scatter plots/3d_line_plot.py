import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd

x=[10,15,6,41]
y=[9,19,12,10]
z=[4,9,3,18] 


# use this loop to put the actual data name to the point and see it in the graph andf use a line segment inbetween them to link those 

fig = plt.figure()
ax= plt.subplot(projection='3d')
ax.scatter3D(x,y,z,color='red')
#we use plot3D to denote the line segment
ax.plot3D(x,y,z,color='green') # green color for the line and red for the points or we can say dots 

#for pointing the names 
ax.text(10,19,4,'point1')


plt.show()