import math
import numpy as np
# parameter
import main4
from main4 import tangents
from main4 import cps
import inline as inline
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


datalog = np.genfromtxt('21_apr_21_exprmnt_pnts_2.csv', delimiter=',')
generated =  np.genfromtxt('algo_geneared_trajectory_1.csv', delimiter=' ')
experiments = [[216, 402], [624, 795], [1030, 1192], [1410, 1580], [1798, 1987], [2201, 2346], [2575, 2740],
               [2959, 3111]
    , [3338, 3487], [3709, 3932], [4144, 4367], [4580, 4776], [4997, 5215], [5435, 5665], [5884, 6090]
    , [6308, 6518], [6739, 6949], [7170, 7238], [7452, 7535], [7754, 7804], [8020, 8070], [8270, 8309]]

datalog = datalog[4457:4874, :]
print(datalog.shape)
print(generated.shape)

x = generated[:,0]
y = generated[:,1]
z = generated[:,2]

h = [0,0,1266]
p1 = [-506,205,828]
p2 = [-340,287,607]
p3 = [-343,404,752]
p4 = [-233,263,789]
p5 = [-402,228,573]
p6 = [-488,265,575]
p7 = [-204,240,613]
p8 = [-480,300,596]
p9 = [-349,314,488]

# p1 = [0,0,0]
# p2 = [100,100,0]
# p3 = [200,0,0]

# points = np.array([np.asarray(p1),np.asarray(p2),np.asarray(p3)])
points = np.array([np.asarray(p1),np.asarray(p2),np.asarray(p3),
                  np.asarray(p4),np.asarray(p5),np.asarray(p6),
                  np.asarray(p7)])

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(x, y, z, c='r')
t = np.asarray(tangents())
print(len(t), " length of the tangensts is")

cps = np.asarray(cps())
print(cps, "control points")

ax.quiver(points[:,0],points[:,1],points[:,2],
          t[:,0],t[:,1],t[:,2], length = 1,arrow_length_ratio =0.1)
# ax.quiver(points[1:7,0],points[1:7,1],points[1:7,2],
#           t[:,0],t[:,1],t[:,2], length = 1,arrow_length_ratio =0.1)

ax.scatter(h[0],h[1],h[2], c = 'green',linewidths = 10)
ax.scatter(p1[0],p1[1],p1[2], c = 'yellow',linewidths = 10)
ax.scatter(p2[0],p2[1],p2[2], c = 'black',linewidths = 10)
ax.scatter(p3[0],p3[1],p3[2], c = 'black',linewidths = 10)
ax.scatter(p4[0],p4[1],p4[2], c = 'black',linewidths = 10)
ax.scatter(p5[0],p5[1],p5[2], c = 'black',linewidths = 10)
ax.scatter(p6[0],p6[1],p6[2], c = 'black',linewidths = 10)
ax.scatter(p7[0],p7[1],p7[2], c = 'red',linewidths = 10)

ax.scatter(cps[0][:,0],cps[0][:,1],cps[0][:,2], c = 'red',linewidths = 2)
ax.scatter(cps[1][:,0],cps[1][:,1],cps[1][:,2], c = 'red',linewidths = 2)
ax.scatter(cps[2][:,0],cps[2][:,1],cps[2][:,2], c = 'red',linewidths = 2)
ax.scatter(cps[3][:,0],cps[3][:,1],cps[3][:,2], c = 'red',linewidths = 2)
ax.scatter(cps[4][:,0],cps[4][:,1],cps[4][:,2], c = 'red',linewidths = 2)
# ax.scatter(cps[5][:,0],cps[5][:,1],cps[5][:,2], c = 'red',linewidths = 10)


ax.scatter(datalog[:, 0], datalog[:, 1], datalog[:, 2], c='b')
plt.show()
# plt.savefig('exp_1_p3_two_p4.png')