import inline as inline
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
from numpy import dot, matrix, deg2rad
from math import pi
from math import cos, sin

""" read csv file and extract one row at a time from column D-J """
df = pd.read_csv("LogFile_1_edited_1.csv")
# print(df.head(1))
# df2 = df[["ZeitInSec", "ZeitInNanoSec","axisQMsr_LBR_iiwa_7_R800_1[0]", "axisQMsr_LBR_iiwa_7_R800_1[1]","axisQMsr_LBR_iiwa_7_R800_1[2]", "axisQMsr_LBR_iiwa_7_R800_1[3]","axisQMsr_LBR_iiwa_7_R800_1[4]","axisQMsr_LBR_iiwa_7_R800_1[5]","axisQMsr_LBR_iiwa_7_R800_1[6]"]]
df2 = df[["ZeitInSec","ZeitInNanoSec","axisQCmdT1m_LBR_iiwa_7_R800_1[0]", "axisQCmdT1m_LBR_iiwa_7_R800_1[1]","axisQCmdT1m_LBR_iiwa_7_R800_1[2]", "axisQCmdT1m_LBR_iiwa_7_R800_1[3]","axisQCmdT1m_LBR_iiwa_7_R800_1[4]","axisQCmdT1m_LBR_iiwa_7_R800_1[5]","axisQCmdT1m_LBR_iiwa_7_R800_1[6]"]]
every_row = df2.iloc[1::1]
every_row_np = every_row.values

""""DH transformation matrix" function"""
def DH(angles, joint):
    # angles = np.rad2deg(angles)
    DH = [[cos(angles[joint]), -(sin(angles[joint]) * cos(alpha[joint])), sin(angles[joint]) * sin(alpha[joint]),
           a[joint] * cos(angles[joint])],
          [sin(angles[joint]), cos(angles[joint]) * cos(alpha[joint]), -(cos(angles[joint]) * (sin(alpha[joint]))),
           a[joint] * sin(angles[joint])],
          [0, sin(alpha[joint]), cos(alpha[joint]), d[joint]],
          [0, 0, 0, 1]]
    DH = np.matrix(DH)
    return DH
""""Transformation chain"  function"""
def transformation(angles, joints):
    temp3 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    temp3 = np.matrix(temp3)
    for i in range(joints):
        temp3 = dot(temp3, DH(angles, i))
    return temp3
"""Global Configuration"""
def gc(i):  # theta2 is gc(1); theta4 is gc(3); theta6 is gc(5)
    if (theta[i] >= 0):
        return 1
    else:
        return -1

print('#################################################')
print(every_row_np[:,2:][0])
print('#################################################')
time = np.arange(0.858, 284.038, 0.02)
time = np.reshape(time, (time.shape[0], 1))
# print(time.shape)
# print(time)
positions = []
rotation = []
for i in range(every_row_np.shape[0]):
    angles = every_row_np[:,2:][i]
    """input data: DH parameters of kuka iiwa7, initial theta angles, end effector position transformation matrix."""

    d_bs, d_se, d_ew, d_wf = 340, 400, 400, 126
    d = np.array([d_bs, 0, d_se, 0, d_ew, 0, d_wf])
    theta = np.array([deg2rad(angles[0]), deg2rad(angles[1]), deg2rad(angles[2]), deg2rad(angles[3]), deg2rad(angles[4]), deg2rad(angles[5]), deg2rad(angles[6])])
    alpha = np.array([-pi / 2, pi / 2, pi / 2, -pi / 2, -pi / 2, pi / 2, 0])
    a = np.array([0, 0, 0, 0, 0, 0, 0])
    dh_parameters = [[a[0], alpha[0], d[0], theta[0]], [a[1], alpha[1], d[1], theta[1]], [a[2], alpha[2], d[2], theta[2]],
                     [a[3], alpha[3], d[3], theta[3]], [a[4], alpha[4], d[4], theta[4]], [a[5], alpha[5], d[5], theta[5]],
                     [a[6], alpha[6], d[6], theta[6]]]
    dh_parameters = np.matrix(dh_parameters)
    T07 = transformation(theta, 7)
    R07 = matrix(T07[:3, :3])
    P07 = matrix(T07[:3, 3])
    positions.append(P07)
    rotation.append(R07)
    # print("these are positions "+str(P07))
positions = np.asarray(positions) #to convert 'postions' from list to numpy array
rotation = np.asarray(rotation)
# print(rotation[750])
# print("\n")
L = np.empty([every_row_np.shape[0], 3])
for i in range(every_row_np.shape[0]):
    for j in range (3):
        L[i][j]  = positions[i][j][0]

# L = np.hstack((L,time))
print(L)
np.savetxt("21_apr_21_exprmnt_pnts_1.csv", L, delimiter=",")
# x = np.array([])
# y = np.array([])
# z = np.array([])
x = L[:,0]
y = L[:,1]
z = L[:,2]
print(x[0:10])
# for i in range(every_row_np.shape[0]):
#         x = np.append(x,[L[i][0]])
#         y = np.append(y,L[i][1])
#         z = np.append(z,L[i][2])


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x,y,z, zdir='z',c = 'gray')
plt.show()
# H
# ax.scatter(0,0,1266, color='r')
# ax.text(0,0,1266, "H", size=10, zorder=1, color='g')
#
# # P1
# ax.scatter(317,353,443, color='r')
# ax.text(317,353,443, "p1", size=10, zorder=1, color='g')
#
# # P2
# ax.scatter(477.5,153,520.8, color='r')
# ax.text(477.5,153,520.8, "p2", size=10, zorder=1, color='g')
#
# # P3
# ax.scatter(350.9,-345.3,568.9, color='r')
# ax.text(350.9,-345.3,568.9, "p3", size=10, zorder=1, color='g')
#
# # P4
# ax.scatter(351.6,-370.6,842.6, color='r')
# ax.text(351.6,-370.6,842.6, "p4", size=10, zorder=1, color='g')
#
# # P5
# ax.scatter(262.9,-285,1084.1, color='r')
# ax.text(262.9,-285,1084.1, "p5", size=10, zorder=1, color='g')
#
# # P6
# ax.scatter(650.7,-45.2,348.4, color='r')
# ax.text(650.7,-45.2,348.4, "p6", size=10, zorder=1, color='g')
#
# # P7
# ax.scatter(662.1,231.8,710.3, color='r')
# ax.text(662.1,231.8,710.3, "p7", size=10, zorder=1, color='g')
#
# # P8
# ax.scatter(361.1,601.5,710.3, color='r')
# ax.text(361.1,601.5,710.3, "p8", size=10, zorder=1, color='g')
#
# # AN
# ax.scatter(475.6,257.3,864.3, color = 'b')
# ax.text(475.6,257.3,864.3, "An", size=10, zorder=1, color='b')
#
# # AN
# ax.scatter(335.2, -347.5, 584, color = 'b')
# ax.text(335.2, -347.5, 584, "An", size=10, zorder=1, color='b')
#
#
# # plt.show
# # plt.imshow
# plt.savefig('12_jan_21_generated_plotting.png')
#
# ll = 1880
# ul = 1961
#
# x_snip = x[ll:ul]
# y_snip = y[ll:ul]
# z_snip = z[ll:ul]
# fig2 = plt.figure()
# ax2 = plt.axes(projection="3d")
# ax2.plot3D(x_snip,y_snip,z_snip,zdir='z',c = 'green')
#
# # H
# ax2.scatter(0,0,1266, color='r')
# ax2.text(0,0,1266, "H", size=10, zorder=1, color='g')
#
# # P1
# ax2.scatter(317,353,443, color='r')
# ax2.text(317,353,443, "p1", size=10, zorder=1, color='g')
#
# # P2
# ax2.scatter(477.5,153,520.8, color='r')
# ax2.text(477.5,153,520.8, "p2", size=10, zorder=1, color='g')
#
# # P3
# ax2.scatter(350.9,-345.3,568.9, color='r')
# ax2.text(350.9,-345.3,568.9, "p3", size=10, zorder=1, color='g')
#
# # P4
# ax2.scatter(351.6,-370.6,842.6, color='r')
# ax2.text(351.6,-370.6,842.6, "p4", size=10, zorder=1, color='g')
#
# # P5
# ax2.scatter(262.9,-285,1084.1, color='r')
# ax2.text(262.9,-285,1084.1, "p5", size=10, zorder=1, color='g')
#
# # P6
# ax2.scatter(650.7,-45.2,348.4, color='r')
# ax2.text(650.7,-45.2,348.4, "p6", size=10, zorder=1, color='g')
#
# # P7
# ax2.scatter(662.1,231.8,710.3, color='r')
# ax2.text(662.1,231.8,710.3, "p7", size=10, zorder=1, color='g')
#
# # P8
# ax2.scatter(361.1,601.5,710.3, color='r')
# ax2.text(361.1,601.5,710.3, "p8", size=10, zorder=1, color='g')
#
# # AN
# ax2.scatter(475.6,257.3,864.3, color = 'b')
# ax2.text(475.6,257.3,864.3, "An", size=10, zorder=1, color='b')
#
# # AN
# ax2.scatter(335.2, -347.5, 584, color = 'b')
# ax2.text(335.2, -347.5, 584, "An", size=10, zorder=1, color='b')
#
# plt.savefig('delete_this.png')




