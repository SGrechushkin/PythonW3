    #Python - Output Variables for Lesson2
'''https://www.w3schools.com/python/python_variables_output.asp'''
'''
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#Result - Python is awesome

#or

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
#Result - Pythonisawesome

a=4
b=5
print(a+b)
#Result - 9
'''

    #Global Variables

'''
x="awesome"

def myfunc():
    print("Python is",x)

myfunc()

print("You are " + x)
'''
#----------
'''
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''
#---------
    #Python Data Types
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
    #Getting the Data Type
'''
x = 5
print(type(x))
'''
#---------
'''
Example                     	                Data Type	                print result
x = "Hello World"	                                str	                    Hello World
x = 20	                                            int	                    20
x = 20.5	                                        float	                20.5
x = 1j	                                            complex	                lj
x = ["apple", "banana", "cherry"]	                list	                ['apple', 'banana', 'cherry']
x = ("apple", "banana", "cherry")	                tuple	                ('apple', 'banana', 'cherry')
x = range(6)	                                    range	                range(0, 6)
x = {"name" : "John", "age" : 36}	                dict	                {'name': 'John', 'age': 36}
x = {"apple", "banana", "cherry"}	                set	                    {'apple', 'cherry', 'banana'}
x = frozenset({"apple", "banana", "cherry"})	    frozenset	            frozenset({'banana', 'apple', 'cherry'})
x = True	                                        bool	                True
x = b"Hello"	                                    bytes	                b'Hello'
x = bytearray(5)	                                bytearray	            bytearray(b'\x00\x00\x00\x00\x00')
x = memoryview(bytes(5))	                        memoryview	            <memory at 0x00A78FA0>
x = None	                                        NoneType                None
'''

#---------------
    #Python Numbers Type Conversion
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''
#---------
    #Random Number
'''
import random

print(random.randrange(1, 10))
'''

