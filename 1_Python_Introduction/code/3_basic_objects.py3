basic_list = [1, 2, 3, 4, 5]
basic_dict = {1: 'Hello', 2: 'World'}
basic_tuple = ('Hello', 'World')

# Lists

print('Get a list\'s length')
print(len(basic_list))

print('Iterate through a list')
for item in basic_list:
	print(item)

print('Add items to a lists')
basic_list.append(6)
print(basic_list)

print('We don\'t care about type')
basic_list.append('Hello')
print(basic_list)

# Tuples

print('Get a tuple\'s length')
print(len(basic_tuple))

print('Iterate through a list')
for item in basic_tuple:
	print(item)

print('Tuples are immutable, you can only create new ones.')
second_tuple = basic_tuple + ('not', )
print(second_tuple)

# Dictionaries
print('iterate though a dictionary')
for item in basic_dict:
	print(item)

print('Iterate, getting both key and value')
for key, item in basic_dict.items():
	print(f'{key}: {item}')

print('Add a new value')
basic_dict[3] = 'not'
print(basic_dict)

# Advanced Concepts

print('Dictionaries can have lists and vice versa')
complex_list = []
for i in range(10):
	print(f'Adding {i}: {i*2} to complex_list')
	complex_list.append({i: i*2})
print(complex_list)

print('We can make a dictionary determining if any value is even')
even_dict = {'even': [], 'odd': []}
for i in range(20):
	if i%2 == 0:
		print(f'{i} is even')
		even_dict['even'].append(i)
	else:
		print(f'{i} is odd')
		even_dict['odd'].append(i)
print(even_dict)
