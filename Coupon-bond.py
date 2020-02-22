import numpy as np
import matplotlib.pyplot as plt

par_value = 10000
capital_increase = 10000
bond_duration = 10
bond_interest = 0.02

clean_price = [par_value, par_value]
years = 20
time = np.linspace(0, years, num=years+1)
y = [0, 0]
for i in range(len(time)):
    clean_price.append(int(par_value*(1+bond_interest)))
    y.append(i+1)
    clean_price.append(int(par_value))
    y.append(i+1)
clean_price.append(0)
y.append(len(y)/2-1)
x = clean_price

plt.scatter(y, x, s=0)
plt.plot(y, x)
plt.show()
