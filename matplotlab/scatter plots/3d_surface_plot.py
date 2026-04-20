import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd
import numpy as np 

fig = plt.figure()

x=np.linspace(-1,1,10)
y=np.linspace(-1,1,10)

xx,yy=np.meshgrid(x,y)

z= xx**2 + yy**2

ax =plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap='viridis')

fig.colorbar(p)

plt.show()