#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
import csv

data = pd.read_csv('Matrix_Data.csv')

plt.rcParams["figure.figsize"] = [20.00, 10.00]
plt.rcParams["figure.autolayout"] = False
im = plt.imread("VPD_Matrix.jpg")
fig, ax = plt.subplots()

plt.gca().invert_yaxis()

im = ax.imshow(im, extent=[32.5, 92.5, 82.5, 58.5])
#ax.plot(data['RH'], data['°F'], ls='solid', linewidth=1, color='black')
# 35 - 2.5 to 90 + 2.5
#x = np.array(range(55))
#ax.plot(x, x, ls='dotted', linewidth=2, color='red')
plt.xlabel('RH')
plt.ylabel('°F')
plt.xticks(np.arange(35, 92, 5.0))
plt.yticks(np.arange(59, 83, 1.0))
m = 500

def animate(i):
    ax.plot(data['RH'][i*m], data['°F'][i*m], 'bo') # draw the next line
    #print(83-data['RH'][i*m]+59)
    print (data['Date'][i*m], data['RH'][i*m], data['°F'][i*m])

# setup and animation
anim = FuncAnimation( fig, animate, interval=10, frames=int(len(data['RH'])/m)-1)

plt.show()
