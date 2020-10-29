#to determine how many elements are in a list weuse len function 
K=0
L=[1,2,3,4,5]
K=len(L)
print("the length of the list L is :", K)

#to print the last element of a list and delete it we use pop 
L.pop() 
print("the list L after pop: ")
print(L)

#to print and delete an element knowing its indexe we use pop and give the index of the element as an argument
print(L.pop(0))
print(L)