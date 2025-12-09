# The print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma:
# For numbers, the + character works as a mathematical operator:
# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

print("=============Output Variables=============")
x = "Python is awesome"
print(x)

print("In the print() function, you output multiple variables, separated by a comma:")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print("You can also use the + operator to output multiple variables:")

x = "Python"
y = " is "
z = "awesome"

print(x+y+z)

x = 5
y = 10
print(x + y)

print("In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:")

x = 5
y = "John"
print(x+ y) #Getting Error here

print("6...")
x = 5
y = "John"
print(x, y)
