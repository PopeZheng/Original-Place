import random
#Use entered num to decide the multidimensional list、
def get_matrix():
	matrix = []
	row_num = int(input('Row number:'))
	column_num = int(input('Column number:'))
	for i in range(row_num):
		current_list = []
		for j in range(column_num):
			current_list.append(int(input('Enter the element:')))
		matrix.append(current_list)
	return matrix

#print each element in the multidimensional list
def print_each(matrix):
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			print(matrix[row][column],end = ' ')

#get the sum of all element in the multidimensional list
def sum(matrix):
	total = 0
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			total += matrix[row][column]
	return total

#get the sum of each column in the multidimensional list
def sum_column(matrix):
	sum_column_list = []
	for column in range(len(matrix[0])):
		total = 0
		for row in range(len(matrix)):
			total += matrix[row][column]
		sum_column_list.append(total)
	return sum_column_list

def sumMajorDiagonal(matrix):
	total = 0
	for row in range(len(matrix)):
		total += matrix[row][row]
	return total

#get row which has the max sum and the sum
def maxsum_row(matrix):
	max_rowsum = 0
	total_list = []
	maxrow_list = []
	for row in range(len(matrix)):
		total = 0
		for column in range(len(matrix[row])):
			total += matrix[row][column]
		total_list.append(total)
		if total > max_rowsum:
			max_rowsum = total
		else:
			pass

	for i in range(len(total_list)):
		if total_list[i] == max_rowsum:
			maxrow_list.append(i)
	return [max_rowsum,maxrow_list]

#mess the multidimensional list up
def messup(matrix):
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			i = random.randint(0,len(matrix) - 1)
			j = random.randint(0,len(matrix[0]) - 1)
			matrix[row][column],matrix[i][j] = matrix[i][j],matrix[row][column]
	return matrix

def main():
	matrix = get_matrix()
	print(matrix)
	print(sum(matrix))
	print(sum_column(matrix))
	print(maxsum_row(matrix))
	print(messup(matrix))

