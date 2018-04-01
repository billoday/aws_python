# Basic Objects

## Lists

```python
basic_list = [1, 2, 3, 4, 5]
```

Lists are unordered collections of variables. 

```python
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
```

They are not typed, meaning it can be difficult if you think you're getting something of a specific type and need to plan for that.

We're also introducing *for* loops here. This will allow us to iterate over an *iterator* of some sort (this can be a list, a dictionary, an iterator like *range* or *items* of a dictionary)

## Dictionaries

```python
basic_dict = {1: 'Hello', 2: 'World'}
```

Dictionaries are key, value pairs. They are very powerful and have a number of features.

```python
print('iterate though a dictionary')
for item in basic_dict:
	print(item)

print('Iterate, getting both key and value')
for key, item in basic_dict.items():
	print(f'{key}: {item}')

print('Add a new value')
basic_dict[3] = 'not'
print(basic_dict)
```

We'll go over these in much greater detail, but this is a basic set of tools needed to work with dictionaries.


## Tuples

```python
basic_tuple = ('Hello', 'World')
```

Tuples are immutable collections. You'll probably not use them too much directly, but they do show up from time to time, so it's good to be aware of the various gotchas associated with them.

```python
print('Get a tuple\'s length')
print(len(basic_tuple))

print('Iterate through a list')
for item in basic_tuple:
	print(item)

print('Tuples are immutable, you can only create new ones.')
second_tuple = basic_tuple + ('not', )
print(second_tuple)
```

If you try to append to a tuple, you will get an error like this:
```
TypeError: 'tuple' object does not support item assignment
```

## More Advanced Concepts

We can have a list of dictionaries:
```python
complex_list = []
for i in range(10):
	print(f'Adding {i}: {i*2} to complex_list')
	complex_list.append({i: i*2})
print(complex_list)
```

We can also have a dictionary of lists
```python
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
```

Note, that this introduces the if statement as well. In python, 
if [statement]: will run the indented code if that condition is met, 
elif [statement]: will run if a subsequent condition is met, and 
else: will run if none of the preceding conditions are met.