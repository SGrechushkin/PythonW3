#--------------
    #Python - Remove List Items

#Remove Specified Item
#The remove() method removes the specified item.
'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
'''

#Remove Specified Index
#The pop() method removes the specified index.
'''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
'''

#The del keyword also removes the specified index. The del keyword can also delete the list completely.

'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
'''

#Clear the List
#The clear() method empties the list.

'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''

#-----------------
    #Python - Loop Lists

#Loop Through a List
#You can loop through the list items by using a for loop:

'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
'''

#Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.

'''
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
'''

#Using a While Loop
#You can loop through the list items by using a while loop.

'''
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
'''

#Looping Using List Comprehension
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
'''

#-------------------
    #Python - List Comprehension

#Замість використання FOR можна використовувати List Comprehension. Ми використовуємо його для створення нового списку.
'''
Приклад з FOR

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
'''

'''
Приклад з List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
'''

#The Syntax for List Comprehension
'''newlist = [expression for item in iterable if condition == True]'''

#Condition - The condition is like a filter that only accepts the items that evaluate to True.

#Iterable - The iterable can be any iterable object, like a list, tuple, set etc.

#Expression - The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
'''


#----------------------
    #Python - Sort Lists

#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

result ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
'''

#Sort Descending
#To sort descending, use the keyword argument reverse = True:

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

result [100, 82, 65, 50, 23]
'''

#Customize Sort Function
#You can also customize your own function by using the keyword argument key = function.
#The function will return a number that will be used to sort the list (the lowest number first):

'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

result  [50, 65, 23, 82, 100] - повертає список відсортований по віддаленості від 50.
'''

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
#Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
'''

#Reverse Order
#The reverse() method reverses the current sorting order of the elements.

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
'''