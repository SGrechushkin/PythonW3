#------------
    #Python Lists
    #https://www.w3schools.com/python/python_lists.asp
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
'''

'''
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 
> 3
'''
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List                      -  is a collection which is ordered and changeable. Allows duplicate members.
Tuple                     -  is a collection which is ordered and unchangeable. Allows duplicate members.
Set                       -  is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary                -  is a collection which is ordered** and changeable. No duplicate members.
'''

#----------------------
    #Python - Access List Items
'''
Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

Note: The search will start at index 2 (included) and end at index 5 (not included).
result ['cherry', 'orange', 'kiwi']
'''

#Check if Item Exists
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''
#--------------
    #Python - Change List Items
#Change Item Value
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

or

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
'''

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
'''

#-------------
    #Python - Add List Items
#https://www.w3schools.com/python/python_lists_add.asp

#Append Items
#To add an item to the end of the list, use the append() method:
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
'''

#Insert Items
#To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
#To append elements from another list to the current list, use the extend() method.
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
'''

'''
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
'''