import numpy as np
import pandas as pd
import matplotlib
import math
from numpy import savetxt
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def mapFromTo(x, a, b, c, d):
    y = (x - a) / (b - a) * (d - c) + c
    return y


def map_test(k):
    j = []
    for i in range(k.shape[0]):
        j.append((k[i] - np.min(k)) / (np.max(k) - np.min(k)))
    j = np.asarray(j, dtype=np.float)
    return j


def generated_pos_vals(t, coeffs, degrees):
    op = 0
    for i in range(degrees):
        op += (t ** (degrees - i)) * coeffs[i]
    return op


def vel(x, y, z):
    velo = []
    for i in range(x.shape[0]):
        if i == x.shape[0] - 1 or i == y.shape[0] or i == z.shape[0]:
            return velo
        else:
            velocity = math.sqrt(((x[i + 1] - x[i]) ** 2) + ((y[i + 1] - y[i]) ** 2) + ((z[i + 1] - z[i]) ** 2)) / (0.02)
            velo.append(velocity)
    return velo


def acceleration(velocity):
    # velocity = np.asarray(vel(x, y, z))
    for i in range(velocity.shape[0]):
        if i == velocity.shape[0] - 1:
            return acc
        else:
            k = (velocity[i + 1] - velocity[i]) / (0.02)
            acc.append(k)
    return acc

def experiment(exp_num):
    exp_1 = [218, 452, 483, 490, 496, 502, 514, 739];      exp_2 = [739, 996, 1029, 1035, 1041, 1048, 1060, 1283]
    exp_3 = [1283, 1541, 1574, 1581, 1628, 1664, 1890];    exp_4 = [1890, 2150,2183,2199,2255,2473]
    exp_5 = [2473,2732, 2765, 2771, 2782, 2836, 3050];     exp_6 = [3050, 3309, 3342, 3353, 3386, 3426, 3648]
    exp_7 = [3648,3906,3939,3946,3952,3963,4187];          exp_8 = [4187,4445,4477,4484,4490,4509,4733]
    exp_9 = [4733,4990,5023,5029,5035,5061,5286];          exp_10 = [5286,5543,5575,5582,5588,5619,5847]
    exp_11 = [5847,6104,6150,6194,6239,6245,6257,6481];    exp_12 = [6481,6737,6817,6855,6894,6900,6912,7136]
    exp_13 = [7136,7394,7426,7433,7439,7445,7458,7682];    exp_14 = [7682,7940,7972,7991,8012,8034,8047,8271]
    exp_15 = [8271,8528,8561,8584,8650,8673,8687,8911];    exp_16 = [8911,9168,9201,9230,9275,9300,9314,9538]
    exp_17 = [9538,9795,9827,9864,9909,9938,9965,10175];   exp_18 = [10175,10433,10465,10502,10547,10576,10603,10813]
    exp_19 = [10813,11069,11115,11340];    exp_20 = [11340,11599,11641,11866]
    exp_21 = [11866,12125,12160,12388]; exp_22 =[12388,12650,12684,12908]
    exp_23 = [12908,13840,13875,14100]
    if exp_num == 1: return exp_1
    elif exp_num == 2: return exp_2
    elif exp_num == 3: return exp_3
    elif exp_num == 4: return exp_4
    elif exp_num == 5: return exp_5
    elif exp_num == 6: return exp_6
    elif exp_num == 7: return exp_7
    elif exp_num == 8: return exp_8
    elif exp_num == 9: return exp_9
    elif exp_num == 10: return exp_10
    elif exp_num == 11: return exp_11
    elif exp_num == 12: return exp_12
    elif exp_num == 13: return exp_13
    elif exp_num == 14: return exp_14
    elif exp_num == 15: return exp_15
    elif exp_num == 16: return exp_16
    elif exp_num == 17: return exp_17
    elif exp_num == 18: return exp_18
    elif exp_num == 19: return exp_19
    elif exp_num == 20: return exp_20
    elif exp_num == 21: return exp_21
    elif exp_num == 22: return exp_22
    elif exp_num == 23: return exp_23
    else: return None

df = pd.read_csv("20_jan_21_txyz.csv")
all = df.to_numpy()
all = all[:,0:4]
# print(all)
# list_p12 = [[1880, 1962], [2549, 2630], [3791, 3861], [5064, 5145], [6432, 6508], [8214, 8298], [10308, 10374],
#             [11083, 11160], [11871, 11950]]
# list_p23 = [[2630, 2753], [3861, 3984], [5145, 5267], [6508, 6627], [8298, 8416], [10374, 10513], [11160, 11289],
#             [11950, 12072]]
# list_p34 = [[2753,2815],[3984,4046],[5267,5329],[11289,11350],[12072,12135]]
# ll = 11871
# ul = 11950
degrees = int(5)

coeffs = []
x = []
t = []
velo = []; acc = []

def plot(exp_number, p1, p2):
    current_exp = experiment(exp_number)
    ll = current_exp[p1]
    ul = current_exp[p2]
    x_values = all[ll:ul][:,1];     y_values = all[ll:ul][:,2];    z_values = all[ll:ul][:,3]
    x_values = x_values.astype('float64'); y_values = y_values.astype('float64'); z_values = z_values.astype('float64');
    unmapped_t_values = all[ll:ul][:,0]
    unmapped_t_values.flags.writeable = False
    mapped_t_values = map_test(unmapped_t_values).astype(dtype=float)
    t.append(mapped_t_values) ############################################################
    # print(type(mapped_t_values[0]))
    # print(type(x_values[0]))
    coeffs_x = np.polyfit(unmapped_t_values, x_values, deg=degrees)
    coeffs_y = np.polyfit(mapped_t_values, y_values, deg=degrees)
    coeffs_z = np.polyfit(mapped_t_values, z_values, deg=degrees)
    x_gen = generated_pos_vals(unmapped_t_values, coeffs_x, degrees)
    y_gen = generated_pos_vals(mapped_t_values, coeffs_y, degrees)
    z_gen = generated_pos_vals(mapped_t_values, coeffs_z, degrees)

    velocity = np.asarray(vel(x_values, y_values, z_values))
    a = np.asarray(acceleration(velocity))
    plt.subplot(2, 3, 1);    plt.plot(unmapped_t_values, x_values);    plt.xlabel('time');    plt.ylabel('x_vals');    plt.yscale('linear')
    plt.subplot(2, 3, 2);    plt.plot(mapped_t_values, y_values);    plt.xlabel('time');    plt.ylabel('y_vals');    plt.yscale('linear')
    plt.subplot(2, 3, 3);    plt.plot(mapped_t_values, z_values);    plt.xlabel('time');    plt.ylabel('z_vals');    plt.yscale('linear')
    plt.subplot(2, 3, 4);    plt.plot(unmapped_t_values, x_gen);    plt.xlabel('time');    plt.ylabel('x_gen');    plt.yscale('linear')
    plt.subplot(2, 3, 5);    plt.plot(mapped_t_values, y_gen);    plt.xlabel('time');    plt.ylabel('y_gen');    plt.yscale('linear')
    plt.subplot(2, 3, 6);    plt.plot(mapped_t_values, z_gen);    plt.xlabel('time');    plt.ylabel('z_gen');    plt.yscale('linear')
    # plt.subplot(2, 4, 7);    plt.plot(mapped_t_values, velocity);    plt.xlabel('time');    plt.ylabel('velocity');    plt.yscale('linear')
    # plt.subplot(2, 4, 8);    plt.plot(mapped_t_values, a);    plt.xlabel('time');    plt.ylabel('acceleration');    plt.yscale('linear')
    plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_values, y_values, z_values)
    ax.scatter(x_gen, y_gen, z_gen)
    # plt.show()
    # plt.savefig('13_jan_21_exp_data_plot.png')
    return mapped_t_values, x_values, x_gen, coeffs_x, coeffs_y, coeffs_z

p1 = 3
p2 = 4
mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(15,p1,p2); print(coeffs_x); print(coeffs_y); print(coeffs_z)

# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(20,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(21,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(22,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(23,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(16,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(17,p1,p2); print(coeffs_x)
# mapped_time, x_vals, x_gen_vals, coeffs_x, coeffs_y, coeffs_z = plot(18,p1,p2); print(coeffs_x)

# print(mapped_time)
# print(x_vals)
# print(x_gen_vals)

# print(coeffs_y)
# print(coeffs_z)

