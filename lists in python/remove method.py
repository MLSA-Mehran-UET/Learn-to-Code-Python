#to remove an element in a list we use delete that takes an element and delete its first appearance in the list 
#if the element to remove is not in the list it raises a ValueError
L=[1,2,3,4,3]
print("the list before remove :")
print(L)
L.remove(3)
print("the list after remove : ")
print(L)
#L.remove(8)
#this commend will raise a ValueError 

