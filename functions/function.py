#to create a function the keyword is def 
def my_function1 () : 
    print("hello world ! ")
#to add arguments put them between parentheses seperated by "," 
def my_function2 (msg) : 
    print(msg) 
#to return a value we use the key word return 
def my_function3 (a,b) :
    som=a+b 
    return(som) 
#to call a function already defined
print("fonction without arguments : ")
my_function1() 
print("function with 1 argument")
my_function2("write your message here")
print("function with 2 arguments and a returned value")
print("the sum of 3 and 5 is : " , my_function3(3,5))




