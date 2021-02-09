import numpy as np
import matplotlib.pyplot as plt

def newton(w, h, iters):
    """Plot basins of attraction for Newton's method."""
    def f(x):  return x**3 - 1
    def df(x): return 2*x**2

    x, y = np.ogrid[ -2:2:h*1j,
                     -2:2:w*1j ]
    z = x + y*1j
    basins = np.zeros(z.shape, dtype=int)

    w = [1,
         np.exp(np.pi*1j / 3),
         np.exp(2*np.pi*1j / 3)]

    for i in range(iters):
        z = z - f(z)/df(z)

    w_dists  = [(z - wi) * np.conj(z - wi) for wi in w]
    w2_basin = (w_dists[1] >= w_dists[0]) & (w_dists[1] >= w_dists[2])
    w3_basin = (w_dists[2] >= w_dists[0]) & (w_dists[2] >= w_dists[1])

    basins[w2_basin] = 5
    basins[w3_basin] = 10
    
    return(basins)

plt.imshow(newton(1024, 1024, 20))
plt.show()
