import numpy as np


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
	R = int(input("Enter the number of rows:"))
	C = int(input("Enter the number of columns:"))

	print("Enter the entries in a single line (separated by space): ")

	# User input of entries in a
	# single line separated by space
	a = list(map(int, input().split()))

	# For printing the matrix
	matrix = np.array(a).reshape(R, C)
	print(matrix)

print('Determinant of the matrix is :', determinantOfMatrix(a))





