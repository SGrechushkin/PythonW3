#---------------------------------
        #Python Tuples
#A tuple is a collection which is ordered and unchangeable.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
'''

#Tuple Length
'''
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
'''

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
'''
thistuple = ("apple",)
print(type(thistuple))
'''

#Tuple Items - Data Types - Tuple items can be of any data type:
'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
'''

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
'''
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
'''

#Python Collections (Arrays)
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#----------------------
    #Python - Access Tuple Items

#Access Tuple Items
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
'''

#Negative Indexing
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
'''

#Range of Indexes
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
'''

#Check if Item Exists

#To determine if a specified item is present in a tuple use the in keyword:
'''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
'''

#-----------------------
    #Python - Update Tuples

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
'''

#Add Items
#   1.  Convert into a list:
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
'''
#   2. Add tuple to a tuple.
'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
'''

#----------------------
    #Python - Unpack Tuples

#Unpacking a Tuple
'''
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)  - apple
print(yellow) - banana
print(red)    - cherry

Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
'''

#Using Asterisk*
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)  - apple
print(yellow) - ['banana', 'cherry', 'strawberry']
print(red)    - raspberry
'''

#-------------------------
    #Python - Loop Tuples

#Loop Through a Tuple
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
'''

#Loop Through the Index Numbers
'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
'''

#Using a While Loop
'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
'''

#------------------------
    #Python - Join Tuples

#Join Two Tuples
'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
'''

#Multiply Tuples
'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
result - ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
'''

#------------------------
    #Python - Tuple Methods
'''
Method	        Description
count()	        Returns the number of times a specified value occurs in a tuple
index()	        Searches the tuple for a specified value and returns the position of where it was found
'''