# Functions and Classes

And with this whirlwind introduction to python, we're going to go over functions and classes.

## Functions

```python
# Function to print out test_string
def sampleFunction(test_string):
	print(test_string)

# Fibonacci Function
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
```

The first function will just print out the variable passed.

The second is a bit more complicated, it takes three values (although only one of them needs to be explicit). The first value, num_iterators says how many times this will *recursively* run through itself, meaning this is a function that will call itself. It builds the next values for the recursive call and then does a check on the remaining iterations.

If there's no more iterations, it returns an empty string. Which would then be added to the special case of one remaining iteration that doesn't include the comma.

Otherwise, it constructs a string of "[value1] [next iteration]" down the chain and returns it. The final return is the Fibonacci sequence of num_iterations.

We can call this via:
```python
print(fibonacci(num_iterations))
```

Although, this is kind of boring seeing as we would have to define num_iterations beforehand. This allows us to introduce taking command line arguments.

## Arguments

Sometimes, we don't know what we want to do prior to running the program. We could take input in the script, but for our purposes, this isn't usually useful. Instead we take command line arguments that we then pass into the script. We do this by:

```python
import sys

if len(sys.argv) > 1:
	num_iterations = int(sys.argv[1])
else:
	num_iterations = 10
```

This is introducing the concept of importing sys, one of the standard libraries shipped with python (in this case, giving us access to things like the command being entered). sys.argv is a list of all arguments. The 0 element of the list is the command itself, so "4_functions_classes.py3" in this case. Each one after that is an argument that can be read in.

Here, we're checking if the length of the list of sys.argv is greater than 1. If it is, then that next argument would be the number of iterations we want to run through the Fibonacci function we wrote earlier.

Now we have the ability to define how many iterations we want to run everytime we run it.

## Classes

```python
# Simple Counter Class
class Counter:
	def __init__(self, list_of_items):
		self.counts = dict.fromkeys(list_of_items, 0)

	def increment(self, key):
		self.counts[key] += 1

	def getCount(self, key):
		return self.counts[key]
```

Here we have a simple class to create a Counter object that will increment the count on some identifier. This is very simple and merely an example of what you can do with classes. As we move forward, these concepts will be expanded and will be made much more useful.

This code in and of itself is totally useless. It won't run until you *instantiate* an instance of this class.

```python
print('Class Object Example')
counter_instance = Counter(['even', 'odd'])
for i in range(num_iterations):
	if i%2 == 0:
		counter_instance.increment('even')
	else:
		counter_instance.increment('odd')

print(f'Number of even numbers: {counter_instance.getCount("even")}')
print(f'Number of odd numbers: {counter_instance.getCount("odd")}')
```

Now, we've created a counter that counts instances of 'even' and 'odd'. To test that everything works, we iterate through a range of "num_iterations" and determine if the value is even or odd, incrementing the counter value accordingly. Finally, we print out the results.

Classes give us a great deal of flexibility and allow us to not have to repeat a lot of code as we use it. This will come in handy as we start working with AWS as most services are built with many of the same building blocks and we will only have to write implementations for dealing with them once and simply take advantage of our code there.