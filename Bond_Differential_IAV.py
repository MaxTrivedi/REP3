import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

Par_Value = float(input("Enter initial price of the bond:"))
print("£" + str(Par_Value))
if Par_Value == 0:
    Par_Value = 10000
    Capital_Increase = 10000
    Bond_Duration = 10
    Bond_Interest = 0.08
else:
    Capital_Increase = float(input("Enter yearly capital increase:"))

    Bond_Duration = int(input("Enter the duration of the bond(years):"))
    print(str(Bond_Duration)+" years")

    Bond_Interest = float(input("Enter interest rate of the bond(as %):"))
    Bond_Interest = Bond_Interest/100




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
    i = 0.02888
    dydt = k + r*y - i*y
    return dydt

# initial condition
y0 = Par_Value

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