#-------------------
    #Python If ... Else
#https://www.w3schools.com/python/python_conditions.asp

#Python Conditions and If statements
'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''

'''
a = 33
b = 200
if b > a:
  print("b is greater than a")
'''

#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
'''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
'''

#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
'''

#Short Hand If
'''
a = 200
b = 33

if a > b: print("a is greater than b")
'''

#Short Hand If ... Else
'''
a = 2
b = 330

print("A") if a > b else print("B")
'''

#And
#The and keyword is a logical operator, and is used to combine conditional statements:
'''
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
'''

#Or
#The or keyword is a logical operator, and is used to combine conditional statements:
'''
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
'''

#Not
#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
'''
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
'''

#Nested If
#You can have if statements inside if statements, this is called nested if statements.
'''
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
'''

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
'''
a = 33
b = 200

if b > a:
  pass
'''

#----------------------------
    #Python Match - The match statement is used to perform different actions based on different conditions.

#The Python Match Statement
#Instead of writing many if..else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.
'''
This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.
'''
'''
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
'''

#Default Value
#Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
#The value _ will always match, so it is important to place it as the last case to make it beahave as a default case.
'''
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
'''
#Combine Values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
'''
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
'''

#If Statements as Guards
#You can add if statements in the case evaluation as an extra condition-check:
'''
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
'''

#-----------------------------
    #Python While Loops

#Python Loops
#Python has two primitive loop commands:
#           while loops
#           for loops

#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
'''
i = 1
while i < 6:
  print(i)
  i += 1
'''

#The break Statement
#With the break statement we can stop the loop even if the while condition is true:
'''
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
'''

#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result
'''

#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''