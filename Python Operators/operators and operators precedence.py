
#operator precedence
#** Exponentiation (raise to the power)
#~ + - Ccomplement, unary plus and minus (method names for
#the last two are +@ and -@)
#* / % // Multiply, divide, modulo and floor division
#+ - Addition and subtraction
#>> << Right and left bitwise shift
#& Bitwise 'AND'
#^ | Bitwise exclusive `OR' and regular `OR'
#<= < > >= Comparison operators
#Python
#42
#<> == != Equality operators
#= %= /= //= -= +=
#*= **=
#Assignment operators
#is is not Identity operators
#in not in Membership operators
#not or and Logical operators 

# arthemetic operators
a=20
b=3
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a**b
i=a%b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
#bitwise operators
b1=2
b2=3
# or operator between 10 and 11 would be 11 or 3
print(b1|b2)
#and operator 10 11 would be 10
print(b1&b2)
# xor operaotr 10 11 would be 01
print(b1^b2)
# ~ twos compliment or bit
print(~b2)
# right shift and left shift
#logical operators
print(True and False)
print(True or False)
print(not(True or False))
#in and not in operators
arr=[2,3,4,5,6,1]
print(1 in arr)
print(1 not in arr)

#is and is not operator
a = 20
b = 20
if ( a is b ):
 print ("Line 1 - a and b have same identity")
else:
 print ("Line 1 - a and b do not have same identity")
if ( id(a) == id(b) ):
 print ("Line 2 - a and b have same identity")
else:
 print ("Line 2 - a and b do not have same identity")
b = 30
if ( a is b ):
 print ("Line 3 - a and b have same identity")
else:
 print ("Line 3 - a and b do not have same identity")
if ( a is not b ):
 print ("Line 4 - a and b do not have same identity")
else:
 print ("Line 4 - a and b have same identity")
