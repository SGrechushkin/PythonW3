# Python Booleans
# https://www.w3schools.com/python/python_booleans.asp
"""
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
"""

#Python Operators
#https://www.w3schools.com/python/python_operators.asp

#----------Arithmetic Operators--------
'''
Operator	Name	    Example	
+	    Addition	    x + y	
-	    Subtraction	    x - y	
*	    Multiplication	x * y	
/	    Division	    x / y	
%	    Modulus	        x % y	
**	    Exponentiation	x ** y	
//	    Floor division	x // y
'''

#---------Assignment Operators-------------
'''
Operator	Example	        Same As	
=	        x = 5	        x = 5
+=	        x += 3	        x = x + 3
-=	        x -= 3	        x = x - 3
*=	        x *= 3	        x = x * 3
/=	        x /= 3	        x = x / 3
%=	        x %= 3	        x = x % 3
//=	        x //= 3	        x = x // 3
**=	        x **= 3	        x = x ** 3
&=	        x &= 3	        x = x & 3
|=	        x |= 3	        x = x | 3
^=	        x ^= 3	        x = x ^ 3
>>=	        x >>= 3	        x = x >> 3
<<=	        x <<= 3	        x = x << 3
:=	        print(x := 3)	x = 3
                            print(x)
'''

#The Walrus Operator
#Python 3.8 introduced the := operator, known as the "walrus operator".
# It assigns values to variables as part of a larger expression:


#This long
'''
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")
'''
#same as this
'''
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
'''

#----------------Comparison Operators---------------
'''
Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''
