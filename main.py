from manim import *
import numpy as np 
import random 
import math
import svg.path
import matplotlib.pyplot as plt

spline = "M18321.96 4983.72c-1081.39,-191.32 -1469.31,6584.41 -3452,5848.98 -3036.35,-1126.27 -6545.39,323.09 -7876.96,1350.3 273,-714 525,-1470 441,-2226 -63,-756 -525,-1533 -1260,-1743 -252,-63 -567,-63 -777,105 -210,168 -294,525 -105,714 168,168 462,168 651,21 189,-126 315,-336 420,-567 273,-609 399,-1302 378,-1974 -105,483 -504,861 -924,1113 -420,252 -903,420 -1344,651 -1323,735 -2226,2184 -2310,3717 210,84 462,42 630,-126 168,-168 168,-462 42,-651 -378,-42 -735,399 -672,798 63,378 441,651 819,777 378,105 777,84 1176,84 399,-21 798,0 1155,147 714,315 1029,1176 1071,1953 84,1449 -504,2835 -1092,4158 -63,-336 -441,-567 -777,-483 -336,84 -546,462 -462,777 147,525 903,630 1365,336 462,-294 693,-819 966,-1302 735,-1344 1848,-2478 3234,-3108 1386,-630 3066,-651 4410,42 1344,693 2310,2184 2226,3696 -147,-462 -924,-441 -1113,0 -189,441 147,840 630,945 462,105 966,-21 1239,-420 273,-399 357,-882 378,-1365 21,-483 -21,-966 21,-1449 84,-756 672,-1491 924,-2226 252,-714 315,-1470 231,-2226 -84,-756 -693,-1512 -1428,-1743 -252,-84 -546,-105 -798,21 -252,126 -420,378 -378,651 42,378 504,609 882,525 378,-84 672,-357 924,-651 1176,-1386 1134,-2163 147,-3654 -777,-1176 1616.39,-594.89 408.96,-2516.28z"
spline = "M920.41 12963.18c225.92,-204.89 1903.36,-3413.35 1789.4,-4128.2 -113.95,-714.85 -735.57,-1139.61 -569.81,217.56 165.77,1357.18 51.8,1875.18 207.21,3677.84 155.4,1802.67 393.68,2672.93 300.43,1626.54 -93.23,-1046.36 -580.16,-2123.83 -186.47,-3139.12 393.67,-1015.29 859.89,-1813.01 1419.34,-2217.06 559.45,-404.04 1750.87,196.84 652.67,507.65 -1098.16,310.8 -1056.71,0 -1512.55,973.86 -455.87,973.84 -497.3,953.11 -600.9,1263.92 -103.61,310.81 62.16,383.34 310.81,621.63 248.63,238.25 1854.45,1471.13 1875.17,1678.33 20.73,207.19 -310.81,631.95 -631.97,238.26 -321.16,-393.66 -642.33,-673.4 -1098.17,-1222.47 -455.84,-549.09 -745.93,-414.41 -352.24,-818.45 393.69,-404.04 3335.95,1398.6 3398.11,1823.37 62.17,424.76 942.78,694.12 1367.55,424.76 424.76,-269.36 486.92,-559.44 424.76,-1398.6 -62.17,-839.18 -72.52,-1367.55 -155.4,-2175.63 -82.88,-808.09 103.6,-1688.7 -341.89,-1978.79 -445.49,-290.08 -1191.42,-176.12 -1170.69,518.01 20.72,694.12 0,1201.77 41.45,2113.48 41.42,911.68 -165.78,1833.72 -93.26,2123.8 72.53,290.09 466.22,1564.39 2372.47,362.61 1906.27,-1201.77 1019.45,-2554.43 1094.97,-3940.66 75.55,-1386.22 37.29,-1286.27 500.42,-1425.74 463.12,-139.47 843.67,320.81 984.48,1088.24 140.82,767.43 100.61,2033.12 94.35,2947.48 -6.23,914.37 -300.31,1061.25 14.1,1499.46 314.42,438.18 1828.53,527 2109.39,360.99 280.83,-165.98 989.25,-3448.31 848.6,-4656.76 -140.61,-1208.43 60.96,-1636.13 -887.44,-1144.05 -948.37,492.08 -1576.05,434.5 -1028.21,1626.92 547.85,1192.45 690.17,1896.65 1228.24,1767.51 538.09,-129.15 511.58,-20.38 335.05,288.26 -176.53,308.64 -1771.99,1491.39 -1994.06,1701.51 -222.08,210.13 -923.31,299.51 -88.47,632.07 834.87,332.59 1108.3,335.63 2737.18,124.61 1628.9,-211.05 2600.77,-611.97 2797.48,105.5 196.68,717.44 -1346.48,917.82 -2620.4,1053.72 -1273.95,135.93 -10868.52,-360.82 -11622.1,-552.04 -753.6,-191.22 -1544.96,-1633.79 -1776.7,-1887.09 -253.91,-277.57 -228.04,-633.25 -172.9,-683.23z"
# spline = "M12069.34 19192.21c0,0 2446.81,-36.31 2517.62,-52.95 70.78,-16.66 136.57,-80.95 127.69,-451.1 -8.85,-370.15 -246.26,-4180.27 -246.26,-4180.27 0,0 32.22,-212.5 -288.54,-240.76 -320.77,-28.25 -1809.3,12.3 -1886.32,92.56 -77.02,80.23 34.84,133.61 167.4,172.49 132.56,38.88 1522.09,125.58 1641.68,82.48 119.56,-43.07 198,-15.96 266.71,-152.11 68.74,-136.16 124.68,-382.99 134.51,-626.89 9.83,-243.92 46.76,-874.75 23.49,-1033.77 -23.29,-159.02 36.24,-376.01 -486.79,-401.9 -523.01,-25.86 -1272.3,-23.52 -1370.97,-23.66 -98.69,-0.15 -141.46,-8.58 -185.14,266.54 -43.67,275.12 -53.44,280.48 -130.06,303.25 -76.59,22.77 -1782.69,-239.85 -2074.8,-238.18 -292.11,1.67 -1304.92,56.76 -1431.1,117.09 -126.18,60.34 -215.09,153.61 25.26,184.32 240.38,30.67 2270.01,110.86 2442.5,81.95 172.52,-28.88 411.95,-37.23 499.72,-70.61 87.74,-33.37 587.48,-47.96 -38.91,-589 -626.39,-541.04 -819.28,-656.21 -819.28,-656.21 0,0 -107.27,-127.67 -725.65,-119.32 -618.41,8.36 -991.35,-11.35 -1126.92,37.49 -135.56,48.86 -227.51,123.98 -372.99,303.3 -145.46,179.3 -390.3,612.35 -547.03,702.06 -156.73,89.71 -1090.96,50.78 -1639.9,-9.88 -548.95,-60.65 -2244.32,-96.22 -2398.26,-79.63 -153.91,16.58 -449.18,68.53 -536.03,-57.19 -86.81,-125.75 -193.31,-259.91 65.85,-311.19 259.18,-51.3 1374.58,-44.64 1585.18,-32.52 210.6,12.09 652.08,-0.65 626.74,155.03 -25.37,155.71 -188.33,415.51 -359.77,435.37 -171.42,19.85 -1263.7,23.99 -1415.04,21.97 -151.34,-2.02 -238.09,-46.24 -397.56,37.81 -159.47,84.05 -238.73,177.3 -278.34,353.76 -39.6,176.48 -21,616.86 -4.61,785.93 16.39,169.05 19.7,446.22 123.06,466.22 103.38,20 179.85,-39.53 188.5,-252.5 8.66,-212.97 -73.05,-813.72 102.18,-942.99 175.21,-129.24 295.6,-163.73 527.58,-182.79 231.94,-19.03 2511.63,-2.74 2700.18,4.42 188.53,7.16 361.54,44.39 407.31,192.87 45.77,148.49 135.58,663.2 95.5,788.42 -40.11,125.21 -97.62,335.21 -257.96,398.28 -160.37,63.08 -548.03,56.77 -558.5,405.96 -10.45,349.17 268.48,3564.89 187.93,3785.34 -80.54,220.45 -51.51,243.57 -193.97,321.73 -142.44,78.19 -2947.62,314.23 -2996.11,-308.02 -48.48,-622.24 -23.47,-3338.29 47.26,-3555.6 70.76,-217.31 -53.54,-604.39 725.98,-600.7 779.55,3.69 1798.28,11.65 1921.81,26.04 123.53,14.37 462.68,-40.48 547.75,510.56 85.07,551.02 173.29,1852.38 198.28,1947.05 24.99,94.68 -57.66,359.05 349.84,449.81 407.51,90.73 527.9,95.32 665.27,34.99 137.38,-60.36 212.22,88.59 304.38,-297.74 92.13,-386.33 26.94,-673.5 127.27,-916.53 100.32,-243.02 53.25,-254.94 201.33,-399.77 148.07,-144.86 313.58,-100.71 489.08,-76 175.51,24.72 607.59,53.08 785.19,309.69 179.6,259.51 374.88,501.96 447.91,524.06 73.03,22.1 107.52,-24.02 80.16,-182.89 -27.36,-158.87 -5.06,-194.06 -165.21,-459.88 -87.94,-145.98 -97.74,-177.93 -413.12,-326.1 -114.42,-53.75 -253.89,-69.94 -335.82,-78.94 -81.93,-8.98 -272.16,-3.49 -344.81,-13.94 -72.65,-10.45 -191.35,-25.64 -241.65,-65.97 -50.31,-40.33 76.02,-117.42 188.3,-143.24 112.28,-25.84 443.55,-90.43 724.21,4.19 280.63,94.6 412.24,89.14 671.78,429.33 259.5,340.22 238.93,459.84 239.9,632.4 0.97,172.57 -26.31,1039.98 -350.32,1289.56 -324,249.56 -1146.9,677.15 -1810.75,-32.69 -663.82,-709.84 -446.16,-1357.88 -421.52,-1555.71 20.65,-165.7 413.22,-996.06 1112.03,-1197.23 278.42,-80.16 544.54,-3.49 869.86,104.05 562.34,185.94 1246.99,819.73 1297.52,2006.79 50.53,1187.03 -1566.3,2762.14 -3306.12,1582.06 -1739.84,-1180.04 -885.17,-3102.33 -655.84,-3402.84 229.35,-300.51 1060.68,-1052.9 1929.86,-1065.77 869.19,-12.87 1004.52,-142.41 1969.2,851.95 964.66,994.37 805.84,2459.36 598.63,2693.68 -207.18,234.32 -450.16,1119.07 -1501.24,1371.99 -1051.07,252.93 145.41,165.44 601.18,169.8 440.68,4.21 762.64,-49.66 762.64,-49.66z"

frame_scale = 2
scale = 0.0012
time_scale = 5
number_of_points = 1000 # number of points to calculate scalar product
number_of_components = 30 # number of components to use in fourier series

config.frame_height = 8 * frame_scale
config.frame_width = 14.22 * frame_scale

# calculate scalar product of two functions 
def scalar_product(f, g, number_of_points):
    x = np.linspace(0, 1, number_of_points)
    dx = x[1] - x[0]
    return np.dot(f(x), g(x)) * dx

def fourier_exp(func, number_of_points, N):
    c = []
    for i in range(-N, N + 1):
        exp = lambda x: np.e ** (-1j * 2 * np.pi * i * x)
        c.append((scalar_product(func, exp, number_of_points), i))
    return c

def spline_decomposition(spline, scale, number_of_points, number_of_components):
    path = svg.path.parse_path(spline)
    path_func = np.vectorize(lambda t: path.point(t) * scale)

    c = fourier_exp(path_func, number_of_points, number_of_components)
    return c

def get_length_and_start_proportion(c):
    length = np.sqrt(c.real ** 2 + c.imag ** 2)
    prop = math.atan2(-c.imag, c.real) 
    if prop < 0: prop += 2 * math.pi
    prop /= 2 * math.pi
    return length, prop


def fourier_exp_func(c, N):
    return lambda x: sum([c[i + len(c) // 2][0] * np.e ** (1j * 2 * np.pi * i * x)  for i in range(-N, N + 1)])

def fourierise_exp(func, number_of_points, N):
    c = fourier_exp(func, number_of_points, N)
    return fourier_exp_func(c, N)

# show the original spline and its fourier series

# path = svg.path.parse_path(spline)
# path_func = np.vectorize(lambda t: path.point(t) * scale)
# f = fourierise_exp(path_func, number_of_points, number_of_components)

# x = np.linspace(0, 1, number_of_points)
# plt.figure()
# plt.plot(path_func(x).real, -path_func(x).imag)

# plt.figure()
# plt.plot(f(x).real, -f(x).imag)

# plt.show()

# exit(0)



class RotatingCircle(Circle):
    def __init__(self, radius, frequency, initial_dot_position, parent, **kwargs):
        super().__init__(radius=radius, **kwargs)
        self.parent = parent
        self.frequency = frequency
        self.dot_position = initial_dot_position

        if parent is not None:
            self.move_to(parent.point_from_proportion(parent.dot_position % 1))


class DotOnCircle(Dot):
    def __init__(self, inner_circle, **kwargs):
        super().__init__(**kwargs)
        self.inner_circle = inner_circle

        if inner_circle is not None:
            self.move_to(inner_circle.point_from_proportion(inner_circle.dot_position % 1))
    

class VectorInCircle(Arrow):
    def __init__(self, inner_circle, **kwargs):
        super().__init__(start=inner_circle.get_center(), end=inner_circle.point_from_proportion(inner_circle.dot_position % 1))
        self.inner_circle = inner_circle


class Drawing(ZoomedScene):
    def construct(self):

        num = MathTex(f'N = {number_of_components}', color=WHITE).to_corner(UL).scale(2)
        self.add(num)

        self.camera.frame.set(width=15 * frame_scale)

        def rotating_circle_updater(circle, dt):
            circle.dot_position += (dt * circle.frequency) # change on circle dot position 
            if circle.parent is not None:
                circle.move_to(circle.parent.point_from_proportion(circle.parent.dot_position % 1)) # move center to parent circle dot position 

        def dot_on_circle_updater(dot, dt):
            if dot.inner_circle is not None:
                dot.move_to(dot.inner_circle.point_from_proportion(dot.inner_circle.dot_position % 1))

        def vector_in_circle_updater(vector, dt):
            vector.put_start_and_end_on(vector.inner_circle.get_center(), vector.inner_circle.point_from_proportion(vector.inner_circle.dot_position % 1))


        coefficients = spline_decomposition(spline, scale, number_of_points, number_of_components)
        coefficients.sort(key=lambda x: np.sqrt(x[0].real ** 2 + x[0].imag ** 2), reverse=True) # sort by length
        # coefficients.sort(key=lambda x: x[1]) # sort by frequency 

        components = []

        for coefficient in coefficients:
            r, a = get_length_and_start_proportion(coefficient[0])
            n = coefficient[1] / time_scale
            if n == 0: continue

            c = RotatingCircle(r, n, a, components[-1][0] if len(components) > 0 else None, color=WHITE, stroke_width=0.5)
            # d = DotOnCircle(c, color=BLUE)
            v = VectorInCircle(c, color=WHITE)

            c.add_updater(rotating_circle_updater)
            # d.add_updater(dot_on_circle_updater)
            v.add_updater(vector_in_circle_updater)

            components.append([c, v])

        for i in range(len(components)):
            self.add(components[i][0], components[i][1])
            

        trace = TracedPath(components[-1][1].get_end, stroke_color=BLUE, stroke_width=5, dissipating_time=4.8)
        self.add(trace)

        self.wait(10) 
