def getLower(array):
	lower = array[0]
	lower_index = 0
	for i in range(1, len(array)):
		if array[i] < lower:
			lower = array[i]
			lower_index = i
	return lower_index

def sortByLower(array):
	tempArray = []
	for i in range(len(array)):
		lower = getLower(array)
		tempArray.append(array.pop(lower))
	return tempArray

print(sortByLower([4, 1, 25, 5, 10, 12]))
