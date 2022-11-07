import inline as inline
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
from numpy import dot, matrix, deg2rad
from statistics import mode

from math import pi
from math import cos, sin

df = pd.read_csv("12_jan_21_exprmnt_pnts_1.csv")
all = df.to_numpy()
all = all[:,0:4]
print(all)
ll = 218
ul = 739
degrees = 5
x = np.array([])
y = np.array([])
z = np.array([])

def mapFromTo(x, a, b, c, d):
    y = (x - a) / (b - a) * (d - c) + c
    return y


x_values = all[ll:ul][:, 1] / 1000
y_values = all[ll:ul][:, 2] / 1000
z_values = all[ll:ul][:, 3] / 1000
def equispaced(x_values,roc_tolerance):
    x_roc = []
    for i in range(x_values.shape[0]):
        if i < x_values.shape[0]-1:
            roc = abs(x_values[i+1] - x_values[i])
            x_roc.append(roc)
        else:
            None
    x_roc = mode(x_roc)
    x_equispaced = []
    for i in range(x_values.shape[0]):
        if i < x_values.shape[0] - 1:
            if (x_roc + (roc_tolerance * x_roc)) <= x_values[i+1] - x_values[i] <= (x_roc + (roc_tolerance * x_roc)):
                x_equispaced.append(x_values[i])
    return x_equispaced

for i in range(all.shape[0]):
        x = np.append(x,[all[i][0]])
        y = np.append(y,all[i][1])
        z = np.append(z,all[i][2])

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x,y,z,zdir='z',c = 'gray')

# H
ax.scatter(0,0,1266, color='r')
ax.text(0,0,1266, "H", size=10, zorder=1, color='g')

# P1
ax.scatter(309.35,272.64,589.52, color='r')
ax.text(309.35,272.64,589.52, "p1", size=10, zorder=1, color='g')

# P2
ax.scatter(325.50,288.85, 605.77, color='r')
ax.text(325.50,288.85, 605.77, "p2", size=10, zorder=1, color='g')

# P3
ax.scatter(341.73,305.14,622.10, color='r')
ax.text(341.73,305.14,622.10, "p3", size=10, zorder=1, color='g')

# P4
ax.scatter(358.08,321.52,638.51, color='r')
ax.text(358.08,321.52,638.51, "p4", size=10, zorder=1, color='g')

# P5
ax.scatter(374.43,337.97,655.01, color='r')
ax.text(374.43,337.97,655.01, "p5", size=10, zorder=1, color='g')

# P6
ax.scatter(390.89,354.50,671.59, color='r')
ax.text(390.89,354.50,671.59, "p6", size=10, zorder=1, color='g')

# P7
ax.scatter(407.42,371.12,688.26, color='r')
ax.text(407.42,371.12,688.26, "p7", size=10, zorder=1, color='g')

# P8
ax.scatter(424.07,387.82,705.01, color='r')
ax.text(424.07,387.82,705.01, "p8", size=10, zorder=1, color='g')

# AN
ax.scatter(440.73,404.60,721.84, color = 'b')
ax.text(440.73,404.60,721.84, "An", size=10, zorder=1, color='b')

# AN
ax.scatter(457.50,421.46,738.76, color = 'b')
ax.text(457.50,421.46,738.76, "An", size=10, zorder=1, color='b')


# plt.show
# plt.imshow
plt.savefig('12_jan_21_generated_plotting.png')