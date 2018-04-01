import sys

# Function to print out test_string
def sampleFunction(test_string):
	print(test_string)

# Fibonicci Function
def fibonacci(num_iterations, value1=0, value2=1):
	new_value2 = value1 + value2
	new_value1 = value2
	if num_iterations == 0:
		return ''
	elif num_iterations == 1:
		r_list = f'{new_value1} {fibonacci(num_iterations-1, value1=new_value1, value2=new_value2)}'
	else:
		r_list = f'{new_value1}, {fibonacci(num_iterations-1, value1=new_value1, value2=new_value2)}'
	return r_list

# Simple Counter Class
class Counter:
	def __init__(self, list_of_items):
		self.counts = dict.fromkeys(list_of_items, 0)

	def increment(self, key):
		self.counts[key] += 1

	def getCount(self, key):
		return self.counts[key]


sampleFunction('Hello World')

if len(sys.argv) > 1:
	num_iterations = int(sys.argv[1])
else:
	num_iterations = 10

print(fibonacci(num_iterations))

print('Class Object Example')
counter_instance = Counter(['even', 'odd'])
for i in range(num_iterations):
	if i%2 == 0:
		counter_instance.increment('even')
	else:
		counter_instance.increment('odd')

print(f'Number of even numbers: {counter_instance.getCount("even")}')
print(f'Number of odd numbers: {counter_instance.getCount("odd")}')
