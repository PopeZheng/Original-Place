# Writed by myself First idea
def sort(origin_items):
	sorted_items = []
	succession_items = origin_items[:]
	for i in range(0,len(origin_items)):
		min_index = 0
		min_item = succession_items[0]
		for j in range(1,len(succession_items)):
			if min_item > succession_items[j]:
				min_item = succession_items[j]
				min_index = j
			else:
				pass
		sorted_items.append(min_item)
		del succession_items[min_index]
	return sorted_items

#simple select_swap
def select_sort(origin_items, comp=lambda x, y: x < y):
         """简单选择排序"""
	items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
           	if comp(items[j], items[min_index]):
                min_index = j
        		items[i], items[min_index] = items[min_index], items[i]
    return items

#bubble_sort fundamental
def bubble_sort1(origin_items):
	succession_items = origin_items[:]
	for i in range(len(succession_items)-1):
		for j in range(len(succession_items)-1-i):
			if succession_items[j] > succession_items[j+1]:
				succession_items[j],succession_items[j+1] = succession_items[j+1],succession_items[j]
			else:
				pass
	return succession_items
			

#bubble_sort   
#external loop can be limited by if exchange happen 87612345
#inner loop's floor can't be limited by the index where the first exchange take place randomly   24681234
#inner loop's ceil can be limited by the index where the last swap occur 243156789
def bubble_sort2(origin_items):
	succession_items = origin_items[:]
	last_exchange = len(succession_items)-1
	for i in range(len(succession_items)-1):
		exchanged = False
		for j in range(last_exchange):
			if succession_items[j] > succession_items[j+1]:
				succession_items[j],succession_items[j+1] = succession_items[j+1],succession_items[j]
				exchanged = True
				last_exchange = j
			else:
				pass
		if not exchanged:
			break
		'''if exchanged:
			print(succession_items)    For test''' 
	return succession_items

#bubble_sort in two directions in the same loop
def bubble_sort3(origin_items):
	succession_items = origin_items[:]
	for i in range(len(succession_items)//2):
		exchanged = False
		for j in range(i,len(succession_items)-1-i):
			if succession_items[j] > succession_items[j+1]:
				succession_items[j],succession_items[j+1] = succession_items[j+1],succession_items[j]
				exchanged = True
			else:
				pass
			#print(succession_items)

		if exchanged:
			exchanged =False
			for j in range(len(succession_items)-2-i,i,-1):
				if succession_items[j-1] > succession_items[j]:
					succession_items[j-1],succession_items[j] = succession_items[j],succession_items[j-1]
					exchanged = True
				else:
					pass
				#print(succession_items)

		if not exchanged:
			break
	return succession_items

#The most supreme version
def bubble_sort4(origin_items):
	succession_items = origin_items[:]
	floor = 0
	ceil = len(succession_items)-1
	for i in range(len(succession_items)//2):
		exchanged = False
		for j in range(floor,ceil):
			if succession_items[j] > succession_items[j+1]:
				succession_items[j],succession_items[j+1] = succession_items[j+1],succession_items[j]
				exchanged = True
				ceil = j
			else:
				pass
			#print(succession_items)

		if exchanged:
			exchanged = False
			for j in range(ceil,floor,-1):
				if succession_items[j-1] > succession_items[j]:
					succession_items[j-1],succession_items[j] = succession_items[j],succession_items[j-1]
					exchanged = True
					floor = j
				else:
					pass
				#print(succession_items)
		if not exchanged:
			break
	return succession_items

#merge sort
def merge(items1,items2):
	index1 = index2 = 0
	sorted_items = []
	while index1 in range(len(items1)) and index2 in range(len(items2)):
		if items1[index1] <= items2[index2]:
			sorted_items.append(items1[index1])
			index1 += 1
		else:
			sorted_items.append(items2[index2])
			index2 += 1
	sorted_items += items1[index1:]
	sorted_items += items2[index2:]
	return sorted_items

def merge_sort(origin_items):
	if len(origin_items) < 2:
		sorted_items = origin_items[:]
	mid = len(origin_items)//2
	left = merge_sort(origin_items[:mid])
	right = merge_sort(origin_items[mid:])
	return merge(left,right)











