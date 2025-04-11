#-------------------
    #Python Dictionaries
#https://www.w3schools.com/python/python_dictionaries.asp
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
'''

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Dictionary Items
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
'''

#Dictionary Length
'''
print(len(thisdict))
'''

#Dictionary Items - Data Types
#The values in dictionary items can be of any data type:
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
'''

#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.
'''
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''

#-----------------------
    #Python - Access Dictionary Items

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
'''
#There is also a method called get() that will give you the same result:
'''
x = thisdict.get("model")
'''

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
result dict_keys(['brand', 'model', 'year'])
'''

#Get Values
#The values() method will return a list of all the values in the dictionary.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
'''

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)

result dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
'''

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
'''

#----------------------
    #Python - Change Dictionary Items

#Change Values
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
'''

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
'''

#------------------------
    #Python - Add Dictionary Items

#Adding Items
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
'''

#Update Dictionary
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
'''

#---------------------
    #Python - Remove Dictionary Items

#Removing Items
#The pop() method removes the item with the specified key name:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
'''

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
'''

#The del keyword removes the item with the specified key name:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
'''

#The del keyword can also delete the dictionary completely:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
'''

#The clear() method empties the dictionary:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
'''

#-----------------
    #Python - Loop Dictionaries

#Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
result 
brand
model
year
'''

#Print all values in the dictionary, one by one:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
'''

#You can also use the values() method to return values of a dictionary:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
'''

#You can use the keys() method to return the keys of a dictionary:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
'''

#Loop through both keys and values, by using the items() method:
'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
  
result
brand Ford
model Mustang
year 1964
'''

#-------------------------
    #Python - Copy Dictionaries

#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
#Make a copy of a dictionary with the copy() method:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
'''

#Another way to make a copy is to use the built-in function dict().
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
'''

#------------------------
    #Python - Nested Dictionaries

#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
result      {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
'''

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
'''

#Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
'''

#Loop Through Nested Dictionaries
#You can loop through a dictionary by using the items() method like this:
'''
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x, obj in myfamily.items(): #Повертає назви вкладених бібліотек
    print(x)

    for y in obj: 
        print(y + ':', obj[y]) #Повертає значення з вкладених бібліотек
'''

#------------------------------
    #Python Dictionary Methods
#Dictionary Methods
'''
Method	                Description
clear()	                Removes all the elements from the dictionary
copy()	                Returns a copy of the dictionary
fromkeys()	            Returns a dictionary with the specified keys and value
get()	                Returns the value of the specified key
items()	                Returns a list containing a tuple for each key value pair
keys()	                Returns a list containing the dictionary's keys
pop()	                Removes the element with the specified key
popitem()	            Removes the last inserted key-value pair
setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	            Updates the dictionary with the specified key-value pairs
values()	            Returns a list of all the values in the dictionary
'''

