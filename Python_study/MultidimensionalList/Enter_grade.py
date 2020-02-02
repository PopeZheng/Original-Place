names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
     # 录入五个学生三门课程的成绩
     # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
     # scores = [[None] * len(courses)] * len(names)
def get_matrix1(names,courses):
	scores = [[None] * len(courses) for _ in range(len(names))]
	for row, name in enumerate(names):
	    for col, course in enumerate(courses):
	        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
	print(scores)

#My idea
def get_matrix2(names,courses):
	matrix = []
	for name in range(len(names)):
		gradelist = []
		for course in range(len(courses)):
			grade = eval(input(str(names[name]) + ' ' + str(courses[course]) + ':'))
			gradelist.append(grade)
		matrix.append(gradelist)
	print(matrix)

def main():
	get_matrix1(names,courses)
	get_matrix2(names,courses)

if __name__ == '__main__':
	main()



