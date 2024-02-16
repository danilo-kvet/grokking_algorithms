def max_value(list):
	if len(list) == 1:
		return list[0] 
	elif list[0] > list[1]:
		return max_value(list[:1] + list[2:])	
	else:
		return max_value(list[1:])

result_1 = max_value([1, 22, 10, 103, -1, 0, -10])
result_2 = max_value([-1, -22, -10, -103, -1, 0, -10])
result_3 = max_value([-1, -22, -10, -103, -12])

print(result_1)
print(result_2)
print(result_3)
