import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns ds/dt
def model(y,t):
    k = 0
    r = 0.04
    dydt = k + r*y
    return dydt

def modelIAV(y,t):
    k = 0
    r = 0.04
    i = 0.02888
    dydt = k + r*y - i*y
    return dydt

# initial condition
y0 = 1000

# time points
t = np.linspace(0,10)

# solve ODE
y = odeint(model,y0,t)
y2 = odeint(modelIAV,y0,t)


# plot results

plt.plot(t,y)
plt.plot(t,y2)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()