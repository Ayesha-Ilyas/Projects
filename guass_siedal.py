# This
# program
# implements
# Gauss
# Seidel
# Iteration
# Method
# for solving systems of linear equation in python programming language.
# In
# Gauss
# Seidel
# method, we
# first
# arrange
# given
# system
# of
# linear
# equations in diagonally
# dominant
# form.For
# example,
# if system of linear equations are:
#
# 3
# x + 20
# y - z = -18
# 2
# x - 3
# y + 20
# z = 25
# 20
# x + y - 2
# z = 17
# Then
# they
# will
# be
# arranged
# like
# this:
#
# 20
# x + y - 2
# z = 17
# 3
# x + 20
# y - z = -18
# 2
# x - 3
# y + 20
# z = 25
# After
# arranging
# equations in diagonally
# dominant
# form, we
# form
# equations
# for x, y, & z like this:
#
# x = (17 - y + 2z) / 20
# y = (-18 - 3x+z) / 20
# z = (25 - 2x+3y) / 20
# These
# equations
# are
# defined
# later in Gauss
# Seidel
# python
# program
# using
# lambda expression.
#
# Python
# Source
# Code: Gauss
# Seidel
# Method

# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x, y, z: (17 - y + 2 * z) / 20
f2 = lambda x, y, z: (-18 - 3 * x + z) / 20
f3 = lambda x, y, z: (25 - 2 * x + 3 * y) / 20

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
    e1 = abs(x0 - x1);
    e2 = abs(y0 - y1);
    e3 = abs(z0 - z1);

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
# Python
# Program
# Output: Gauss
# Seidel
# Method
# Enter
# tolerable
# error: 0.0001
#
# Count
# x
# y
# z
#
# 1
# 0.8500 - 1.0275
# 1.0109
#
# 2
# 1.0025 - 0.9998
# 0.9998
#
# 3
# 1.0000 - 1.0000
# 1.0000
#
# 4
# 1.0000 - 1.0000
# 1.0000
#
# Solution: x = 1.000, y = -1.000 and z = 1.000
