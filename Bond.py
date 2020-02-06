#For a Zero Coupon Bond (A bond with compound interest) and yield to maturity = rate of return
#Par Value = Original investment / face value of bond
#
import matplotlib.pyplot as plt

Par_Value = float(input("Enter initial price of the bond:"))
print("£" + str(Par_Value))


Bond_Duration = int(input("Enter the duration of the bond(years):"))
if Bond_Duration == '':
    Bond_Duration = 10
print(str(Bond_Duration)+" years")

Bond_Interest = float(input("Enter interest rate of the bond(as %):"))

Bond_Interest = Bond_Interest / 100
Maturity_Value = Par_Value * (1 + Bond_Interest)**Bond_Duration

print("Maturity value is £" + str(round(Maturity_Value,2)))

#Prints bond value for every year
i=0
x = []
y = []
while i <= Bond_Duration:
    Value_i = Par_Value * (1+ Bond_Interest)**i
    print("Value at year " + str(i) + ": " + str(round(Value_i,2)))
    i += 1
    x.append(int(i))
    y.append(int(Value_i))

if Bond_Duration == 3:
    Inflation_Adjusted_Value = Maturity_Value / 1.07
elif Bond_Duration == 5:
    Inflation_Adjusted_Value = Maturity_Value / 1.12
elif Bond_Duration == 10:
    Inflation_Adjusted_Value = Maturity_Value / 1.32
elif Bond_Duration == 20:
    Inflation_Adjusted_Value = Maturity_Value / 1.73

print("Inflation adjusted value: £" + str(round(Inflation_Adjusted_Value,2)))

plt.xlabel("Years")
plt.ylabel("Value")
for i in range(len(y)):
    plt.plot(x,[pt for pt in y])
plt.show()
