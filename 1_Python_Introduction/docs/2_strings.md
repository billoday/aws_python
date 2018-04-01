# Strings

Here, we're going to talk about basic string operations

Let's start with basic setup:
```python
hello_string = 'hello'
name_string = 'Bill'
```

This gets us two strings, hello_string and name_string. We're going to work with them from now on.

```python
# Assemble basic string using %s
full_string = '%s %s' % (hello_string, name_string)
print(full_string)
```

This will get us "hello Bill" using a classic construction.

```python
# Construct basic string
full_string = hello_string + ' ' + name_string
print(full_string)
```

This is a way to construct strings a different way.

```python
# Construct using fstring
full_string = f'{hello_string} {name_string}'
print(full_string)
```

This is the newest way to construct strings (and the way we'll primarily use, but is only available in Python 3.6 and later)

```python
# Capitalize first letter of full_string
# Note what happens to name_string
print(full_string.capitalize())
```

This is a way to capitalize the first character of a string, but convert the rest to lower case.

```python
# All upper case
print(full_string.upper())

# All lower case
print(full_string.lower())
```

These convert to upper or lower case respectively.

```python
# Split and reorder string
full_string_list = full_string.split(' ')
reverse_string = full_string_list[1] + ', ' + full_string_list[0]
print(reverse_string)
```

Here, we're taking the full string, and flipping it around so that it will output "Bill, hello"
