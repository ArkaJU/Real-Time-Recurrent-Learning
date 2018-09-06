import numpy as np
from math import sin
from scipy.integrate import odeint
from numpy import linspace
class plant:
    def __init__(self):
        return
    
    def helicopter(self, y, t, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, u0, u1):
        x, y1, y2, z1, z2 = y
        #u0 = np.real(a10*x**2*sin((2*a2*a7 - a4*x**2 + x*(4*a3*a2**2*x**2 - 4*a1*a2*a4*x**2 - 4*a7*a2*a4 + a4**2*x**2)**0.5 + 2*a1*a2*x**2)/(2*a2**2*x**2)) - a8*x - a9*x**2 - a11)                     
        #u1 = np.real((a13*(x*(4*a3*a2**2*x**2 - 4*a1*a2*a4*x**2 - 4*a6*a2*a4*y2**2 - 4*a5*a2*a4*y2 - 4*a7*a2*a4 + a4**2*x**2)**0.5 + 2*a2*a7 - a4*x**2 + 2*a2*a5*y2 + 2*a1*a2*x**2 + 2*a2*a6*y2**2))/(2*a2**2*x**2) - a14*x**2*sin(z1) - a12)
        dydt = [a8 * x + a10 * (x ** 2) * sin(z1) + a9 * (x ** 2) + a11 + u0 , y2, (x**2) * (a1 + a2 * z1 - (a3 + a4 * z1)**(1 / 2)) + a5 * y2 + a6 * (y2**2) + a7, z2, a13 * z1 + a14 * (x ** 2) * sin(z1) + a15 * z2 + a12 + u1]
        return dydt

    def Predict(self, x):
        t = linspace(0, 0.0002, 5000)
        a1 = 5.19791e-4 
        a2 = 1.51992e-2 
        a3 = 2.70183e-7 
        a4 = 1.58009e-5 
        a5 = -0.1 
        a6 = -0.1 
        a7 = -17.67 
        a8 = -0.7 
        a9 = -0.0028 
        a10 = -0.0028 
        a11 = -13.92 
        a12 = 434.88 
        a13 = -800 
        a14 = -0.1
        a15 = -65
        u0, u1 = x[5:]
        sol = odeint(self.helicopter, x[:5], t, args=(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, u0, u1))
        end = len(sol)
        sol[end-1]=np.real(sol[end-1])
        if sol[end-1,0] < 74.25:
            sol[end-1,0] = 74.25

        if sol[end-1,0] > 180:
            sol[end-1,0] = 180

        if sol[end-1,1] < 0:
            sol[end-1,1] = 0.00001

        if sol[end-1,1] > 2:
            sol[end-1,1] = 2

        if sol[end-1,2] < -2.85:
            sol[end-1,2] = -2.85

        if sol[end-1,2] > 5.70:
            sol[end-1,2] = 5.70

        if sol[end-1,3] < (1.75 * 10 ** (-2)):
            sol[end-1,3] = (1.75 * 10 ** (-2))

        if sol[end-1,3] > (2.45 * 10 ** (-1)):
            sol[end-1,3] = (2.45 * 10 ** (-1))

        if sol[end-1,4] < -9.52:
            sol[end-1,4] = -9.52

        if sol[end-1,4] > 9.52:
            sol[end-1,4] = 9.52
        
        return sol[end-1]
        