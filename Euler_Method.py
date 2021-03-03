from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

def func(x, y):
    return (x + y )


# Function for euler formula
def euler(x0, y, h, x):
    temp = -0

    # Iterating till the point at which we
    # need approximation
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h

        # Printing approximation
    print("Approximate solution at x = ", x, " is ", "%.6f" % y)


# Driver Code
# Initial Values
x0 = 0
y0 = 1
h = 0.1

# Value of x at which we need approximation
x = 0.5

euler(x0, y0, h, x)
def f(y,x):
    return (x+y)
y0=xs=np.arange(0,0.5,0.1);
ys=odeint(f,y0,xs)
plt.plot(xs,ys,'-')
plt.plot(xs,ys, 'ro')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Differential eq: dy/dx=x+y,y(0)=1,xrange=[0,0.5]')
plt.show()