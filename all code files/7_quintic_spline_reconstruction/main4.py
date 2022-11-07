import numpy as np
import math
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

# p1 = [0,0,0]
# p2 = [100,100,0]
# p3 = [200,0,0]
import matplotlib
import mpl_toolkits




def Tangent_mid(p1,p2,p3):

    V1 = [p1[0]-p2[0], p1[1]-p2[1],p1[2]-p2[2]] #BA
    V2 = [p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2]] #BC
    magV1 = np.linalg.norm(V1)
    magV2 = np.linalg.norm(V2)
    angle_between_BA_and_BC = math.acos((V1[0]*V2[0]+V1[1]*V2[1]+V1[2]*V2[2])/(magV1*magV2))
    #cross_product
    #print(np.degrees(angle_between_BA_and_BC/2),'angular bisector angle')# half of angle b/w ba and bc
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
    #print(c_new,'c_new')
    #angle = angle_between_BA_and_BC/2
    perc = 0.5
    # wt_av_1 = magV1/(magV1+magV2)
    # wt_av_2 = magV2/(magV1+magV2)
    wt_av_1 = 0.65
    wt_av_2 = 1-wt_av_1
    #Tnagent Magnitude
    # if magV1 < magV2:
    #     magnitude = perc* magV2
    # elif magV2 < magV1:
    #     magnitude = perc* magV2
    magnitude = perc * min(magV1, magV2)
    # magnitude = 0.5 * (wt_av_1*(magV2) + wt_av_2*(magV1))
    # magnitude = 0.75 * magV2
    BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]] #BCnew
    BCnew_mag = np.linalg.norm(BCnew)
    #print(BCnew_mag,'new_vector_mag')
    theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
    #print(np.degrees(theta_new),'angle_betweenw_BA_and_BC new')
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
        #print(c_new, 'c_new')
        # angle = angle_between_BA_and_BC/2
        # Tnagent Magnitude
        magnitude = perc * min(magV1, magV2)
        # if magV1 < magV2:
        #     magnitude = perc * magV2
        # else:
        #     magnitude = perc * magV1
        # magnitude = 0.5 *(wt_av_1 * (magV2) + wt_av_2 * (magV1))
        # magnitude = 0.75 * magV2
        BCnew = [c_new[0] - p2[0], c_new[1] - p2[1], c_new[2] - p2[2]]  # BCnew
        BCnew_mag = np.linalg.norm(BCnew)
        #print(BCnew_mag, 'new_vector_mag')
        theta_new = math.acos((V1[0] * BCnew[0] + V1[1] * BCnew[1] + V1[2] * BCnew[2]) / (magV1 * BCnew_mag))
        #print(np.degrees(theta_new), 'angle_betweenw_BA_and_BC new')


    #checkpoint = angular bisector
    #next step ---- rotate BC with 90 - angular bisector angle(90-(theta/2))
    rotation_angle = -angle_between_BA_and_BC/2 + np.deg2rad(90)
    # (angle_between_BA_and_BC)
    #rotation_angle = i * (np.deg2rad(90)-(angle_between_BA_and_BC/2))
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
    #print(np.degrees(angle_between_bc_and_bc_perpendicular),'angle_between_bc_and_bc_perpendicular')

    #Last step find the unit vector for bc_perpendicular and multiply with mag

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
    # return np.asarray([0, 0, 0])

def acceleration_mid(a,b,c,ta,tb,tc): #tangenta,tangentb,tangentc
    tangent_a = np.asarray(ta)
    tangent_b = np.asarray(tb)
    tangent_c = np.asarray(tc)
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.asarray(c)

    # print(a,b,c,'a,b,c')
    # print(tangent_a,tangent_b,tangent_c,'tangent_a,tangent_b,tangent_c')

    #**** double derivation*** = 6A + 2tA + 4tB − 6B
    V1 = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]  # BA
    V2 = [b[0] - c[0], b[1] - c[1], b[2] - c[2]]  # BC
    magV1 = np.linalg.norm(V1)
    magV2 = np.linalg.norm(V2)

    s_AB_double_derivative =  (6*a)+(2*ta)+(4*tb)-(6*b)
    s_BC_double_derivative =  -(6*b)-(4*tb)-(2*tc)+(6*c)

    alpha = magV2/(magV1+magV2)
    beta = magV1/(magV1+magV2)

    acceleration = (alpha*s_AB_double_derivative)+(beta*s_BC_double_derivative)
    return  np.asarray(acceleration)

def acceleration_end_points(a,b,ta,tb,i):
    #i = 0 for start point and 1 for last point
    if i == 0:
        # start point
        s_AB_double_derivative = (6 * a) + (2 * ta) + (4 * tb) - (6 * b)
    else:  # b = a, c= b
        s_AB_double_derivative = -(6 * a) - (2 * tb) - (4 * ta) + (6 * b)

    return np.asarray(-6 * s_AB_double_derivative)
    # return np.asarray([0,0,0])


# spline_points = [p1,p2,p3]
spline_points = np.array([p1,p2,p3,p4,p5,p6,p7])

tangents_for_all_points = []
acceleration_for_all_points = []

for i in range(len(spline_points)):
    if i == 0:
        tangent = tangent_end_points(spline_points[0],spline_points[1],0)
        tangents_for_all_points.append(np.asarray(tangent))
    elif i != 0 and i != len(spline_points)-1:
        tangent= Tangent_mid(spline_points[i-1],spline_points[i],spline_points[i+1])
        tangents_for_all_points.append(np.asarray(tangent))
    elif i == len(spline_points) - 1:
        tangent = tangent_end_points(spline_points[len(spline_points)-2], spline_points[len(spline_points)-1],1)
        tangents_for_all_points.append(np.asarray(tangent))

# print(p1, p2, p3)
print(p1, p2, p3, p4, p5, p6, p7)
print(tangents_for_all_points,'tangents_for_all_points')

def tangents():
    return tangents_for_all_points
# print(len(spline_points),'len of spline points')#6




for i in range(len(spline_points)):
    if i == 0:
        acceleration = acceleration_end_points(spline_points[0],spline_points[1],tangents_for_all_points[0],tangents_for_all_points[1],0)
        acceleration_for_all_points.append(np.asarray(acceleration))
    elif i == len(spline_points)-1:
        acceleration = acceleration_end_points(spline_points[len(spline_points)-2], spline_points[len(spline_points)-1],tangents_for_all_points[len(tangents_for_all_points)-2], tangents_for_all_points[len(tangents_for_all_points)-1],1)
        acceleration_for_all_points.append(np.asarray(acceleration))
    else:
        acceleration = acceleration_mid(spline_points[i-1],spline_points[i],spline_points[i+1],tangents_for_all_points[i-1],tangents_for_all_points[i],tangents_for_all_points[i+1])
        acceleration_for_all_points.append(np.asarray(acceleration))

print(acceleration_for_all_points,'acceleration')

control_points = []
final_trajectory = []
for i in range(len(spline_points)):
    while i <(len(spline_points)-1):
        c0 = np.asarray(spline_points[i])
        c5 = np.asarray(spline_points[i+1])
        c1 = (0.2 * tangents_for_all_points[i]) + c0
        c4 = c5 - (0.2 * tangents_for_all_points[i + 1])
        c2 = (0.05 * acceleration_for_all_points[i]) + (2 * c1) - c0
        c3 = (0.05 * acceleration_for_all_points[i + 1]) + (2 * c4) - c5
        c1 = np.asarray(c1)
        c4 = np.asarray(c4)
        c2 = np.asarray(c2)
        c3 = np.asarray(c3)

        control_points.append([c0,c1,c2,c3,c4,c5])
        print(c0, " control point 0")
        print(c1, " control point 1")
        print(c2, " control point 2")
        print(c3, " control point 3")
        print(c4, " control point 4")
        print(c5, " control point 5")

        #bc spline piece

        number_of_pieces = 50
        for i in range(number_of_pieces):
            t = i / number_of_pieces
            trajectory = (pow((1 - t), 5) * c0) + (5 * pow((1 - t), 4) * t * c1) + (
                    10 * pow((1 - t), 3) * pow(t, 2) * c2) + (10 * pow((1 - t), 2) * pow(t, 3) * c3) + (
                                 5 * pow((1 - t), 1) * pow(t, 4) * c4) + (pow(t, 5) * c5)
            final_trajectory.append(trajectory)

# print(final_trajectory)
def cps():
    return control_points
np.savetxt('algo_geneared_trajectory_1.csv',final_trajectory )


# spline_points = [p1,p2,p3,p4,p5]
#
# for i in range(len(spline_points)):
#     if i ==0:
#         p1 = spline_points[i]
#         p2 = spline_points[i+1]
#     elif i ==1 and i != len(spline_points)-1:
#         p1 = spline_points[i-1]
#         p2 = spline_points[i]
#         p3 = spline_points[i+1]
#         Tangent_mid(p1,p2,p3)
#
#     elif i == len(spline_points)-1:
#         p1 = spline_points[i-1]
#         p2 = spline_points[i]
#         t = 2 # variable time
#         tangent_first_last(p1, p2, t)









