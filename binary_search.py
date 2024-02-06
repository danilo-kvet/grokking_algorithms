import math

def binary_search(list, item):
	low = 0;
	high = len(list) - 1;
	while (low <= high):
		mid = math.floor((low + high) / 2)
		selected_item = list[mid]
		
		if selected_item == item:
			return mid
		if selected_item > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

generic_list = [1, 3, 5, 7, 9]

print(binary_search(generic_list, 3))
print(binary_search(generic_list, -1))	
