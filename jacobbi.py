# 3x + 20y - z = -18
# 2x - 3y + 20z = 25
# 20x + y - 2z = 17
# Then they will be arranged like this:
#
# 20x + y - 2z = 17
# 3x + 20y -z = -18
# 2x - 3y + 20z = 25
# After arranging equations in diagonally dominant form, we form equations for x, y, & z like this:
#
# x = (17-y+2z)/20
# y = (-18-3x+z)/20
# z = (25-2x+3y)/20

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x ,y ,z: (10 + y - z ) /5
f2 = lambda x ,y ,z: (11 + 2 * x + z ) /8
f3 = lambda x ,y ,z: (3 +  x -  y ) /4

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0 ,y0 ,z0)
    y1 = f2(x0 ,y0 ,z0)
    z1 = f3(x0 ,y0 ,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1, y1, z1))
    e1 = abs(x0 - x1);
    e2 = abs(y0 - y1);
    e3 = abs(z0 - z1);

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))

# from pprint import pprint
# from numpy import array, zeros, diag, diagflat, dot
#
# def jacobi(A,b,N=25,x=None):
#     """Solves the equation Ax=b via the Jacobi iterative method."""
#     # Create an initial guess if needed
#     if x is None:
#         x = zeros(len(A[0]))
#
#     # Create a vector of the diagonal elements of A
#     # and subtract them from A
#     D = diag(A)
#     R = A - diagflat(D)
#
#     # Iterate for N times
#     for i in range(N):
#         x = (b - dot(R,x)) / D
#     return x
#
# A = array([[2.0,1.0],[5.0,7.0]])
# b = array([11.0,13.0])
# guess = array([1.0,1.0])
#
# sol = jacobi(A,b,N=25,x=guess)
#
# print "A:"
# pprint(A)
#
# print "b:"
# pprint(b)
#
# print "x:"
# pprint(sol)