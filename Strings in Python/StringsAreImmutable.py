# strings are immutable means if we create a string then we cannot change it
string="string"
print(string[1])
# string[1]="T" This will give error

print(string.replace("t","T")) # This creates a new string, dont think like it is changed
string.replace("t","T")
print(string)                   # This prints the original string because replace method creates a new one

new_string=string.replace("t","T")
print(string)
print(new_string)