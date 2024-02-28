from manim import *
import numpy as np 
import random 
import math
import svg.path
import matplotlib.pyplot as plt

spline = "M18321.96 4983.72c-1081.39,-191.32 -1469.31,6584.41 -3452,5848.98 -3036.35,-1126.27 -6545.39,323.09 -7876.96,1350.3 273,-714 525,-1470 441,-2226 -63,-756 -525,-1533 -1260,-1743 -252,-63 -567,-63 -777,105 -210,168 -294,525 -105,714 168,168 462,168 651,21 189,-126 315,-336 420,-567 273,-609 399,-1302 378,-1974 -105,483 -504,861 -924,1113 -420,252 -903,420 -1344,651 -1323,735 -2226,2184 -2310,3717 210,84 462,42 630,-126 168,-168 168,-462 42,-651 -378,-42 -735,399 -672,798 63,378 441,651 819,777 378,105 777,84 1176,84 399,-21 798,0 1155,147 714,315 1029,1176 1071,1953 84,1449 -504,2835 -1092,4158 -63,-336 -441,-567 -777,-483 -336,84 -546,462 -462,777 147,525 903,630 1365,336 462,-294 693,-819 966,-1302 735,-1344 1848,-2478 3234,-3108 1386,-630 3066,-651 4410,42 1344,693 2310,2184 2226,3696 -147,-462 -924,-441 -1113,0 -189,441 147,840 630,945 462,105 966,-21 1239,-420 273,-399 357,-882 378,-1365 21,-483 -21,-966 21,-1449 84,-756 672,-1491 924,-2226 252,-714 315,-1470 231,-2226 -84,-756 -693,-1512 -1428,-1743 -252,-84 -546,-105 -798,21 -252,126 -420,378 -378,651 42,378 504,609 882,525 378,-84 672,-357 924,-651 1176,-1386 1134,-2163 147,-3654 -777,-1176 1616.39,-594.89 408.96,-2516.28z"
# spline = "M2632.82 1761.02c0,0 581.03,-78.52 1429.02,675.25 847.99,753.77 -282.66,1303.4 -141.33,502.52 141.33,-800.88 1287.69,-1224.88 1287.69,-1224.88 0,0 1570.36,-581.03 1381.91,847.99 -188.45,1429.02 -1491.83,3706.03 -2151.38,3517.59 -659.55,-188.44 -4444.1,-3957.29 -1805.91,-4318.47z"

frame_scale = 2
scale = 0.0008
time_scale = 5
number_of_points = 1000 # number of points to calculate scalar product
number_of_components = 40 # number of components to use in fourier series

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
'''
path = svg.path.parse_path(spline)
path_func = np.vectorize(lambda t: path.point(t) * scale)
f = fourierise_exp(path_func, number_of_points, number_of_components)

x = np.linspace(0, 1, number_of_points)
plt.figure()
plt.plot(path_func(x).real, -path_func(x).imag)

plt.figure()
plt.plot(f(x).real, -f(x).imag)

plt.show()

exit(0)
'''


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
