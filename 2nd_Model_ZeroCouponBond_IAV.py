import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


Par_Value = 1000
Capital_Increase = 100
Bond_Duration = 10000
Bond_Interest = 0.04
i = 0.0321


# function that returns ds/dt
def model(y,t):
    global Capital_Increase
    global Bond_Interest
    k = Capital_Increase
    r = Bond_Interest
    dydt = k + r*y
    return dydt

def modelIAV(y,t):
    global Capital_Increase
    global Bond_Interest
    k = Capital_Increase
    r = Bond_Interest
    dydt = k + r*y - i*y
    return dydt


# initial condition
y0 = Par_Value

# time points
t = np.linspace(0,10,100)

# solve ODE
y = odeint(model, y0, t)
y2 = odeint(modelIAV, y0, t)

# plot results
plt.xlim((0,10))
plt.ylim((0,3000))

plt.plot(t,y, label ='Not Inflation Adjusted')
plt.plot(t,y2, label = 'Inflation Adjusted')

plt.legend(loc='lower right')

plt.xlabel('time')
plt.ylabel('y(t)')
x = np.linspace(0,10,100)

h1 = plt.hlines(y = 2720, xmin = 0, xmax= 10, linestyles = ':')
v1 = plt.vlines(x = 10, ymin = 0, ymax = 2720,linestyles = ':')

h2 = plt.hlines(y = 2115, xmin = 0, xmax= 10, linestyles = ':')



plt.plot(x, y, 'b', label = 'y=')
plt.grid()
plt.show()


#https://thismatter.com/money/bonds/bond-pricing.htm

'''
To do:
Label axis, bond price
Add line for par/face value & Maturity
Note discount price
https://qph.fs.quoracdn.net/main-qimg-170b2f89d5b9f229b7d5123b0c18feaf.webp
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.quora.com%2FHow-do-you-explain-the-%25E2%2580%259Csawtooth%25E2%2580%259D-pattern-in-coupon-bond-prices&psig=AOvVaw3cpYWLZjp-1ci0TtkTAzgw&ust=1582852499314000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCJCMzZrH8OcCFQAAAAAdAAAAABAP
'''
