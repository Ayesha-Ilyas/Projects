import matplotlib.pyplot as plt
from scipy.integrate import quad
# Define function to integrate
def f(x):
    return  x **(1/2)

    def integrand(x):
        return x ** (1 / 2)

    ans, err = quad(integrand, 1, 2)

    print(ans)
    return ans

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




# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

exc, err = quad(f, lower_limit, upper_limit)

print("The Exact result is %0.6f" % exc )


# Call trapezoidal() method and get result
simp = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (simp))
simp_error = ((exc-simp)/exc)*100
print("Percentage Error is: %0.6f" % (simp_error) )

tarp = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (tarp) )
tarp_error = ((exc-tarp)/exc)*100
print("Percentage Error is: %0.6f" % (tarp_error) )


Method = ['Exact', 'Trapeziodal','simpsons 1/3']
value = [exc,tarp,simp]

plt.bar(Method,value)
plt.title('Analysis of Exact Method with Trapeziodal and Simpsons')
plt.xlabel('Methods')
plt.ylabel('values')
plt.show()
