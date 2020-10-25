# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result
y = thisdict.get("model")
print(y)

# You can change the value of a specific item by referring to its key name
thisdict["year"] = 2018
print(thisdict["year"])

# You can loop through a dictionary by using a for loop
# Print all key names in the dictionary, one by one
for i in thisdict:
  print(i)
  
# Print all values in the dictionary, one by one
for j in thisdict:
  print(thisdict[j])
  
# Loop through both keys and values, by using the items() method
for a, b in thisdict.items():
  print(a, b)
