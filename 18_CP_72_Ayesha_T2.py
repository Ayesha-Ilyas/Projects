#DETERMINANT OF MATRIX
def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(a):

	if(len(a) == 2):
		value = a[0][0] * a[1][1] - a[1][0] * a[0][1]
		return value


	Sum = 0

	for current_column in range(len(a)):

		sign = (-1) ** (current_column)

		sub_det = determinantOfMatrix(getcofactor(a, 0, current_column))

		Sum += (sign * a[0][current_column] * sub_det)


	return Sum

if __name__ == '__main__':
    a = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]


    print('Determinant of the matrix is :', determinantOfMatrix(a))

# 1 DETERMINANT OF TRANSPOSE OF MATRIX



def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(result):

	if(len(result) == 2):
		value = result[0][0] * result[1][1] - result[1][0] * result[0][1]
		return value


	Sum = 0

	for current_column in range(len(result)):

		sign = (-1) ** (current_column)

		sub_det = determinantOfMatrix(getcofactor(result, 0, current_column))

		Sum += (sign * result[0][current_column] * sub_det)


	return Sum

if __name__ == '__main__':
    x = [[1, 0, 2, -1],
         [3, 0, 0, 5],
         [2, 1, 4, -3],
         [1, 0, 5, 0]]

    result = [[0, 0, 0,  0],
              [0, 0, 0, 0 ],
              [0, 0, 0,  0],
              [0, 0, 0, 0]]

    # iterate through rows
    for i in range(len(x)):
        # iterate through columns
        for j in range(len(x[0])):
            result[j][i] = x[i][j]



    print('Determinant of transpose of matrix is :', determinantOfMatrix(result))

#2 DETERMINAT OF TRIANGULAR MATRIX

def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(a):

	if(len(a) == 2):
		value = a[0][0] * a[1][1] - a[1][0] * a[0][1]
		return value


	Sum = 0

	for current_column in range(len(a)):

		sign = (-1) ** (current_column)

		sub_det = determinantOfMatrix(getcofactor(a, 0, current_column))

		Sum += (sign * a[0][current_column] * sub_det)


	return Sum

if __name__ == '__main__':
    a = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 4, -3],
         [0, 0, 0, 1]]


    print('Determinant of the matrix is :', determinantOfMatrix(a))


# 3 DETERMINANT OF unity OF MATRIX

def Identity(size):
	for row in range(0, size):
		for col in range(0, size):

			# Here end is used to stay in same line
			if (row == col):
				print("1 ", end=" ")
			else:
				print("0 ", end=" ")
		print()

# Driver Code
size = 5
Identity(size)

# 4 DETERMINANT OF det(AB) = det(A)*det(B) OF MATRIX


#det(A)*det(B) OF MATRIX

def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
q=[]
def determinantOfMatrix(a):

	if(len(a) == 2):
		value = a[0][0] * a[1][1] - a[1][0] * a[0][1]
		return value


	Suma = 0

	for current_column in range(len(a)):

		sign = (-1) ** (current_column)

		sub_det = determinantOfMatrix(getcofactor(a, 0, current_column))

		Suma += (sign * a[0][current_column] * sub_det)


	return Suma

def determinantOfMatrix(b):
    if(len(b) == 2):
        value = b[0][0] * b[1][1] - b[1][0] * b[0][1]
        return value
    Sumb = 0
    for current_column in range(len(b)):
        sign = (-1) ** (current_column)
        sub_det = determinantOfMatrix(getcofactor(b, 0, current_column))
        Sumb += (sign * b[0][current_column] * sub_det)
    return Sumb

if __name__ == '__main__':

    b = [[1, 0, 2, -1],
         [7, 0, 0, 5],
         [5, 4, 4, -3],
         [2, 0, 5, 0]]

    a = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]


    print('Determinant of the a matrix is :', determinantOfMatrix(a))
    q.insert(0,determinantOfMatrix(a))
    print(q)

    print('Determinant of the a matrix is :', determinantOfMatrix(b))
    q.insert(1,determinantOfMatrix(b))
    print(q)
    mul = q[0] * q[1]
    print(" multiplication of a and b matrix after determinant", mul)

#  DETERMINANT OF det(AB)
# 4x4 matrix multiplication using Python3
# Function definition
def matrix_multiplication(M, N):
    # List to store matrix multiplication result
    R = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]

    for i in range(0, 4):
        for j in range(0, 4):

            print(R[i][j], end=" ")
        print("\n", end="")
        return R


# First matrix. M is a list
M = [[1, 0, 2, -1],
         [7, 0, 0, 5],
         [5, 4, 4, -3],
         [2, 0, 5, 0]]
# Second matrix. N is a list
N = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]



def getcofactor(m, i, j):
	return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(result):

	if(len(result) == 2):
		value = result[0][0] * result[1][1] - result[1][0] * result[0][1]
		return value


	Sum = 0

	for current_column in range(len(result)):

		sign = (-1) ** (current_column)

		sub_det = determinantOfMatrix(getcofactor(result, 0, current_column))

		Sum += (sign * result[0][current_column] * sub_det)


	return Sum

if __name__ == '__main__':
    result=matrix_multiplication(M, N)
    print('Determinant of ab matrix is :', determinantOfMatrix(result))

# Write a program for the manipulation of matrix such that addition, subtraction,
# multiplication for 3*3 and 4*4 Matrix. OF MATRIX

#Multiplication

def matrix_multiplication(M, N):
    # List to store matrix multiplication result
    R = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]

    for i in range(0, 4):
        for j in range(0, 4):

            print(R[i][j], end=" ")
        print("\n", end="")
        return R

    # First matrix. M is a list
M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
# Second matrix. N is a list

N = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]

if __name__ == '__main__':
    t=matrix_multiplication(M, N)
    print('multiplication is ', t)

#ADDITION OF 2 MATRIX

# Program to add two matrices using nested loop

X = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]

Y = [[1, 0, 2, -1],
         [7, 0, 0, 5],
         [5, 4, 4, -3],
         [2, 0, 5, 0]]

result = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print('ADDITION OF 2 MATRIX',r)

#SUBTRACTION OF 2 MATRIX


import numpy as np


# creating first matrix
A = np.array([[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]])

# creating second matrix
B = np.array([[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))


