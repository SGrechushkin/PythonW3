#Lesson3
#https://www.w3schools.com/python/python_casting.asp

    #Python Casting
'''
Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
'''
from ctypes import HRESULT

#---------------
    #Python Strings

#Quotes Inside Quotes
'''
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
'''

#Multiline Strings
'''
a="""Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
"""
print(a)
'''

#Strings are Arrays
'''
a="Sergii"
print(a[0])
result - S
'''

#Looping Through a String
'''
for x in "banana":
  print(x)
result -
b
a
n
a
n
a
'''

#String Length
'''
a = "Hello, World!"
print(len(a))
'''

#Check String
'''
txt='Як чудово вивчати пайтон'
if 'пайтон' in txt:
    print("Yes 'пайтон' is present.")
'''
#Check if NOT
'''
txt = "The best things in life are free!"
print("expensive" not in txt)
result - True
'''

'''
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
'''

#---------
    #Slicing

'''
b = "Hello, World!"
print(b[2:6])
result - llo,
'''
#Slice From the Start
'''
b = "Hello, World!"
print(b[:5])
'''
#Slice To the End
'''
b = "Hello, World!"
print(b[2:])
'''
#Negative Indexing
'''
b = "Hello, World!"
print(b[-5:-2])
'''

#-----------
    #Python - Modify Strings
#Upper Case
'''
a="Hello, world!"
print(a.upper())
'''
#Lower Case
'''
a = "Hello, World!"
print(a.lower())
'''
#Remove Whitespace
'''
a = " Hello, World! "
print(a.strip()) 
returns "Hello, World!"
'''
#Replace String
'''
a = "Hello, World!"
print(a.replace("H", "J"))
'''
#Split String
'''
a = "Hello, World!"
print(a.split(",")) 
returns ['Hello', ' World!']
'''
#-------------
    #String Concatenation
'''
a = "Hello"
b = "World"
c = a + b
print(c)
'''

'''
a = "Hello"
b = "World"
c = a + " " + b
print(c)
'''

#-------------
    #Python - Format - Strings

#F-Strings
'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)
'''

#Placeholders and Modifiers
'''
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
returns - The price is 59.00 dollars
'''

'''
txt = f"The price is {20 * 59} dollars"
print(txt)
'''
#-----------------
    #Python - Escape Characters

#An escape character is a backslash \ followed by the character you want to insert.
'''
txt = "We are the so-called \"Vikings\" from the north."
'''
#escape characters used in Python:
'''
Code	    Result	
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''

#-----------------
    #Python - String Methods
'''
Method	                    Description
capitalize()	            Converts the first character to upper case
casefold()	                Converts string into lower case
center()	                Returns a centered string
count()	                    Returns the number of times a specified value occurs in a string
encode()	                Returns an encoded version of the string
endswith()	                Returns true if the string ends with the specified value
expandtabs()	            Sets the tab size of the string
find()	                    Searches the string for a specified value and returns the position of where it was found
format()	                Formats specified values in a string
format_map()	            Formats specified values in a string
index()	                    Searches the string for a specified value and returns the position of where it was found
isalnum()	                Returns True if all characters in the string are alphanumeric
isalpha()	                Returns True if all characters in the string are in the alphabet
isascii()	                Returns True if all characters in the string are ascii characters
isdecimal()	                Returns True if all characters in the string are decimals
isdigit()	                Returns True if all characters in the string are digits
isidentifier()	            Returns True if the string is an identifier
islower()	                Returns True if all characters in the string are lower case
isnumeric()	                Returns True if all characters in the string are numeric
isprintable()	            Returns True if all characters in the string are printable
isspace()	                Returns True if all characters in the string are whitespaces
istitle()	                Returns True if the string follows the rules of a title
isupper()	                Returns True if all characters in the string are upper case
join()	                    Joins the elements of an iterable to the end of the string
ljust()	                    Returns a left justified version of the string
lower()	                    Converts a string into lower case
lstrip()	                Returns a left trim version of the string
maketrans()	                Returns a translation table to be used in translations
partition()	                Returns a tuple where the string is parted into three parts
replace()	                Returns a string where a specified value is replaced with a specified value
rfind()	                    Searches the string for a specified value and returns the last position of where it was found
rindex()	                Searches the string for a specified value and returns the last position of where it was found
rjust()	                    Returns a right justified version of the string
rpartition()	            Returns a tuple where the string is parted into three parts
rsplit()	                Splits the string at the specified separator, and returns a list
rstrip()	                Returns a right trim version of the string
split()	                    Splits the string at the specified separator, and returns a list
splitlines()	            Splits the string at line breaks and returns a list
startswith()	            Returns true if the string starts with the specified value
strip()	                    Returns a trimmed version of the string
swapcase()	                Swaps cases, lower case becomes upper case and vice versa
title()	                    Converts the first character of each word to upper case
translate()	                Returns a translated string
upper()	                    Converts a string into upper case
zfill()	                    Fills the string with a specified number of 0 values at the beginning
'''