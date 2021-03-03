# Euler method python program
def f(x, y):
    return x + y

# Euler method
def euler(x0, y0, xn, n):

    h = (xn - x0) / n

    print('\nSOLUTION')

    print('x0\ty0\tslope\tyn')

    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, slope, yn))

        y0 = yn
        x0 = x0 + h

    print('\nAt x=%.4f, y=%.4f' % (xn, yn))


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

euler(x0, y0, xn, step)

# code for error percentage:
# # error percentage = np.abs((actual - predicted) / actual).mean(axis=0) * 100
#
# this is for exact method
# # Sym y(x)
# # Ode=2*x*y*(diff(y)=(x^2)-(y^2))
# # Sol=dsolve(ode)