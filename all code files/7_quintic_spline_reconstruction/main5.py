import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity
import similaritymeasures
import csv

#Tangent_start(p1,p2,p3)
p1 = [-506,205,828]
p2 = [-340,287,607]
p3 = [-343,404,752]
p4 = [-233,263,789]
p5 = [-402,228,573]
p6 = [-488,265,575]
p7 = [-204,240,613]
p8 = [-480,300,596]
p9 = [-349,314,488]
spline_points = np.array([p1,p2,p3,p4,p5,p6,p7])

def Tangent_mid(p1,p2,p3, variable_0):
    V1 = [p1[0]-p2[0], p1[1]-p2[1],p1[2]-p2[2]] #BA
    V2 = [p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2]] #BC
    magV1 = np.linalg.norm(V1)
    magV2 = np.linalg.norm(V2)
    angle_between_BA_and_BC = math.acos((V1[0]*V2[0]+V1[1]*V2[1]+V1[2]*V2[2])/(magV1*magV2))
    end_vector = np.cross(V1,V2)
    mag_end_vector = np.linalg.norm(end_vector)
    Unit_Normal_for_ABC_plane = end_vector/mag_end_vector
    i = +1
    angle_between_BA_and_BC_with_90_added = (-1)*i*((angle_between_BA_and_BC/2))# i = +1 for counter clock wise (theta is positive)
    c1 = p2
    c2 = np.asarray(V2)*np.cos(angle_between_BA_and_BC_with_90_added)
    c3 = (np.cross(Unit_Normal_for_ABC_plane,V2))*(np.sin(angle_between_BA_and_BC_with_90_added)) # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
    c4 = (Unit_Normal_for_ABC_plane*(np.dot(Unit_Normal_for_ABC_plane, V2)))*(1-np.cos(angle_between_BA_and_BC_with_90_added))
    c_new = c1+c2+c3+c4
    perc = variable_0
    # perc = 0.5
    magnitude = perc * min(magV1, magV2)
    BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]] #BCnew
    BCnew_mag = np.linalg.norm(BCnew)
    theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
    if (np.round(theta_new,0) != np.round((angle_between_BA_and_BC/2)),0):
        i = -1
        angle_between_BA_and_BC_with_90_added = (-1) * i * (
                    (angle_between_BA_and_BC / 2))  # i = +1 for counter clock wise (theta is positive)
        c1 = p2
        c2 = np.asarray(V2) * np.cos(angle_between_BA_and_BC_with_90_added)
        c3 = (np.cross(Unit_Normal_for_ABC_plane, V2)) * (np.sin(angle_between_BA_and_BC_with_90_added))  # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
        c4 = (Unit_Normal_for_ABC_plane * (np.dot(Unit_Normal_for_ABC_plane, V2))) * (
                    1 - np.cos(angle_between_BA_and_BC_with_90_added))
        c_new = c1 + c2 + c3 + c4
        magnitude = perc * min(magV1, magV2)
        BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]]  # BCnew
        BCnew_mag = np.linalg.norm(BCnew)
        theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
    rotation_angle = -angle_between_BA_and_BC/2 + np.deg2rad(90)
    c1 = p2
    c2 = np.asarray(V2) * np.cos(rotation_angle)
    c3 = (np.cross(Unit_Normal_for_ABC_plane, V2)) * (np.sin(rotation_angle))  # sin(-angle_betweenw_BA_and_BC) because we need bisector which is smaller than the original angle_betweenw_BA_and_BC
    c4 = (Unit_Normal_for_ABC_plane * (np.dot(Unit_Normal_for_ABC_plane, V2))) * (1 - np.cos(rotation_angle))
    c_perpendicular = c1 + c2 + c3 + c4
    #print(c_perpendicular, 'c_perpendicular')

    #vector BC perpendicular

    BC_perpendicular = [c_perpendicular[0]-p2[0],  c_perpendicular[1]-p2[1],  c_perpendicular[2]-p2[2]]
    BC_perpendicular_mag = np.linalg.norm(BC_perpendicular)

    angle_between_bc_and_bc_perpendicular = math.acos((V2[0] * BC_perpendicular[0] + V2[1] * BC_perpendicular[1] + V2[2] * BC_perpendicular[2]) / (magV2 * BC_perpendicular_mag))
    unit_bc_perpendicular = BC_perpendicular/BC_perpendicular_mag
    Final_tangent = magnitude*unit_bc_perpendicular
    return np.asarray(Final_tangent)

def tangent_end_points(a, b,i):
    #i = 0 for start point and 1 for last point
    if i == 0:              # based on previous points, direction has to fixed
        # start point
        ta = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]  # -BA
        # print(ta, 'last piece tangent')
    elif i ==1:  # b = a, c= b
        ta = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
        # ta = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]  # BA

    return np.asarray(ta)

def acceleration_mid(a,b,c,ta,tb,tc,variable_1, variable_2): #tangenta,tangentb,tangentc
    tangent_a = np.asarray(ta)
    tangent_b = np.asarray(tb)
    tangent_c = np.asarray(tc)
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.asarray(c)
    #**** double derivation*** = 6A + 2tA + 4tB − 6B
    V1 = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]  # BA
    V2 = [b[0] - c[0], b[1] - c[1], b[2] - c[2]]  # BC
    magV1 = np.linalg.norm(V1)
    magV2 = np.linalg.norm(V2)

    s_AB_double_derivative =  (6*a)+(2*ta)+(4*tb)-(6*b)
    s_BC_double_derivative =  -(6*b)-(4*tb)-(2*tc)+(6*c)

    alpha = variable_1
    beta = variable_2
    # alpha = magV2/(magV1+magV2)
    # beta = magV1/(magV1+magV2)

    acceleration = (alpha*s_AB_double_derivative)+(beta*s_BC_double_derivative)
    return  np.asarray(acceleration)

def acceleration_end_points(a,b,ta,tb,i, variable_3):
    #i = 0 for start point and 1 for last point
    if i == 0:
        # start point
        s_AB_double_derivative = (6 * a) + (2 * ta) + (4 * tb) - (6 * b)
    else:  # b = a, c= b
        s_AB_double_derivative = -(6 * a) - (2 * tb) - (4 * ta) + (6 * b)

    return np.asarray(variable_3 * s_AB_double_derivative)

# variables = [0.5,0.5,0.5,-6]
def similarity_check(variables, exp_no):
    datalog = np.genfromtxt('21_apr_21_exprmnt_pnts_2.csv', delimiter=',')
    experiments = [[102,500],[500,907],[907,1287],[1287,1675],[1675,2078],[2078,2452],[2452,2835],[2835,3215]
                   ,[3215,3586],[3586,4021],[4021,4457],[4457,4874],[4874,5312],[5312,5761],[5761,6185]
                   ,[6185,6616],[6616,7047],[7047,7328],[7328,7630],[7630,7908],[7908,8161],[8161,8402]]
    datalog_start, datalog_end = experiments[exp_no][0], experiments[exp_no][1]
    datalog = datalog[datalog_start:datalog_end, :]

    tangents_for_all_points = []
    acceleration_for_all_points = []

    for i in range(len(spline_points)):
        if i == 0:
            tangent = tangent_end_points(spline_points[0], spline_points[1], 0)
            tangents_for_all_points.append(np.asarray(tangent))
        elif i != 0 and i != len(spline_points) - 1:
            tangent = Tangent_mid(spline_points[i - 1], spline_points[i], spline_points[i + 1], variables[0])
            tangents_for_all_points.append(np.asarray(tangent))
        elif i == len(spline_points) - 1:
            tangent = tangent_end_points(spline_points[len(spline_points) - 2], spline_points[len(spline_points) - 1],1)
            tangents_for_all_points.append(np.asarray(tangent))

    for i in range(len(spline_points)):
        if i == 0:
            acceleration = acceleration_end_points(spline_points[0], spline_points[1], tangents_for_all_points[0],
                                                   tangents_for_all_points[1], 0, variables[3])
            acceleration_for_all_points.append(np.asarray(acceleration))
        elif i == len(spline_points) - 1:
            acceleration = acceleration_end_points(spline_points[len(spline_points) - 2],
                                                   spline_points[len(spline_points) - 1],
                                                   tangents_for_all_points[len(tangents_for_all_points) - 2],
                                                   tangents_for_all_points[len(tangents_for_all_points) - 1], 1, variables[3])
            acceleration_for_all_points.append(np.asarray(acceleration))
        else:
            acceleration = acceleration_mid(spline_points[i - 1], spline_points[i], spline_points[i + 1],
                                            tangents_for_all_points[i - 1], tangents_for_all_points[i],
                                            tangents_for_all_points[i + 1], variables[1], variables[2])
            acceleration_for_all_points.append(np.asarray(acceleration))

    # print(p1, p2, p3)
    # print("POINTS")
    # print(p1, p2, p3, p4, p5, p6, p7)
    # print('TANGENTS')
    # print(tangents_for_all_points)
    # print('ACCELERATION')
    # print(acceleration_for_all_points)

    control_points = []
    final_trajectory = []
    for i in range(len(spline_points)):
        while i < (len(spline_points) - 1):
            c0 = np.asarray(spline_points[i])
            c5 = np.asarray(spline_points[i + 1])
            c1 = (0.2 * tangents_for_all_points[i]) + c0
            c4 = c5 - (0.2 * tangents_for_all_points[i + 1])
            c2 = (0.05 * acceleration_for_all_points[i]) + (2 * c1) - c0
            c3 = (0.05 * acceleration_for_all_points[i + 1]) + (2 * c4) - c5
            c1 = np.asarray(c1)
            c4 = np.asarray(c4)
            c2 = np.asarray(c2)
            c3 = np.asarray(c3)
            # print('\n' + "#SEGMENT " + str(i + 1) + '\n')
            control_points.append([c0, c1, c2, c3, c4, c5])
            # print(c0, " control point 0")
            # print(c1, " control point 1")
            # print(c2, " control point 2")
            # print(c3, " control point 3")
            # print(c4, " control point 4")
            # print(c5, " control point 5")
            # bc spline piece
            number_of_pieces = 50
            for i in range(number_of_pieces):
                t = i / number_of_pieces
                trajectory = (pow((1 - t), 5) * c0) + (5 * pow((1 - t), 4) * t * c1) + (
                        10 * pow((1 - t), 3) * pow(t, 2) * c2) + (10 * pow((1 - t), 2) * pow(t, 3) * c3) + (
                                     5 * pow((1 - t), 1) * pow(t, 4) * c4) + (pow(t, 5) * c5)
                final_trajectory.append(trajectory)

    x = final_trajectory
    y = datalog
    dtw, d = similaritymeasures.dtw(x, y)

    return dtw, d, control_points, tangents_for_all_points

variables = [0.5,0.5,0.5,-6]
score, distance_matrix, control_points, tangents_for_all_points = similarity_check(variables, 12)


trial = []
with open('experiment_id_and_indexes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        trial.append(row)
names = []
row_indexes = []
experiment_id = []
for i in range(len(trial)):
    temp = trial[i][0].split(",")
    names.append(temp[0])
    row_indexes.append(int(temp[1]))
    experiment_id.append(int(temp[2]))
records = np.rec.fromarrays((np.asarray(names),np.asarray(row_indexes),np.asarray(experiment_id)),
                            names=('pos','index','exp_id'))
# res = differential_evolution(score, bounds=bounds, tol=0.01)

def exp_seg(ex,seg_start, seg_end):
    item_index = np.where(records['exp_id'] == ex)
    segment = records['index'][item_index[0]]
    seg_start_index = np.where(records['pos'][item_index[0]] == seg_start)
    seg_end_index = np.where(records['pos'][item_index[0]] == seg_end)
    k = segment[seg_start_index[0]]
    l = segment[seg_end_index[0]]
    if len(k) == 1 and len(l)==1:
        if k[0]<l[0]:
            return k[0],l[0]
        else:
            print("please enter a valid order of points")
            return 0,0
    elif len(k) == 1 and len(l)>1:
        if k[0] < l[0]:
            return k[0],l[0]
        else:
            return k[0], l[-1]
    elif len(k) > 1 and len(l)==1:
        if k[-1]<l[0]:
            return k[-1], l[0]
        else:
            return k[0], l[0]
    elif len(k) > 1 and len(l) > 1:
        return k[0], l[-1]

def tangents():
    return tangents_for_all_points

def cps():
    return control_points

# np.savetxt('algo_geneared_trajectory_1.csv',final_trajectory )









