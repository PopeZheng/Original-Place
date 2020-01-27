#my first idea
def seq_search(items,key):
	key_items = []
	for i in range(len(items)):
		if items[i] == key:
			key_items.append(i)
	if len(key_items) == 0:
		return -1
	else:
		return key_items

#Use enumerate method
def seq_serch(items,key):
	key_items = []
	for index,element in enumerate(items):
		if element == key:
			key_items.append(index)
	if len(key_items) == 0:
		return -1
	else:
		return key_items


#binary_search can only be used in list which is in order
def binary_search_up(items,key):
	floor = 0
	ceil = len(items) - 1
	while floor <= ceil:
		mid = (floor + ceil) // 2
		if key > items[mid]:
			floor = mid
		elif key < items[mid]:
			ceil = mid
		else:
			return mid
	return -1




