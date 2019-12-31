import math

# print(math.sqrt(11))
# print(type(3.3))
# print(str(3.3).split('.'))

# print('sasikant nair'.split())

def square_or_square_root(arr):
	result = []
	for i in arr:
		temp = str(math.sqrt(i)).split('.')
		# print(temp)
		if int(temp[1]) == 0:
			result.append(temp[0])
			# print('found root')
		else:
			result.append(i*i)
			# print('raised 2')
	return print(result)

square_or_square_root([4, 3, 9, 7, 2, 1 ])
square_or_square_root([100, 101, 5, 5, 1, 1])
square_or_square_root([1, 2, 3, 4, 5, 6])