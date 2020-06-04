# print hello world
print("Hello, world!")

# declare a variable
name = "Artem"

# print a variable
print(name)

# String concatenation
print("Hello " + name)
# `Hello ${name}`
print(f'Hello {name}')

# Data structures

# Lists (Arrays)
p = [10, 60, 20, 5, "Banana"]
print(p)
# add an element to the end of P
p.append(77)
print(p)

# Let's loop over the list P, and print every element
# for every element in P, do some sort of code
for element in p:
    print(element)

# Let's print the index and element at the index of P
# enumerate(P) => [(0, 10), (1, 60), (2, 20) ... ]
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]}')

# List comprehensions
# another way to create a list
numbers = [1, 4, 9, 16, 25]
# create a new list of squares from the numbers list
# this is the lame way of creating this list
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# let's use List Comprehensions
# for each element from numbers, multiply by itself, and add to cooler_squares
cooler_squares = [num*num for num in numbers]
print(cooler_squares)

# Let's create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)

names = ["Sarah", "jorge", "sam", "Frank", "Bob", "sandy", "Shawn"]
# create a new list containing only names that start with s
# Also all names should be capitalized
s_names = [name.capitalize() for name in names if name[0].lower() == 's']

# the verbose way of writing the above statement
s_names_verbose = []
for name in names:
    if (name[0].lower() == 's'):
        s_names_verbose.append(name.capitalize())

print(s_names)

# Dictionaries!
# Otherwise known as maps/hashmaps/objects
# A key => value data structure
new_dict = {}

# create a dictionary with some keys and values

food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}
print(food_dict)

# let's add a new key value pair
food_dict['cucumber'] = 'is maybe a vegetable?'
print(food_dict)

# access and print a specific element in food_dict
choosen_food = 'apple'
# food_dict.apple is not allowed in python (only javascript)
print(food_dict[choosen_food])

# iterate through the keys and values of a dictionary
# for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key} : {value}')

# how can we check if an element exists in a dictionary?
# is apple in food_dict ?
print('is a fruit' in food_dict.values)
print('banana' in food_dict)

# Tuples and Sets

# Tuples
tup = (1,2,3,4)
for item in tup:
    print(item)

# access a particular element
print(tup[1])

# you cannot modify tup in any way

# Sets are basically dictionaries without values - UNORDERED
# Sets are quick to search through, lists are not
fruit = {'cucumber', 'apple', 'banana'}
fruit.add('pizza')

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I don't think cucumber is a fruit")