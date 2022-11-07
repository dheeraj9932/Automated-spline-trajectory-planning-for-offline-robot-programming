import numpy as np
import pandas as pd
import matplotlib
import math
import statistics
from statistics import mode

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

df = pd.read_csv("12_jan_21_exprmnt_pnts_1.csv")
all = df.to_numpy()
all = all[:, :4]
ll = 218
ul = 739
degrees = 5

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
x_equispaced = np.asarray(equispaced(x_values,0.01))
y_equispaced = np.asarray(equispaced(y_values,0.01))
z_equispaced = np.asarray(equispaced(z_values,0.01))

x_x =  np.asarray(list(range(len(x_equispaced))))
x_y =  np.asarray(list(range(len(y_equispaced))))
x_z =  np.asarray(list(range(len(z_equispaced))))

unmapped_t_values = all[ll:ul][:, 3]
unmapped_t_values.flags.writeable = False


def map_test(k):
    j = []
    for i in range(k.shape[0]):
        j.append((k[i] - np.min(k)) / (np.max(k) - np.min(k)))
    j = np.asarray(j)
    return j


mapped_t_values = map_test(unmapped_t_values)

coeffs_x = np.polyfit(x_x, x_equispaced, deg=degrees)
coeffs_y = np.polyfit(x_y, y_equispaced, deg=degrees)
coeffs_z = np.polyfit(x_z, z_equispaced, deg=degrees)


def generated_pos_vals(t, coeffs, degrees):
    op = 0
    for i in range(degrees):
        op += (pow(t, (degrees - i)))* coeffs[i]
    return op

#
# velo = []
#
#
# def vel(x, y, z):
#     for i in range(x.shape[0]):
#         if i == x.shape[0] - 1 or i == y.shape[0] or i == z.shape[0]:
#             return velo
#         else:
#             velocity = math.sqrt(((x[i + 1] - x[i]) ** 2) + ((y[i + 1] - y[i]) ** 2) + ((z[i + 1] - z[i]) ** 2)) / (
#                 0.02)
#             velo.append(velocity)
#     return velo
#
#
# velocity = np.asarray(vel(x_values, y_values, z_values))
#
# acc = []
#
#
# def acceleration():
#     # velocity = np.asarray(vel(x, y, z))
#     for i in range(velocity.shape[0]):
#         if i == velocity.shape[0] - 1:
#             return acc
#         else:
#             k = (velocity[i + 1] - velocity[i]) / (0.02)
#             acc.append(k)
#     return acc

#
# a = np.asarray(acceleration())
#
# print('acceleration values are ' + str(a))
# print('max and min acceleration values  ' + str(np.max(a)) + "   " + str(np.min(a)))
# print('\n')
# print('velocity values are ' + str(velocity))
# print('max and min velocity values  ' + str(np.max(velocity)) + "   " + str(np.min(velocity)))
#
# plt.plot(mapped_t_values[:-2], a)
# plt.xlabel('time');
# plt.ylabel('acceleration')
# plt.show()
#
# plt.plot(mapped_t_values[:-1], velocity)
# plt.xlabel('time');
# plt.ylabel('velocity')
# plt.show()

plt.subplot(2, 3, 1)
plt.plot(x_x, x_equispaced)
plt.xlabel('time');
plt.ylabel('x')
plt.yscale('linear')

plt.subplot(2, 3, 2)
plt.plot(x_y, y_equispaced)
plt.xlabel('time');
plt.ylabel('y')
plt.yscale('linear')

plt.subplot(2, 3, 3)
plt.plot(x_z, z_equispaced)
plt.xlabel('time');
plt.ylabel('z')
plt.yscale('linear')

plt.subplot(2, 3, 4)
plt.plot(x_x, generated_pos_vals(x_x, coeffs_x, degrees))
plt.xlabel('time');
plt.ylabel('gen_x')
plt.yscale('linear')

plt.subplot(2, 3, 5)
plt.plot(x_y, generated_pos_vals(x_y, coeffs_y, degrees))
plt.xlabel('time');
plt.ylabel('gen_y')
plt.yscale('linear')

plt.subplot(2, 3, 6)
plt.plot(x_z, generated_pos_vals(x_z, coeffs_z, degrees))
plt.xlabel('time');
plt.ylabel('gen_z')
plt.yscale('linear')

print('x coefficients are: ' + str(coeffs_x) + '\n',
      'y coefficients are: ' + str(coeffs_y) + '\n',
      'z coefficients are: ' + str(coeffs_z))

plt.show()
