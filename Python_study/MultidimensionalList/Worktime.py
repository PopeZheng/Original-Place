	'''
	2 4 3 4 5 8 8
	7 3 4 3 3 4 4
	3 3 4 3 3 2 2
	9 4 3 7 3 4 1
	3 5 4 3 6 3 8
	3 4 4 6 3 4 4
	3 7 4 8 3 8 4
	6 3 5 9 2 7 9
	'''
def get_matrix():
	matrix = []
	EMPLOYEE = 8
	for employee in range(EMPLOYEE):
		daylist = []
		timelist = input().split()
		for time in  timelist:
			daylist.append(int(time))
		matrix.append(daylist)
	return matrix

def sumRow(matrix):
	sumrow = []
	for employee in range(len(matrix)):
		total = 0
		for day in range(len(matrix[employee])):
			total += matrix[employee][day]
		sumrow.append(total)
	return sumrow

def sort(sumrow):
	sortlist = []
	for i in range(len(sumrow)):
		max_time = sumrow[0]
		max_index = 0
		for j in range(1,len(sumrow)):
			if sumrow[j] > max_time:
				max_time = sumrow[j]
				max_index = j
		sortlist.append(max_index)
		sumrow[max_index] = 0
	return sortlist
def main():
	matrix = get_matrix()
	sumrow = sumRow(matrix)
	sortlist = sort(sumrow)
	print(sortlist)
if __name__ == '__main__':
	main()




