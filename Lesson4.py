#------------
    #Python Booleans
#https://www.w3schools.com/python/python_booleans.asp

#Boolean Values
'''
print(10 > 9) > True
print(10 == 9) > False
print(10 < 9) > False
'''

'''
a = 123
b = 345
if a>b:
    print("'a' is greater than 'b'")
else:
    print("'b' is greater than 'a'")
'''


#Evaluate Values and Variables
'''
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

x = "Hello"
y = 15

print(bool(x)) > True
print(bool(y)) > True
'''

#Functions can Return a Boolean
'''
def myFunction():
    return True
print(myFunction())
'''
'''
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
'''

'''
x = 200
print(isinstance(x, int)) > True - перевіряє змінну на відповідність типу даних

x=200
print(isinstance(x, str)) > False
'''

#--------------
    #Python Operators

#Python Arithmetic Operators
'''
Operator	                 Name	                    Example
    +	                    Addition	x + y
    -	                    Subtraction	x - y
    *	                    Multiplication	x * y
    /	                    Division	x / y
    %	                    Modulus	x % y
    **	                    Exponentiation	x ** y      #same as 2*2*2*2*2
    //	                    Floor division	x // y      #the floor division // rounds the result down to the nearest whole number
'''
#Python Assignment Operators
'''
Operator	    Example	        Same As	
=	            x = 5	        x = 5	
+=	            x += 3	        x = x + 3	
-=	            x -= 3	        x = x - 3	
*=	            x *= 3	        x = x * 3	
/=	            x /= 3	        x = x / 3	
%=	            x %= 3	        x = x % 3	
//=	            x //= 3	        x = x // 3	
**=	            x **= 3	        x = x ** 3	
&=	            x &= 3	        x = x & 3	
|=	            x |= 3	        x = x | 3	
^=	            x ^= 3	        x = x ^ 3	
>>=	            x >>= 3	        x = x >> 3	
<<=	            x <<= 3	        x = x << 3	
:=	            print(x := 3)	x = 3
                                print(x)
'''

#Python Comparison Operators
'''
Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y
'''

#Python Logical Operators
'''
Operator	            Description	                                                Example	
    and 	    Returns True if both statements are true	                        x < 5 and  x < 10	
    or	        Returns True if one of the statements is true	                    x < 5 or x < 4	
    not	        Reverse the result, returns False if the result is true	            not(x < 5 and x < 10)
'''

#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
'''
Operator	                Description	                                        Example	
is          	Returns True if both variables are the same object	            x is y	
is not	        Returns True if both variables are not the same object	        x is not y
'''

'''
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content
'''

#Python Membership Operators
'''
Operator	        Description	                                                                    Example	
in 	        Returns True if a sequence with the specified value is present in the object	        x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	    x not in y
'''

#Python Bitwise Operators
'''
Operator	    Name	                Description	                                                                                                Example	
& 	            AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	            OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	            XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~	            NOT	                    Inverts all the bits	                                                                                    ~x	
<<	            Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>	            Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
'''

#Operator Precedence "()"
'''
print(3*(6 + 3))
'''

'''
The precedence order is described in the table below, starting with the highest precedence at the top:
Operator	                                     Description
()	                                             Parentheses	
**	                                             Exponentiation	
+x  -x  ~x	                                     Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                     Multiplication, division, floor division, and modulus	
+  -	                                         Addition and subtraction	
<<  >>	                                         Bitwise left and right shifts	
&	                                             Bitwise AND	
^	                                             Bitwise XOR	
|	                                             Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	 Comparisons, identity, and membership operators	
not	                                             Logical NOT	
and	                                             AND	
or	                                             OR
'''

