import math
import numpy as np
# parameter
import inline as inline
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

MAX_T = 100.0  # maximum time to the goal [s]
MIN_T = 5.0  # minimum time to the goal[s]


class QuinticPolynomial:

    def __init__(self, spx, svx, sax, epx, evx, eax, time):
        # calc coefficient of quintic polynomial
        # See jupyter notebook document for derivation of this equation.
        self.a0 = spx
        self.a1 = svx
        self.a2 = sax / 2.0

        A = np.array([[time ** 3, time ** 4, time ** 5],
                      [3 * time ** 2, 4 * time ** 3, 5 * time ** 4],
                      [6 * time, 12 * time ** 2, 20 * time ** 3]])
        b = np.array([epx - self.a0 - self.a1 * time - self.a2 * time ** 2,
                      evx - self.a1 - 2 * self.a2 * time,
                      eax - 2 * self.a2])
        x = np.linalg.solve(A, b)

        self.a3 = x[0]
        self.a4 = x[1]
        self.a5 = x[2]

    def calc_point(self, t):
        xt = self.a0 + self.a1 * t + self.a2 * t ** 2 + \
             self.a3 * t ** 3 + self.a4 * t ** 4 + self.a5 * t ** 5

        return xt

    def calc_first_derivative(self, t):
        xt = self.a1 + 2 * self.a2 * t + \
             3 * self.a3 * t ** 2 + 4 * self.a4 * t ** 3 + 5 * self.a5 * t ** 4

        return xt

    def calc_second_derivative(self, t):
        xt = 2 * self.a2 + 6 * self.a3 * t + 12 * self.a4 * t ** 2 + 20 * self.a5 * t ** 3

        return xt

    def calc_third_derivative(self, t):
        xt = 6 * self.a3 + 24 * self.a4 * t + 60 * self.a5 * t ** 2

        return xt


def quintic_polynomials_planner(pa, svx, svy, svz, sax, say, saz
                                , pb, evx, evy, evz, eax, eay, eaz, max_accel, max_jerk, dt):
    """
    quintic_polynomials_planner(pa[0],pa[1],pa[2], vxs,vys,vzs, axs,ays,azs,
                                                       pb[0],pb[1],pb[2], vxe,vye,vze, axe,aye,aze, max_accel, max_jerk, dt)
    quintic polynomial planner

    input
        s_x: start x position [m]
        s_y: start y position [m]
        s_yaw: start yaw angle [rad]
        sa: start accel [m/ss]
        epx: goal x position [m]
        epy: goal y position [m]
        gyaw: goal yaw angle [rad]
        ga: goal accel [m/ss]
        max_accel: maximum accel [m/ss]
        max_jerk: maximum jerk [m/sss]
        dt: time tick [s]

    return
        time: time result
        rx: x position result list
        ry: y position result list
        ryaw: yaw angle result list
        rv: velocity result list
        ra: accel result list



    vxs = sv * math.cos(syaw)
    vys = sv * math.sin(syaw)
    vxg = gv * math.cos(gyaw)
    vyg = gv * math.sin(gyaw)

    axs = sa * math.cos(syaw)
    ays = sa * math.sin(syaw)
    axg = ga * math.cos(gyaw)
    ayg = ga * math.sin(gyaw)
"""

    spx = pa[0];
    spy = pa[1];
    spz = pa[2]
    epx = pb[0];
    epy = pb[1];
    epz = pb[2]

    time, rx, ry, ryaw, rv, ra, rj = [], [], [], [], [], [], []

    for T in np.arange(MIN_T, MAX_T, MIN_T):
        xqp = QuinticPolynomial(spx, svx, sax, epx, evx, eax, T)
        yqp = QuinticPolynomial(spy, svy, say, epy, evy, eay, T)
        zqp = QuinticPolynomial(spz, svz, saz, epz, evz, eaz, T)

        time, rx, ry, rz, ryaw, rv, ra, rj = [], [], [], [], [], [], [], []
        # print("T = " + str(T))
        for t in np.arange(0.0, T + dt, dt):
            time.append(t)
            rx.append(xqp.calc_point(t))
            ry.append(yqp.calc_point(t))
            rz.append(zqp.calc_point(t))

            vx = xqp.calc_first_derivative(t)
            vy = yqp.calc_first_derivative(t)
            vz = zqp.calc_first_derivative(t)

            v = [vx, vy, vz]
            v = np.linalg.norm(v)
            rv.append(v)

            ax = xqp.calc_second_derivative(t)
            ay = yqp.calc_second_derivative(t)
            az = zqp.calc_second_derivative(t)
            a = [ax, ay, az]
            a = np.linalg.norm(a)

            if len(rv) >= 2 and rv[-2] - rv[-1] > 0.0:
                a *= -1
            ra.append(a)

            jx = xqp.calc_third_derivative(t)
            jy = yqp.calc_third_derivative(t)
            jz = zqp.calc_third_derivative(t)
            j = [jx, jy, jz]
            j = np.linalg.norm(j)

            if len(ra) >= 2 and ra[-1] - ra[-2] < 0.0:
                j *= -1
            rj.append(j)

        # rx = np.asarray(rx); ry = np.asarray(rx); rz = np.asarray(rx)

        if max([abs(i) for i in ra]) <= max_accel and max([abs(i) for i in rj]) <= max_jerk:
            print("find path!!")
            break

    return time, rx, ry, rz, rv, ra, rj


def main():
    print(__file__ + " start!!")
    show_animation = False
    start_row = 285
    end_row = 313
    datalog = np.genfromtxt('21_apr_21_exprmnt_pnts_2.csv', delimiter=',')
    datalog = datalog[start_row:end_row, :]
    pa = np.array(datalog[0])  # point A
    pb = np.array(datalog[-1])  # point B
    print("pa is: ", pa);
    print("pb is: ", pb)
    step_size = 0.05  # the time difference between each row of the datalog. 20rows/sec or 20 data points per second. so 1 row = 0.05 seconds
    start_vel = (np.subtract(datalog[1], datalog[0])) / 0.05  # 1 represents 1 second of time. vel = Dist/time
    row_s1 = datalog[0];
    row_e1 = datalog[-1]
    row_s2 = datalog[1];
    row_e2 = datalog[-2]
    row_s3 = datalog[2];
    row_e3 = datalog[-3]
    svx = (row_s2[0] - row_s1[0]) / 5  # position at (row2-row1)cms/50 milliseconds.
    svy = (row_s2[1] - row_s1[1]) / 5  # m/s
    svz = (row_s2[2] - row_s1[2]) / 5  # m/s
    evx = -(row_e2[0] - row_e1[0]) / 5  # m/s
    evy = -(row_e2[1] - row_e1[1]) / 5  # m/s
    evz = -(row_e2[2] - row_e1[2]) / 5  # m/s

    sax = ((row_s3[0] - row_s2[0]) / 5 - (row_s2[0] - row_s1[0]) / 5) / 10  # m/s^2
    say = ((row_s3[1] - row_s2[1]) / 5 - (row_s2[1] - row_s1[1]) / 5) / 10  # m/s^2
    saz = ((row_s3[2] - row_s2[2]) / 5 - (row_s2[2] - row_s1[2]) / 5) / 10  # m/s^2
    eax = ((row_e3[0] - row_e2[0]) / 5 - (row_e2[0] - row_e1[0]) / 5) / 10  # m/s^2
    eay = ((row_e3[1] - row_e2[1]) / 5 - (row_e2[1] - row_e1[1]) / 5) / 10  # m/s^2
    eaz = ((row_e3[2] - row_e2[2]) / 5 - (row_e2[2] - row_e1[2]) / 5) / 10  # m/s^2

    max_accel = 0.0815  # max accel [m/ss] #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815 #0.0815
    max_jerk = 0.1  # max jerk [m/sss]
    dt = 3  # time tick [s]

    time, x, y, z, v, row_s1, j = quintic_polynomials_planner(pa, svx, svy, svz, sax, say, saz,
                                                              pb, evx, evy, evz, eax, eay, eaz, max_accel, max_jerk, dt)

    # print("start vel ", start_vel)
    # # print("direction test", np.subtract(pa,pb))
    # # print("direction test", np.subtract(pb,pa))
    # direction = np.subtract(datalog[1], datalog[0])
    # print("direction ", direction)
    # print("distance ", np.linalg.norm(direction))
    # unit_vector = direction/np.linalg.norm(direction)
    # print("unit vector ", unit_vector)
    # velocity = (unit_vector)*start_vel
    # print(velocity)
    # print(datalog[0])
    # print(datalog[20])
    x = np.array(x);
    y = np.array(y);
    z = np.array(z);
    # print(np.stack((x,y,z), axis=-1))
    plot_points = np.stack((x, y, z), axis=-1)
    print(plot_points)
    print(plot_points.shape)
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    # ax.plot3D(x, y, zs=z, zdir='z', c='gray')
    ax.scatter(x, y, z, c='r')
    ax.scatter(datalog[:, 0], datalog[:, 1], datalog[:, 2], c='b')
    # ax.scatter(-340,287,604, c='g')
    # ax.scatter(-233,263, 789, c='y')
    # ax.contour3D(x,y,z, zdir=z, color='r')
    # ax.contour3D(datalog[:,0],datalog[:,1],datalog[:,2],zdir=z, color='b')
    plt.show()
    plt.savefig('exp_1_p3_two_p4.png')


def velocity(datalog):
    start_vel = datalog[0:20][20] - datalog[0:20][0]

    return None


if __name__ == '__main__':
    main()
