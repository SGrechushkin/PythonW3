#----------------------------
    #Python Sets
#https://www.w3schools.com/python/python_sets.asp

#A set is a collection which is unordered, unchangeable*, and unindexed.
'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
'''

#Duplicates Not Allowed
'''
thisset = {"apple", "banana", "cherry", "apple", True, 1, 2, False, 0}

print(thisset)
'''

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

#Get the Length of a Set
'''
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
'''

#Set Items - Data Types
#A set can contain different data types:
'''
set1 = {"abc", 34, True, 40, "male"}
'''

#The set() Constructor
'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''

#Python Collections (Arrays)
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

#----------------------
    #Python - Access Set Items

'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
'''

'''
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
'''

#------------------
    #Python - Add Set Items

#Add Items
#To add one item to a set use the add() method.
'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
'''

#Add Sets
#To add items from another set into the current set, use the update() method.

'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
'''

#Add Any Iterable
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
'''

#-------------------
    #Python - Remove Set Items

#Remove Item
#o remove an item in a set, use the remove(), or the discard() method.
'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
'''

'''
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
'''

#Remove a random item by using the pop() method:
'''
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
'''

#The clear() method empties the set:
'''
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
'''

#The del keyword will delete the set completely:
'''
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
'''

#----------------------
    #Python - Loop Sets

#Loop Items
#You can loop through the set items by using a for loop:
'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
'''

#---------------------
    #Python - Join Sets

#Join Sets
#There are several ways to join two or more sets in Python.
'''
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

#Union
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) or can use set3 = set1 | set2
print(set3)
'''

#Join multiple sets with the union() method:
'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
'''

#Join a Set and a Tuple with the union() method:
'''
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
'''

#Update
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
#Note: Both union() and update() will exclude any duplicate items.
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
'''

#Intersection
#Keep ONLY the duplicates
#The intersection() method will return a new set, that only contains the items that are present in both sets.
#You can use the & operator instead of the intersection() method, and you will get the same result.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) or set1 & set2
print(set3)
result "apple"
'''

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
'''

#Difference
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#You can use the - operator instead of the difference() method, and you will get the same result.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) or set1 - set2

print(set3)
result  {'banana', 'cherry'}
'''

#The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
'''

#Symmetric Differences
#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2) or set1 ^ set2

print(set3)
'''

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
'''

#----------------------------
    #Python - Set Methods

#Python has a set of built-in methods that you can use on sets.
'''
Method	                    Shortcut	                    Description
add()	 	                                                Adds an element to the set
clear()	 	                                                Removes all the elements from the set
copy()	 	                                                Returns a copy of the set
difference()	                -	                        Returns a set containing the difference between two or more sets
difference_update()	            -=	                        Removes the items in this set that are also included in another, specified set
discard()	 	                                            Remove the specified item
intersection()	                &	                        Returns a set, that is the intersection of two other sets
intersection_update()	        &=	                        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                                        Returns whether two sets have a intersection or not
issubset()	                    <=	                        Returns whether another set contains this set or not
 	                            <	                        Returns whether all items in this set is present in other, specified set(s)
issuperset()	                >=	                        Returns whether this set contains another set or not
 	                            >	                        Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                                Removes an element from the set
remove()	 	                                            Removes the specified element
symmetric_difference()	        ^	                        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	                        Inserts the symmetric differences from this set and another
union()	                        |	                        Return a set containing the union of sets
update()	                    |=	                        Update the set with the union of this set and others

'''