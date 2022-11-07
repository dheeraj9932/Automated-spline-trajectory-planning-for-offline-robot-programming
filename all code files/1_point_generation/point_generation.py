import numpy as np
import math
from matplotlib import pyplot as plt

import random

# xrange = (-800.0, 800.0)
# yrange = (-800.0, 800.0)
# zrange = (0, 1300.0)
#
# points = []
#
# [ points.append((random.uniform(*xrange), random.uniform(*yrange), random.uniform(*zrange))) for i in range(2000) ]
# # print("random points are:: ")
# # print(np.array(points))
# points = np.asarray(points)


def generated_pos_vals(t, coeffs, degrees):
    op = 0
    for i in range(degrees):
        op += (t ** (degrees - i)) * coeffs[i]
    op = op + coeffs[degrees]
    return op
#
# def mapFromTo(x, a, b, c, d):
#     y = (x - a) / (b - a) * (d - c) + c
#     return y
def map(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = (value - leftMin) / (leftSpan)
    return rightMin + (valueScaled * rightSpan)

def volume_check(point):
    # rr = (math.pow(point[0],2) + (math.pow(point[1], 2))) + (math.pow(point[2]-340, 2))
    rr = math.sqrt((math.pow(point[0],2) + (math.pow(point[1], 2))) + (math.pow(point[2], 2)))
    inner_r = 400; outer_r = 800;
    if inner_r < rr:
        if outer_r > rr:
            if point[2] > -340:
                return True
            else:
                return False

def origin_transformation(survived_points):
    for i in range(survived_points.shape[0]):
        survived_points[:,2][i] = survived_points[:,2][i] + 340
    return survived_points




coeffs_x = [1,3,5,5,3,1]; coeffs_x = np.asarray(coeffs_x)
coeffs_y = [2,4,6,6,4,2]; coeffs_y = np.asarray(coeffs_y)
coeffs_z = [3,5,7,7,5,3]; coeffs_z = np.asarray(coeffs_z)
time = np.arange(0, 1, 0.002)
# time = np.linspace(-1, 1, num=1000)
degrees = 5

x_values = []; x_values.append(generated_pos_vals(time, coeffs_x, degrees))
y_values = []; y_values.append(generated_pos_vals(time, coeffs_y, degrees))
z_values = []; z_values.append(generated_pos_vals(time, coeffs_z, degrees))

temp = []
for i,value in enumerate(x_values):
    # j = map(value, np.min(x_values), np.max(x_values), -600, +600) # real af
    j = map(value, np.min(x_values), np.max(x_values), -800*3, +800*3)
    # if ( j <= -400) & (j >= 400): 000
    temp.append(j)
x_vals = np.asarray(temp)

temp = []
for i in y_values:
    temp.append(map(i, np.min(y_values), np.max(y_values), -800*3, +800*3))
y_vals = np.asarray(temp)

temp = []
for i in z_values:
    temp.append(map(i, np.min(z_values), np.max(z_values), -800*3, +800*3))
z_vals = np.asarray(temp)

points = np.vstack((x_vals,y_vals,z_vals)).T



survived = []
for i, value in enumerate(points):
    if volume_check(value):
        survived.append(value)

survived = np.asarray(survived)

survived = origin_transformation(survived)
print(survived.shape)
print(survived)

for i in range(survived.shape[1]):
    np.random.shuffle(survived[:,i])

print(survived)
np.savetxt("points_generated_3.csv",survived, delimiter=",")


# plt.plot(time, generated_pos_vals(time, coeffs_y, degrees))
# plt.show()
