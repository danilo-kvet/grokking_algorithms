def sum(array):
	if len(array) == 1:
		return array[0]
	else:
		return array[0] + sum(array[1:])

print(sum([1, 2, 3, 4, 5]))
