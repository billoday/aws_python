hello_string = 'hello'
name_string = 'Bill'

# Assemble basic string using %s
full_string = '%s %s' % (hello_string, name_string)
print(full_string)

# Construct basic string
full_string = hello_string + ' ' + name_string
print(full_string)

# Construct using fstring
full_string = f'{hello_string} {name_string}'
print(full_string)

# Capitalize first letter of full_string
# Note what happens to name_string
print(full_string.capitalize())

# All upper case
print(full_string.upper())

# All lower case
print(full_string.lower())

# Split and reorder string
full_string_list = full_string.split(' ')
reverse_string = full_string_list[1] + ', ' + full_string_list[0]
print(reverse_string)
