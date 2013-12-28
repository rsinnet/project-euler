#!/usr/bin/python

# Project Euler
# Problem 144
# Investigating multiple reflections of a laser beam

# unsolved

import numpy as np
import matplotlib.pyplot as p
from math import sqrt as s

w = np.linspace(-5, 5, 300)
z = map(lambda x : s(100 - 4*x**2), w)

x = np.concatenate((w, np.fliplr([w]).flatten()))
y = np.concatenate((z, np.fliplr([[-v for v in z]]).flatten()))

laser = np.array([[0., 10.1]])
laser = np.concatenate((laser, np.array([[1.4, -9.6]])))

def get_eqn(p0, p1):
    [m, y0] = np.linalg.solve([[p0[0], 1], [p1[0], 1]], \
                                  [p0[1], p1[1]])
    return [m, y0]

def find_intersection():
    # find the intersection of a line and the ellipse
    return False

# Get equation.
[m, y0] = get_eqn(laser[0, :], laser[1, :])

# Rinse and repeat:
# Reflect line
print 'Tangent at intersection: {}, normal:{}'.format(\
    -4 * laser[1, 0]/laser[1, 1], 1/(-4 * laser[1, 0]/laser[1, 1]))


# Solve for intersection.

# If intersection is at top between -.01 and .01, then exit

p.plot(x, y)
p.plot(laser[:, 0], laser[:, 1])
p.axis('equal')
p.show()
