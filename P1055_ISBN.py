def main():
	string = input()
	list1 = []
	list1.append(string[0])
	for i in range(2,5):
		list1.append(string[i])
	for j in range(6,11):
		list1.append(string[j])
	list1.append(string[12])

	end = 0
	for i in range(len(list1)-1):
		end += (i+1) * int(list1[i])
	end = end % 11
	if end == 10:
		end = 'X'
	if str(end) == list1[9]
		print('Right')
	else:
		print(string[:12] + str(end))

if __name__ == '__main__':
	main()