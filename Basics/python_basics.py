"""
# STRINGS
message = 'Hello World'

print(message)
print(len(message))
print(message[0])
print(message[0:5])              # 1st index is inclusive last is exclusive          
print(message[6:])
print(message.lower())           # upper()
print(message.count('H'))        # counts the no of 'H' is Hello World
print(message.find('World'))     # World starts at index 6,if not there it will return -1

message = message.replace('World','Universe')
print(message)

# String Concatination
greeting = 'Hello'
name = 'Sanket'
message = greeting+" "+name
print(message)

# without using +sign
message = '{} {} Welcome'.format(greeting,name);
print(message)

# by using f-strings
message = f'{greeting} {name.upper()}'
print(message)

print(help(str.lower))         # gives description of lower function

"""



"""
# INTEGERS AND FLOAT

num = 3
print(type(num))
num = 3.14
print(type(num))

print(3+2)
print(3/2)         # output:1.5
print(3//2)        # output:1 (floor division)
print(3 ** 2)      # output:9 ((**)-> exponent)

print(abs(-2))          # 2
print(round(3.75))      # 4
print(round(3.75,1))    # 3.8  rounds 1 digit

num1 = '100'
num2 = '200'
print(num1 + num2)    # 100200

#Casting
num1 = int('100')
num2 = int('200')
print(num1 + num2)





# LISTS TUPLES AND SETS
# Lists and Tuples allow us to work with sequential data
# Sets are unordered collection of values with no duplicates

# 1.Lists

courses = ['Phy', 'Chem', 'Maths', 'Comp']
print(courses)
print(len(courses))

print(courses[0])
print(courses[-1])           # -1 index to access the last element of List

# Modifying Lists

courses.append('Art')        # Art will be placed at the end of the list
courses.insert(0,'Art')      # Art will be inserted at index 0

course2 = ['Bio', 'CN']
courses.extend(course2)      # will add values to the last

courses.remove('Chem')
courses.pop()
print(courses)

# Sorting Lists

courses.reverse()
courses.sort()                   # will Sort in Alphabetical Order
courses.sort(reverse=True)       # will Sort in Descending Order
sorted_list = sorted(courses)    # if we dont want to Alter out Original List

nums = [1,2,3,4]                 
print(min(nums))                 # Min,Max,Sum,Avg

print(courses.index('Art'))     # if not present then it will give error,hence use 'Math' in Courses(TRUE,FALSE)
print('Math' in courses)    
print(courses)

courses_str = ", ".join(courses)
print(courses_str)              # will give us , seperated list elements without[]

li = [1,2,3,-4,-5,-6]
s_li = sorted(li,key=abs)        # Output ->  1,2,3,-4,-5.-6

tup = (1,6,3,7,2,8,5)
s_tup = sorted(tup)             # Similar for Dictionaries,will sort according to key 
print(s_tup)   
"""


"""
# TUPLES -> are inmutable hence can't perform remove,add,append operations

tuple_1 = ('Math','Chem','Phy','Comp')
print(tuple_1)

#SETS -> are unordered data and don't contain duplicates

course = {'Math','Chem','Phy','Comp','Math'}
print('Math' in course)           # To check for duplicate values,can be done by lists also but sets are optimized ones

courses_art = {'Art' , 'Math' , 'Phy'}
print(course.intersection(courses_art))        
print(course.difference(courses_art))
print(course.union(courses_art))

"""


"""

# DICTONARIES -> Key,Value Pair

student = {'name':'Sanket' , 'age':25 , 'courses':['Math','Phy']}
print(student)
print(student['name'])
# print(student['phone'])                         # will give us an error hence use gett method
print(student.get('phone' , 'Not Found'))       # if key is not there will display Not Found

student['phone'] = 907790;
student['name'] = 'Sahil'               # will update name
student.update({'name': 'Swapnil' , 'age':20 , 'phone':86750})           # if we want to update multiple values
print(student)

del student['age']       # OR age = student.pop('age')
print(len(student))
print(student.keys())    # .values  .items

for key, values in student.items():
    print(key,values)
    
"""


"""
# CONDITIONAL STATEMENTS   if,else,elif,and,or,not

a = [1,2,3]
b = [1,2,3]

print(a == b)           # true
print(a is b)           # prints false as a,b are 2 differet objects

# LOOPS 

nums = [1,2,3,4]
for i in nums:
    for letters in 'ab':
        print(i,letters);
        
for i in range(1,11):
    print(i)
    
x = 0

while x<=10:
    print(x)
    x += 1;

"""


"""
# FUNCTIONS

def hello_func():
    pass                                    # If we have to keep function blank write pass else it will give error

def hello(greeting):
    return '{} Sanket'.format(greeting)
print(hello('Hi').upper())

def practice(greeting,name='You'):
    return '{} {}'.format(greeting,name)
print(practice('Hi','Sanket'))

def student_info(*args , **kwargs):
    print(args)
    print(kwargs)

student_info('Comp','Art',name='Sanket',age=20)

# Use the symbol * in Python to allow a variable number of positional arguments/parameters to the function.

def function_singleasterix(*someargs):
    for i in someargs:
        print(i)
        
listdata=[ "Alex","Tom","John","Alice"]
function_singleasterix(listdata)

# Use the symbol ** in Python to allow a variable number of keyword arguments/parameters to the function. 
# Note that the argument after must be a mapping (dictionary key-value pair) items, not a tuple or a list.
# a list - *
# tuple - *
# dictionary - **

def function_doubleasterix(**keywordargs):
    print("The keys in the kwargs dicionary are -", keywordargs.keys())
    print("The values in the kwargs dicionary are -", keywordargs.values())
    
function_doubleasterix(SNo001 ='Alex', SNo002 ='Tom')

"""

"""
# GLOBAL LOCAL

x = 'global x'

def test():
    global x
    x = 'local x'
    
test()
print(x)

"""

"""
# LIST COMPREHENSIONS

nums = [1,2,3,4,5,6,7,8,9]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n*n for n in nums]
print(my_list)
my_list = [n for n in nums if n%2==0]
print(my_list)

# I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
        
print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

"""


"""
# STRING FORMATING

person = {'name':'Sanket', 'age':20}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age'])+ ' years old.'
print(sentence)

sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])
print(sentence)

tag = 'hi'
text = 'This is a headline'

sentence = '{0},{1}</{0}'.format(tag,text)
print(sentence)

person = {'name': 'Sanket', 'age': 20}
sentence = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)       # : to Specify that we want formating
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

for in in range(1,11)
    sentence = f'Value is {i:}'
    print(sentence)
    
"""

"""
# RANDOM NUMBERS
import random

value = random.random()             # gives random value between 0 & 1
print(value)

value = random.uniform(1,10)
print(value)                        # gives random floating value between 0 & 1

value = random.randint(1,6)         # gives random interger value between 0 & 6(both inclusive)

names = ['Sanket' , 'Swapnil' , 'Sahil']
value = random.choice(names)        # Random Values from list
print(value)

colors = ['Red' , 'Green' , 'Blue']
value = random.choices(colors, k=5)         # will give 5 random values from list
print(value)            

deck = list(range(1,53))
random.shuffle(deck)
print(deck)
hand = random.sample(deck , k=5)
print(hand)

"""

"""
# GENERATORS

# def square_no(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# nums = [1,2,3,4,5]
# sq_no = square_no(nums)
# print(sq_no)
        
# for generators
def square_no(nums):
    for i in nums:
        yield(i*i)

nums = [1,2,3,4,5]
sq_no = square_no(nums)
# sq_no = [x*x for x in nums]
for num in sq_no:               # No need to take list and append
    print(num)
    
nums = [1,2,3,4,5]
sq_no = (x*x for x in nums)        # Need less memory and time for generators as it waits for us to loop in to get the values
print(list(sq_no))

"""

# CLOSURES

# def outer_func():
#     message = 'hi'
    
#     def inner_func():
#         print(message)
#     # return inner_func()
#     return inner_func       # -> will not execute as () not there
    
# execute = outer_func()
# execute()                   # After putting (), it will execute
# execute()

# def outer_func(msg):
#     def inner_func():
#         print(msg)
#     return inner_func

# hi_func = outer_func('Hi')
# by_func = outer_func('Bye')

# hi_func()
# by_func()
    
# DECORATORS -> takes input as a function and return a function

def decorator_funct(original_func):
    def wrapper_func():
        return original_func()
    return wrapper_func

@decorator_funct
def display():
    print('Display Function Ran')
    
# decorator_display = decorator_funct(display)          # instead write @decorator_funct0

display()

