#Python Introduction
'''
print("Hello, world!")
'''
#Python Getting Started
'''
import sys
print (sys.version) #version
'''
#Python Syntax
    #Python Indentation
'''
if 5>2:
    print("Five is greater than two!")
'''
#Python Variables
'''
x=5
y="Sergii"
print(x,y)

x=4
x="test"
print(x)

x=str(3)  # x will be '3'
y=int(3)  # y will be 3
z=float(3) # z will be 3.0
print(x,y,z)

x=5
y="test"
print(type(x))
print(type(y))
'''
    #Python - Variable Names
'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
    #Python Variables - Assign Multiple Values
        #Many Values to Multiple Variables
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''
        #One Value to Multiple Variables
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''
        #Unpack a Collection
'''
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x,y,z)
'''


