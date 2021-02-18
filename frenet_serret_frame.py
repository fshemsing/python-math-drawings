import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3

def knot(p,q,t):
    r = np.cos(q*t) + np.full_like(t,2)
    x = r*np.cos(p*t)
    y = r*np.sin(p*t)
    z = -np.sin(q*t)
    return (x,y,z)

def cdiff(f):
    df = np.zeros_like(f)
    for n in range(len(f)):
        h = np.pi
        i1 = np.mod(n+1,len(f))
        i2 = np.mod(n-1,len(f))
        df[n] = (f[i1] - f[i2])/(2*h)
    return df

def normalize(v):
    return v / np.linalg.norm(v)

def fs_frame(x,y,z):
    tx, ty, tz = [], [], []
    nx, ny, nz = [], [], []
    bx, by, bz = [], [], []
    for dx,dy,dz in zip(cdiff(x), cdiff(y), cdiff(z)):
        [x,y,z] = normalize([dx,dy,dz])
        tx.append(x)
        ty.append(y)
        tz.append(z)
    for x, y, z in zip(cdiff(tx), cdiff(ty), cdiff(tz)):
        [x,y,z] = normalize([x,y,z])
        nx.append(x)
        ny.append(y)
        nz.append(z)
    for x1,y1,z1,x2,y2,z2 in zip(tx,ty,tz,nx,ny,nz):
        [x,y,z] = normalize(np.cross([x1,y1,z1],[x2,y2,z2]))
        bx.append(x)
        by.append(y)
        bz.append(z)
    return (tx,ty,tz,nx,ny,nz,bx,by,bz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

m = 1000
I = np.linspace(0, 2*np.pi, m)[:-1]
(x,y,z) = knot(2, 3, I)
ax.plot(x,y,z)

r = 0.2
skip = m / 100

tx,ty,tz,nx,ny,nz,bx,by,bz = fs_frame(x,y,z)
for px,py,pz,tx,ty,tz,nx,ny,nz,bx,by,bz in zip(x[::skip],y[::skip],z[::skip],
                                               tx[::skip],ty[::skip],tz[::skip],
                                               nx[::skip],ny[::skip],nz[::skip],
                                               bx[::skip],by[::skip],bz[::skip]):

    ax.plot([px,px+r*tx],[py,py+r*ty],[pz,pz+r*tz],'r-')
    ax.plot([px,px+r*nx],[py,py+r*ny],[pz,pz+r*nz],'b-')
    ax.plot([px,px+r*bx],[py,py+r*by],[pz,pz+r*bz],'g-')

plt.show()
