import math

def binary_search(list, target, low = 0, high = None):
	if high is None: 
		high = len(list) - 1;
	
	while (low <= high):
		mid = math.floor((low + high) / 2)
		selected_item = list[mid]
		
		if selected_item == target:
			return mid
		if selected_item > target:
			high = mid - 1
		else:
			low = mid + 1
	return None

generic_list = [1, 3, 5, 7, 9]
bigger_list = [i for i in range(1000001)]

random_list = [38, 39, 42, 43, 45, 47, 48, 50, 51, 52, 54, 55, 57, 58, 59, 60, 61, 62, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 149, 150]


print('binary', binary_search(generic_list, 3))
print('binary', binary_search(generic_list, -1))	
print('binary', binary_search(bigger_list, 506978))	

def exponential_search(list, target):
	if list[0] == target:
		return 0

	i = 1
	n = len(list)

	while i < n and list[i] < target:
		if list[i] == target:
			return i

		i *= 2

	return binary_search(list, target, i // 2, min(i, n))

print('exponential', exponential_search(bigger_list, 1))	
print('exponential', exponential_search(bigger_list, 1000000))	
print('exponential', exponential_search(bigger_list, 506978))	

print('exponential', exponential_search(random_list, 38))	
print('exponential', exponential_search(random_list, 119))	
print('exponential', exponential_search(random_list, 88))	
print('exponential', exponential_search(random_list, 150))	