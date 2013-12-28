#!/usr/bin/python

# Project Euler
# Problem 144
# Investigating multiple reflections of a laser beam

import numpy as np
import matplotlib.pyplot as p
from math import sqrt as s

from scipy.optimize import fsolve as fs

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

def get_y_int_from_slope(p, m):
    return p[1] - m*p[0]

def find_line_int(A, B):
    [x, y] = np.linalg.solve([[-A[0], 1], [-B[0], 1]], \
                                  [A[1], B[1]])
    return np.array([x, y])

# Rinse and repeat:
k = 1
while True:
    # Reflect line
    # Find the tangent:
    m_tan = -4 * laser[-1, 0]/laser[-1, 1]
    m_perp = -1 / m_tan
    #print 'Tangent at intersection: {}, normal:{}'.format(m_tan, m_perp)

    y_tan = get_y_int_from_slope(laser[-2, :], m_tan)
    y_perp = get_y_int_from_slope(laser[-1, :], m_perp)

    #print 'y-ints: tan: {}, perp: {}'.format(y_tan, y_perp)

    # Solve for intersection.
    p_int = find_line_int([m_tan, y_tan], [m_perp, y_perp])
    #print p_int, laser[-2, :]

    v = p_int - laser[-2, :]
    p_ref = p_int + v

    p_dir = p_ref - laser[-1, :]

    [m, y0] = get_eqn(laser[-1, :], p_ref)
    x0 = fs(lambda x : [m*x[0] + y0 - x[1], 4*x[0]**2 + x[1]**2 - 100], \
                laser[-1, :] + 10 * p_dir)

    # If intersection is at top between -.01 and .01, then exit
    if x0[0] <= .01 and x0[0] >= -.01 and x0[1] > 0:
        break
    k += 1

    laser = np.append(laser, [x0], axis=0)
print '{} bounces!'.format(k)

#print laser
p.plot(x, y)
p.plot(laser[:, 0], laser[:, 1])
#p.plot([-10., 10.], [m_tan*-10. + y_tan, m_tan*10. + y_tan])
#p.plot([-10., 3.], [m_perp*-10. + y_perp, m_perp*3. + y_perp])
#p.plot([laser[-2, 0], p_ref[0]], [laser[-2, 1], p_ref[1]])
#p.plot([laser[-1, 0], x0[0]], [laser[-1, 1], x0[1]])
p.axis('equal')

p.show()
