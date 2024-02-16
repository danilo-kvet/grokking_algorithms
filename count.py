def count(list):
	if len(list) == 1:
		return 1
	else:
		return 1 + count(list[1:])

result = count([1, 4, 5, 6, 7])

print(result)
