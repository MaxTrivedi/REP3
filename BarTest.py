from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


Par_Value = 1000


Capital_Increase = 0
Bond_Duration = 10
Repay_Freq = 1
Bond_Interest = 0.16/Repay_Freq

Value = [Par_Value]
Bars = []



for i in range(Bond_Duration*Repay_Freq):
    Value.append((Value[i]*(1+Bond_Interest)))
    Bars.append(str(i))
Bars.append(str(len(Value)))

'''


for i in range(Bond_Duration*Repay_Freq):
    Value.append((Value[0]+(i+1)*(Value[0]*Bond_Interest)))
    Bars.append(str(i))
Bars.append(str(len(Value)))
'''
y_pos = np.arange(len(Bars))

plt.bar(y_pos, Value)
plt.xticks(y_pos, Bars)






def model(y,t):
    global Capital_Increase
    global Bond_Interest
    k = Capital_Increase
    r = Bond_Interest
    dydt = k + r*y
    return dydt

# initial condition
y0 = Par_Value

# time points
t = np.linspace(0,10,5)

# solve ODE
y = odeint(model,y0,t)


# plot results

plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()













plt.show()