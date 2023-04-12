## Notes written in the actual lecture
# The other file is better commented.



# f(x) = 2*x

''' Mulitline comments
are yay!
'''

def f(x):
    y = 2*x
    return y

f(3)


'''
- int
- float
- str (string)
- bool

int(3.0)
str(1)


- list
- tuple
- set
- dict
'''


1 + 1
print(0.1 + 0.2)
10 * 2
print(10 / 5)
print(10 // 5)
10 % 2
3**2

True
False

'abc'
"abc"
'''abc'''
"""abc"""

not True
not False
not (1 == 2)


1 == 1  # True
1 == 2  # False
print(1.0 == 1)

print("Hello" + "world")
print("hello", "world")

# "1, 2, " + 3
print('hello' * 3)
'-' * 43


None

def f(x):
    y = 2*x
    # return y

print(f(3))

print(13 + True)

# Type hinting
z = 3

x: int = 3
x = 3.14

def f(x: int) -> float:
    return 1 / x


y = 'abc'
# y[0] = 'b'
'abc'[0]

x, y = 1, 2

x += 1
x -= 1
x *= 2
x /= 2
x **= 2
# x++
x += 1


# List

liste = [1, 2, 3]
liste[0]
liste[0] = 4

liste2 = liste
liste2[0] = 13
[13, 2, 3]
[13, 2, 3]

# liste2 = [...liste]
# liste2 = liste[::]

print(type(f))

liste.append(6)
print(liste)

liste = ['a', 'b', 'c']
# liste.join(';')
';'.join(liste)

print(len(liste))

print(
    len(liste),
type(liste),
    liste
)


list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list3[2:6])
print(list3[2:])
print(list3[2:])
print(list3[:-3])

stuff = 'whatever.html'
stuff[:-5]
stuff[-4:]

stuff.split('.')


## Dicts
my_dict = {'key1': 'Hello', 'key2': 'World'}
print(my_dict)

my_dict2 = {
    1: 'Hello',
    2: 'World',
}
print(my_dict)

my_dict['key1']
my_dict['key1'] = 'Howdy'
my_dict['key3'] = 'stuff'

my_dict.keys()  # 'key1', 'key2', 'key3'
my_dict.values()  # 'Howdy', 'World', 'stuff'
my_dict.items()  # [('key', 'Howdy'), (...)...]


# if
if 1 == 2:
    print('something')
    xx = 5
elif 2 == 2:
    yy = 6
else:
    pass

# {1: 'a', 2: 'b'}[x]


x = 0
while x < 3:
    print(x)
    x += 1


# For loops

for i in range(10):
    print(i)

range(10)  # 0..9
range(2, 10)  # 2..9
range(2, 10, 3)  # 2, 5, 8

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i)

# list(range(10))


list_of_names = ['Paul', 'Ken', 'John']
for name in list_of_names:
    print(name)


# for key in my_dict.keys():
for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)



def f(x):
    y = 2*x
    return y


def f(x, y, z):
    y = 2 * x * y * z
    return y

f(3, 4, 5)


def f(x):
    y1 = 2*x
    y2 = 1/x
    return y1, y2

a, b = f(3)

'''
Biggest differences between JS and Python:
- Python uses indentation instead of curly brackets.
- Things like !, ||, && are replaces with not, or, and.

'''

# Single-line comments start with a hashtag.
# Only what's _after_ the hashtag is a comment

'''Multi-line comments stars and ends with
either 3 single or double fnutts ( or ").'''

"""Actually, this makes a string, not a comment,
but when not printed or stored in a variable,
the interpreter ignores it."""

# Unlike JS, Python does not use semicolons.
# Well, it won't crash, but it makes you wierd if you use them. :)))
print('hei');

'''Python also has multiple different datatypes. Like:
- int
- float
- str (string)
- bool

In addition, it has multiple grouping datatypes. E.g.:
- list
- tuple (very similar to array/list)
- set (like an unordered, unique list)
- dict (dictionary: basically a JS object/map)

And you can make your own datatypes using classes/objects.
'''



## Operators

# We got all of the operators :D

1 + 1  # 2
0.1 + 0.2  # Same as in JS
8 - 1  # 7
10 * 2  # 20
35 / 5  # 7.0 (always a float)
5 / 2  # 2.5
7 // 2  # 3 (whole number division, rounds down, always results in an in)
7 % 2  # 1 (modulo. Samme som i JS)
3**2  # 9. Exponentiation.

# Bitwise operations works the same, I think? Nobody uses them anyway.
1 << 2

# Order of operations are being followed.
(1 + 3) * 2

# No (built-in) support for infinity, NaN or undefined in Python :(



## Bools

# Bools are the same, but first letter is upper-case
True
False

'abc'
"abc"
'''abc'''
"""abc"""

# How to boolean algebra in Python
not True  # False (!)
True and True  # True (&&)
False or True  # True (||)

# We have no ===. All tests are value-comparions.
# To test type, one can do either of the following:
type('hei') == type('nei')
type('hei') is type('nei')
# What's the difference? 'is' is more correct, but it basically makes no difference.
# So to do ===, you can write something like:
# if type(x) == type(y) and x == y

# Otherwise, the operators are mostly the same.
1 == 1  # True
2 == 1  # False
not 1 == 2  # True
not (1 == 2)  # True. Brackets are not necessary, but can be useful for
# clustering or for readability.



## Strings ++

'Hello, ' + 'World!'  # 'Hello, World!'. Concatenate strings with pluss
'Hey ' * 3  # 'Hey Hey Hey'. Multiplying strings with integers.
# '1, 2, ' + 3  # Error! Cannot add str and int. Same applies for str and list.

"5" == 5  # False

# We have None instead of null.
None

# And yes, we can do a lot of bool-int-hackery
13 + True  # 14

# We can use indexes on just about anything, using curly brackets:
'ABC'[0]  # 'A' (and yes, they start at 0. This isn't Matlab.)

# We can also use negative indexes to go from the end:
'ABC[-1]'  # 'C' (and yes, they start at 0. Apperentally we are Matlab.)

# And also, we have slicing :D :D :D
'ABCDEFG'[2:5]  # 'CDE'

# Get the length of a string, list, etc. with the built-in len function
len('hello')  # 5



## Variables

'''
Variable names can be letters, numbers and underscore (_), but cannot start with a number.
Standard naming scheme is snake_case. I.e. separate each word with an underscore. All lower case.
'''

# We make a variable simply by stating variable_name = value.
x = 3

# We _can_ (and probably should in properly written code bases) use type hinting.
# This can be used by tools like mypy to to type checking. VS Code has this built in.
x: int = 3

# We _can_ also make multiple variables on a single line, but I don't really bother.
x, y = 3, 4

# We have similar shorthand operators as in JS:
x += 1
x *= 2
# x /= 3  # VS Code gives an red underline here. 
# Not because it is wrong, but because it will make x a float. And we said it should be an int.
x -= 2
x %= 1
# And so on. We do _not_ however, have the x++ operators :(
# So x += 1 is the most compact way to increment a value.



## Lists  ++

# Create a list using square brackets
liste = ['Hello', 45, True]

# Access indexes in the normal way
liste[1]

# Add to list
liste.append(3.14)

# Still find the length using len
len(liste)

# We have the join-function, but it belongs to the string, not the int.
';'.join(['a', 'b', 'c'])

# As said earlier, we can also slice.
liste[0:2]



## Tuple and set

# The tuple is basically a list, with some small changes.
Y = (1, 2, 3)
# We cannot now update Y by using Y[0] = 4, because tuples are 'immutable'. I.e. cannot be changed.
# That's the downside. Upside: They can sometimes be somewhat faster, and they
# can be used as keys in dicts (more on this in the next section).

# The set is also basically a list, but it is unordered and unique (and has a
# lot of built in set functions (mathematical set theory)).
# E.g. set.intersection().

my_set = {1, 1, 2, 3, 3, 2, 3}  # {1, 2, 3}

# Useful for:
# 1. Converting a list to set to list: X = list(set(X)), and thereby removing
#       any duplicate items
# 2. Checking if a value is in the set: if 1 in X: ..., which is a lot faster
#       then using a list or a tuple. (But those also works fine.)



## Dicts (objects)

# The dictionary, or dict, is Python's version of the JS Object.
# It works in basically the same way, except keys have to be a datatype.
# E.g. string, int, etc.
my_dict = {'key1': 'Hello', 'key2': 'World'}
# Keys cannot be simple key1, but must be a string, int, float, bool or tuple
# (more on those later).

# We can access values in objects by using the square brackets (but not
# dot-notation, like in JS.)
my_dict['key2'] = 'Earth'

# We can create new values by just setting them equal to a new value
my_dict['key3'] = 'hey ho'



## Loops

# This is where a lot of people fall off the class, because there is a lot of
# ways to iterate.

# Basic for loop
for i in range(10):
    pass
# pass just means do nothing

# This loop iterates through the list-like object range, which contains the
# values 0, 1, 2, ..., N-1, where N is 10 here. I.e. 0...9. These are of course
# also the index of a list, so we can write something like
for i in range(4):
    print(liste[i])

# The for loop only iterates over objects, so we can also loop directly over
# lists or strings (letter by letter).
for x in liste:
    print(x)
# This method is usually the best method to loop through values.

# If you need the index, the best way is to use the function enumerate.
for i, x in enumerate(liste):
    print(i, x)
# However, this method, while great, is usually not considered a beginners
# method.

# We also have while loops, but not do-while, sadly.
x = 0
while x < 3:
    x += 1



## Functions

# How to basic f(x) = x^2 function
def f1(x):
    return x**2

# We can also do a bunch in the function, of course
def f2(x):
    p = x**2 + 3*x - 1
    z = 1/x
    y = p - z
    return y

# We call the function in the JS way:

f2(3)

# We can give more parameters to the function:
def f3(x, y):
    return x * y

f3(3, 4)

# We can also return multiple values. (Actually, we return a tuple (list-like
# thing) with multiple values, but same same)
def f4(x):
    y1 = 2 * x
    y2 = 1 / x
    return y1, y2  # we could also write return (y1, y2) to show more clearly.

# We then receive the two values (split up the tuple) by writing x, y = ...
a, b = f4(3)

# We can also type hint functions, like thus:
def f5(x: int) -> float:
    return 1 / x



## Classes

# Simple point class
class Point:
    x = 0
    y = 0

p = Point()
p.x = 3
p.y = 4

# How to constructor
class Point_v2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point_v2(3, 4)

## The __blabla__ methods are special methods, for things like operator
# overloading. All methods must accept the 'self' argument, to have access to
# the rest of the object.



## Important built-in functions

# print: Python's console.log. Takes any number of items.
print(1, '2', False, [1, 2, 3])

# input: receives input (commented out, because it stops the program flow).
# x = input('Write answer: ')

# range: loop-related. Returns a list-like object of 0...A (and other sets)



## Importing modules

# We can import more functionality using the import keywords (preferrably at
# the top of the file).
import math

math.sqrt(2)

# We can give it a shorter name, which is sometimes useful
import math as m
m.sqrt(2)

# And we can import specific functions or submodules
from math import sqrt
sqrt(2)

# We can also import other files from our own code. The file hello.py can be
# imported as follows:
# import hello
# Giving us access to all our functions in hello, by running 
# 'hello.function_one(x, y, z)'.

## List vs tuple vs set
X = [1, 2, 3]  # list
X = (1, 2, 3)  # tuple
X = {1, 2, 3}  # set


## Set
Y = {1, 2, 3, 2, 1, 3, 4, 2, 1, 2, 2, 1}
# {1, 2, 3, 4}

# What sets are useful for, part 1: Removing duplicates
Z = [1, 2, 3, 2, 1, 3, 4, 2, 1, 2, 2, 1]
Z = list(set(Z))  # [1, 2, 3, 4]

# Part 2:
# Checking if a value is in a set of values
if 5 in X:
    pass
# This can be done with lists, tuples, strings, etc. but sets are a looooot
# faster than lists and tuples. Especially for large lists/tuples/sets.


## More on functions
# Not all functions need input-arguments, nor to return anything.
def fnavn():
    print('hei')
# A more realistic example of this, is a function to create an empty save file.


## More on strings
# String function important for this weeks exercise.
stringliste = 'string:blabla'.split(':')
# There are a looot more string functions you can use to all sorts of stuff. :D


## Classes
# Simple class (without constructor)
class Punkt:
    x = None
    y = None

# Create object
p = Punkt()
p.x = 3
p.y = 4

print(p.x)

# Class with constructor
class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create and initialize object
p2 = Punkt2D(3 ,4)
print(p2.x)


## Import built-in modules
import math

print(math.sqrt(2))


## Import my own modules (or just files)
# We have an example file called 'example_file.py' in the same directory.
# import example_file


## It has a function called 'some_function' in, which takes x and multiplies it
# with 2.

def some_function(x):
    return 2 * x
print(some_function(10))  # 6


## Install external modules
# Use 'pip' in the command line:
# pip install urllib3
# You may need to use 'pip3', or even 'python -m pip' or 'python3 -m pip'
# or 'py -m pip'

