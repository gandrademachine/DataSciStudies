# This is a hardcode with only basic modules for a linear regression

import numpy as np
import matplotlib.pyplot as plt

class linear:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    def lstsqr(self):
        xdist = np.array([i-np.mean(self.x) for i in self.x])
        ydist = np.array([i-np.mean(self.x) for i in self.y])
        xdistsq = [(i-np.mean(self.x))**2 for i in self.x]
        a = np.sum(xdist*ydist)/np.sum(xdistsq)
        b = np.mean(self.y)-a*np.mean(self.x)
        print(a, b) 
        linearized = np.array([a*i+b for i in self.x])
        plt.plot(self.x,self.y,'.b',ms=3.5,label='Crude Data')
        plt.plot(self.x, linearized, 'r-.', label='Linearized')
        plt.xlabel("wealth")
        plt.ylabel("consumption")
        plt.title("Data got from Wikipedia for validation")
        plt.legend(loc='lower right')
x = [139, 126, 90, 144, 163, 136, 61, 62, 41, 120]  
y = [122, 114, 86, 134, 146, 107, 68, 117, 71, 98]   

lin = linear(x,y)
lin.lstsqr()
plt.show()
