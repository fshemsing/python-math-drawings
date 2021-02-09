import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import mpl_toolkits.mplot3d as a3
from itertools import product

fig = plt.figure()
ax = a3.Axes3D(fig, xlim3d=[-1,1], ylim3d=[-1,1], zlim3d=[0,1])

def plane_field(x, y, z, h):
    """ generate the plane field for the standard contact structure on R^3 """
    plane_v1 = np.array([0, 1, 0])
    plane_v2 = np.array([1, 0, y])
    plane_v2 = plane_v2 / np.linalg.norm(plane_v2)

    p = np.array([x, y, z])

    tri1 = [p + (h/2) * ( plane_v1 + plane_v2),
            p + (h/2) * ( plane_v1 - plane_v2),
            p + (h/2) * (-plane_v1 + plane_v2)]
    
    tri2 = [p + (h/2) * ( plane_v1 - plane_v2),
            p + (h/2) * (-plane_v1 + plane_v2),
            p + (h/2) * (-plane_v1 - plane_v2)]

    return([tri1, tri2])

I = np.linspace(-1,1,7)
K = np.linspace(0,1,6)
polylist = []
for x, y, z in product(I, I, K):
    [tri1, tri2] = plane_field(x,y,z,0.1)
    polylist.append(tri1)
    polylist.append(tri2)

polys = a3.art3d.Poly3DCollection(polylist)
ax.add_collection3d(polys)
pl.show()
