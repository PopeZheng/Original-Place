import sys
def get_matrix():
	matrix = []
	rownum,columnnum = map(int,input().split())
	for row in range(rownum):
		current_list = []
		current_row = input().split()
		for column in current_row:
			current_list.append(float(column))
		matrix.append(current_list)
	return matrix
		
#Only for n by n-1 equation
'''def get_matrix():
	matrix = []
	matrix.append([])
	current_row = input().split()
	length = len(current_row) - 1
	for element in current_row:
		matrix[0].append(int(element))
	for row in range(length - 1):
		list1 = []
		current_row = input().split()
		for element in current_row:
			list1.append(int(element))
		matrix.append(list1)
	return matrix''' 

def print_matrix(matrix):
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			print(matrix[row][column],end = ' ')
		print()

#Gauss algorithm first step:elimination
def Gauss1_elimination(matrix):
	for row in range(len(matrix) - 1):
		while matrix[row][row] == 0:
			matrix[row],matrix[row+1] = matrix[row+1],matrix[row]
		for i in range(row +1,len(matrix)):
			divde = matrix[i][row] / matrix[row][row]
			for column in range(row,len(matrix[row+1])):
				matrix[i][column] -= matrix[row][column] * divde
	return matrix
	
#Gauss algorithm second step:substitution
def Gauss2_substitution(matrix):
	for row in range(len(matrix)-1,0,-1):
		if matrix[row][len(matrix[row]) - 1] == 0:
			for column in matrix[row]:
				if column != 0:
					print('-----------result-------------')
					print('No root')
					sys.exit(0)

		fine = False
		if matrix[row][len(matrix[row]) - 1] != 0:
			for j in range(len(matrix[row]) -1):
				if matrix[row][j] != 0:
					fine = True
			if not fine:
				print('-----------result-------------')
				print('No root')
				sys.exit(0)
				break
		if matrix[row][row] == 0:
			continue
		else:
			for i in range(row-1,-1,-1):
				divde = matrix[i][row] / matrix[row][row]
				for column in range(len(matrix[i])-1,row-1,-1):
					matrix[i][column] -= divde * matrix[row][column]
			for column in range(len(matrix[row]) - 1,row - 1, -1):
				matrix[row][column] /= matrix[row][row]
	for column in range(len(matrix[0]) - 1,-1,-1):
		matrix[0][column] /= matrix[0][0]
	return matrix

def main():
	 matrix1 = get_matrix()
	 matrix2 = Gauss1_elimination(matrix1)
	 matrix3 = Gauss2_substitution(matrix2)
	 print('-----------result-------------')
	 print_matrix(matrix3)


if __name__ == '__main__':
	main()

