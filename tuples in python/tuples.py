#tuples in python are structures that collects element , it is ordered but unchangeable 
#in order to create a tuple we use () or tuple
t=tuple( )
tup=('python' , 'javascript' , 'c++','ruby' , 'css' ) 
print(tup)
#to access items in a tuple we use its index , don't forget that the index of elements starts with 0 
print(tup[0])
print(tup[1])
#index could be negative
print(tup[-1])
#you can choose the element to print , here in the example we will print element from index 1 to 3 because 4 is not inluded
print(tup[1:4])
#checking if an element exists 
if "css" in tup:
  print("Yes, 'css' is in the tuple")