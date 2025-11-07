#--------------------------
    #Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function
#In Python a function is defined using the def keyword:
'''
def my_function():
  print("Hello from a function")
'''

#Calling a Function
#To call a function, use the function name followed by parenthesis:
'''
def my_function():
  print("Hello from a function")

my_function()
'''

#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

result:
Emil Refsnes
Tobias Refsnes
Linus Refsnes
'''

#Number of Arguments
#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
'''
def my_function(fname, lname):
  print(fname + " " + lname)
names = [("Emil", "Refsnes"), ("Anna", "Ivanova"), ("John", "Smith")]

for fname, lname in names:
    my_function(fname, lname)
result:
Emil Refsnes
Anna Ivanova
John Smith
'''

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'''

#Keyword Arguments
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
'''

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
'''

#Passing a List as an Argument
'''
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
'''

#Sending a dictionary as an argument:
'''
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
'''

#Return Values
#Functions can return values using the return statement:

'''
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)
'''

#Returning Different Data Types
'''
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
'''
def add_numbers(a, b):
    print(a + b)

result = add_numbers(2, 3)
print(result)