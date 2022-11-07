import numpy as np
from numpy import dot, matrix, deg2rad, cross
from math import pi
import math
from math import cos, sin, acos, asin

# input data: DH parameters of kuka iiwa7, initial theta angles, end effector position transformation matrix.


d_bs, d_se, d_ew, d_wf = 340, 400, 400, 126
d = np.array([d_bs, 0, d_se, 0, d_ew, 0, d_wf])
# theta = np.array([d2r(-115.8158), d2r(107.2721),d2r(0),d2r(75),d2r(-143.2641),d2r(25.8884),d2r(-90.9575)])
theta1 = np.array([deg2rad(30), deg2rad(-45), deg2rad(60), deg2rad(75), deg2rad(-20), deg2rad(95), deg2rad(-80)])
theta = np.array([deg2rad(0), deg2rad(0), deg2rad(0), deg2rad(0), deg2rad(0), deg2rad(0), deg2rad(0)])
alpha = np.array([-pi / 2, pi / 2, pi / 2, -pi / 2, -pi / 2, pi / 2, 0])
a = np.array([0, 0, 0, 0, 0, 0, 0])
axis_ranges = np.array([[-170,170],[-120,120],[-170,170],[-120,120],[-170,170],[-120,120],[-175,175]]) # +/-170 +/-120 +/-170 +/-120 +/-170 +/-120 +/-175

from numpy import genfromtxt
my_data = genfromtxt('point_generated_2.csv', delimiter=',')

"DH transformation matrix"
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

"Transformation chain"

def transformation(angles, joints):
    temp3 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    temp3 = np.matrix(temp3)
    for i in range(joints):
        temp3 = dot(temp3, DH(angles, i))
    return temp3


def mag(x):
    return np.linalg.norm(x)


def skew(x):
    return np.matrix([[0, -x.item(2), x.item(1)],
                      [x.item(2), 0, -x.item(0)],
                      [-x.item(1), x.item(0), 0]])

def range_check(x):
    for i, angle in enumerate(x):
        if angle>= 0:
            if angle > np.deg2rad(axis_ranges[i][1]):
                #print("angle is greater than upper limit")
                out_of_range = True
                break
            else:
                out_of_range = False
                continue
        else:
            if angle < np.deg2rad(axis_ranges[i][0]):
                #print("angle is less than lower limit")
                out_of_range = True
                break
            else:
                out_of_range = False
                continue
    return out_of_range

def IK(T):
    #Global Configuration

    GC = np.array([[1, 1, 1], [-1, 1, 1], [1, 1, -1], [-1, 1, -1], [1, -1, 1], [-1, -1, 1], [1, -1, -1], [-1, -1, -1]])

    psi_angles = []
    positive_extreme = 90
    negative_extreme = -90
    step_size = 90
    for i in range(negative_extreme, positive_extreme + 1, step_size):
        psi_angles.append(i)
    psi_angles_radian = deg2rad(psi_angles)

    # FORWARD KINEMATICS _ --- 0 to 7 - base to end effector transformation matrix _


    # T07 = transformation(theta1, 7)

    T07 = T
    R07 = matrix(T07[:3, :3])
    P07 = matrix(T07[:3, 3])

    P02 = matrix([0, 0, d_bs]).T
    P24 = matrix([0, d_se, 0]).T
    P46 = matrix([0, 0, d_ew]).T
    P67 = matrix([0, 0, d_wf]).T

    P26 = P07 - P02 - dot(R07, P67)
    print("mag value is "+ str(mag(P26)))

    for i, g_cnfg in enumerate(GC):
        g_cnfg2 = g_cnfg[0];
        g_cnfg4 = g_cnfg[1];
        g_cnfg6 = g_cnfg[2]

        print("\n")
        for j, psi in enumerate(psi_angles_radian):
            k = (((mag(P26) ** 2) - (d_se ** 2) - (d_ew ** 2)) / (2 * d_se * d_ew))
            print(k)
            print(acos(k))
            theta4_v = g_cnfg4 * acos(k)
            """ virtual theta 1 """
            R01 = [[0], [0], [1]]
            alignment = mag(np.cross(P26, R01, axis=0))  # axis = 0 because R01 and P26 are column vectors
            if alignment > 0:
                theta1_v = math.atan2(P26[1:2], P26[0:1])
            elif alignment == 0:
                theta1_v = 0

            """calculating Phi for Virtual Theta 2 and Theta 3"""
            phi = math.acos(((d_se ** 2) + ((mag(P26)) ** 2) - (d_ew ** 2)) / (2 * d_se * (mag(P26))))
            theta2_v = math.atan2(math.sqrt((P26[0:1]) ** 2 + (P26[1:2]) ** 2), P26[2:3]) + (g_cnfg4 * phi)
            theta3_v = 0

            """virtual angles assemble"""
            theta_v = np.array([theta1_v, theta2_v, theta3_v, theta4_v])

            """INVERSE KINEMATICS"""
            P26_hat = P26 / mag(P26)
            P26_skew = skew(P26_hat)
            R03_v = transformation(theta_v, 3)[0:3, 0:3]

            As = np.matmul(P26_skew, R03_v)
            Bs = -1 * np.matmul((P26_skew ** 2), R03_v)
            Cs = np.matmul((np.matmul(P26_hat, P26_hat.T)), R03_v)

            R03 = (As * sin(psi)) + (Bs * cos(psi)) + Cs

            theta1_r = math.atan2(g_cnfg2 * ((As[1, 1] * sin(psi) + Bs[1, 1] * cos(psi) + Cs[1, 1])),
                                  (g_cnfg2 * ((As[0, 1] * sin(psi) + Bs[0, 1] * cos(psi) + Cs[0, 1]))))
            theta2_r = g_cnfg2 * math.acos((As[2, 1] * sin(psi)) + (Bs[2, 1] * cos(psi)) + Cs[2, 1])
            theta3_r = math.atan2(g_cnfg2 * ((-As[2, 2] * sin(psi)) - (Bs[2, 2] * cos(psi)) - Cs[2, 2]),
                                  (g_cnfg2 * ((-As[2, 0] * sin(psi)) - (Bs[2, 0] * cos(psi)) - Cs[2, 0])))
            theta4_r = theta4_v

            """real angles 1-4 """
            theta_r = np.array([theta1_r, theta2_r, theta3_r, theta4_r])

            R34 = DH(theta_r, 3)[0:3, 0:3]
            Aw = R34.T * As.T * R07
            Bw = R34.T * Bs.T * R07
            Cw = R34.T * Cs.T * R07

            R47 = Aw * sin(psi) + Bw * cos(psi) + Cw

            theta5_r = math.atan2((g_cnfg6 * (Aw[1, 2] * sin(psi) + Bw[1, 2] * cos(psi) + Cw[1, 2])),
                                  (g_cnfg6 * (Aw[0, 2] * sin(psi) + Bw[0, 2] * cos(psi) + Cw[0, 2])))
            theta6_r = g_cnfg6 * math.acos(Aw[2, 2] * sin(psi) + Bw[2, 2] * cos(psi) + Cw[2, 2])
            theta7_r = math.atan2((g_cnfg6 * (Aw[2, 1] * sin(psi) + Bw[2, 1] * cos(psi) + Cw[2, 1])),
                                  (g_cnfg6 * (- Aw[2, 0] * sin(psi) - Bw[2, 0] * cos(psi) - Cw[2, 0])))

            theta_r = np.append(theta_r, theta5_r)
            theta_r = np.append(theta_r, theta6_r)
            theta_r = np.append(theta_r, theta7_r)

            if range_check(theta_r):
                return False, np.rad2deg(theta_r)
                # print(str(np.rad2deg(psi)) + "  " + str(g_cnfg) + "  " + "no solution within joint limits")
            else:
                return True, np.rad2deg(theta_r)
                # print(str(np.rad2deg(psi)) + "  " + str(g_cnfg) + "  " + str(np.rad2deg(theta_r)))