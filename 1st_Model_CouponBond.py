import numpy as np
import matplotlib.pyplot as plt

par_value = 5000
bond_duration = 10
bond_interest = 0.02

clean_price = [par_value, par_value]
years = 20
time = np.linspace(0, years - 1, num=years)
y = [0, 0]
for i in range(len(time)):
    clean_price.append(int(par_value*(1+bond_interest)))
    y.append(i+1)
    clean_price.append(int(par_value))
    y.append(i+1)
#clean_price.append(0)
y.append(len(y)/2-1)
y.pop()
clean_price.pop()
y.pop()
x = clean_price


interest_accrued = []
y2 = []
for i in range(len(time)+1):
    y2.append(i)
    interest_accrued.append(int(par_value*(bond_interest)*i))
x2 = interest_accrued

print(len(x2))
print(len(y))

plt.scatter(y, x, s=0)
plt.plot(y, x)

plt.scatter(y2, x2, s=0)
plt.plot(y2, x2)

plt.xlabel('Time, t')
plt.ylabel('ylabel')
plt.show()

#https://www.glynholton.com/notes/bond-accrued-interest/
#https://thismatter.com/money/bonds/bond-pricing.htm

'''
To change:
As per this image https://thismatter.com/money/bonds/images/bond-price-graph-accrued-interest.svg
Add axis names, add lines for coupon amount, flat price, caption for accruing interest and interest payment.
Change frequency of interest to 6 months rather than annualy.
'''