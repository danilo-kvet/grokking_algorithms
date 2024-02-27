def quicksort(list):
	if len(list) < 2:
		return list
	else:
		pivot = list[0]
		lower_list = [i for i in list[1:] if i <= pivot]
		bigger_list = [i for i in list[1:] if i > pivot]
		return quicksort(lower_list) + [pivot] + quicksort(bigger_list)

result = quicksort([1, -1, 10, 234, 5, 13, 30, 0])
print(result)
