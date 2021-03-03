import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as plt
fig = plt.figure()
x = np.arange(10)
y = 3 * np.sin(x / 20 * np.pi)




# Define function to integrate
def f(x):
    return 1 / (1 + x ** 2)
    def integrand(x):
        return x ** (1 / 2)

    ans, err = quad(integrand, 1, 2)

    print(ans)
    return ans



# Implementing trapezoidal method
def trapezoidal(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    # Finding final integration value
    integration = integration * h / 2

    return integration

# Implementing Simpson's 1/3
def simpson13(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Finding final integration value
    integration = integration * h / 3

    return integration

# Simpson's 3/8 Rule

# Define function to integrate
def f(x):
    return 1 / (1 + x ** 2)


# Implementing Simpson's 3/8
def simpson38(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)

    # Finding final integration value\
    integration = integration * 3 * h / 8

    return integration


# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))
exc, err = quad(f, lower_limit, upper_limit)
print("The Exact result is %0.6f" % exc )

# Call trapezoidal() method and get result
result1 = trapezoidal(lower_limit, upper_limit, sub_interval)
trap_error = ((exc-result1)/exc)*100
plt.errorbar(x, y + 5, yerr=trap_error,label ='Line1')

print("Integration result by Trapezoidal method is: %0.6f" % (result1))

# Call trapezoidal() method and get result
result2 = simpson13(lower_limit, upper_limit, sub_interval)
simp13_error = ((exc-result2)/exc)*100
plt.errorbar(x, y + 5, yerr = simp13_error,uplims = True,label ='Line2')
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result2))

# Call trapezoidal() method and get result
result3 = simpson38(lower_limit, upper_limit, sub_interval)
simp38_error = ((exc-result3)/exc)*100
plt.errorbar(x, y + 5, yerr =simp38_error ,uplims = True,lolims = True,label ='Line3')
print("Integration result by Simpson's 3/8 method is: %0.6f" % (result3))

# Implementation of matplotlib function
#
#

plt.title('matplotlib.pyplot.errorbar()\
tra=blue,sim13=org,sim38=green')
plt.show()
