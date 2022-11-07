import numpy as np
import math
import similaritymeasures
from datetime import datetime
from scipy.optimize import rosen, differential_evolution
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
np.seterr(divide='ignore', invalid='ignore')

def similarity_check(variable):
    def Tangent_mid(p1, p2, p3, variable_0):
        V1 = [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]  # BA
        V2 = [p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2]]  # BC
        magV1 = np.linalg.norm(V1)
        magV2 = np.linalg.norm(V2)
        # print(magV1, magV2)
        angle_between_BA_and_BC = math.acos((V1[0] * V2[0] + V1[1] * V2[1] + V1[2] * V2[2]) / (magV1 * magV2))
        end_vector = np.cross(V1, V2)
        mag_end_vector = np.linalg.norm(end_vector)
        # print(mag_end_vector)
        Unit_Normal_for_ABC_plane = end_vector / mag_end_vector
        i = +1
        angle_between_BA_and_BC_with_90_added = (-1) * i * (
            (angle_between_BA_and_BC / 2))  # i = +1 for counter clock wise (theta is positive)
        c1 = p2
        c2 = np.asarray(V2) * np.cos(angle_between_BA_and_BC_with_90_added)
        c3 = (np.cross(Unit_Normal_for_ABC_plane, V2)) * (np.sin(
            angle_between_BA_and_BC_with_90_added))  # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
        c4 = (Unit_Normal_for_ABC_plane * (np.dot(Unit_Normal_for_ABC_plane, V2))) * (
                1 - np.cos(angle_between_BA_and_BC_with_90_added))
        c_new = c1 + c2 + c3 + c4
        perc = variable_0
        # perc = 0.5
        magnitude = perc * min(magV1, magV2)
        BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]]  # BCnew
        BCnew_mag = np.linalg.norm(BCnew)
        theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
        if (np.round(theta_new, 0) != np.round((angle_between_BA_and_BC / 2)), 0):
            i = -1
            angle_between_BA_and_BC_with_90_added = (-1) * i * (
                (angle_between_BA_and_BC / 2))  # i = +1 for counter clock wise (theta is positive)
            c1 = p2
            c2 = np.asarray(V2) * np.cos(angle_between_BA_and_BC_with_90_added)
            c3 = (np.cross(Unit_Normal_for_ABC_plane, V2)) * (np.sin(
                angle_between_BA_and_BC_with_90_added))  # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
            c4 = (Unit_Normal_for_ABC_plane * (np.dot(Unit_Normal_for_ABC_plane, V2))) * (
                    1 - np.cos(angle_between_BA_and_BC_with_90_added))
            c_new = c1 + c2 + c3 + c4
            magnitude = perc * min(magV1, magV2)
            BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]]  # BCnew
            BCnew_mag = np.linalg.norm(BCnew)
            theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
        rotation_angle = -angle_between_BA_and_BC / 2 + np.deg2rad(90)
        c1 = p2
        c2 = np.asarray(V2) * np.cos(rotation_angle)
        c3 = (np.cross(Unit_Normal_for_ABC_plane, V2)) * (np.sin(
            rotation_angle))  # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
        c4 = (Unit_Normal_for_ABC_plane * (np.dot(Unit_Normal_for_ABC_plane, V2))) * (1 - np.cos(rotation_angle))
        c_perpendicular = c1 + c2 + c3 + c4
        # vector BC perpendicular
        BC_perpendicular = [c_perpendicular[0] - p2[0], c_perpendicular[1] - p2[1], c_perpendicular[2] - p2[2]]
        BC_perpendicular_mag = np.linalg.norm(BC_perpendicular)
        angle_between_bc_and_bc_perpendicular = math.acos(
            (V2[0] * BC_perpendicular[0] + V2[1] * BC_perpendicular[1] + V2[2] * BC_perpendicular[2]) / (
                    magV2 * BC_perpendicular_mag))
        unit_bc_perpendicular = BC_perpendicular / BC_perpendicular_mag
        Final_tangent = magnitude * unit_bc_perpendicular
        return np.asarray(Final_tangent)
    def tangent_end_points(a, b, i):
        # i = 0 for start point and 1 for last point
        if i == 0:  # based on previous points, direction has to fixed
            # start point
            ta = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]  # -BA
            # print(ta, 'last piece tangent')
        elif i == 1:  # b = a, c= b
            ta = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
            # ta = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]  # BA

        return np.asarray(ta)
    def acceleration_mid(a, b, c, ta, tb, tc, variable_1, variable_2):  # tangenta,tangentb,tangentc
        a = np.asarray(a)
        b = np.asarray(b)
        c = np.asarray(c)
        # **** double derivation*** = 6A + 2tA + 4tB − 6B
        V1 = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]  # BA
        V2 = [b[0] - c[0], b[1] - c[1], b[2] - c[2]]  # BC
        magV1 = np.linalg.norm(V1)
        magV2 = np.linalg.norm(V2)

        s_AB_double_derivative = (6 * a) + (2 * ta) + (4 * tb) - (6 * b)
        s_BC_double_derivative = -(6 * b) - (4 * tb) - (2 * tc) + (6 * c)

        alpha = variable_1
        beta = variable_2
        # alpha = magV2/(magV1+magV2)
        # beta = magV1/(magV1+magV2)

        acceleration = (alpha * s_AB_double_derivative) + (beta * s_BC_double_derivative)
        return np.asarray(acceleration)
    def acceleration_end_points(a, b, ta, tb, i, variable_3):
        # i = 0 for start point and 1 for last point
        if i == 0:
            # start point
            s_AB_double_derivative = (6 * a) + (2 * ta) + (4 * tb) - (6 * b)
        else:  # b = a, c= b
            s_AB_double_derivative = -(6 * a) - (2 * tb) - (4 * ta) + (6 * b)

        return np.asarray(variable_3 * s_AB_double_derivative)
    tangents_for_all_points = []
    acceleration_for_all_points = []
    average_distances = []
    datalog = np.genfromtxt('21_apr_21_exprmnt_pnts_2.csv', delimiter=',')
    for i in range(len(experiments_list)):
        l = len(experiments_list[i])
        if l >=minimum_Segments:
            exp_no = i
            spline_points = np.asarray(experiments_list[exp_no])
            datalog_start, datalog_end = experiments[exp_no][0], experiments[exp_no][1]
            datalog = datalog[datalog_start:datalog_end, :]
            for j in range(len(spline_points)):
                if j == 0:
                    tangent = tangent_end_points(spline_points[0], spline_points[1], 0)
                    tangents_for_all_points.append(np.asarray(tangent))
                elif j != 0 and j != len(spline_points) - 1:
                    tangent = Tangent_mid(spline_points[j - 1], spline_points[j], spline_points[j + 1], variable[0])
                    tangents_for_all_points.append(np.asarray(tangent))
                elif j == len(spline_points) - 1:
                    tangent = tangent_end_points(spline_points[len(spline_points) - 2],
                                                 spline_points[len(spline_points) - 1], 1)
                    tangents_for_all_points.append(np.asarray(tangent))

            for k in range(len(spline_points)):
                if k == 0:
                    acceleration = acceleration_end_points(spline_points[0], spline_points[1], tangents_for_all_points[0],
                                                           tangents_for_all_points[1], 0, variable[3])
                    acceleration_for_all_points.append(np.asarray(acceleration))
                elif k == len(spline_points) - 1:
                    acceleration = acceleration_end_points(spline_points[len(spline_points) - 2],
                                                           spline_points[len(spline_points) - 1],
                                                           tangents_for_all_points[len(tangents_for_all_points) - 2],
                                                           tangents_for_all_points[len(tangents_for_all_points) - 1], 1,
                                                           variable[3])
                    acceleration_for_all_points.append(np.asarray(acceleration))
                else:
                    acceleration = acceleration_mid(spline_points[k - 1], spline_points[k], spline_points[k + 1],
                                                    tangents_for_all_points[k - 1], tangents_for_all_points[k],
                                                    tangents_for_all_points[k + 1], variable[1], variable[2])
                    acceleration_for_all_points.append(np.asarray(acceleration))
            control_points = []
            final_trajectory = []
            for m in range(len(spline_points)):
                while m < (len(spline_points) - 1):
                    c0 = np.asarray(spline_points[m])
                    c5 = np.asarray(spline_points[m + 1])
                    c1 = (0.2 * tangents_for_all_points[m]) + c0
                    c4 = c5 - (0.2 * tangents_for_all_points[m + 1])
                    c2 = (0.05 * acceleration_for_all_points[m]) + (2 * c1) - c0
                    c3 = (0.05 * acceleration_for_all_points[m + 1]) + (2 * c4) - c5
                    c1 = np.asarray(c1)
                    c4 = np.asarray(c4)
                    c2 = np.asarray(c2)
                    c3 = np.asarray(c3)
                    control_points.append([c0, c1, c2, c3, c4, c5])
                    number_of_pieces = 50
                    for n in range(number_of_pieces):
                        t = n / number_of_pieces
                        trajectory = (pow((1 - t), 5) * c0) + (5 * pow((1 - t), 4) * t * c1) + (
                                10 * pow((1 - t), 3) * pow(t, 2) * c2) + (10 * pow((1 - t), 2) * pow(t, 3) * c3) + (
                                             5 * pow((1 - t), 1) * pow(t, 4) * c4) + (pow(t, 5) * c5)
                        final_trajectory.append(trajectory)
            x = final_trajectory
            y = datalog
            dtw, d = similaritymeasures.dtw(x, y)
            average_distances.append(dtw/l)
            # print(dtw)
    average_metric = sum(average_distances)
    return average_metric

# hyper_parameters
bounds = [(0, 1), (0, 1), (0, 1), (-5, 5)]
h = [0, 0, 1266]
p1 = [-506, 205, 828]
p2 = [-340, 287, 607]
p3 = [-343, 404, 752]
p4 = [-233, 263, 789]
p5 = [-402, 228, 573]
p6 = [-488, 265, 575]
p7 = [-204, 240, 613]
p8 = [-480, 300, 596]
p9 = [-349, 314, 488]
experiments_list = [[p1, p2, p3, p4, p5, p6, p7], [p1, p2, p3, p4, p5, p1], [p1, p2, p3, p4, p5, p2],
                    [p1, p2, p3, p4, p5, p3], [p1, p2, p3, p4, p5, p4], [p1, p2, p3, p4, p5, p6],
                    [p1, p2, p3, p4, p5, p7],
                    [p1, p2, p3, p4, p5, p8], [p1, p2, p3, p4, p5, p9], [p1, p2, p3, p1, p5, p6, p7],
                    [p1, p2, p3, p2, p5, p6, p7], [p1, p2, p3, p4, p5, p6, p7], [p1, p2, p3, p5, p5, p6, p7],
                    [p1, p2, p3, p6, p5, p6, p7], [p1, p2, p3, p7, p5, p6, p7], [p1, p2, p3, p8, p5, p6, p7],
                    [p1, p2, p3, p8, p5, p6, p7], [p1, p3, p4], [p1, p2, p3], [p1, p2], [p2, p3], [p3, p4]
                    ]
experiments = [[216, 402], [624, 795], [1030, 1192], [1410, 1580], [1798, 1987], [2201, 2346], [2575, 2740],
               [2959, 3111], [3338, 3487], [3709, 3932], [4144, 4367], [4580, 4776], [4997, 5215], [5435, 5665],
               [5884, 6090]
    , [6308, 6518], [6739, 6949], [7170, 7238], [7452, 7535], [7754, 7804], [8020, 8070], [8270, 8309]]
minimum_Segments = 6
print("Current Time =", current_time)
print(similarity_check([0,0,0,0]))
print("Current Time =", current_time)

#
# print("Current Time =", current_time)
# result = differential_evolution(similarity_check, bounds, maxiter=1, popsize=5)
# #other parameters: population size;
# opt_ctrl_var = result.x
# opt_dist = result.fun
# print(opt_ctrl_var)
# print(opt_dist)
# print("Current Time =", current_time)











