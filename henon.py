import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Henon():
    def __init__(self, h, a = 1.4, b = 0.3):
        self.h, self.a, self.b = h, a, b
        self.fig, self.ax = plt.subplots()
        self.x, self.y = np.mgrid[-1:1:(self.h)*1j,
                                  -1:1:(self.h)*1j]
        # plot initial square invisibly to initialize Line2D objects
        self.plot = plt.plot(self.x, self.y, 'k.', linewidth = 0, markersize = 1)
        self.ax.set_visible(False)
        
    def init(self):
        self.x, self.y = np.mgrid[-1:1:(self.h)*1j,
                                  -1:1:(self.h)*1j]
        self.ax.set_xlim(-2,2)
        self.ax.set_ylim(-1,1)
        self.ax.set_visible(True)
        
    def update(self, frame):
        if frame != 0:
            x_tmp = self.x
            self.x = np.ones_like(x_tmp) - self.a*x_tmp**2 + self.y
            self.y = self.b*x_tmp
        # update every Line2D object with data for current iteration
        for (x,y,ln) in zip(self.x, self.y, self.plot):
            ln.set_data(x,y)
        return self.plot

obj = Henon(500)
ani = FuncAnimation(obj.fig, obj.update, frames = 10,
                    interval=500, init_func = obj.init, blit = False)
plt.show()
